from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel, EmailStr
from typing import Optional
import fitness_backend as backend

app = FastAPI(title="Fitness App API")


# ============================================================
# AUTH DEPENDENCY
# ============================================================

def get_current_user_id(authorization: Optional[str] = Header(None)):
    """Reads the 'Authorization: Bearer <token>' header, validates the
    token, and returns the user_id it belongs to. Every protected
    endpoint below takes this as a parameter - FastAPI calls it
    automatically before the endpoint's own code runs, so a request
    with a missing/invalid/expired token never reaches the endpoint
    body at all."""
    if authorization is None or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing or malformed Authorization header")

    token = authorization.removeprefix("Bearer ")
    user_id = backend.decode_access_token(token)

    if user_id is None:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

    return user_id


# ============================================================
# REQUEST BODIES
# ============================================================

class SignupIn(BaseModel):
    email: EmailStr
    password: str


class LoginIn(BaseModel):
    email: EmailStr
    password: str


class ForgotPasswordIn(BaseModel):
    email: EmailStr


class ResetPasswordIn(BaseModel):
    token: str
    new_password: str


class ProfileIn(BaseModel):
    age: int
    height: float
    weight: float
    goal: str
    gender: Optional[str] = None


class LogWeightIn(BaseModel):
    weight: float


@app.get("/")
def root():
    return {"status": "ok"}


# ============================================================
# AUTH ENDPOINTS
# ============================================================

@app.post("/auth/signup")
def signup(data: SignupIn):
    if len(data.password) < 8:
        raise HTTPException(status_code=400, detail="Password must be at least 8 characters")
    try:
        user_id = backend.create_user(data.email, data.password)
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))

    token = backend.create_access_token(user_id)
    return {"access_token": token, "token_type": "bearer"}


@app.post("/auth/login")
def login(data: LoginIn):
    user_id = backend.authenticate_user(data.email, data.password)
    if user_id is None:
        # Same error for "no such email" and "wrong password" -
        # distinguishing them tells an attacker which emails have
        # accounts on this app at all.
        raise HTTPException(status_code=401, detail="Incorrect email or password")

    token = backend.create_access_token(user_id)
    return {"access_token": token, "token_type": "bearer"}


@app.post("/auth/forgot-password")
def forgot_password(data: ForgotPasswordIn):
    raw_token = backend.create_password_reset_token(data.email)

    if raw_token is not None:
        # TODO: actually send this via an email provider (e.g. Resend,
        # SendGrid). Wiring in real email sending is a separate step -
        # for now this only generates and stores the token server-side.
        reset_link = f"https://yourapp.example.com/reset-password?token={raw_token}"
        print(f"[DEV ONLY] Password reset link for {data.email}: {reset_link}")

    # Always return the same response whether or not the email exists,
    # so this endpoint can't be used to check which emails are
    # registered.
    return {"message": "If an account with that email exists, a reset link has been sent."}


@app.post("/auth/reset-password")
def reset_password(data: ResetPasswordIn):
    if len(data.new_password) < 8:
        raise HTTPException(status_code=400, detail="Password must be at least 8 characters")

    success = backend.reset_password_with_token(data.token, data.new_password)
    if not success:
        raise HTTPException(status_code=400, detail="Reset link is invalid or has expired")

    return {"message": "Password has been reset. You can now log in with your new password."}


# ============================================================
# PROFILE ENDPOINTS (require login)
# ============================================================

@app.get("/profile")
def get_profile(authorization: Optional[str] = Header(None)):
    user_id = get_current_user_id(authorization)
    profile = backend.load_user_profile(user_id)
    if profile is None:
        raise HTTPException(status_code=404, detail="No profile set yet")
    return profile


@app.post("/profile")
def update_profile(data: ProfileIn, authorization: Optional[str] = Header(None)):
    user_id = get_current_user_id(authorization)
    backend.save_user_profile(user_id, data.age, data.height, data.weight, data.goal, data.gender)
    return backend.load_user_profile(user_id)


# ============================================================
# HOME SCREEN ENDPOINTS (require login)
# ============================================================

@app.get("/home/current-week")
def current_week(authorization: Optional[str] = Header(None)):
    """Locked/in-progress card — only training_days is meaningful here."""
    user_id = get_current_user_id(authorization)
    return backend.get_in_progress_week_preview(user_id)


@app.get("/home/week/{weeks_ago}")
def finalized_week(weeks_ago: int, authorization: Optional[str] = Header(None)):
    """Finalized card for a completed week. weeks_ago=1 is last week,
    2 is two weeks ago, etc. Use /home/current-week for this week instead."""
    user_id = get_current_user_id(authorization)
    if weeks_ago < 1:
        raise HTTPException(
            status_code=400,
            detail="weeks_ago must be 1 or more — use /home/current-week for this week"
        )
    return backend.get_home_screen_week_summary(user_id, weeks_ago=weeks_ago)


# ============================================================
# BODY WEIGHT LOGGING (require login)
# ============================================================

@app.post("/body-weight")
def log_weight(data: LogWeightIn, authorization: Optional[str] = Header(None)):
    user_id = get_current_user_id(authorization)
    backend.save_body_weight(user_id, data.weight)
    return {"message": "Weight logged"}
