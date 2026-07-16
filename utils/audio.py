"""Hindi audio generation via gTTS, with local disk caching so repeated lookups are instant
and the app only needs internet the first time a given word/phrase is requested."""
import os
import hashlib

AUDIO_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "audio_cache")
os.makedirs(AUDIO_DIR, exist_ok=True)


def _cache_path(text):
    h = hashlib.md5(text.encode("utf-8")).hexdigest()
    return os.path.join(AUDIO_DIR, f"{h}.mp3")


def get_audio_path(text):
    """Returns a local mp3 path for the given Hindi text, generating + caching it if needed.
    Returns None if generation fails (e.g. no internet)."""
    if not text or not text.strip():
        return None
    path = _cache_path(text)
    if os.path.exists(path):
        return path
    try:
        from gtts import gTTS
        tts = gTTS(text=text, lang="hi")
        tts.save(path)
        return path
    except Exception:
        return None
