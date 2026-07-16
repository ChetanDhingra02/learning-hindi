import random
import streamlit as st

from data.alphabet import VOWELS, CONSONANT_GROUPS, MATRAS, SPECIAL_MARKS, CONJUNCTS, READING_LADDER, ALL_LETTERS
from data.vocab import VOCAB, all_vocab_flat
from data.phrases import PHRASES, all_phrases_flat
from data.verbs import VERBS, PRONOUNS, PRONOUN_LABELS
from data.grammar import GRAMMAR_LESSONS, CEFR_MILESTONES
from data.storyline import STORYLINE_CHAPTERS, STORYLINE_BY_ID, STORYLINE_LEVELS, CEFR_LABELS
from data.pronunciation import (PRONUNCIATION_INTRO, VOWEL_LENGTH_NOTE, ASPIRATION_NOTE,
                                 RETROFLEX_NOTE, NASAL_NOTE, STRESS_NOTE, SYLLABLE_TIPS)
from utils.storage import load_progress, save_progress, touch_streak
from utils.srs import get_card, is_due, review, due_count
from utils.quiz import mcq_from_vocab, mcq_from_letters, mcq_from_verb_form
from utils.search_index import build_index, search
from utils.dictionary import load_dictionary, search_dictionary, word_of_the_day
from utils.transliterate import transliterate
from utils.audio import get_audio_path
from utils.homework import build_worksheet, normalize

st.set_page_config(page_title="सीखें Hindi — Learn Hindi", page_icon="🇮🇳", layout="wide")

USER_NAME = "Dalton"

