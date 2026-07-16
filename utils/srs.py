"""A simplified SM-2-style spaced repetition scheduler."""
from datetime import date, timedelta

DEFAULT_CARD = {"interval": 0, "ease": 2.5, "due": None, "reps": 0}


def get_card(progress, key):
    return progress["srs_cards"].get(key, dict(DEFAULT_CARD))


def is_due(card):
    if card["due"] is None:
        return True
    return date.today().isoformat() >= card["due"]


def review(progress, key, quality):
    """quality: 0=again, 1=hard, 2=good, 3=easy"""
    card = get_card(progress, key)
    reps = card["reps"]
    ease = card["ease"]

    if quality == 0:  # again
        reps = 0
        interval = 0
        ease = max(1.3, ease - 0.2)
        due = date.today().isoformat()
    else:
        if quality == 1:
            ease = max(1.3, ease - 0.15)
            mult = 1.2
        elif quality == 2:
            mult = ease
        else:  # easy
            ease = ease + 0.15
            mult = ease * 1.3

        if reps == 0:
            interval = 1
        elif reps == 1:
            interval = 3
        else:
            interval = max(1, round(card["interval"] * mult))
        reps += 1
        due = (date.today() + timedelta(days=interval)).isoformat()

    progress["srs_cards"][key] = {"interval": interval, "ease": ease, "due": due, "reps": reps}
    return progress


def due_count(progress, keys):
    return sum(1 for k in keys if is_due(get_card(progress, k)))
