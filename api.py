from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import fitness_backend as backend

app = FastAPI(title="Fitness App API")


class ProfileIn(BaseModel):
    age: int
    height: float
    weight: float
    goal: str
    gender: Optional[str] = None


@app.get("/")
def root():
    return {"status": "ok"}


@app.get("/profile")
def get_profile():
    profile = backend.load_user_profile()
    if profile is None:
        raise HTTPException(status_code=404, detail="No profile set yet")
    return profile


@app.post("/profile")
def update_profile(data: ProfileIn):
    connection = backend.get_database_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT id FROM user_profile ORDER BY id DESC LIMIT 1")
    existing = cursor.fetchone()

    if existing:
        cursor.execute("""
            UPDATE user_profile
            SET age = ?, height = ?, body_weight = ?, goal = ?, gender = ?
            WHERE id = ?
        """, (data.age, data.height, data.weight, data.goal, data.gender, existing["id"]))
    else:
        cursor.execute("""
            INSERT INTO user_profile (age, height, body_weight, goal, gender)
            VALUES (?, ?, ?, ?, ?)
        """, (data.age, data.height, data.weight, data.goal, data.gender))

    connection.commit()
    connection.close()
    return backend.load_user_profile()


@app.get("/home/current-week")
def current_week():
    """Locked/in-progress card — only training_days is meaningful here."""
    return backend.get_in_progress_week_preview()


@app.get("/home/week/{weeks_ago}")
def finalized_week(weeks_ago: int):
    """Finalized card for a completed week. weeks_ago=1 is last week,
    2 is two weeks ago, etc. Use /home/current-week for this week instead."""
    if weeks_ago < 1:
        raise HTTPException(
            status_code=400,
            detail="weeks_ago must be 1 or more — use /home/current-week for this week"
        )
    return backend.get_home_screen_week_summary(weeks_ago=weeks_ago)