# ---------------------------------------------------------------
# Custom styling — themed to match the Claude platform (claude.ai)
# ---------------------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Source+Serif+4:wght@500;600;700&display=swap');

    :root {
        --clay: #CC785C;
        --clay-dark: #B25A3F;
        --clay-light: #F3DFD5;
        --ink: #1F1E1D;
        --ink-soft: #55524D;
        --cream: #FAF9F5;
        --cream-deep: #F0EEE5;
        --card-border: #E5E2D9;
    }

    html, body, [class*="css"] { font-family: 'Inter', -apple-system, sans-serif; }
    .stApp { background-color: var(--cream); }
    section[data-testid="stSidebar"] { background-color: var(--cream-deep); border-right: 1px solid var(--card-border); }

    h1, h2, h3 {
        font-family: 'Source Serif 4', Georgia, serif;
        color: var(--ink) !important;
        font-weight: 600;
    }
    p, span, label, li, div { color: var(--ink); }
    .stMarkdown, .stCaption, .stText { color: var(--ink); }

    /* Hero banner */
    .hero {
        background: linear-gradient(135deg, var(--clay) 0%, var(--clay-dark) 100%);
        padding: 2.2rem 2.4rem; border-radius: 18px; color: white; margin-bottom: 1.4rem;
        box-shadow: 0 4px 18px rgba(178, 90, 63, 0.18);
    }
    .hero h1 { font-family: 'Source Serif 4', Georgia, serif; color: white !important; margin-bottom: 0.35rem; }
    .hero p { color: #FBEAE2; font-size: 1.05rem; margin: 0; }
    .hero .greeting { font-size: 0.95rem; color: #FBEAE2; opacity: 0.9; margin-bottom: 0.5rem; letter-spacing: 0.02em; }

    .devnote { font-size: 2.2rem; font-weight: 600; color: var(--clay-dark); font-family: 'Source Serif 4', Georgia, serif; }

    .pill {
        display: inline-block; padding: 0.15rem 0.7rem; border-radius: 999px;
        background: var(--clay-light); color: var(--clay-dark); font-size: 0.78rem; font-weight: 600; margin-right: 0.3rem;
    }

    /* Custom metric cards (replace st.metric for guaranteed contrast/theming) */
    .metric-row { display: flex; gap: 0.9rem; flex-wrap: wrap; margin-bottom: 0.4rem; }
    .metric-card {
        flex: 1; min-width: 140px; background: white; border: 1px solid var(--card-border);
        border-radius: 12px; padding: 0.9rem 1.1rem; box-shadow: 0 1px 3px rgba(0,0,0,0.04);
    }
    .metric-card .label { font-size: 0.78rem; color: var(--ink-soft); font-weight: 500; margin-bottom: 0.15rem; }
    .metric-card .value { font-size: 1.6rem; font-weight: 700; color: var(--ink); }

    /* Native streamlit metric fallback (still used in a couple spots) — force contrast */
    div[data-testid="stMetric"] {
        background: white; border: 1px solid var(--card-border); border-radius: 12px; padding: 0.7rem 0.9rem;
    }
    div[data-testid="stMetricLabel"] * { color: var(--ink-soft) !important; }
    div[data-testid="stMetricValue"] * { color: var(--ink) !important; }

    /* Sidebar nav */
    .sidebar-brand { font-family: 'Source Serif 4', Georgia, serif; font-size: 1.25rem; font-weight: 600; color: var(--ink); margin-bottom: 0; }
    .sidebar-user {
        display: flex; align-items: center; gap: 0.55rem; padding: 0.6rem 0.7rem; margin: 0.6rem 0 0.8rem 0;
        background: white; border: 1px solid var(--card-border); border-radius: 10px;
    }
    .sidebar-user .avatar {
        width: 30px; height: 30px; border-radius: 50%; background: var(--clay); color: white;
        display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 0.9rem; flex-shrink: 0;
    }
    .sidebar-user .name { font-weight: 600; font-size: 0.88rem; color: var(--ink); }
    .sidebar-user .sub { font-size: 0.72rem; color: var(--ink-soft); }

    section[data-testid="stSidebar"] div[role="radiogroup"] label {
        border-radius: 8px; padding: 0.35rem 0.5rem; margin-bottom: 0.1rem;
    }
    section[data-testid="stSidebar"] div[role="radiogroup"] label:hover { background: var(--clay-light); }

    /* Buttons */
    .stButton>button {
        border-radius: 8px; border: 1px solid var(--card-border); color: var(--ink);
    }
    .stButton>button:hover { border-color: var(--clay); color: var(--clay-dark); }
    .stButton>button[kind="primary"] { background: var(--clay); border-color: var(--clay); color: white; }
    .stButton>button[kind="primary"]:hover { background: var(--clay-dark); border-color: var(--clay-dark); }

    /* Tabs */
    button[data-baseweb="tab"] { color: var(--ink-soft); }
    button[data-baseweb="tab"][aria-selected="true"] { color: var(--clay-dark) !important; font-weight: 600; }
    div[data-baseweb="tab-highlight"] { background-color: var(--clay) !important; }

    /* Expanders / info boxes keep readable text regardless of underlying theme */
    div[data-testid="stExpander"] summary { color: var(--ink); }
    .stAlert p { color: var(--ink) !important; }

    hr { border-color: var(--card-border); }

    /* Checkboxes/radios: force readable label text even when disabled */
    div[data-testid="stCheckbox"] label p,
    div[data-testid="stCheckbox"] label span,
    div[role="radiogroup"] label p,
    div[role="radiogroup"] label span {
        color: var(--ink) !important;
        opacity: 1 !important;
    }
    div[data-testid="stCheckbox"] svg { color: var(--clay) !important; }

    /* Audio player: force a minimum width so the play/volume controls never get
       compressed away when this sits inside a narrow column or on mobile */
    div[data-testid="stAudio"] { width: 100%; }
    audio { width: 100%; min-width: 230px; height: 40px; }

    /* Word result cards (Dictionary Search / Pronunciation lookup) */
    .word-card {
        background: white; border: 1px solid var(--card-border); border-radius: 12px;
        padding: 0.9rem 1.1rem; margin-bottom: 0.6rem;
    }
    .word-card-hi { font-family: 'Source Serif 4', Georgia, serif; font-size: 1.4rem; font-weight: 600; color: var(--ink); }
    .word-card-sub { color: var(--ink-soft); font-size: 0.92rem; margin-top: 0.1rem; }
</style>
""", unsafe_allow_html=True)


def metric_cards(items):
    """items: list of (label, value) tuples. Renders themed cards with guaranteed contrast."""
    cards_html = "".join(
        f'<div class="metric-card"><div class="label">{label}</div><div class="value">{value}</div></div>'
        for label, value in items
    )
    st.markdown(f'<div class="metric-row">{cards_html}</div>', unsafe_allow_html=True)


# ---------------------------------------------------------------
# session / progress init
# ---------------------------------------------------------------
if "progress" not in st.session_state:
    st.session_state.progress = load_progress()
    st.session_state.progress = touch_streak(st.session_state.progress)
progress = st.session_state.progress

CURRICULUM_UNITS = [
    "1. Devanagari Script Foundations",
    "2. Sounds & Speaking Basics",
    "3. Core Grammar",
    "4. Vocabulary & Conversation",
    "5. Reading & Writing Fluency",
    "6. Immersion & Fluency",
]


def mark_lesson_done(title):
    if title not in progress["lessons_completed"]:
        progress["lessons_completed"].append(title)
        save_progress(progress)


def audio_button(text, key):
    """Renders a small button that generates/plays cached TTS audio for Hindi text."""
    if st.button("🔊 Listen", key=key):
        with st.spinner("Fetching audio..."):
            path = get_audio_path(text)
        if path:
            st.audio(path)
        else:
            st.caption("⚠️ Audio needs an internet connection (first play only, then it's cached).")


def render_word_card(hindi, translit, english, pos=None, audio_key="", extra=None):
    """Card layout for a dictionary/search result — keeps the audio player at full
    card width so its play/volume controls never get compacted away.
    `extra` is metadata (e.g. "Vocabulary · Drinks") shown in the subtitle."""
    pos_html = f'<span class="pill">{pos}</span>' if pos else ""
    extra_html = f" · {extra}" if extra else ""
    st.markdown(
        f"""<div class="word-card">
            <div class="word-card-hi">{hindi}</div>
            <div class="word-card-sub"><em>{translit}</em> — {english}{extra_html} {pos_html}</div>
        </div>""",
        unsafe_allow_html=True,
    )
    audio_button(hindi, audio_key)


# ---------------------------------------------------------------
# My Storyline — chapter quiz engine (shared across all 50 chapters)
# ---------------------------------------------------------------
def _build_storyline_questions(ch):
    n = ch["n_questions"]
    qtype = ch["quiz_type"]
    questions = []
    if qtype == "static":
        pool = ch["quiz_static"]
        chosen = random.sample(pool, min(n, len(pool)))
        for q in chosen:
            opts = q["options"][:]
            random.shuffle(opts)
            questions.append({"prompt": q["prompt"], "options": opts, "answer": q["answer"]})
    elif qtype == "letters":
        pool = ch["quiz_pool"]
        chosen = random.sample(pool, min(n, len(pool)))
        for item in chosen:
            q = mcq_from_letters(pool, item)
            questions.append({
                "prompt": f"**{q['question']}** — which is the correct transliteration?",
                "options": q["options"], "answer": q["correct"],
            })
    elif qtype == "vocab":
        pool = ch["quiz_pool"]
        chosen = random.sample(pool, min(n, len(pool)))
        for item in chosen:
            direction = random.choice(["hi_to_en", "en_to_hi"])
            q = mcq_from_vocab(pool, item, direction)
            prompt = f"**{q['question']}** means:" if direction == "hi_to_en" else f"\"{q['question']}\" in Hindi is:"
            questions.append({"prompt": prompt, "options": q["options"], "answer": q["correct"]})
    elif qtype == "verb":
        cfg = ch["quiz_verb"]
        for _ in range(n):
            vkey = random.choice(cfg["keys"])
            tense = random.choice(cfg["tenses"])
            pronoun = random.choice(PRONOUNS)
            gender_idx = random.choice([0, 1])
            q = mcq_from_verb_form(VERBS, vkey, tense, pronoun, gender_idx)
            gender_word = "masculine" if gender_idx == 0 else "feminine"
            prompt = f"Conjugate **{q['verb']['hi']}** ({q['verb']['meaning']}) for *{PRONOUN_LABELS[pronoun]}*, {gender_word}, {tense} tense:"
            questions.append({"prompt": prompt, "options": q["options"], "answer": q["correct"]})
    random.shuffle(questions)
    return questions


def render_chapter_quiz(ch, progress):
    key = f"story_{ch['id']}"
    state = st.session_state.setdefault(key, {})
    if "questions" not in state:
        state["questions"] = _build_storyline_questions(ch)
        state["idx"] = 0
        state["score"] = 0
        state["answered"] = False

    total = len(state["questions"])
    if total == 0:
        st.warning("This chapter has no quiz questions configured.")
        return

    if state["idx"] >= total:
        pct = round(100 * state["score"] / total)
        passed = pct >= ch["pass_pct"]
        sl = progress["storyline"]
        prev_best = sl["scores"].get(ch["id"], 0)
        if pct > prev_best:
            sl["scores"][ch["id"]] = pct
        newly_mastered = passed and ch["id"] not in sl["completed"]
        if newly_mastered:
            sl["completed"].append(ch["id"])
        save_progress(progress)

        if passed:
            st.success(f"🎉 Chapter mastered! Score: {state['score']}/{total} ({pct}%)")
            if newly_mastered:
                st.balloons()
        else:
            st.warning(f"Score: {state['score']}/{total} ({pct}%) — you need {ch['pass_pct']}% to master this chapter. Give it another go!")
        if st.button("🔁 Retry this chapter's quiz", key=f"{key}_retry"):
            del st.session_state[key]
            st.rerun()
        return

    q = state["questions"][state["idx"]]
    st.caption(f"Question {state['idx'] + 1} of {total} · Score so far: {state['score']}")
    st.markdown(q["prompt"])
    choice = st.radio("Your answer:", q["options"], key=f"{key}_choice_{state['idx']}", label_visibility="collapsed")

    if not state["answered"]:
        if st.button("Check answer", key=f"{key}_check_{state['idx']}"):
            state["answered"] = True
            state["last_correct"] = (choice == q["answer"])
            if state["last_correct"]:
                state["score"] += 1
            st.rerun()
    else:
        if state["last_correct"]:
            st.success("Correct! ✅")
        else:
            st.error(f"Not quite — correct answer: **{q['answer']}**")
        if st.button("Next question →", key=f"{key}_next_{state['idx']}"):
            state["idx"] += 1
            state["answered"] = False
            st.rerun()


# =========================================================
# SIDEBAR NAV
# =========================================================
st.sidebar.markdown('<div class="sidebar-brand">🇮🇳 हिंदी सीखें</div>', unsafe_allow_html=True)
st.sidebar.caption("Full self-paced Hindi course")
st.sidebar.markdown(f"""
<div class="sidebar-user">
    <div class="avatar">{USER_NAME[0]}</div>
    <div>
        <div class="name">{USER_NAME}</div>
        <div class="sub">Learning Hindi</div>
    </div>
</div>
""", unsafe_allow_html=True)
page = st.sidebar.radio("Navigate", [
    "🏠 Home",
    "🛤️ My Storyline",
    "📖 Learn (Curriculum)",
    "🔤 Script Trainer",
    "🗣️ Pronunciation",
    "🗂️ Vocabulary & Flashcards",
    "💬 Phrases",
    "🔁 Verb Trainer",
    "📝 Homework",
    "🔍 Dictionary Search",
    "📊 My Progress",
], label_visibility="collapsed")

st.sidebar.divider()
with st.sidebar:
    metric_cards([("🔥 Streak", progress["streak"]["count"]), ("📚 Lessons", len(progress["lessons_completed"]))])
st.sidebar.caption("144,000+ word dictionary · 15 conjugated verbs · 185 core vocab words")

# =========================================================
# HOME
# =========================================================
if page == "🏠 Home":
    st.markdown(f"""
    <div class="hero">
        <div class="greeting">👋 Welcome back, {USER_NAME}</div>
        <h1>🇮🇳 हिंदी सीखें — Learn Hindi</h1>
        <p>A complete, self-paced Hindi course — script, sounds, grammar, vocabulary, verbs,
        pronunciation, and a 144,000-word dictionary — built for English/French speakers starting from zero.</p>
    </div>
    """, unsafe_allow_html=True)

    metric_cards([
        ("Streak", f"{progress['streak']['count']} 🔥"),
        ("Dictionary words", "144,000+"),
        ("Verbs available", len(VERBS)),
        ("Lessons completed", len(progress["lessons_completed"])),
    ])

    st.divider()

    left, right = st.columns([2, 1])
    with left:
        st.subheader("Your Learning Path")
        for i, unit in enumerate(CURRICULUM_UNITS):
            done = unit in progress["lessons_completed"]
            st.checkbox(unit, value=done, key=f"home_unit_{i}", disabled=True)

        next_unit = next((u for u in CURRICULUM_UNITS if u not in progress["lessons_completed"]), None)
        if next_unit:
            st.info(f"👉 **Recommended next step:** {next_unit} — open it in **Learn (Curriculum)**.")
        else:
            st.success("You've marked every unit complete! Keep sharpening with Homework and Flashcards.")

    with right:
        st.subheader("📖 Word of the Day")
        df = load_dictionary()
        import datetime
        wod = word_of_the_day(df, datetime.date.today().isoformat())
        st.markdown(f"<div class='devnote'>{wod['hindi']}</div>", unsafe_allow_html=True)
        st.write(f"*{wod['translit']}* — {wod['english']}")
        audio_button(wod["hindi"], "wod_audio")

    st.divider()
    st.subheader("Where to start")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("**🆕 New to Hindi?**")
        st.write("Start with **Script Trainer** to learn Devanagari, then **Pronunciation** to nail the sounds.")
    with c2:
        st.markdown("**📘 Know the script?**")
        st.write("Jump into **Learn → Core Grammar**, then drill in **Verb Trainer** and **Homework**.")
    with c3:
        st.markdown("**💬 Want conversation?**")
        st.write("Use **Vocabulary & Flashcards** plus **Phrases**, organized by real-life situation.")

# =========================================================
# MY STORYLINE
# =========================================================
elif page == "🛤️ My Storyline":
    sl = progress["storyline"]
    completed_ids = set(sl["completed"])
    total_chapters = len(STORYLINE_CHAPTERS)

    def _unlocked(idx):
        return idx == 0 or STORYLINE_CHAPTERS[idx - 1]["id"] in completed_ids

    open_id = st.session_state.get("storyline_open_chapter")

    # ---------------- CHAPTER DETAIL VIEW ----------------
    if open_id and open_id in STORYLINE_BY_ID:
        ch = STORYLINE_BY_ID[open_id]
        idx = ch["num"] - 1
        if not _unlocked(idx):
            st.warning("This chapter isn't unlocked yet — master the previous one first.")
            st.session_state.storyline_open_chapter = None
        else:
            if st.button("← Back to roadmap"):
                st.session_state.storyline_open_chapter = None
                st.rerun()
            st.caption(f"{ch['level']} · {CEFR_LABELS[ch['level']]} · Chapter {ch['num']} of {total_chapters}")
            st.title(ch["title"])
            st.markdown(f"*{ch['hook']}*")
            st.divider()
            for sec in ch["sections"]:
                st.subheader(sec["heading"])
                st.markdown(sec["body"])
            st.divider()
            st.subheader("✅ Master this chapter")
            if ch["id"] in completed_ids:
                st.success(f"Already mastered — best score: {sl['scores'].get(ch['id'], 0)}%. Retry any time to improve it.")
            st.caption(f"Score {ch['pass_pct']}% or higher across {ch['n_questions']} questions to unlock the next chapter.")
            render_chapter_quiz(ch, progress)

    # ---------------- ROADMAP VIEW ----------------
    else:
        next_idx = next((i for i, c in enumerate(STORYLINE_CHAPTERS) if c["id"] not in completed_ids), None)
        current_level = STORYLINE_CHAPTERS[next_idx]["level"] if next_idx is not None else "C1"

        st.markdown(f"""
        <div class="hero">
            <div class="greeting">🛤️ {USER_NAME}'s path from zero to fluent</div>
            <h1>My Storyline</h1>
            <p>One linear path, {total_chapters} chapters, from absolute beginner (A1) all the way to
            strong intermediate/advanced (B2/C1). Each chapter unlocks the next once you master it.</p>
        </div>
        """, unsafe_allow_html=True)

        done = len(completed_ids)
        st.progress(done / total_chapters, text=f"{done} / {total_chapters} chapters mastered")

        if next_idx is None:
            metric_cards([("Status", "🏆 All chapters mastered!"), ("Chapters", f"{total_chapters} / {total_chapters}")])
            st.success("You've completed the entire Storyline — genuinely a C1 milestone. See the final chapter for what to do next.")
        else:
            metric_cards([
                ("Chapters mastered", f"{done} / {total_chapters}"),
                ("Current level", f"{current_level} · {CEFR_LABELS[current_level]}"),
                ("Up next", f"Ch. {STORYLINE_CHAPTERS[next_idx]['num']}: {STORYLINE_CHAPTERS[next_idx]['title']}"),
            ])

        st.divider()

        for level in STORYLINE_LEVELS:
            level_chapters = [c for c in STORYLINE_CHAPTERS if c["level"] == level]
            level_done = sum(1 for c in level_chapters if c["id"] in completed_ids)
            expanded = (level == current_level)
            with st.expander(f"**{level} · {CEFR_LABELS[level]}**  —  {level_done}/{len(level_chapters)} chapters mastered", expanded=expanded):
                for c in level_chapters:
                    idx = c["num"] - 1
                    unlocked = _unlocked(idx)
                    mastered = c["id"] in completed_ids
                    icon = "✅" if mastered else ("🔓" if unlocked else "🔒")
                    col1, col2, col3 = st.columns([0.5, 5, 1.3])
                    col1.markdown(f"### {icon}")
                    col2.markdown(f"**{c['num']}. {c['title']}**")
                    col2.caption(c["hook"])
                    if mastered:
                        col3.caption(f"Best: {sl['scores'].get(c['id'], 0)}%")
                    if unlocked:
                        if col3.button("Open", key=f"roadmap_open_{c['id']}"):
                            st.session_state.storyline_open_chapter = c["id"]
                            st.rerun()
                    else:
                        col3.caption("🔒 Locked")

# =========================================================
# LEARN (CURRICULUM)
# =========================================================
elif page == "📖 Learn (Curriculum)":
    st.title("📖 Learn — Full Curriculum")
    tabs = st.tabs(CURRICULUM_UNITS)

    with tabs[0]:
        st.markdown("### Devanagari Script Foundations")
        st.write("Go to **🔤 Script Trainer** for the full interactive letter charts, matras, "
                  "conjuncts, and reading ladder — plus quizzes and audio.")
        if st.button("Mark this unit complete", key="u1done"):
            mark_lesson_done(CURRICULUM_UNITS[0]); st.success("Marked complete!")

    with tabs[1]:
        st.markdown("### Sounds & Speaking Basics")
        st.write("Full pronunciation training is now in its own **🗣️ Pronunciation** tab. Pronouns, "
                  "numbers, days, and survival phrases are in **Vocabulary & Flashcards** and **Phrases**.")
        st.markdown("""
**Shadowing technique (practice daily):**
1. Pick a 1–2 min native-speaker clip.
2. Listen once for meaning.
3. Listen again reading a transcript.
4. Speak along in real time — match rhythm, not just words.
5. Record yourself and compare against the original.
""")
        if st.button("Mark this unit complete", key="u2done"):
            mark_lesson_done(CURRICULUM_UNITS[1]); st.success("Marked complete!")

    with tabs[2]:
        st.markdown("### Core Grammar")
        for lesson in GRAMMAR_LESSONS:
            with st.expander(lesson["title"]):
                st.markdown(lesson["content"])
                done = lesson["title"] in progress["lessons_completed"]
                if st.checkbox("Mark complete", value=done, key=f"gram_{lesson['title']}"):
                    mark_lesson_done(lesson["title"])
        st.info("Once you've read these, drill them in **🔁 Verb Trainer** and **📝 Homework**.")

    with tabs[3]:
        st.markdown("### Vocabulary & Conversation")
        st.write("Full themed vocabulary with flashcard practice is in **Vocabulary & Flashcards**. "
                  "Sample real-world dialogues:")
        st.markdown("**At a Restaurant**")
        st.code("ग्राहक — नमस्ते, मेनू दिखाइए।\nवेटर — जी हाँ, यह लीजिए।\n"
                "ग्राहक — एक दाल और दो रोटी दीजिए।\nवेटर — पीने के लिए क्या लेंगे?\n"
                "ग्राहक — एक पानी की बोतल, कृपया।\nवेटर — जी ज़रूर।\nग्राहक — बिल दीजिए, कृपया।", language=None)
        st.markdown("**Asking for Directions**")
        st.code("पर्यटक — माफ़ कीजिए, स्टेशन कहाँ है?\nराहगीर — सीधे जाइए, फिर दायें मुड़िए।\n"
                "पर्यटक — कितनी दूर है?\nराहगीर — बस पांच मिनट।\nपर्यटक — धन्यवाद!\nराहगीर — कोई बात नहीं।", language=None)
        if st.button("Mark this unit complete", key="u4done"):
            mark_lesson_done(CURRICULUM_UNITS[3]); st.success("Marked complete!")

    with tabs[4]:
        st.markdown("### Reading & Writing Fluency")
        st.markdown("""
**Connecting words** you need to move beyond short simple sentences:

| Hindi | Meaning |
|---|---|
| और | and |
| लेकिन / पर | but |
| क्योंकि | because |
| इसलिए | therefore |
| अगर...तो | if...then |
| जब | when |
""")
        st.code("मेरा नाम मार्क है। मैं फ्रांस से हूँ, लेकिन अब मैं भारत में रहता हूँ। "
                "मुझे हिंदी सीखना बहुत पसंद है, क्योंकि यह एक सुंदर भाषा है। हर दिन मैं एक घंटा "
                "हिंदी पढ़ता हूँ और थोड़ा लिखता भी हूँ। मेरे दोस्त मेरी मदद करते हैं, इसलिए मैं जल्दी सीख रहा हूँ।",
                language=None)
        st.caption("My name is Mark. I am from France, but now I live in India. I really like learning "
                   "Hindi because it is a beautiful language. Every day I study Hindi for an hour and "
                   "also write a little. My friends help me, so I am learning quickly.")
        if st.button("Mark this unit complete", key="u5done"):
            mark_lesson_done(CURRICULUM_UNITS[4]); st.success("Marked complete!")

    with tabs[5]:
        st.markdown("### Immersion & Fluency Milestones")
        for stage, desc in CEFR_MILESTONES:
            st.markdown(f"**{stage}** — {desc}")
        st.write("Watch Hindi shows with Hindi subtitles, listen to podcasts/music daily, and have a "
                 "weekly unscripted conversation with a tutor or exchange partner.")
        if st.button("Mark this unit complete", key="u6done"):
            mark_lesson_done(CURRICULUM_UNITS[5]); st.success("Marked complete!")

# =========================================================
# SCRIPT TRAINER
# =========================================================
elif page == "🔤 Script Trainer":
    st.title("🔤 Devanagari Script Trainer")
    sub = st.tabs(["Vowels", "Consonants", "Matras", "Special Marks", "Conjuncts", "Reading Ladder", "Quiz Me"])

    with sub[0]:
        for v in VOWELS:
            c1, c2, c3, c4, c5 = st.columns([1, 1, 3, 3, 1])
            c1.markdown(f"## {v['hi']}")
            c2.markdown(f"**{v['translit']}**")
            c3.write(v["sound"]); c4.write(v["example"])
            with c5:
                audio_button(v["hi"], f"vaudio_{v['hi']}")

    with sub[1]:
        for g in CONSONANT_GROUPS:
            st.markdown(f"#### {g['group']}" + (f" — *{g['note']}*" if g["note"] else ""))
            for l in g["letters"]:
                c1, c2, c3, c4, c5 = st.columns([1, 1, 3, 3, 1])
                c1.markdown(f"## {l['hi']}")
                c2.markdown(f"**{l['translit']}**")
                c3.write(l["sound"]); c4.write(l["example"])
                with c5:
                    audio_button(l["hi"], f"caudio_{l['hi']}")

    with sub[2]:
        st.write("Vowel signs (matras) attached to क:")
        for m in MATRAS:
            c1, c2, c3 = st.columns([3, 2, 2])
            c1.write(m["mark"]); c2.markdown(f"## {m['with_ka']}"); c3.write(m["sound"])
        st.info("The ि matra is written BEFORE its consonant but pronounced AFTER — कि = 'ki'.")

    with sub[3]:
        for m in SPECIAL_MARKS:
            c1, c2, c3, c4 = st.columns([1, 2, 4, 3])
            c1.markdown(f"## {m['mark']}"); c2.write(f"**{m['name']}**")
            c3.write(m["function"]); c4.write(m["example"])

    with sub[4]:
        for c in CONJUNCTS:
            c1, c2, c3 = st.columns([1, 2, 3])
            c1.markdown(f"## {c['conjunct']}"); c2.write(c["built_from"]); c3.write(c["example"])

    with sub[5]:
        for lvl in READING_LADDER:
            st.markdown(f"**Level {lvl['level']}**")
            for word in lvl["words"]:
                cc1, cc2 = st.columns([5, 1])
                cc1.write(f"{word[0]}  —  *{word[1]}*  —  {word[2]}")
                with cc2:
                    audio_button(word[0], f"ladder_{word[0]}")

    with sub[6]:
        st.write("Test your letter recognition.")
        if "letter_quiz_item" not in st.session_state or st.button("New question"):
            st.session_state.letter_quiz_item = random.choice(ALL_LETTERS)
            st.session_state.letter_quiz_q = mcq_from_letters(ALL_LETTERS, st.session_state.letter_quiz_item)
        q = st.session_state.letter_quiz_q
        st.markdown(f"# {q['question']}")
        choice = st.radio("What sound is this?", q["options"], key="letter_quiz_choice")
        if st.button("Check answer", key="letter_quiz_check"):
            if choice == q["correct"]:
                st.success("Correct! ✅")
                if q["item"]["hi"] not in progress["letters_known"]:
                    progress["letters_known"].append(q["item"]["hi"]); save_progress(progress)
            else:
                st.error(f"Not quite — correct answer: **{q['correct']}**")
        st.caption(f"Letters marked known: {len(progress['letters_known'])} / {len(ALL_LETTERS)}")

# =========================================================
# PRONUNCIATION
# =========================================================
elif page == "🗣️ Pronunciation":
    st.title("🗣️ Pronunciation")
    st.markdown(PRONUNCIATION_INTRO)

    tool_tab, learn_tab = st.tabs(["🔧 Pronounce Any Word", "📘 Sound System Deep-Dive"])

    with tool_tab:
        st.write("Type a Hindi word (Devanagari) **or** an English word to look up — get the "
                 "transliteration and hear it spoken aloud.")
        query = st.text_input("Word", placeholder="e.g. पानी, address, namaste...")
        if query:
            df = load_dictionary()
            # if query is Devanagari, transliterate directly
            if any('\u0900' <= ch <= '\u097F' for ch in query):
                st.markdown(f"<div class='devnote'>{query}</div>", unsafe_allow_html=True)
                st.write(f"Transliteration: **{transliterate(query)}**")
                audio_button(query, "tool_audio_direct")
            else:
                results = search_dictionary(df, query, limit=10)
                if results.empty:
                    st.warning("No match found in the dictionary — try the Dictionary Search page for fuzzier matching.")
                else:
                    for i, r in results.iterrows():
                        render_word_card(
                            r["hindi"], r["translit"], r["english"], pos=r["pos"],
                            audio_key=f"tool_audio_{i}",
                        )

    with learn_tab:
        st.markdown(VOWEL_LENGTH_NOTE)
        st.markdown(ASPIRATION_NOTE)
        st.markdown(RETROFLEX_NOTE)
        st.markdown(NASAL_NOTE)
        st.markdown(STRESS_NOTE)
        st.markdown(SYLLABLE_TIPS)

# =========================================================
# VOCABULARY & FLASHCARDS
# =========================================================
elif page == "🗂️ Vocabulary & Flashcards":
    st.title("🗂️ Vocabulary & Flashcards")
    mode = st.radio("Mode", ["Browse by theme", "Flashcard review (spaced repetition)", "Multiple-choice quiz"], horizontal=True)

    if mode == "Browse by theme":
        theme = st.selectbox("Theme", list(VOCAB.keys()))
        for item in VOCAB[theme]:
            g = f" ({item['gender']})" if item.get("gender") else ""
            c1, c2 = st.columns([6, 1])
            c1.write(f"**{item['hi']}**{g}  —  *{item['translit']}*  —  {item['en']}")
            with c2:
                audio_button(item["hi"], f"vocab_audio_{theme}_{item['hi']}")

    elif mode == "Flashcard review (spaced repetition)":
        flat = all_vocab_flat()
        due_keys = [f"vocab:{v['hi']}" for v in flat]
        n_due = due_count(progress, due_keys)
        st.caption(f"{n_due} card(s) due for review out of {len(flat)} total.")
        due_items = [v for v in flat if is_due(get_card(progress, f"vocab:{v['hi']}"))]
        if not due_items:
            st.success("No cards due right now — nice work! Come back later or browse by theme.")
        else:
            if "flash_item" not in st.session_state or st.session_state.get("flash_needs_new"):
                st.session_state.flash_item = random.choice(due_items)
                st.session_state.flash_revealed = False
                st.session_state.flash_needs_new = False
            item = st.session_state.flash_item
            st.markdown(f"<div class='devnote'>{item['hi']}</div>", unsafe_allow_html=True)
            st.caption(item["theme"])
            audio_button(item["hi"], "flash_audio")
            if not st.session_state.flash_revealed:
                if st.button("Show answer"):
                    st.session_state.flash_revealed = True
            else:
                st.markdown(f"**{item['translit']}** — {item['en']}")
                st.write("How well did you know it?")
                c1, c2, c3, c4 = st.columns(4)
                key = f"vocab:{item['hi']}"
                if c1.button("Again"):
                    review(progress, key, 0); save_progress(progress); st.session_state.flash_needs_new = True; st.rerun()
                if c2.button("Hard"):
                    review(progress, key, 1); save_progress(progress); st.session_state.flash_needs_new = True; st.rerun()
                if c3.button("Good"):
                    review(progress, key, 2); save_progress(progress); st.session_state.flash_needs_new = True; st.rerun()
                if c4.button("Easy"):
                    review(progress, key, 3); save_progress(progress); st.session_state.flash_needs_new = True; st.rerun()

    else:
        theme = st.selectbox("Quiz theme", ["All themes"] + list(VOCAB.keys()), key="quiz_theme")
        direction = st.radio("Direction", ["Hindi → English", "English → Hindi"], horizontal=True)
        pool = all_vocab_flat() if theme == "All themes" else [dict(x, theme=theme) for x in VOCAB[theme]]
        if len(pool) < 4:
            st.warning("Need at least 4 words in this theme for multiple choice.")
        else:
            if "vocab_quiz_q" not in st.session_state or st.button("New question", key="vocab_new_q"):
                item = random.choice(pool)
                d = "hi_to_en" if direction == "Hindi → English" else "en_to_hi"
                st.session_state.vocab_quiz_q = mcq_from_vocab(pool, item, d)
            q = st.session_state.vocab_quiz_q
            st.markdown(f"### {q['question']}")
            choice = st.radio("Choose the correct translation:", q["options"], key="vocab_quiz_choice")
            if st.button("Check answer", key="vocab_quiz_check"):
                score = st.session_state.get("vocab_score", [0, 0]); score[1] += 1
                if choice == q["correct"]:
                    st.success("Correct! ✅"); score[0] += 1
                else:
                    st.error(f"Not quite — correct answer: **{q['correct']}**")
                st.session_state.vocab_score = score
            if "vocab_score" in st.session_state:
                st.caption(f"Score this session: {st.session_state.vocab_score[0]} / {st.session_state.vocab_score[1]}")

# =========================================================
# PHRASES
# =========================================================
elif page == "💬 Phrases":
    st.title("💬 Conversational Phrases")
    cat = st.selectbox("Category", list(PHRASES.keys()))
    for p in PHRASES[cat]:
        c1, c2 = st.columns([6, 1])
        c1.write(f"**{p['hi']}**  —  *{p['translit']}*  —  {p['en']}")
        with c2:
            audio_button(p["hi"], f"phrase_audio_{cat}_{p['hi']}")

# =========================================================
# VERB TRAINER
# =========================================================
elif page == "🔁 Verb Trainer":
    st.title("🔁 Verb Conjugation Trainer")
    mode = st.radio("Mode", ["Browse conjugation tables", "Practice quiz"], horizontal=True)
    verb_keys = list(VERBS.keys())
    verb_labels = {k: f"{VERBS[k]['hi']} ({VERBS[k]['translit']}) — {VERBS[k]['meaning']}" for k in verb_keys}

    if mode == "Browse conjugation tables":
        vkey = st.selectbox("Choose a verb", verb_keys, format_func=lambda k: verb_labels[k])
        verb = VERBS[vkey]
        c1, c2 = st.columns([5, 1])
        c1.subheader(f"{verb['hi']} — {verb['translit']} — {verb['meaning']}")
        with c2:
            audio_button(verb["hi"], f"verb_audio_{vkey}")
        if verb.get("note"):
            st.info(verb["note"])
        tense = st.selectbox("Tense", ["present", "future", "past"], format_func=lambda t: t.capitalize())
        st.write("**Pronoun | Masculine | Feminine**")
        if tense == "past":
            labels = verb["past_subject_labels"]
            for pr in PRONOUNS:
                m, f = verb["past"][pr]
                st.write(f"{labels[pr]} — **{m}** ({transliterate(m)}, m) / **{f}** ({transliterate(f)}, f)")
            if verb["past_needs_ne"]:
                st.caption("This verb takes ने (ne) in the past, and agrees with the object, not the subject.")
        else:
            for pr in PRONOUNS:
                m, f = verb[tense][pr]
                st.write(f"{PRONOUN_LABELS[pr]} — **{m}** ({transliterate(m)}, m) / **{f}** ({transliterate(f)}, f)")

    else:
        tense = st.selectbox("Tense to practice", ["present", "future", "past"], format_func=lambda t: t.capitalize(), key="verb_quiz_tense")
        if st.button("New question", key="verb_new_q") or "verb_quiz_q" not in st.session_state:
            vkey = random.choice(verb_keys)
            pronoun = random.choice(PRONOUNS)
            gender_idx = random.choice([0, 1])
            st.session_state.verb_quiz_q = mcq_from_verb_form(VERBS, vkey, tense, pronoun, gender_idx)
        q = st.session_state.verb_quiz_q
        gender_word = "masculine" if q["gender_idx"] == 0 else "feminine"
        subj = q["verb"]["past_subject_labels"][q["pronoun"]] if tense == "past" else PRONOUN_LABELS[q["pronoun"]]
        st.markdown(f"### {subj} ___ ({q['verb']['hi']} — {q['verb']['meaning']}, {gender_word} subject, {tense} tense)")
        choice = st.radio("Choose the correct form:", q["options"], key="verb_quiz_choice")
        if st.button("Check answer", key="verb_quiz_check"):
            score = st.session_state.get("verb_score", [0, 0]); score[1] += 1
            if choice == q["correct"]:
                st.success("Correct! ✅"); score[0] += 1
            else:
                st.error(f"Not quite — correct answer: **{q['correct']}**")
            st.session_state.verb_score = score
        if "verb_score" in st.session_state:
            st.caption(f"Score this session: {st.session_state.verb_score[0]} / {st.session_state.verb_score[1]}")

# =========================================================
# HOMEWORK
# =========================================================
elif page == "📝 Homework":
    st.title("📝 Homework")
    st.write("Generate a randomized, self-checking worksheet. Type answers as transliteration "
             "(spelling doesn't need to be perfect — close phonetic matches are accepted).")

    c1, c2, c3 = st.columns(3)
    topic = c1.selectbox("Topic", ["Vocabulary", "Phrases", "Verbs", "Mixed Review"])
    n = c2.select_slider("Number of questions", options=[5, 10, 15, 20], value=10)
    if c3.button("🎲 Generate worksheet", use_container_width=True) or "hw_worksheet" not in st.session_state:
        st.session_state.hw_worksheet = build_worksheet(topic, n)
        st.session_state.hw_topic = topic
        st.session_state.hw_submitted = False

    worksheet = st.session_state.hw_worksheet
    st.divider()

    with st.form("homework_form"):
        answers = []
        for i, ex in enumerate(worksheet):
            st.markdown(f"**{i+1}.** {ex['prompt']}")
            if ex["type"] == "mcq":
                ans = st.radio("Answer", ex["options"], key=f"hw_{i}", label_visibility="collapsed")
            else:
                ans = st.text_input("Answer", key=f"hw_{i}", label_visibility="collapsed")
            answers.append(ans)
            st.write("")
        submitted = st.form_submit_button("✅ Submit Homework")

    if submitted:
        st.session_state.hw_submitted = True
        score = 0
        results = []
        for ex, ans in zip(worksheet, answers):
            if ex["type"] == "mcq":
                correct = (ans == ex["answer"])
                reveal = ex["answer"]
            else:
                correct = normalize(ans) in [normalize(a) for a in ex["accept"]] and ans.strip() != ""
                reveal = ex["reveal"]
            if correct:
                score += 1
            results.append((ex["prompt"], ans, correct, reveal))
        st.session_state.hw_results = results
        st.session_state.hw_score = score

        from datetime import date
        progress["quiz_history"].append({
            "date": date.today().isoformat(), "topic": st.session_state.hw_topic,
            "score": score, "total": len(worksheet),
        })
        save_progress(progress)

    if st.session_state.get("hw_submitted"):
        score = st.session_state.hw_score
        total = len(worksheet)
        pct = round(100 * score / total) if total else 0
        st.subheader(f"Score: {score} / {total} ({pct}%)")
        st.progress(pct / 100)
        for i, (prompt, ans, correct, reveal) in enumerate(st.session_state.hw_results):
            icon = "✅" if correct else "❌"
            with st.expander(f"{icon} Question {i+1}"):
                st.markdown(prompt)
                st.write(f"Your answer: *{ans or '(blank)'}*")
                if not correct:
                    st.write(f"Correct answer: **{reveal}**")

# =========================================================
# DICTIONARY SEARCH
# =========================================================
elif page == "🔍 Dictionary Search":
    st.title("🔍 Dictionary Search")
    tab1, tab2 = st.tabs(["📚 Full Dictionary (144,000+ words)", "⭐ Quick Reference (curated)"])

    with tab1:
        st.write("Search the complete dictionary in Hindi, transliteration, or English.")
        df = load_dictionary()
        c1, c2 = st.columns([3, 1])
        query = c1.text_input("Search", placeholder="e.g. address, location, पानी, khaana...", key="full_dict_q")
        pos_options = ["All"] + sorted(df["pos"].unique().tolist())
        pos_filter = c2.selectbox("Part of speech", pos_options)

        if query:
            results = search_dictionary(df, query, pos_filter=pos_filter, limit=150)
            st.caption(f"Showing {len(results)} result(s)" + (" (capped at 150 — refine your search)" if len(results) == 150 else "") + " — each with meaning, pronunciation, and audio.")
            for idx, r in results.iterrows():
                render_word_card(
                    r["hindi"], r["translit"], r["english"], pos=r["pos"],
                    audio_key=f"dict_audio_{idx}",
                )
        else:
            st.info("Start typing to search 144,000+ dictionary entries.")

    with tab2:
        st.write("Search across curated vocabulary, phrases, verbs, and script letters.")
        if "search_index" not in st.session_state:
            st.session_state.search_index = build_index()
        query2 = st.text_input("Search curated content", key="curated_q")
        if query2:
            results2 = search(st.session_state.search_index, query2)
            st.caption(f"{len(results2)} result(s)")
            type_to_pos = {"Vocabulary": "noun", "Verb": "verb"}
            for i, r in enumerate(results2[:100]):
                render_word_card(
                    r["hi"], r["translit"], r["en"],
                    pos=type_to_pos.get(r["type"]),
                    extra=f"{r['type']} · {r['category']}",
                    audio_key=f"curated_audio_{i}",
                )
        else:
            st.info("Start typing to search the curated dictionary.")

# =========================================================
# PROGRESS
# =========================================================
elif page == "📊 My Progress":
    st.title(f"📊 {USER_NAME}'s Progress")
    metric_cards([
        ("Streak", f"{progress['streak']['count']} day(s) 🔥"),
        ("Letters known", f"{len(progress['letters_known'])} / {len(ALL_LETTERS)}"),
        ("Lessons completed", len(progress["lessons_completed"])),
        ("Homework sets done", len(progress["quiz_history"])),
    ])

    st.subheader("Curriculum checklist")
    for unit in CURRICULUM_UNITS:
        st.checkbox(unit, value=unit in progress["lessons_completed"], disabled=True, key=f"prog_{unit}")
    for lesson in GRAMMAR_LESSONS:
        st.checkbox(f"Grammar: {lesson['title']}", value=lesson["title"] in progress["lessons_completed"], disabled=True, key=f"prog_g_{lesson['title']}")

    st.subheader("Flashcards due today")
    flat = all_vocab_flat()
    due_keys = [f"vocab:{v['hi']}" for v in flat]
    st.write(f"{due_count(progress, due_keys)} card(s) due — head to Vocabulary & Flashcards to review them.")

    st.subheader("Homework history")
    if progress["quiz_history"]:
        for h in reversed(progress["quiz_history"][-15:]):
            pct = round(100 * h["score"] / h["total"]) if h["total"] else 0
            st.write(f"{h['date']} — **{h['topic']}** — {h['score']}/{h['total']} ({pct}%)")
    else:
        st.caption("No homework completed yet — visit the Homework page to get started.")

    st.divider()
    if st.button("⚠️ Reset all progress"):
        from utils.storage import DEFAULT_PROGRESS
        import json
        st.session_state.progress = json.loads(json.dumps(DEFAULT_PROGRESS))
        save_progress(st.session_state.progress)
        st.success("Progress reset."); st.rerun()
