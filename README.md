# हिंदी सीखें — Learn Hindi (Streamlit App)

A full, self-paced, Duolingo-style Hindi course for English/French speakers — script,
pronunciation (with audio), grammar, vocabulary, verb conjugation, phrases, homework,
and a **144,000+ word searchable dictionary** — all running locally on your machine.

## What's new in this version

- **Real dictionary, not a toy list.** The Dictionary Search page is built on a cleaned,
  deduplicated English→Hindi dataset (144,482 entries after cleaning ~198k raw rows),
  covering everyday words like "address," "location," "password," "internet," alongside
  core vocabulary — with part-of-speech filtering and a custom-built transliteration
  engine (with word-final schwa deletion, so it reads "kitaab" not "kitaaba").
- **Pronunciation tab.** A "pronounce any word" tool (type Hindi or English, get the
  transliteration + audio) plus a full sound-system deep-dive: aspiration, retroflex vs.
  dental, vowel length, nasal vowels, stress.
- **Audio.** Every letter, word, phrase, verb form, and dictionary result has a 🔊 Listen
  button (via Google TTS). Audio is cached locally after the first play, so it only needs
  internet once per word.
- **Homework.** Auto-generated, randomized, self-checking worksheets (Vocabulary, Phrases,
  Verbs, or Mixed Review) with typed answers, fuzzy matching, scoring, and history tracking.
- **Better UI.** Custom styling, a home dashboard with a "recommended next step," and a
  Word of the Day.

## Full feature list

- **Learn (Curriculum)** — 6-unit course with built-in grammar lessons (word order,
  gender, postpositions, all three tenses, the ने construction, negation, questions).
- **Script Trainer** — every vowel/consonant/matra/conjunct, with audio and a
  letter-recognition quiz.
- **Pronunciation** — lookup tool + full sound-system lessons.
- **Vocabulary & Flashcards** — 185 curated words across 17 themes, spaced-repetition
  flashcards (SM-2 style), and MCQ quizzes.
- **Phrases** — 40+ real conversational phrases by situation.
- **Verb Trainer** — present/future/past tables (m/f, 7 pronouns) for 15 core verbs,
  with a conjugation-drill quiz.
- **Homework** — randomized worksheets with self-checking and history.
- **Dictionary Search** — 144,000+ words (full dataset) plus a curated quick-reference tab.
- **My Progress** — streak, lessons, letters known, flashcards due, homework history —
  saved locally to `progress.json`.

## How to run it

1. Install Python 3.9+.
2. In this folder:
   ```
   pip install -r requirements.txt
   ```
3. Launch:
   ```
   streamlit run app.py
   ```
4. Opens automatically at `http://localhost:8501`.

## Notes on audio

Audio uses `gTTS`, which calls Google's Translate TTS service — it needs an internet
connection **the first time** each word/phrase is played. After that, the mp3 is cached
in `audio_cache/` and plays instantly offline. If you're fully offline, the app still
works perfectly for everything except new audio — just click "🔊 Listen" and you'll see
a friendly notice instead of an error.

## Data sources & methodology

- The 144k-word dictionary was built from an open-source English–Hindi CSV, cleaned to
  remove malformed/duplicate/non-dictionary rows (198,572 raw rows → 144,482 clean
  entries), with part-of-speech normalized.
- Since the raw dataset had no romanization, a custom rule-based Devanagari→Roman
  transliteration engine (`utils/transliterate.py`) was written specifically for this
  app — it handles matras, conjuncts (halant), nukta letters, anusvara/visarga, and
  word-final schwa deletion so the output is actually speakable, not just a letter-by-letter
  dump.
- Curated vocabulary/verbs/grammar content is hand-verified against standard Hindi
  pedagogy (CEFR-style progression, frequency-informed word choice).

## Extending it

Everything lives in plain Python/CSV in `data/`:
- `data/full_dictionary.csv` — the big dictionary (english, hindi, pos, translit columns)
- `data/vocab.py`, `data/phrases.py`, `data/verbs.py`, `data/grammar.py`,
  `data/pronunciation.py`, `data/alphabet.py` — curated content, easy to extend by
  following the existing patterns.
