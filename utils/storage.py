"""Simple local JSON-based progress persistence for the single-user app."""
import json
import os
from datetime import date

PROGRESS_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "progress.json")

DEFAULT_PROGRESS = {
    "lessons_completed": [],       # list of lesson titles marked done
    "srs_cards": {},               # key -> {"interval": int, "ease": float, "due": "YYYY-MM-DD", "reps": int}
    "quiz_history": [],            # list of {"date":..., "topic":..., "score":..., "total":...}
    "streak": {"count": 0, "last_active": None},
    "letters_known": [],           # devanagari letters marked as learned
    "storyline": {"completed": [], "scores": {}},   # chapter_id -> best % score; completed = mastered chapter ids
}


def load_progress():
    if os.path.exists(PROGRESS_PATH):
        try:
            with open(PROGRESS_PATH, "r", encoding="utf-8") as f:
                data = json.load(f)
            # backfill any missing keys (for forward-compat)
            for k, v in DEFAULT_PROGRESS.items():
                if k not in data:
                    data[k] = v
            return data
        except Exception:
            pass
    return json.loads(json.dumps(DEFAULT_PROGRESS))


def save_progress(progress):
    with open(PROGRESS_PATH, "w", encoding="utf-8") as f:
        json.dump(progress, f, ensure_ascii=False, indent=2)


def touch_streak(progress):
    today = date.today().isoformat()
    last = progress["streak"].get("last_active")
    if last == today:
        return progress
    if last is not None:
        y = date.fromisoformat(last)
        gap = (date.today() - y).days
        if gap == 1:
            progress["streak"]["count"] += 1
        elif gap > 1:
            progress["streak"]["count"] = 1
    else:
        progress["streak"]["count"] = 1
    progress["streak"]["last_active"] = today
    save_progress(progress)
    return progress
