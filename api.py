from fastapi import FastAPI, HTTPException, Header
from fastapi.responses import HTMLResponse
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


class GoogleSignInIn(BaseModel):
    id_token: str


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
        reset_link = f"{backend.APP_BASE_URL}/reset-password?token={raw_token}"
        backend.send_password_reset_email(data.email, reset_link)

    # Always return the same response whether or not the email exists,
    # so this endpoint can't be used to check which emails are
    # registered.
    return {"message": "If an account with that email exists, a reset link has been sent."}


@app.get("/reset-password", response_class=HTMLResponse)
def reset_password_page(token: str = ""):
    """A minimal, self-contained page the reset email links to, so
    password reset works today even before the Flutter app has its own
    reset screen (or as a permanent web fallback for anyone opening the
    link outside the app)."""
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Reset your password</title>
        <style>
            body {{ font-family: sans-serif; max-width: 400px; margin: 60px auto; padding: 0 20px; }}
            input {{ width: 100%; padding: 10px; margin: 8px 0; box-sizing: border-box; }}
            button {{ width: 100%; padding: 10px; background: #2E6B4F; color: white; border: none; border-radius: 6px; }}
            #message {{ margin-top: 12px; }}
        </style>
    </head>
    <body>
        <h2>Reset your password</h2>
        <input type="password" id="new_password" placeholder="New password (min 8 characters)">
        <button onclick="submitReset()">Reset password</button>
        <p id="message"></p>
        <script>
            const token = {token!r};
            async function submitReset() {{
                const password = document.getElementById("new_password").value;
                const messageEl = document.getElementById("message");
                try {{
                    const res = await fetch("/auth/reset-password", {{
                        method: "POST",
                        headers: {{ "Content-Type": "application/json" }},
                        body: JSON.stringify({{ token: token, new_password: password }})
                    }});
                    const data = await res.json();
                    messageEl.textContent = res.ok
                        ? "Password reset. You can now log in in the app."
                        : (data.detail || "Something went wrong.");
                }} catch (e) {{
                    messageEl.textContent = "Network error - please try again.";
                }}
            }}
        </script>
    </body>
    </html>
    """


@app.post("/auth/reset-password")
def reset_password(data: ResetPasswordIn):
    if len(data.new_password) < 8:
        raise HTTPException(status_code=400, detail="Password must be at least 8 characters")

    success = backend.reset_password_with_token(data.token, data.new_password)
    if not success:
        raise HTTPException(status_code=400, detail="Reset link is invalid or has expired")

    return {"message": "Password has been reset. You can now log in with your new password."}


@app.post("/auth/google")
def google_sign_in(data: GoogleSignInIn):
    google_info = backend.verify_google_id_token(data.id_token)
    if google_info is None:
        raise HTTPException(status_code=401, detail="Invalid or unverified Google sign-in")

    user_id = backend.find_or_create_google_user(google_info["email"], google_info["google_sub"])

    # Same app-issued token as email/password login - everything past
    # this point (profile, home screen, etc.) doesn't need to know or
    # care which method the person signed in with.
    token = backend.create_access_token(user_id)
    return {"access_token": token, "token_type": "bearer"}


@app.get("/auth/me")
def get_current_user_info(authorization: Optional[str] = Header(None)):
    """Lets the app check 'who is currently logged in' using just the
    stored token - e.g. on app launch, to restore a session without
    asking the person to log in again every time they open the app."""
    user_id = get_current_user_id(authorization)
    email = backend.get_user_email(user_id)
    return {"user_id": user_id, "email": email}


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
