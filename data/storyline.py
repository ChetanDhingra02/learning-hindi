"""
My Storyline — a single linear, chapter-by-chapter Hindi curriculum.

Unlike the free-roaming reference pages elsewhere in the app, this module defines
one fixed path from absolute zero (CEFR A1) to strong intermediate/advanced (B2/C1).
Each chapter must be "mastered" (pass its quiz) before the next one unlocks.

Chapter dict shape:
    id            unique string id, also used as the storage key
    num           1-based order in the path
    level         CEFR band: "A1" | "A2" | "B1" | "B2" | "C1"
    title         short chapter title
    hook          one-line motivating framing shown at the top of the chapter
    sections      list of {"heading": str, "body": markdown str} — the actual lesson
    quiz_type     "letters" | "vocab" | "verb" | "static"
    quiz_pool     for "letters"/"vocab": a list of data dicts to quiz from
    quiz_verb     for "verb": {"keys": [...verb keys...], "tenses": [...]}
    quiz_static   for "static": list of {"prompt","options","answer"} MCQs
    pass_pct      integer 0-100, minimum score to master the chapter (default 70)
    n_questions   how many questions to ask per attempt (default 6)
"""

from data.alphabet import VOWELS, CONSONANT_GROUPS, MATRAS, SPECIAL_MARKS, CONJUNCTS
from data.vocab import VOCAB
from data.phrases import PHRASES
from data.verbs import VERBS

_ALL_CONSONANTS = [l for g in CONSONANT_GROUPS for l in g["letters"]]

CEFR_LABELS = {
    "A1": "Beginner",
    "A2": "Elementary",
    "B1": "Intermediate",
    "B2": "Upper-Intermediate",
    "C1": "Advanced",
}

_CHAPTERS_RAW = [
    # =====================================================================
    # A1 — BEGINNER: the script, sounds, and absolute survival basics
    # =====================================================================
    {
        "level": "A1", "title": "Welcome — How Hindi Works",
        "hook": "Before any words, let's see the shape of the language you're about to learn.",
        "sections": [
            {"heading": "The big picture", "body": """
Hindi is written in **Devanagari**, a script where letters are grouped left-to-right
just like English, but where **vowels attach to consonants as small marks** rather
than standing alone in the middle of a word most of the time.

Three things make Hindi very learnable for an English/French speaker:
- It's spelled **exactly as it sounds** — once you know the script, you can read any word aloud correctly, unlike English.
- Grammar is **regular** — very few irregular verbs, no irregular plurals to memorize case by case.
- A huge amount of vocabulary is **shared with English** (bus, ticket, school, table) thanks to loanwords.

One thing that will feel new: the **verb comes at the end** of the sentence, and adjectives/possessives
change form to agree with gender — like French, but Hindi also makes the *verb* agree with gender.
"""},
            {"heading": "What's ahead", "body": """
This Storyline takes you chapter by chapter through:
1. **A1** — reading the script, sounds, and your first survival phrases
2. **A2** — building grammatically correct sentences in the present/future
3. **B1** — the past tense, politeness levels, and real unscripted conversation
4. **B2** — passive/causative verbs, conditionals, and reading/writing paragraphs
5. **C1** — register, idioms, and reading real unadapted Hindi

Each chapter ends with a short mastery check. Score high enough and the next chapter unlocks.
You can always retry a chapter as many times as you like.
"""},
        ],
        "quiz_type": "static", "pass_pct": 60, "n_questions": 3,
        "quiz_static": [
            {"prompt": "What script is Hindi written in?", "options": ["Devanagari", "Cyrillic", "Arabic script", "Hangul"], "answer": "Devanagari"},
            {"prompt": "In a Hindi sentence, where does the verb usually go?", "options": ["First", "Second", "Last", "Anywhere"], "answer": "Last"},
            {"prompt": "Is Hindi spelling generally phonetic (sounds match spelling)?", "options": ["Yes, very consistently", "No, full of silent letters", "Only for loanwords", "Only vowels are phonetic"], "answer": "Yes, very consistently"},
        ],
    },
    {
        "level": "A1", "title": "Vowels — Your First 11 Sounds",
        "hook": "Every Hindi word is built from these eleven vowel sounds. Get these right and everything else is easier.",
        "sections": [
            {"heading": "The independent vowels", "body": """
These are the **standalone** forms, used at the start of a word or on their own.
Open the **Script Trainer → Vowels** tab to hear each one, then come back and quiz yourself.

| Letter | Sounds like | Example |
|---|---|---|
""" + "\n".join(f"| {v['hi']} ({v['translit']}) | {v['sound']} | {v['example']} |" for v in VOWELS) + """

Notice the pairs: अ/आ, इ/ई, उ/ऊ — each pair is the *same* sound, just short vs. held longer.
That length difference is meaningful in Hindi — it can change a word's meaning entirely.
"""},
            {"heading": "Why this matters early", "body": """
Once attached to a consonant, most of these vowels become small marks called **matras**
(you'll meet those in a later chapter) — but they always keep the same sound. Learn the
sound here once, and you'll recognize it in every word from now on.
"""},
        ],
        "quiz_type": "letters", "quiz_pool": VOWELS, "pass_pct": 70, "n_questions": 6,
    },
    {
        "level": "A1", "title": "Consonants I — Stops (क to न)",
        "hook": "Hindi stop-consonants come in aspirated/unaspirated pairs that don't exist in English — this is where careful listening pays off.",
        "sections": [
            {"heading": "Velars, palatals, retroflex, dentals", "body": """
Hindi organizes consonants by **where in the mouth** they're made — a system that's actually
more logical than English's. The four groups below run from the back of the mouth to the front:

""" + "\n\n".join(
                f"**{g['group']}** ({g['note']}): " + "  ".join(f"{l['hi']} ({l['translit']})" for l in g["letters"])
                for g in CONSONANT_GROUPS[:4]
            ) + """

The retroflex row (ट ठ ड ढ ण) is the one with **no equivalent in English or French** — the
tongue curls back to touch the roof of the mouth. Contrast it against the dental row (त थ द ध न),
where the tongue touches the back of the teeth. Say "tomato" (टमाटर) vs "star" (तारा) and feel
the difference in tongue position.
"""},
            {"heading": "Aspiration: the puff of air", "body": """
Pairs like क/ख or ट/ठ differ only in **aspiration** — whether a puff of air follows the sound.
Hold your hand in front of your mouth: **ख** should puff air onto it, **क** should not. English
speakers do this unconsciously already (compare the "p" in "pin" vs "spin") — Hindi just makes
it meaningful for spelling and meaning.
"""},
        ],
        "quiz_type": "letters", "quiz_pool": [l for g in CONSONANT_GROUPS[:4] for l in g["letters"]], "pass_pct": 65, "n_questions": 6,
    },
    {
        "level": "A1", "title": "Consonants II — Semivowels & Sibilants (य to ह)",
        "hook": "The rest of the consonant chart — including sounds that will show up constantly in everyday speech.",
        "sections": [
            {"heading": "Labials, semivowels, sibilants, and ह", "body": """
""" + "\n\n".join(
                f"**{g['group']}** ({g['note']}): " + "  ".join(f"{l['hi']} ({l['translit']})" for l in g["letters"])
                for g in CONSONANT_GROUPS[4:]
            ) + """

**स** (sa) and **श** (sha) are the two you'll hear constantly (स is far more common day-to-day);
**ह** (ha) shows up in many high-frequency words like है (hai, "is") and हाँ (haan, "yes").
"""},
        ],
        "quiz_type": "letters", "quiz_pool": [l for g in CONSONANT_GROUPS[4:] for l in g["letters"]], "pass_pct": 65, "n_questions": 6,
    },
    {
        "level": "A1", "title": "Matras — Attaching Vowels to Consonants",
        "hook": "In real words, vowels rarely stand alone — they attach to the consonant before them as a small mark.",
        "sections": [
            {"heading": "The matra chart", "body": """
Here's every vowel mark attached to क (ka), so you can see the pattern that repeats on
every consonant in the language:

| Vowel mark | क + mark | Sound |
|---|---|---|
""" + "\n".join(f"| {m['mark'] if m['mark'] else '(none — inherent अ)'} | {m['with_ka']} | {m['sound']} |" for m in MATRAS) + """
"""},
            {"heading": "The one everyone trips on", "body": """
The **ि** matra (short i) is written **before** its consonant but pronounced **after** it:
**कि** is written क + ि but read "ki", not "ik". Every other matra in the chart above is
written in reading order. This is the single most common beginner mistake — expect it,
and read words a syllable at a time until it becomes automatic.
"""},
        ],
        "quiz_type": "static", "pass_pct": 65, "n_questions": 5,
        "quiz_static": [
            {"prompt": "क with no vowel mark at all is pronounced:", "options": ["ka", "k", "kaa", "ki"], "answer": "ka"},
            {"prompt": "Which matra is written BEFORE its consonant but read AFTER it?", "options": ["ि (i)", "ा (aa)", "ी (ii)", "ु (u)"], "answer": "ि (i)"},
            {"prompt": "How do you write \"ki\" (कि)?", "options": ["क + ि", "ि + क", "क + ी", "इ + क"], "answer": "क + ि"},
            {"prompt": "What does the ा matra do to क?", "options": ["Makes it 'kaa'", "Makes it silent", "Makes it 'ki'", "Makes it a conjunct"], "answer": "Makes it 'kaa'"},
            {"prompt": "Devanagari vowel marks are called:", "options": ["Matras", "Visargas", "Conjuncts", "Anusvaras"], "answer": "Matras"},
        ],
    },
    {
        "level": "A1", "title": "Nasal Marks, Visarga & Conjuncts",
        "hook": "A handful of extra marks and letter-combinations round out everything you need to read any Hindi word.",
        "sections": [
            {"heading": "Special marks", "body": """
| Mark | Name | What it does | Example |
|---|---|---|---|
""" + "\n".join(f"| {m['mark']} | {m['name']} | {m['function']} | {m['example']} |" for m in SPECIAL_MARKS) + """
"""},
            {"heading": "Conjuncts: two consonants fused together", "body": """
When two consonants occur with no vowel between them, Devanagari often **fuses** them into
a single glyph called a **conjunct**, rather than writing them side by side:

| Conjunct | Built from | Example |
|---|---|---|
""" + "\n".join(f"| {c['conjunct']} | {c['built_from']} | {c['example']} |" for c in CONJUNCTS) + """

Don't try to memorize every conjunct up front — recognize that they exist, and you'll
absorb the common ones naturally through reading practice in later chapters.
"""},
        ],
        "quiz_type": "static", "pass_pct": 65, "n_questions": 4,
        "quiz_static": [
            {"prompt": "The dot above a letter (ं) that nasalizes the vowel is called:", "options": ["Anusvara", "Visarga", "Virama", "Matra"], "answer": "Anusvara"},
            {"prompt": "A small diagonal stroke below a letter that removes its inherent 'a' sound is called:", "options": ["Virama / halant", "Anusvara", "Chandrabindu", "Matra"], "answer": "Virama / halant"},
            {"prompt": "When two consonants fuse into one glyph with no vowel between them, this is called a:", "options": ["Conjunct", "Digraph", "Ligature only in English", "Diphthong"], "answer": "Conjunct"},
            {"prompt": "ज्ञ (used in ज्ञान, \"knowledge\") is an example of a:", "options": ["Conjunct", "Matra", "Visarga", "Vowel"], "answer": "Conjunct"},
        ],
    },
    {
        "level": "A1", "title": "Greetings & Introducing Yourself",
        "hook": "Your first real conversation — say hello, ask how someone is, and say your name.",
        "sections": [
            {"heading": "Core greetings", "body": "\n".join(f"- **{p['hi']}** ({p['translit']}) — {p['en']}" for p in PHRASES["Greetings"])},
            {"heading": "Politeness basics", "body": "\n".join(f"- **{p['hi']}** ({p['translit']}) — {p['en']}" for p in PHRASES["Politeness"])},
            {"heading": "Putting it together", "body": """
A typical first exchange:

> **A: नमस्ते! आप कैसे हैं?** (namaste! aap kaise hain?) — Hello! How are you?
> **B: मैं ठीक हूँ, धन्यवाद। आप?** (main Theek hoon, dhanyavaad. aap?) — I'm fine, thank you. You?
> **A: मैं भी ठीक हूँ।** (main bhee Theek hoon.) — I'm fine too.

**नमस्ते** works for both "hello" and "goodbye," at any time of day, with anyone —
it's the one word you truly cannot get wrong.
"""},
        ],
        "quiz_type": "vocab", "quiz_pool": PHRASES["Greetings"] + PHRASES["Politeness"], "pass_pct": 70, "n_questions": 6,
    },
    {
        "level": "A1", "title": "Numbers 1–20",
        "hook": "Numbers are everywhere — prices, time, phone numbers. Lock in 1 through 20 now.",
        "sections": [
            {"heading": "1 to 20", "body": "\n".join(f"- **{v['hi']}** ({v['translit']}) — {v['en']}" for v in VOCAB["Numbers 1-20"])},
            {"heading": "A quirk to know", "body": """
Unlike French or German, Hindi numbers **don't follow a small repeating pattern** after 10 —
each number from 1 to 100 has traditionally been treated as close to its own word (though you'll
spot family resemblances once you know them). This is genuinely just memorization — flashcards
in **Vocabulary & Flashcards** will help this stick.
"""},
        ],
        "quiz_type": "vocab", "quiz_pool": VOCAB["Numbers 1-20"], "pass_pct": 70, "n_questions": 6,
    },
    {
        "level": "A1", "title": "Pronouns & \"To Be\" in the Present",
        "hook": "The single most-used verb in the language: होना (honaa), \"to be.\"",
        "sections": [
            {"heading": "Pronouns", "body": "\n".join(f"- **{v['hi']}** ({v['translit']}) — {v['en']}" for v in VOCAB["Pronouns"])},
            {"heading": "होना (to be) — present tense", "body": """
| Pronoun | Form | Meaning |
|---|---|---|
| मैं (main) | हूँ (hoon) | I am |
| तू / तुम (too / tum) | है / हो (hai / ho) | you are (intimate / informal) |
| वह / यह (vah / yah) | है (hai) | he/she/it/that/this is |
| हम (ham) | हैं (hain) | we are |
| आप (aap) | हैं (hain) | you are (formal) |
| वे / ये (ve / ye) | हैं (hain) | they are |

**मैं ठीक हूँ** (main Theek hoon) — I am fine.
**वह डॉक्टर है** (vah doctor hai) — He/she is a doctor.
**हम भारत से हैं** (ham bhaarat se hain) — We are from India.
"""},
        ],
        "quiz_type": "static", "pass_pct": 70, "n_questions": 6,
        "quiz_static": [
            {"prompt": "\"I am\" in Hindi is:", "options": ["मैं हूँ", "मैं है", "मैं हैं", "मैं हो"], "answer": "मैं हूँ"},
            {"prompt": "Which form of होना goes with हम (we)?", "options": ["हैं", "हूँ", "है", "हो"], "answer": "हैं"},
            {"prompt": "आप (aap) is the pronoun used for:", "options": ["Formal \"you\"", "Intimate \"you\"", "\"They\"", "\"We\""], "answer": "Formal \"you\""},
            {"prompt": "वह (vah) can mean:", "options": ["he / she / it / that", "I", "we", "you (formal)"], "answer": "he / she / it / that"},
            {"prompt": "\"He is a doctor\" is:", "options": ["वह डॉक्टर है", "मैं डॉक्टर हूँ", "वह डॉक्टर हूँ", "हम डॉक्टर है"], "answer": "वह डॉक्टर है"},
            {"prompt": "Which pronoun takes है (not हैं or हूँ)?", "options": ["वह / यह", "हम", "आप", "मैं"], "answer": "वह / यह"},
        ],
    },
    {
        "level": "A1", "title": "Basic Sentence Building (Word Order)",
        "hook": "The one rule that reorganizes everything: the verb goes last.",
        "sections": [
            {"heading": "Subject–Object–Verb", "body": """
Hindi sentences follow **Subject → Object → Verb**, while English/French use
Subject → Verb → Object.

**मैं पानी पीता हूँ** (main paanee peetaa hoon)
literally *"I water drink"* → **I drink water.**

**राम किताब पढ़ता है** (raam kitaab paRhtaa hai)
literally *"Ram book reads"* → **Ram reads a book.**

As you build any sentence: subject first, then object/details, and save the verb for last.
"""},
            {"heading": "Building longer sentences", "body": """
Extra details (time, place, manner) usually go **between** the subject and the verb,
not at the very end like in English:

**मैं आज स्कूल जाता हूँ** (main aaj school jaataa hoon)
literally *"I today school go"* → **I go to school today.**

Get comfortable holding the verb until the end — it feels backwards at first and becomes
automatic with practice.
"""},
        ],
        "quiz_type": "static", "pass_pct": 70, "n_questions": 4,
        "quiz_static": [
            {"prompt": "Hindi basic word order is:", "options": ["Subject-Object-Verb", "Subject-Verb-Object", "Verb-Subject-Object", "Object-Subject-Verb"], "answer": "Subject-Object-Verb"},
            {"prompt": "मैं पानी पीता हूँ literally means:", "options": ["I water drink", "Water I drink", "I drink water quickly", "Drink water I"], "answer": "I water drink"},
            {"prompt": "In a Hindi sentence, where do time/place words usually go?", "options": ["Between subject and verb", "After the verb", "Before the subject only", "They're never used"], "answer": "Between subject and verb"},
            {"prompt": "Which English sentence order does Hindi NOT use?", "options": ["Subject-Verb-Object", "Subject-Object-Verb", "Both are equally common", "Neither order exists"], "answer": "Subject-Verb-Object"},
        ],
    },
    {
        "level": "A1", "title": "Days, Time & Question Words",
        "hook": "Ask when, where, why — and talk about today, tomorrow, and the days of the week.",
        "sections": [
            {"heading": "Time & days", "body": "\n".join(f"- **{v['hi']}** ({v['translit']}) — {v['en']}" for v in VOCAB["Time & Days"])},
            {"heading": "Question words", "body": "\n".join(f"- **{v['hi']}** ({v['translit']}) — {v['en']}" for v in VOCAB["Question Words"])},
            {"heading": "Sample questions", "body": """
> **आज कौन सा दिन है?** (aaj kaun saa din hai?) — What day is it today?
> **आप कहाँ से हैं?** (aap kahaan se hain?) — Where are you from?
> **यह क्या है?** (yah kyaa hai?) — What is this?

Notice the question word slots into the **same position** the answer would occupy —
Hindi word order doesn't scramble for questions the way English does.
"""},
        ],
        "quiz_type": "vocab", "quiz_pool": VOCAB["Time & Days"] + VOCAB["Question Words"], "pass_pct": 70, "n_questions": 6,
    },
    {
        "level": "A1", "title": "A1 Checkpoint — Survival Conversation",
        "hook": "Pull together everything from A1 into one mastery check before moving to A2.",
        "sections": [
            {"heading": "What you've built so far", "body": """
By this point you can: read the full Devanagari script, greet someone and introduce yourself,
count to 20, use होना ("to be") in the present, build a basic SOV sentence, and ask
basic questions with time/day vocabulary.

This checkpoint mixes questions from all of those areas. Treat it as a real milestone —
passing it means you're genuinely at **CEFR A1**: you can handle short, predictable
survival exchanges with a patient native speaker.
"""},
        ],
        "quiz_type": "static", "pass_pct": 75, "n_questions": 8,
        "quiz_static": [
            {"prompt": "\"Hello/goodbye\" that works any time of day is:", "options": ["नमस्ते", "शुभ रात्रि", "अलविदा only", "धन्यवाद"], "answer": "नमस्ते"},
            {"prompt": "\"Thank you\" in Hindi is:", "options": ["धन्यवाद", "माफ़ कीजिए", "कृपया", "स्वागत है"], "answer": "धन्यवाद"},
            {"prompt": "\"I am fine\" is:", "options": ["मैं ठीक हूँ", "मैं ठीक है", "वह ठीक हूँ", "आप ठीक हैं"], "answer": "मैं ठीक हूँ"},
            {"prompt": "The number 5 (पाँच) is transliterated:", "options": ["paanch", "chaar", "saat", "das"], "answer": "paanch"},
            {"prompt": "Hindi verb position in a sentence is:", "options": ["Last", "First", "Second", "Random"], "answer": "Last"},
            {"prompt": "\"Where\" in Hindi is:", "options": ["कहाँ", "क्या", "कब", "क्यों"], "answer": "कहाँ"},
            {"prompt": "The ि matra is pronounced:", "options": ["After its consonant, though written before", "Before its consonant, exactly as written", "Silent", "As a conjunct"], "answer": "After its consonant, though written before"},
            {"prompt": "आप (aap) is used for:", "options": ["Formal/respectful \"you\"", "Only children", "\"They\"", "\"I\""], "answer": "Formal/respectful \"you\""},
        ],
    },

    # =====================================================================
    # A2 — ELEMENTARY: real grammar, real topics
    # =====================================================================
    {
        "level": "A2", "title": "Noun Gender & Plurals",
        "hook": "Every noun has a gender, and it quietly controls everything else in the sentence.",
        "sections": [
            {"heading": "Gender patterns", "body": """
Every Hindi noun is masculine or feminine — no neuter — and gender affects verb endings
too, unlike French.

| Pattern | Gender | Examples |
|---|---|---|
| Ends in **-आ (aa)** | usually masculine | लड़का (larkaa) boy, कमरा (kamraa) room |
| Ends in **-ई (ii) / -िया** | usually feminine | लड़की (larkee) girl, चिड़िया (chiRiyaa) bird |
| Ends in a consonant | either — no visual rule | किताब (kitaab, f.) book, घर (ghar, m.) house |

Learn the gender **together with the word** from day one — check the gender tag
whenever you look a noun up in **Dictionary Search**.
"""},
            {"heading": "Plurals", "body": """
| Category | Rule | Example |
|---|---|---|
| Masculine, ends in -aa | -aa → -e | लड़का → लड़के |
| Masculine, ends in consonant | no change | घर → घर |
| Feminine, ends in -ii/-iyaa | -ii/-iyaa → -iyaan | लड़की → लड़कियाँ |
| Feminine, ends in consonant | add -en | किताब → किताबें |
"""},
        ],
        "quiz_type": "static", "pass_pct": 70, "n_questions": 5,
        "quiz_static": [
            {"prompt": "Nouns ending in -आ (aa) are usually:", "options": ["Masculine", "Feminine", "Always plural", "Neuter"], "answer": "Masculine"},
            {"prompt": "The plural of लड़का (larkaa, boy) is:", "options": ["लड़के", "लड़किया", "लड़कों", "लड़का"], "answer": "लड़के"},
            {"prompt": "The plural of किताब (kitaab, book, feminine) is:", "options": ["किताबें", "किताबे", "किताबा", "किताब"], "answer": "किताबें"},
            {"prompt": "Does Hindi have a neuter gender?", "options": ["No — only masculine/feminine", "Yes, a third gender", "Only for animals", "Only for abstract nouns"], "answer": "No — only masculine/feminine"},
            {"prompt": "घर (ghar, house) ends in a consonant and is:", "options": ["Masculine", "Feminine", "Neuter", "Unknown without context"], "answer": "Masculine"},
        ],
    },
    {
        "level": "A2", "title": "Adjective Agreement",
        "hook": "Adjectives shape-shift to match the noun they describe — just like French, but with an extra twist.",
        "sections": [
            {"heading": "The -आ adjectives", "body": """
Adjectives ending in **-आ (aa)** change to match the noun's gender and number:

अच्छा लड़का (achchhaa larkaa) *good boy*
→ अच्छी लड़की (achchhee larkee) *good girl*
→ अच्छे लड़के (achchhe larke) *good boys*

| Ending | Agrees with |
|---|---|
| -आ (aa) | masculine singular |
| -ी (ii) | feminine (singular or plural) |
| -े (e) | masculine plural |
"""},
            {"heading": "Adjectives that never change", "body": """
Adjectives that **don't** end in -आ (like सुंदर/sundar, "beautiful", or ज़रूरी/zaroorii, "necessary")
stay exactly the same regardless of gender or number:

सुंदर लड़का, सुंदर लड़की, सुंदर लड़के — no changes needed at all.
"""},
        ],
        "quiz_type": "vocab", "quiz_pool": VOCAB["Common Adjectives"], "pass_pct": 70, "n_questions": 6,
    },
    {
        "level": "A2", "title": "Family & Describing People",
        "hook": "Talk about who's who — parents, siblings, and simple physical/personality descriptions.",
        "sections": [
            {"heading": "Family vocabulary", "body": "\n".join(f"- **{v['hi']}** ({v['translit']}) — {v['en']}" for v in VOCAB["Family"])},
            {"heading": "Describing someone", "body": """
Combine family words with adjectives from the last chapter:

**मेरी माँ बहुत अच्छी है** (meree maan bahut achchhee hai) — My mother is very good/kind.
**मेरा भाई लंबा है** (meraa bhaaii lambaa hai) — My brother is tall.

Notice **मेरा/मेरी** ("my") itself agrees with the noun's gender — मेरा भाई (m.) vs मेरी माँ (f.).
This "possessive agreement" pattern will come up again with postpositions in the next chapter.
"""},
        ],
        "quiz_type": "vocab", "quiz_pool": VOCAB["Family"] + VOCAB["Common Adjectives"], "pass_pct": 70, "n_questions": 6,
    },
    {
        "level": "A2", "title": "Present Habitual Tense (Verbs)",
        "hook": "Now you can actually say what people DO, every day, in full sentences.",
        "sections": [
            {"heading": "How it's built", "body": """
**verb stem + ता/ती/ते** (agreeing with gender/number) **+ a form of होना**

Example with जाना (jaanaa, "to go"):

| Subject | Form | Meaning |
|---|---|---|
| मैं (m/f) | जाता हूँ / जाती हूँ | I go |
| तुम (informal) | जाते हो / जाती हो | you go |
| वह | जाता है / जाती है | he/she goes |
| हम | जाते हैं / जाती हैं | we go |
| आप | जाते हैं / जाती हैं | you go (formal) |

This same pattern applies to **all 15 verbs** in the Verb Trainer — the ending logic
never changes, only the stem does.
"""},
            {"heading": "Practice strategy", "body": """
Open **Verb Trainer → Browse conjugation tables** and read through 3-4 verbs out loud,
then come back for this chapter's quiz, which pulls live questions from all 15 verbs.
"""},
        ],
        "quiz_type": "verb", "quiz_verb": {"keys": list(VERBS.keys()), "tenses": ["present"]}, "pass_pct": 65, "n_questions": 6,
    },
    {
        "level": "A2", "title": "Postpositions I — में, पर, से, को",
        "hook": "Hindi has no prepositions at all — it puts the equivalent word AFTER the noun instead.",
        "sections": [
            {"heading": "The core four", "body": """
| Hindi | Meaning | Example |
|---|---|---|
| में (mein) | in | घर में — in the house |
| पर (par) | on | मेज़ पर — on the table |
| से (se) | from / by / with | स्कूल से — from school |
| को (ko) | to / marks a definite object | राम को — to Ram |

Because the marker comes **after** the noun, you'll need to retrain your instinct to look
for it at the end of the noun phrase, not the beginning.
"""},
            {"heading": "को and definite objects", "body": """
को has a second job beyond "to": it marks a **definite, specific object** —
especially people:

**मैं राम को जानता हूँ** (main raam ko jaantaa hoon) — I know Ram. (a specific person → को appears)
**मैं किताब पढ़ता हूँ** (main kitaab paRhtaa hoon) — I read a/the book. (no को needed here)
"""},
        ],
        "quiz_type": "static", "pass_pct": 70, "n_questions": 5,
        "quiz_static": [
            {"prompt": "\"in the house\" is:", "options": ["घर में", "में घर", "घर पर", "घर से"], "answer": "घर में"},
            {"prompt": "पर (par) means:", "options": ["on", "in", "from", "to"], "answer": "on"},
            {"prompt": "से (se) can mean:", "options": ["from / by / with", "on", "in", "and"], "answer": "from / by / with"},
            {"prompt": "Hindi postpositions come:", "options": ["After the noun", "Before the noun", "At the start of the sentence", "At the very end of the sentence only"], "answer": "After the noun"},
            {"prompt": "को is often used to mark:", "options": ["A specific/definite object, especially a person", "Only locations", "Plural nouns", "Negation"], "answer": "A specific/definite object, especially a person"},
        ],
    },
    {
        "level": "A2", "title": "Postpositions II — Possession & Compound Postpositions",
        "hook": "Possession works like an adjective in Hindi, and several everyday postpositions are actually two words.",
        "sections": [
            {"heading": "का/की/के — \"of / possessive\"", "body": """
का (kaa) works like an adjective: it **agrees with the noun that follows it**, not the owner.

राम **का** घर (raam kaa ghar) — Ram's house (घर is masculine → का)
राम **की** किताब (raam kii kitaab) — Ram's book (किताब is feminine → की)
राम **के** भाई (raam ke bhaaii) — Ram's brothers (plural → के)
"""},
            {"heading": "Compound postpositions", "body": """
| Hindi | Meaning | Example |
|---|---|---|
| के लिए (ke liye) | for | आपके लिए — for you |
| के साथ (ke saath) | with | दोस्त के साथ — with a friend |
| के बाद (ke baad) | after | खाने के बाद — after eating |
| से पहले (se pehle) | before | सोने से पहले — before sleeping |
| के पास (ke paas) | near / "to have" | मेरे पास किताब है — I have a book |
| तक (tak) | until | कल तक — until tomorrow |

**के पास** is worth pausing on: Hindi has no verb "to have" — you express possession as
*"near me [there] is a book"* instead. This will feel unusual at first and become natural fast.
"""},
        ],
        "quiz_type": "static", "pass_pct": 70, "n_questions": 5,
        "quiz_static": [
            {"prompt": "\"Ram's house\" (घर is masculine) is:", "options": ["राम का घर", "राम की घर", "राम के घर", "राम घर का"], "answer": "राम का घर"},
            {"prompt": "How does Hindi express \"I have a book\"?", "options": ["मेरे पास किताब है (\"near me is a book\")", "मैं किताब हूँ", "मुझे किताब", "किताब मेरा है"], "answer": "मेरे पास किताब है (\"near me is a book\")"},
            {"prompt": "के लिए means:", "options": ["for", "with", "after", "before"], "answer": "for"},
            {"prompt": "के साथ means:", "options": ["with", "for", "until", "near"], "answer": "with"},
            {"prompt": "का/की/के agrees with:", "options": ["The noun that follows it (the thing possessed)", "The possessor always", "Nothing — it never changes", "The verb"], "answer": "The noun that follows it (the thing possessed)"},
        ],
    },
    {
        "level": "A2", "title": "Food & Dining Conversations",
        "hook": "Order food, ask for the bill, and understand a menu.",
        "sections": [
            {"heading": "Food vocabulary", "body": "\n".join(f"- **{v['hi']}** ({v['translit']}) — {v['en']}" for v in VOCAB["Food & Dining"])},
            {"heading": "At a restaurant", "body": "\n".join(f"- **{p['hi']}** ({p['translit']}) — {p['en']}" for p in PHRASES["Dining"])},
            {"heading": "A sample exchange", "body": """
> **वेटर: जी हाँ, आप क्या लेंगे?** — Yes, what will you have?
> **आप: एक दाल और दो रोटी दीजिए।** — Please bring one dal and two rotis.
> **वेटर: पीने के लिए क्या लेंगे?** — What will you have to drink?
> **आप: एक पानी की बोतल, कृपया।** — A bottle of water, please.
"""},
        ],
        "quiz_type": "vocab", "quiz_pool": VOCAB["Food & Dining"] + PHRASES["Dining"], "pass_pct": 70, "n_questions": 6,
    },
    {
        "level": "A2", "title": "Negation & Yes/No Questions",
        "hook": "Say what ISN'T true, and ask a simple yes/no question.",
        "sections": [
            {"heading": "Negation", "body": """
Place **नहीं (naheen, "not")** directly **before the verb**:

**मैं नहीं जाता हूँ** (main naheen jaataa hoon) — I don't go.
**यह ठीक नहीं है** (yah Theek naheen hai) — This isn't right.

Word order otherwise stays exactly the same as the positive sentence.
"""},
            {"heading": "Yes/no questions", "body": """
Hindi word order usually **doesn't change** for questions — you can turn any statement
into a yes/no question just by raising your intonation, or by adding **क्या** at the very
start of the sentence as an explicit question marker:

**क्या आप जाते हैं?** (kyaa aap jaate hain?) — Do you go?
**क्या यह सही है?** (kyaa yah sahee hai?) — Is this correct?

Careful: this क्या ("do/does/is") is a different job than क्या meaning "what" — context
makes it clear which one is meant.
"""},
        ],
        "quiz_type": "static", "pass_pct": 70, "n_questions": 5,
        "quiz_static": [
            {"prompt": "Where does नहीं (not) go in a sentence?", "options": ["Directly before the verb", "At the very start", "At the very end", "After the subject only"], "answer": "Directly before the verb"},
            {"prompt": "\"I don't go\" is:", "options": ["मैं नहीं जाता हूँ", "नहीं मैं जाता हूँ", "मैं जाता नहीं हूँ हूँ", "मैं जाता हूँ नहीं"], "answer": "मैं नहीं जाता हूँ"},
            {"prompt": "Adding क्या to the start of a statement can turn it into:", "options": ["A yes/no question", "A negative statement", "A command", "A past-tense sentence"], "answer": "A yes/no question"},
            {"prompt": "Does word order change much for Hindi yes/no questions?", "options": ["No, mostly just intonation or an added क्या", "Yes, subject and verb always swap", "Yes, the verb moves to the front", "Questions aren't possible in Hindi"], "answer": "No, mostly just intonation or an added क्या"},
            {"prompt": "क्या can mean:", "options": ["Both \"what\" and a yes/no question marker", "Only \"what\"", "Only \"why\"", "\"Not\""], "answer": "Both \"what\" and a yes/no question marker"},
        ],
    },
    {
        "level": "A2", "title": "Shopping, Money & Bigger Numbers",
        "hook": "Haggle, ask prices, and count past 20 with the tens system.",
        "sections": [
            {"heading": "Shopping vocabulary", "body": "\n".join(f"- **{v['hi']}** ({v['translit']}) — {v['en']}" for v in VOCAB["Shopping & Money"])},
            {"heading": "Numbers by tens", "body": "\n".join(f"- **{v['hi']}** ({v['translit']}) — {v['en']}" for v in VOCAB["Numbers - tens"])},
            {"heading": "Shopping phrases", "body": "\n".join(f"- **{p['hi']}** ({p['translit']}) — {p['en']}" for p in PHRASES["Shopping"])},
        ],
        "quiz_type": "vocab", "quiz_pool": VOCAB["Shopping & Money"] + VOCAB["Numbers - tens"] + PHRASES["Shopping"], "pass_pct": 70, "n_questions": 6,
    },
    {
        "level": "A2", "title": "Directions & Transport",
        "hook": "Find your way — ask for and understand directions, and talk about how you're getting somewhere.",
        "sections": [
            {"heading": "Directions & transport vocabulary", "body": "\n".join(f"- **{v['hi']}** ({v['translit']}) — {v['en']}" for v in VOCAB["Directions & Transport"])},
            {"heading": "Asking for directions", "body": "\n".join(f"- **{p['hi']}** ({p['translit']}) — {p['en']}" for p in PHRASES["Directions"])},
        ],
        "quiz_type": "vocab", "quiz_pool": VOCAB["Directions & Transport"] + PHRASES["Directions"], "pass_pct": 70, "n_questions": 6,
    },
    {
        "level": "A2", "title": "Future Tense",
        "hook": "Say what WILL happen — plans, promises, predictions.",
        "sections": [
            {"heading": "How it's built", "body": """
**verb stem + ऊँगा/एगा/ओगे...** (agreeing with the subject's gender and number)

Example with जाना (jaanaa, "to go"):

| Subject | Form | Meaning |
|---|---|---|
| मैं (m/f) | जाऊँगा / जाऊँगी | I will go |
| तुम | जाओगे / जाओगी | you will go |
| वह | जाएगा / जाएगी | he/she will go |
| हम | जाएँगे / जाएँगी | we will go |
| आप | जाएँगे / जाएँगी | you will go (formal) |

The future tense agrees with gender the same way the present tense does — that pattern
is now something you can lean on for every new verb you learn.
"""},
        ],
        "quiz_type": "verb", "quiz_verb": {"keys": list(VERBS.keys()), "tenses": ["future"]}, "pass_pct": 65, "n_questions": 6,
    },
    {
        "level": "A2", "title": "A2 Checkpoint — Ordering, Directions & Small Talk",
        "hook": "Mix everything from A2 into one mastery check before entering B1.",
        "sections": [
            {"heading": "What you've built so far", "body": """
You can now form grammatically correct sentences with gender/number agreement, use
postpositions correctly, talk about family, order food, negate a sentence, ask a
yes/no question, shop, get directions, and use both present and future tense.

Passing this checkpoint means you're genuinely at **CEFR A2**: you can handle simple,
routine exchanges on familiar topics, even without a script to follow.
"""},
        ],
        "quiz_type": "static", "pass_pct": 75, "n_questions": 8,
        "quiz_static": [
            {"prompt": "अच्छा (achchhaa, \"good\") describing a feminine noun becomes:", "options": ["अच्छी", "अच्छे", "अच्छा", "अच्छों"], "answer": "अच्छी"},
            {"prompt": "\"Ram's book\" (किताब is feminine) is:", "options": ["राम की किताब", "राम का किताब", "राम के किताब", "किताब का राम"], "answer": "राम की किताब"},
            {"prompt": "\"I don't go\" is:", "options": ["मैं नहीं जाता हूँ", "मैं जाता हूँ नहीं", "नहीं मैं जाता", "मैं न जाता हूँ"], "answer": "मैं नहीं जाता हूँ"},
            {"prompt": "\"in the house\" is:", "options": ["घर में", "घर पर", "घर से", "घर को"], "answer": "घर में"},
            {"prompt": "\"I will go\" (masculine speaker) is:", "options": ["मैं जाऊँगा", "मैं जाता हूँ", "मैं गया", "मैं जाऊँगी"], "answer": "मैं जाऊँगा"},
            {"prompt": "The polite way to have someone bring you something at a restaurant uses the verb ending:", "options": ["दीजिए (\"please give\")", "जाना", "है", "करो"], "answer": "दीजिए (\"please give\")"},
            {"prompt": "\"How much does this cost?\" would use vocabulary from which theme?", "options": ["Shopping & Money", "Family", "Weather & Nature", "Body Parts"], "answer": "Shopping & Money"},
            {"prompt": "क्या at the start of a sentence typically signals:", "options": ["A yes/no question", "The past tense", "A command", "Plural"], "answer": "A yes/no question"},
        ],
    },

    # =====================================================================
    # B1 — INTERMEDIATE: the past tense, politeness, and real conversation
    # =====================================================================
    {
        "level": "B1", "title": "Simple Past & the ने Construction",
        "hook": "The single biggest grammar surprise in Hindi for English/French speakers — worth its own chapter.",
        "sections": [
            {"heading": "The ergative twist", "body": """
In the simple past, **transitive verbs** (verbs with a direct object, like "eat" or "read")
require the subject to take **ने (ne)**, and the **verb agrees with the OBJECT's gender/number**
instead of the subject's:

**मैंने चाय पी** (mainne chaay pee) — "I drank tea." पी is feminine because *चाय* (tea) is
feminine — **not** because "I" am. This construction (called "ergative alignment" by linguists)
has no French or English equivalent, so give it real, deliberate practice.

**राम ने किताब पढ़ी** (raam ne kitaab paRhee) — Ram read the book. (किताब is feminine → पढ़ी)
**राम ने अखबार पढ़ा** (raam ne akhbaar paRhaa) — Ram read the newspaper. (अखबार is masculine → पढ़ा)
"""},
            {"heading": "The rule of thumb", "body": """
1. Is the verb transitive (has a direct object)? → subject takes ने, verb agrees with object.
2. Is the verb intransitive (जाना/to go, आना/to come, सोना/to sleep, etc.)? → **no ने**,
   verb agrees with the subject normally, exactly like present/future tense.

You'll drill the intransitive side next chapter — for now, focus on locking in ने with
transitive verbs like करना, खाना, पीना, देखना, सुनना, पढ़ना, and लिखना.
"""},
        ],
        "quiz_type": "static", "pass_pct": 65, "n_questions": 5,
        "quiz_static": [
            {"prompt": "In the simple past, transitive verbs require the subject to take:", "options": ["ने (ne)", "को (ko)", "से (se)", "में (mein)"], "answer": "ने (ne)"},
            {"prompt": "With ने, the verb agrees with:", "options": ["The object's gender/number", "The subject's gender/number", "Neither — it stays fixed", "The postposition"], "answer": "The object's gender/number"},
            {"prompt": "मैंने चाय पी — पी is feminine because:", "options": ["चाय (tea) is feminine", "मैं (I) is feminine", "It's always feminine in the past", "पीना is an irregular verb"], "answer": "चाय (tea) is feminine"},
            {"prompt": "\"Ram read the newspaper\" (अखबार, masculine) is:", "options": ["राम ने अखबार पढ़ा", "राम ने अखबार पढ़ी", "राम अखबार पढ़ा", "राम का अखबार पढ़ा"], "answer": "राम ने अखबार पढ़ा"},
            {"prompt": "Which kind of verb uses the ने construction in the past?", "options": ["Transitive verbs (verbs with a direct object)", "All verbs, no exceptions", "Only \"to be\"", "Intransitive verbs only"], "answer": "Transitive verbs (verbs with a direct object)"},
        ],
    },
    {
        "level": "B1", "title": "Intransitive Past & Common Irregular Verbs",
        "hook": "Not every verb takes ने — motion and state verbs keep it simple.",
        "sections": [
            {"heading": "No ने needed", "body": """
**Intransitive verbs** (no direct object) — जाना (to go), आना (to come), सोना (to sleep),
होना (to be/happen) — do **not** use ने. The verb simply agrees with the **subject**,
just like present and future tense:

**मैं गया / गई** (main gayaa / gaii) — I went (m/f)
**वह आया / आई** (vah aayaa / aaii) — he/she came
**हम सोए / सोईं** (ham soe / soeen) — we slept

जाना is irregular in the past — its stem changes completely to **गया/गई/गए** rather than
following the expected pattern. This is one of the very few true irregular verbs in Hindi,
so it's worth memorizing on its own.
"""},
            {"heading": "Quick contrast", "body": """
| | Transitive (needs ने) | Intransitive (no ने) |
|---|---|---|
| Marker | subject + ने | subject alone |
| Verb agrees with | the object | the subject |
| Examples | खाना, पीना, पढ़ना, देखना, सुनना, करना, लिखना | जाना, आना, सोना, होना |
"""},
        ],
        "quiz_type": "verb", "quiz_verb": {"keys": ["jaana", "aana", "sona"], "tenses": ["past"]}, "pass_pct": 65, "n_questions": 5,
    },
    {
        "level": "B1", "title": "The Three Levels of \"You\" & Politeness",
        "hook": "Choosing the wrong \"you\" is one of the fastest ways to sound rude — or too formal — in Hindi.",
        "sections": [
            {"heading": "तू / तुम / आप", "body": """
| Hindi | Usage |
|---|---|
| तू (too) | very intimate — very close friends, small children, addressing God |
| तुम (tum) | informal — friends, peers, younger family — like French *tu* |
| आप (aap) | formal/respectful — like French *vous* — always safe as your default |

Default to **आप** with strangers, elders, service staff, and in any professional setting.
Switching down to तुम happens naturally once a relationship becomes close — let the
other person signal that shift first if you're unsure.
"""},
            {"heading": "Politeness markers", "body": "\n".join(f"- **{p['hi']}** ({p['translit']}) — {p['en']}" for p in PHRASES["Politeness"]) + """

Verb endings also carry politeness: **-िए / -िएगा** (as in कीजिए, "please do") is the
polite imperative you'll meet properly in a later chapter — it always pairs with आप.
"""},
        ],
        "quiz_type": "static", "pass_pct": 70, "n_questions": 5,
        "quiz_static": [
            {"prompt": "The safest default \"you\" to use with a stranger is:", "options": ["आप", "तू", "तुम", "It doesn't matter"], "answer": "आप"},
            {"prompt": "तू is used for:", "options": ["Very intimate relationships or addressing God", "Formal business settings", "Elders you've just met", "Government officials"], "answer": "Very intimate relationships or addressing God"},
            {"prompt": "तुम is roughly equivalent to French:", "options": ["tu", "vous", "on", "nous"], "answer": "tu"},
            {"prompt": "Which pronoun pairs with the polite imperative ending -िए (as in कीजिए)?", "options": ["आप", "तू", "तुम", "मैं"], "answer": "आप"},
            {"prompt": "If unsure which \"you\" to use, the safest choice is:", "options": ["आप", "तू", "तुम", "Avoid pronouns entirely"], "answer": "आप"},
        ],
    },
    {
        "level": "B1", "title": "Modal Verbs — सकना (can) & चाहिए (should/need)",
        "hook": "Express ability and obligation — \"I can\" and \"I should/need to.\"",
        "sections": [
            {"heading": "सकना — ability", "body": """
Add **सकना (saknaa)** right after the verb stem to mean "can / to be able to":

**मैं जा सकता हूँ / सकती हूँ** (main jaa saktaa/saktee hoon) — I can go.
**क्या तुम आ सकते हो?** (kyaa tum aa sakte ho?) — Can you come?

सकना itself conjugates like a normal verb (agreeing with the subject), while the main
verb stays in its bare stem form just before it.
"""},
            {"heading": "चाहिए — obligation/need", "body": """
**चाहिए (chaahiye)** expresses "should" or "need to," and works differently from English:
the person who needs something takes **को**, not a subject-verb structure:

**मुझे पानी चाहिए** (mujhe paanee chaahiye) — I need water. (literally "to me, water is necessary")
**आपको जाना चाहिए** (aapko jaanaa chaahiye) — You should go.

चाहिए never conjugates for person — it stays exactly as चाहिए regardless of who needs
something, which makes it easier than it looks.
"""},
        ],
        "quiz_type": "static", "pass_pct": 65, "n_questions": 5,
        "quiz_static": [
            {"prompt": "\"I can go\" (masculine) is:", "options": ["मैं जा सकता हूँ", "मैं जाता हूँ", "मुझे जाना चाहिए", "मैं जा सकती हूँ"], "answer": "मैं जा सकता हूँ"},
            {"prompt": "चाहिए most closely means:", "options": ["should / need to", "can / able to", "want (in the past)", "must never"], "answer": "should / need to"},
            {"prompt": "\"I need water\" is:", "options": ["मुझे पानी चाहिए", "मैं पानी चाहिए हूँ", "मुझे पानी सकता है", "पानी मुझे है"], "answer": "मुझे पानी चाहिए"},
            {"prompt": "The person who needs something with चाहिए takes which marker?", "options": ["को", "ने", "से", "का"], "answer": "को"},
            {"prompt": "Does चाहिए conjugate to agree with the person who needs something?", "options": ["No, it stays the same", "Yes, fully like a regular verb", "Only in the past tense", "Only in questions"], "answer": "No, it stays the same"},
        ],
    },
    {
        "level": "B1", "title": "Imperatives & Polite Requests",
        "hook": "Give instructions and make requests, at every level of politeness.",
        "sections": [
            {"heading": "Three levels of commands", "body": """
| Register | Ending | Example | Pairs with |
|---|---|---|---|
| Casual | stem alone | जा (jaa) — "Go!" | तू |
| Informal | stem + ओ | जाओ (jaao) — "Go." | तुम |
| Polite/formal | stem + िए / िएगा | जाइए / जाइएगा (jaaiye / jaaiyegaa) — "Please go." | आप |

The formal **-िए** ending is what you'll use constantly in real life — restaurants,
shops, asking a stranger for help. Add **कृपया (kripayaa, "please")** at the front for
extra courtesy.
"""},
            {"heading": "Negative commands", "body": """
For "don't do X," use **मत (mat)** with the casual/informal stem, or **न (na)**
with the polite -िए form:

**मत जाओ** (mat jaao) — Don't go. (informal)
**कृपया चिंता न कीजिए** (kripayaa chintaa na keejiye) — Please don't worry. (formal)
"""},
        ],
        "quiz_type": "static", "pass_pct": 70, "n_questions": 5,
        "quiz_static": [
            {"prompt": "The polite/formal imperative ending, used with आप, is:", "options": ["-िए (as in जाइए)", "-ओ (as in जाओ)", "the bare stem alone", "-ता"], "answer": "-िए (as in जाइए)"},
            {"prompt": "\"Please\" in Hindi is:", "options": ["कृपया", "धन्यवाद", "माफ़ कीजिए", "शुभकामनाएँ"], "answer": "कृपया"},
            {"prompt": "\"Don't go\" (informal) is:", "options": ["मत जाओ", "न जाओ है", "जाओ मत नहीं", "मत जाना है"], "answer": "मत जाओ"},
            {"prompt": "Which negative command word pairs with the polite -िए form?", "options": ["न (na)", "मत (mat)", "नहीं-नहीं", "को"], "answer": "न (na)"},
            {"prompt": "जाइए pairs naturally with which pronoun?", "options": ["आप", "तू", "तुम", "मैं"], "answer": "आप"},
        ],
    },
    {
        "level": "B1", "title": "Conjunctive Participle — \"Having Done X\"",
        "hook": "Chain two actions into one fluid sentence — a construction you'll use constantly once you notice it.",
        "sections": [
            {"heading": "The -कर form", "body": """
Add **-कर (kar)** to a verb stem to mean "having done X, [then]...". It links two
actions performed by the same subject into a single sentence, much more naturally
than English's "after doing X, I did Y":

**खाना खाकर मैं सो गया** (khaanaa khaakar main so gayaa)
literally *"having eaten food, I slept"* → **I ate and then slept.**

**घर जाकर वह आराम करेगी** (ghar jaakar vah aaraam karegee)
literally *"having gone home, she will rest"* → **She'll go home and rest.**
"""},
            {"heading": "Why it matters", "body": """
Native speakers use -कर constantly to avoid clunky "and then... and then..." sentences.
Once you can build these, your Hindi starts sounding noticeably more natural and less
like a translated textbook. करना's own -कर form is simply करके (karke).
"""},
        ],
        "quiz_type": "static", "pass_pct": 65, "n_questions": 4,
        "quiz_static": [
            {"prompt": "The conjunctive participle ending meaning \"having done X\" is:", "options": ["-कर (kar)", "-ता (taa)", "-ेगा (egaa)", "-ने (ne)"], "answer": "-कर (kar)"},
            {"prompt": "खाना खाकर मैं सो गया literally means:", "options": ["Having eaten food, I slept", "I will eat and sleep", "I am eating while sleeping", "I ate but didn't sleep"], "answer": "Having eaten food, I slept"},
            {"prompt": "करना's conjunctive participle form is:", "options": ["करके", "करता", "करेगा", "करो"], "answer": "करके"},
            {"prompt": "The -कर construction is mainly used to:", "options": ["Chain two actions by the same subject into one sentence", "Form the future tense", "Negate a sentence", "Ask a question"], "answer": "Chain two actions by the same subject into one sentence"},
        ],
    },
    {
        "level": "B1", "title": "Body, Health & Emergencies",
        "hook": "Say what hurts, and know what to say if something goes wrong.",
        "sections": [
            {"heading": "Body parts", "body": "\n".join(f"- **{v['hi']}** ({v['translit']}) — {v['en']}" for v in VOCAB["Body Parts"])},
            {"heading": "Emergency phrases", "body": "\n".join(f"- **{p['hi']}** ({p['translit']}) — {p['en']}" for p in PHRASES["Emergencies"])},
            {"heading": "Talking about pain", "body": """
Pain uses the same "to me" structure you saw with चाहिए:

**मुझे सिर दर्द है** (mujhe sir dard hai) — I have a headache. (literally "to me, head-pain is")
**मेरे पेट में दर्द है** (mere pet mein dard hai) — I have a stomach ache.
"""},
        ],
        "quiz_type": "vocab", "quiz_pool": VOCAB["Body Parts"] + PHRASES["Emergencies"], "pass_pct": 70, "n_questions": 6,
    },
    {
        "level": "B1", "title": "Weather, Nature & Surroundings",
        "hook": "Describe the weather, seasons, and the world around you.",
        "sections": [
            {"heading": "Weather & nature vocabulary", "body": "\n".join(f"- **{v['hi']}** ({v['translit']}) — {v['en']}" for v in VOCAB["Weather & Nature"])},
            {"heading": "Talking about weather", "body": """
Weather statements typically use होना ("to be") with a noun, not a special "it" like
English's "it is raining":

**आज बहुत गर्मी है** (aaj bahut garmee hai) — It's very hot today. (literally "today, much heat is")
**कल बारिश होगी** (kal baarish hogee) — It will rain tomorrow. (literally "tomorrow, rain will happen")
"""},
        ],
        "quiz_type": "vocab", "quiz_pool": VOCAB["Weather & Nature"], "pass_pct": 70, "n_questions": 6,
    },
    {
        "level": "B1", "title": "Comparison & Superlatives",
        "hook": "Say that one thing is bigger, faster, or the best — without a separate comparative word ending.",
        "sections": [
            {"heading": "Comparatives with से", "body": """
Hindi builds comparisons with the postposition **से** ("than") rather than a special
adjective ending:

**यह उससे बड़ा है** (yah usse baRaa hai) — This is bigger than that.
literally *"this, than-that, big is"*

**ज़्यादा (zyaadaa, "more")** can be added for emphasis: **यह उससे ज़्यादा अच्छा है**
(yah usse zyaadaa achchhaa hai) — This is much better than that.
"""},
            {"heading": "Superlatives with सबसे", "body": """
**सबसे (sabse, "than all")** placed before an adjective creates the superlative:

**यह सबसे बड़ा है** (yah sabse baRaa hai) — This is the biggest.
**वह सबसे अच्छी छात्रा है** (vah sabse achchhee chhaatraa hai) — She is the best student.
"""},
        ],
        "quiz_type": "static", "pass_pct": 65, "n_questions": 4,
        "quiz_static": [
            {"prompt": "Hindi comparisons (\"bigger than\") are built with the postposition:", "options": ["से (se)", "में (mein)", "को (ko)", "का (kaa)"], "answer": "से (se)"},
            {"prompt": "\"This is the biggest\" uses:", "options": ["सबसे (sabse)", "से (se) alone", "को (ko)", "में (mein)"], "answer": "सबसे (sabse)"},
            {"prompt": "यह उससे बड़ा है literally means:", "options": ["This, than-that, big is", "This is very big", "That is bigger than this", "This will be big"], "answer": "This, than-that, big is"},
            {"prompt": "ज़्यादा (zyaadaa) adds the meaning:", "options": ["more / more so", "less", "same as", "never"], "answer": "more / more so"},
        ],
    },
    {
        "level": "B1", "title": "Progressive Aspect — रहा है (\"is doing\")",
        "hook": "Say what's happening RIGHT NOW, distinct from habitual daily actions.",
        "sections": [
            {"heading": "How it's built", "body": """
**verb stem + रहा/रही/रहे + a form of होना**

This is Hindi's equivalent of English "-ing," and it's what separates "I am eating
(right now)" from "I eat (habitually)":

**मैं खा रहा हूँ / रही हूँ** (main khaa rahaa/rahee hoon) — I am eating (right now).
**वह पढ़ रहा है** (vah paRh rahaa hai) — He is reading (right now).
**वे खेल रहे हैं** (ve khel rahe hain) — They are playing (right now).

Compare directly against the present habitual from earlier: **मैं खाता हूँ** ("I eat," in
general) vs. **मैं खा रहा हूँ** ("I am eating," this exact moment).
"""},
            {"heading": "In the past and future too", "body": """
The same रहा pattern extends to other tenses by changing होना's form:

**मैं खा रहा था** (main khaa rahaa thaa) — I was eating.
**मैं खा रहा होऊँगा** (main khaa rahaa hoonga) — I will be eating.
"""},
        ],
        "quiz_type": "static", "pass_pct": 65, "n_questions": 4,
        "quiz_static": [
            {"prompt": "\"I am eating\" (right now, masculine) is:", "options": ["मैं खा रहा हूँ", "मैं खाता हूँ", "मैंने खाया", "मैं खाऊँगा"], "answer": "मैं खा रहा हूँ"},
            {"prompt": "The progressive/continuous marker in Hindi is:", "options": ["रहा / रही / रहे + होना", "ता / ती / ते + होना", "कर", "ने"], "answer": "रहा / रही / रहे + होना"},
            {"prompt": "मैं खाता हूँ vs मैं खा रहा हूँ — the difference is:", "options": ["Habitual action vs. happening right now", "Past vs. future", "Formal vs. informal", "No real difference"], "answer": "Habitual action vs. happening right now"},
            {"prompt": "\"I was eating\" is:", "options": ["मैं खा रहा था", "मैं खा रहा हूँ", "मैं खाऊँगा", "मैंने खाया"], "answer": "मैं खा रहा था"},
        ],
    },
    {
        "level": "B1", "title": "Professions & Daily Routine",
        "hook": "Talk about what people do for work, and describe a typical day.",
        "sections": [
            {"heading": "Professions", "body": "\n".join(f"- **{v['hi']}** ({v['translit']}) — {v['en']}" for v in VOCAB["Professions"])},
            {"heading": "Describing a routine", "body": """
Combine present habitual verbs with time vocabulary to describe a full day:

**मैं सुबह उठता हूँ, नाश्ता करता हूँ, और काम पर जाता हूँ।**
(main subah uThtaa hoon, naashtaa kartaa hoon, aur kaam par jaataa hoon)
— I wake up in the morning, have breakfast, and go to work.

Stringing several present-habitual clauses together with **और (aur, "and")** is one of
the most useful things you can practice at this stage — it's genuinely how routines get
described in real conversation.
"""},
        ],
        "quiz_type": "vocab", "quiz_pool": VOCAB["Professions"], "pass_pct": 70, "n_questions": 6,
    },
    {
        "level": "B1", "title": "B1 Checkpoint — Unscripted Conversation",
        "hook": "Bring together the past tense, politeness, modals, and everything else from B1.",
        "sections": [
            {"heading": "What you've built so far", "body": """
You can now use the past tense (including the tricky ने construction), choose the
right level of "you," express ability/obligation, give polite commands, chain actions
with -कर, describe ongoing actions, and talk about health, weather, and routines.

Passing this checkpoint means you're genuinely at **CEFR B1**: you can hold a real,
unscripted conversation on familiar topics — food, shopping, directions, family, daily
routine — without leaning on a script.
"""},
        ],
        "quiz_type": "static", "pass_pct": 75, "n_questions": 8,
        "quiz_static": [
            {"prompt": "\"I drank tea\" uses which construction?", "options": ["मैंने चाय पी (ने + object agreement)", "मैं चाय पीता हूँ", "मैं चाय पिऊँगा", "चाय मुझे पी"], "answer": "मैंने चाय पी (ने + object agreement)"},
            {"prompt": "जाना (to go) in the past does NOT take ने because it is:", "options": ["Intransitive", "Transitive", "A modal verb", "Irregular in the present only"], "answer": "Intransitive"},
            {"prompt": "The safest \"you\" with someone you've just met is:", "options": ["आप", "तू", "तुम", "None needed"], "answer": "आप"},
            {"prompt": "\"I can go\" is:", "options": ["मैं जा सकता हूँ", "मुझे जाना चाहिए", "मैं जा रहा हूँ", "मैं गया"], "answer": "मैं जा सकता हूँ"},
            {"prompt": "The polite imperative \"please go\" is:", "options": ["जाइए", "जाओ", "जा", "जाना"], "answer": "जाइए"},
            {"prompt": "\"Having eaten, I slept\" uses the ending:", "options": ["-कर (as in खाकर)", "-ता", "-ेगा", "-ने"], "answer": "-कर (as in खाकर)"},
            {"prompt": "\"I am eating\" (right now) is:", "options": ["मैं खा रहा हूँ", "मैं खाता हूँ", "मैं खाऊँगा", "मैंने खाया"], "answer": "मैं खा रहा हूँ"},
            {"prompt": "\"This is bigger than that\" uses the postposition:", "options": ["से", "में", "को", "का"], "answer": "से"},
        ],
    },

    # =====================================================================
    # B2 — UPPER-INTERMEDIATE: nuance, complex clauses, reading/writing
    # =====================================================================
    {
        "level": "B2", "title": "Relative-Correlative Clauses — जो...वह",
        "hook": "The Hindi equivalent of \"who/which/that\" clauses works as a matched PAIR of words, not one.",
        "sections": [
            {"heading": "How the pair works", "body": """
Where English uses a single relative pronoun ("the man **who** came"), Hindi pairs
**जो (jo, \"who/which/that\")** in one clause with a correlative like **वह (vah, \"he/that\")**
in the other — and either clause can come first:

**जो आदमी कल आया, वह मेरा दोस्त है।**
(jo aadmee kal aayaa, vah meraa dost hai)
— The man who came yesterday is my friend.
literally *"which man came yesterday, that [one] is my friend"*

**जो मेहनत करता है, वह सफल होता है।**
(jo mehnat kartaa hai, vah safal hotaa hai)
— Whoever works hard succeeds.
"""},
            {"heading": "Other जो/correlative pairs", "body": """
| जो-side | Correlative | Meaning |
|---|---|---|
| जो (jo) | वह/वे (vah/ve) | who/which → that/those |
| जब (jab) | तब (tab) | when → then |
| जहाँ (jahaan) | वहाँ (vahaan) | where → there |
| जैसा (jaisaa) | वैसा (vaisaa) | as/like → so/that way |
"""},
        ],
        "quiz_type": "static", "pass_pct": 65, "n_questions": 5,
        "quiz_static": [
            {"prompt": "Hindi relative clauses pair जो with which correlative word?", "options": ["वह/वे", "यह/ये", "कौन", "क्या"], "answer": "वह/वे"},
            {"prompt": "जब...तब means:", "options": ["when...then", "who...that", "where...there", "as...so"], "answer": "when...then"},
            {"prompt": "जहाँ...वहाँ means:", "options": ["where...there", "when...then", "who...that", "how...thus"], "answer": "where...there"},
            {"prompt": "In जो...वह sentences, which clause can come first?", "options": ["Either one", "Only the जो clause", "Only the वह clause", "Neither — order is fixed by verb tense"], "answer": "Either one"},
            {"prompt": "\"Whoever works hard succeeds\" uses which pair?", "options": ["जो...वह", "जब...तब", "जहाँ...वहाँ", "जैसा...वैसा"], "answer": "जो...वह"},
        ],
    },
    {
        "level": "B2", "title": "Compound Verbs — Adding Nuance with Helper Verbs",
        "hook": "Native speakers rarely use a bare verb alone — a small helper verb adds shades of completeness, suddenness, or effort.",
        "sections": [
            {"heading": "The pattern", "body": """
A **main verb stem** + a **conjugated helper verb** creates a "compound verb" that adds
nuance the main verb alone doesn't carry:

| Compound | Built from | Nuance added |
|---|---|---|
| कर लेना (kar lenaa) | करना + लेना | doing something for oneself / completing it |
| कर देना (kar denaa) | करना + देना | doing something for someone else / decisively |
| खा लेना (khaa lenaa) | खाना + लेना | finishing eating completely |
| आ जाना (aa jaanaa) | आना + जाना | arriving suddenly/completely |
| बैठ जाना (baiTh jaanaa) | बैठना + जाना | sitting down (completed motion) |

**मैंने खाना खा लिया** (mainne khaanaa khaa liyaa) — I finished eating (completely,
for myself) — noticeably more natural than the bare **मैंने खाना खाया**.
"""},
            {"heading": "Why this matters at B2", "body": """
Compound verbs are one of the clearest markers of natural, fluent Hindi versus
textbook Hindi. You won't need to produce every combination perfectly yet — but
recognizing them when you hear or read them is essential from this point forward.
"""},
        ],
        "quiz_type": "static", "pass_pct": 65, "n_questions": 4,
        "quiz_static": [
            {"prompt": "कर लेना adds the nuance of:", "options": ["Doing something for oneself / completing it", "Doing something for someone else", "Negation", "Future certainty"], "answer": "Doing something for oneself / completing it"},
            {"prompt": "आ जाना suggests:", "options": ["Arriving suddenly/completely", "Never arriving", "Arriving in the future only", "A polite request to come"], "answer": "Arriving suddenly/completely"},
            {"prompt": "A compound verb is built from:", "options": ["A main verb stem + a conjugated helper verb", "Two nouns", "A verb + a postposition", "An adjective + noun"], "answer": "A main verb stem + a conjugated helper verb"},
            {"prompt": "मैंने खाना खा लिया vs मैंने खाना खाया — the compound version emphasizes:", "options": ["Completeness/finishing the action", "The action never happened", "A future event", "A question"], "answer": "Completeness/finishing the action"},
        ],
    },
    {
        "level": "B2", "title": "Passive Voice",
        "hook": "Shift the focus from who did something to what happened to it.",
        "sections": [
            {"heading": "How it's formed", "body": """
Hindi forms the passive with **verb stem + या/ई/ए + जाना (conjugated)** — literally
"comes to be done":

**यह पत्र लिखा जाता है** (yah patra likhaa jaataa hai) — This letter is written. (habitual passive)
**दरवाज़ा खोला गया** (darvaazaa kholaa gayaa) — The door was opened. (past passive)

The doer of the action, if mentioned at all, takes **से**:

**यह किताब लेखक से लिखी गई** (yah kitaab lekhak se likhee gaii) — This book was written by the author.
"""},
            {"heading": "When it's used", "body": """
Like in English, Hindi passive is common in **formal writing, news, and official
language** where the doer is unknown or unimportant — you'll see it constantly once
you start reading newspapers in the C1 chapters ahead.
"""},
        ],
        "quiz_type": "static", "pass_pct": 65, "n_questions": 4,
        "quiz_static": [
            {"prompt": "The Hindi passive is formed with verb stem + या/ई/ए + which helper verb?", "options": ["जाना", "होना", "करना", "सकना"], "answer": "जाना"},
            {"prompt": "In a passive sentence, the doer of the action (if mentioned) takes which postposition?", "options": ["से", "को", "में", "का"], "answer": "से"},
            {"prompt": "\"The door was opened\" is:", "options": ["दरवाज़ा खोला गया", "दरवाज़ा खोलता है", "दरवाज़ा खोलेगा", "दरवाज़ा खोल रहा है"], "answer": "दरवाज़ा खोला गया"},
            {"prompt": "Passive voice in Hindi is especially common in:", "options": ["Formal writing and news", "Casual chat between friends only", "Only questions", "Only commands"], "answer": "Formal writing and news"},
        ],
    },
    {
        "level": "B2", "title": "Causative Verbs — Making Someone Do Something",
        "hook": "One more suffix pattern turns \"to do\" into \"to make someone do\" — and even \"to have someone make someone do.\"",
        "sections": [
            {"heading": "Two degrees of causation", "body": """
Hindi verb stems can take suffixes to add a layer of causation:

| Base | Direct causative (-आ/-वा) | Indirect causative (-वा) |
|---|---|---|
| करना (to do) | कराना (to get done) | करवाना (to have someone else get it done) |
| पढ़ना (to read) | पढ़ाना (to teach) | पढ़वाना (to have someone taught) |
| बनना (to be made) | बनाना (to make) | बनवाना (to have [something] made by someone) |

**मैं बच्चों को पढ़ाता हूँ** (main bachchon ko paRhaataa hoon) — I teach children.
(literally "I cause children to read")

**मैंने घर बनवाया** (mainne ghar banvaayaa) — I had a house built. (by hiring someone)
"""},
            {"heading": "Why this is genuinely advanced", "body": """
Distinguishing "I did X," "I made someone do X," and "I had someone arrange for someone
else to do X" in one clean suffix chain is something few learners nail before B2/C1 —
recognizing the pattern is the real win here; full mastery comes with exposure over time.
"""},
        ],
        "quiz_type": "static", "pass_pct": 60, "n_questions": 4,
        "quiz_static": [
            {"prompt": "पढ़ना (to read) as a direct causative (पढ़ाना) means:", "options": ["To teach", "To have taught by someone else", "To study harder", "To forget"], "answer": "To teach"},
            {"prompt": "करवाना (the indirect causative of करना) means:", "options": ["To have someone else get something done", "To do it yourself", "To never do it", "To ask a question"], "answer": "To have someone else get something done"},
            {"prompt": "मैंने घर बनवाया means:", "options": ["I had a house built (by hiring someone)", "I built a house myself", "I will build a house", "The house was never built"], "answer": "I had a house built (by hiring someone)"},
            {"prompt": "Causative suffixes in Hindi are used to express:", "options": ["Degrees of \"making someone do something\"", "Negation", "The past tense only", "Plural nouns"], "answer": "Degrees of \"making someone do something\""},
        ],
    },
    {
        "level": "B2", "title": "Conditionals — अगर...तो (\"If...Then\")",
        "hook": "Hypotheticals, hopes, and \"what if\" — the conditional mood.",
        "sections": [
            {"heading": "Real and hypothetical conditions", "body": """
**अगर (agar, \"if\") ... तो (to, \"then\")** frames a condition, with तो often optional:

**अगर बारिश होगी, तो हम घर पर रहेंगे।** (agar baarish hogee, to ham ghar par rahenge)
— If it rains, we'll stay home. (real/likely future condition — uses future tense in both clauses)

For **hypothetical/contrary-to-fact** conditions, both clauses shift into a special
subjunctive-like form ending in **-ता** regardless of tense:

**अगर मेरे पास पैसे होते, तो मैं यात्रा करता।** (agar mere paas paise hote, to main yaatraa kartaa)
— If I had money, I would travel. (implying: I don't)
"""},
            {"heading": "Reading the difference", "body": """
The real-condition version uses ordinary future tense and describes something that
could genuinely happen. The hypothetical version's telltale **-ता होता/करता** pattern
signals "this isn't true, but imagine if it were" — a distinction worth listening for
carefully in conversation and in writing.
"""},
        ],
        "quiz_type": "static", "pass_pct": 60, "n_questions": 4,
        "quiz_static": [
            {"prompt": "\"If...then\" in Hindi is expressed with:", "options": ["अगर...तो", "जो...वह", "क्योंकि...इसलिए", "चाहे...फिर भी"], "answer": "अगर...तो"},
            {"prompt": "A real/likely future condition (\"if it rains, we'll stay home\") typically uses:", "options": ["Future tense in both clauses", "The -ता hypothetical form", "The passive voice", "The imperative"], "answer": "Future tense in both clauses"},
            {"prompt": "The hypothetical/contrary-to-fact conditional pattern uses a form ending in:", "options": ["-ता (as in होता/करता)", "-एगा", "-कर", "-वाला"], "answer": "-ता (as in होता/करता)"},
            {"prompt": "अगर मेरे पास पैसे होते, तो मैं यात्रा करता implies:", "options": ["I don't actually have the money", "I definitely have the money", "This will happen tomorrow", "This already happened"], "answer": "I don't actually have the money"},
        ],
    },
    {
        "level": "B2", "title": "Reported Speech — \"He Said That...\"",
        "hook": "Relay what someone else said, without quoting them word for word.",
        "sections": [
            {"heading": "कि — the reporting word", "body": """
**कि (ki, \"that\")** introduces reported speech, much like English "that":

**उसने कहा कि वह आएगा।** (usne kahaa ki vah aayegaa) — He said that he would come.
**मैंने सुना कि वह बीमार है।** (mainne sunaa ki vah beemaar hai) — I heard that he is sick.

Unlike English, Hindi generally does **not** shift tense backward in reported speech —
if the original statement was "मैं आऊँगा" (I will come), the reported version keeps the
same future tense: "उसने कहा कि वह आएगा," not a shifted-back form.
"""},
            {"heading": "Reporting questions", "body": """
Reported questions keep the question word but drop the question mark, folding
naturally into the sentence:

**मैंने पूछा कि वह कहाँ है।** (mainne poochhaa ki vah kahaan hai) — I asked where he was.
"""},
        ],
        "quiz_type": "static", "pass_pct": 65, "n_questions": 4,
        "quiz_static": [
            {"prompt": "The word that introduces reported speech in Hindi is:", "options": ["कि", "जो", "अगर", "और"], "answer": "कि"},
            {"prompt": "\"He said that he would come\" is:", "options": ["उसने कहा कि वह आएगा", "उसने कहा वह आया", "वह कहा कि आएगा उसने", "उसने आएगा कहा"], "answer": "उसने कहा कि वह आएगा"},
            {"prompt": "Does Hindi typically shift tense backward in reported speech the way English does?", "options": ["No, the original tense is usually kept", "Yes, always shifts to past", "Only in formal writing", "Only for questions"], "answer": "No, the original tense is usually kept"},
            {"prompt": "\"I asked where he was\" is:", "options": ["मैंने पूछा कि वह कहाँ है", "मैंने कहा कि वह कहाँ है", "उसने पूछा मैं कहाँ हूँ", "वह कहाँ है मैंने पूछा नहीं"], "answer": "मैंने पूछा कि वह कहाँ है"},
        ],
    },
    {
        "level": "B2", "title": "Discourse Particles — तो, ही, भी, ना",
        "hook": "Tiny one-syllable words that native speakers use constantly to add emphasis, contrast, and tone.",
        "sections": [
            {"heading": "The core particles", "body": """
| Particle | Adds | Example |
|---|---|---|
| तो (to) | topic shift / emphasis / "well then" | तुम तो जानते हो — *You*, well, you know |
| ही (hii) | "only / precisely / exactly" — narrows focus | मैं ही जाऊँगा — I (and only I) will go |
| भी (bhee) | "also / even" | मैं भी आऊँगा — I will come too |
| ना (naa) | softens a statement into a tag question, like "right?" | अच्छा है ना? — It's good, right? |

These particles carry **no dictionary meaning on their own** — their entire job is tone
and emphasis, which is exactly why they're hard to notice as a learner but instantly
recognizable once you know to listen for them.
"""},
            {"heading": "Stacking particles", "body": """
Native speech often stacks two: **मुझे ही तो पता था** (mujhe hii to pataa thaa) —
"I'm the only one who actually knew" — carries a very different emotional color than
the plain **मुझे पता था** ("I knew"), even though the core facts are identical.
"""},
        ],
        "quiz_type": "static", "pass_pct": 60, "n_questions": 4,
        "quiz_static": [
            {"prompt": "ही (hii) adds the nuance of:", "options": ["\"only / precisely / exactly\"", "\"also / even\"", "A question tag", "Negation"], "answer": "\"only / precisely / exactly\""},
            {"prompt": "भी (bhee) means:", "options": ["also / even", "only", "never", "because"], "answer": "also / even"},
            {"prompt": "ना (naa) at the end of a statement often functions like:", "options": ["A tag question (\"...right?\")", "A negative command", "A plural marker", "A postposition"], "answer": "A tag question (\"...right?\")"},
            {"prompt": "Discourse particles like तो/ही/भी/ना mainly affect:", "options": ["Tone and emphasis, not core dictionary meaning", "Verb tense", "Noun gender", "Plural vs singular"], "answer": "Tone and emphasis, not core dictionary meaning"},
        ],
    },
    {
        "level": "B2", "title": "B2 Checkpoint — Reading & Writing a Paragraph",
        "hook": "Pull together relative clauses, compound verbs, passive/causative, conditionals, and particles.",
        "sections": [
            {"heading": "A worked example", "body": """
Read this short paragraph slowly, using everything from B2:

> जो लोग रोज़ पढ़ते हैं, वे जल्दी सीखते हैं। अगर आप मेहनत करेंगे, तो आपको सफलता ज़रूर मिलेगी।
> मैंने सुना है कि यह किताब एक मशहूर लेखक से लिखी गई थी। इसे पढ़कर मुझे बहुत कुछ सीखने को मिला।

*"People who study daily learn quickly. If you work hard, you will definitely find
success. I've heard that this book was written by a famous author. Having read it,
I got to learn a lot."*

Notice जो...वे (relative-correlative), अगर...तो (conditional), a passive (लिखी गई),
कि (reported speech), and सीखकर-style -कर (conjunctive participle) — all in four
sentences. This is genuinely what upper-intermediate written Hindi looks like.
"""},
        ],
        "quiz_type": "static", "pass_pct": 70, "n_questions": 8,
        "quiz_static": [
            {"prompt": "जो लोग रोज़ पढ़ते हैं, वे... uses which construction?", "options": ["Relative-correlative (जो...वे)", "Passive voice", "Causative", "Reported speech"], "answer": "Relative-correlative (जो...वे)"},
            {"prompt": "लिखी गई (\"was written\") is an example of:", "options": ["Passive voice", "Causative", "Conditional", "Discourse particle"], "answer": "Passive voice"},
            {"prompt": "मैंने सुना है कि... introduces:", "options": ["Reported speech", "A conditional", "A compound verb", "A relative clause"], "answer": "Reported speech"},
            {"prompt": "अगर आप मेहनत करेंगे, तो... is a:", "options": ["Real/likely conditional", "Hypothetical conditional", "Passive sentence", "Reported question"], "answer": "Real/likely conditional"},
            {"prompt": "पढ़कर (\"having read\") uses the ending:", "options": ["-कर", "-गया", "-वाना", "-ता"], "answer": "-कर"},
            {"prompt": "बनवाना (causative of बनाना) means:", "options": ["To have something made by someone else", "To make something yourself", "To break something", "To read something"], "answer": "To have something made by someone else"},
            {"prompt": "ज़रूर in the example paragraph adds the sense of:", "options": ["Certainty (\"definitely\")", "Doubt", "The past tense", "A question"], "answer": "Certainty (\"definitely\")"},
            {"prompt": "This checkpoint corresponds to genuinely reaching CEFR level:", "options": ["B2", "A1", "A2", "C2"], "answer": "B2"},
        ],
    },

    # =====================================================================
    # C1 — ADVANCED: register, idiom, and real unadapted Hindi
    # =====================================================================
    {
        "level": "C1", "title": "Registers — Sanskritized vs. Persian/Urdu Vocabulary",
        "hook": "Hindi has two vocabulary registers layered on top of everyday speech — knowing which is which unlocks news, literature, and formal writing.",
        "sections": [
            {"heading": "Two historical layers", "body": """
Modern Hindi draws on two prestige vocabulary sources beyond everyday spoken words:

- **तत्सम (tatsam)** — words borrowed directly from Sanskrit, common in formal, academic,
  and government Hindi: विद्यालय (vidyaalay, "educational institution") vs. everyday स्कूल (school).
- **Perso-Arabic** — words from Persian/Arabic via centuries of Mughal-era contact, common
  in poetry, Bollywood lyrics, and everyday emotional/poetic speech: मोहब्बत (mohabbat, "love")
  alongside the more neutral प्यार (pyaar).

Both layers coexist with everyday spoken vocabulary — a fluent speaker moves between all
three depending on formality and audience, the same way an English speaker shifts between
"help," "assist," and "facilitate."
"""},
            {"heading": "Recognizing register in the wild", "body": """
News broadcasts and government documents lean heavily तत्सम/Sanskritized;
Bollywood lyrics and shayari (poetry) lean Perso-Arabic; daily conversation mixes
freely with English loanwords thrown in too. Learning to *recognize* all three,
even before you can produce them fluently, is what separates B2 from C1 comprehension.
"""},
        ],
        "quiz_type": "static", "pass_pct": 60, "n_questions": 4,
        "quiz_static": [
            {"prompt": "तत्सम (tatsam) words are borrowed directly from:", "options": ["Sanskrit", "Persian", "Arabic", "English"], "answer": "Sanskrit"},
            {"prompt": "मोहब्बत (mohabbat, \"love\") is an example of vocabulary from:", "options": ["Perso-Arabic", "Sanskrit", "English loanwords", "Tamil"], "answer": "Perso-Arabic"},
            {"prompt": "Government documents and news broadcasts tend to lean toward:", "options": ["Sanskritized (तत्सम) vocabulary", "Perso-Arabic poetic vocabulary", "English slang", "Regional dialect only"], "answer": "Sanskritized (तत्सम) vocabulary"},
            {"prompt": "Bollywood lyrics and shayari (poetry) lean toward:", "options": ["Perso-Arabic vocabulary", "Only Sanskrit", "Only everyday spoken words", "Only English"], "answer": "Perso-Arabic vocabulary"},
        ],
    },
    {
        "level": "C1", "title": "Idioms & Proverbs (मुहावरे और कहावतें)",
        "hook": "Figurative language is where fluent speakers actually live — literal translation stops working here.",
        "sections": [
            {"heading": "Common idioms", "body": """
| Idiom | Literally | Actually means |
|---|---|---|
| नाक में दम करना | to put breath in the nose | to harass/exhaust someone relentlessly |
| आँखों में धूल झोंकना | to throw dust in the eyes | to deceive someone |
| दाल में कुछ काला होना | something black is in the lentils | something is suspicious/fishy |
| नौ दो ग्यारह होना | to become nine-two-eleven | to flee/vanish quickly |
"""},
            {"heading": "Common proverbs", "body": """
| Proverb | Meaning |
|---|---|
| जैसी करनी वैसी भरनी | You reap what you sow. |
| अंधों में काना राजा | In the land of the blind, the one-eyed man is king. |
| बूँद-बूँद से सागर बनता है | An ocean is made drop by drop (small efforts add up). |

Idioms and proverbs are learned as **whole units**, not decoded word by word — treat
each one as its own small vocabulary item to memorize.
"""},
        ],
        "quiz_type": "static", "pass_pct": 60, "n_questions": 4,
        "quiz_static": [
            {"prompt": "नाक में दम करना actually means:", "options": ["To harass/exhaust someone relentlessly", "To breathe deeply", "To smell something bad", "To apologize"], "answer": "To harass/exhaust someone relentlessly"},
            {"prompt": "आँखों में धूल झोंकना means:", "options": ["To deceive someone", "To cry", "To clean something", "To fall asleep"], "answer": "To deceive someone"},
            {"prompt": "जैसी करनी वैसी भरनी corresponds to the English proverb:", "options": ["You reap what you sow", "The early bird catches the worm", "Actions speak louder than words", "Better late than never"], "answer": "You reap what you sow"},
            {"prompt": "The best way to learn idioms is to:", "options": ["Memorize them as whole units, not word-by-word", "Translate each word literally", "Avoid them entirely", "Only use them in writing, never speech"], "answer": "Memorize them as whole units, not word-by-word"},
        ],
    },
    {
        "level": "C1", "title": "Formal, Literary & Media Hindi",
        "hook": "News anchors, official notices, and novels use structures you won't hear on the street — recognize them on sight.",
        "sections": [
            {"heading": "Markers of formal/media register", "body": """
- Heavy use of the **passive voice** (from your B2 chapter) to sound objective:
  **यह निर्णय लिया गया है** (yah nirnay liyaa gayaa hai) — "This decision has been taken."
- **Sanskritized compound nouns** stacked together: राष्ट्रपति (raashTrapati, "president",
  literally "lord of the nation"), प्रधानमंत्री (pradhaanamantree, "prime minister").
- Longer, subordinate-clause-heavy sentences using जो/कि/जबकि (jabki, "whereas") to
  connect ideas, rather than short simple sentences.
"""},
            {"heading": "A worked news-style sentence", "body": """
**सरकार द्वारा घोषित नई नीति के अनुसार, अगले वर्ष से सभी विद्यालयों में यह लागू की जाएगी।**
(sarkaar dvaaraa ghoshit naii neeti ke anusaar, agle varsh se sabhee vidyaalayon mein
yah laagoo kee jaaegee)
— "According to the new policy announced by the government, this will be implemented
in all schools starting next year."

Note **द्वारा (dvaaraa, "by")** as the formal alternative to से for marking the doer in
passive sentences — a register marker on its own.
"""},
        ],
        "quiz_type": "static", "pass_pct": 60, "n_questions": 4,
        "quiz_static": [
            {"prompt": "Formal/media Hindi favors which voice, to sound objective?", "options": ["Passive voice", "First-person imperative", "Casual present tense only", "Question form"], "answer": "Passive voice"},
            {"prompt": "द्वारा (dvaaraa) is a formal alternative to which everyday postposition for marking the doer?", "options": ["से", "को", "में", "का"], "answer": "से"},
            {"prompt": "जबकि (jabki) means:", "options": ["whereas", "because", "therefore", "although never"], "answer": "whereas"},
            {"prompt": "राष्ट्रपति (\"president\") is an example of:", "options": ["A Sanskritized compound noun", "A Perso-Arabic loanword", "An English loanword", "A casual slang term"], "answer": "A Sanskritized compound noun"},
        ],
    },
    {
        "level": "C1", "title": "Expressing Opinion, Nuance & Argument",
        "hook": "Agree, disagree, hedge, and build a persuasive point — the language of real debate and discussion.",
        "sections": [
            {"heading": "Framing an opinion", "body": """
| Hindi | Meaning |
|---|---|
| मेरे विचार से (mere vichaar se) | In my opinion |
| मुझे लगता है कि (mujhe lagtaa hai ki) | I feel/think that |
| एक तरफ...दूसरी तरफ (ek taraf...doosree taraf) | On one hand...on the other hand |
| हालाँकि (haalaanki) | Although / however |
| इसलिए (isliye) | Therefore |
| इसके अलावा (iske alaavaa) | In addition to this |
"""},
            {"heading": "A short argumentative paragraph", "body": """
**मेरे विचार से, तकनीक ने शिक्षा को बेहतर बनाया है। हालाँकि, कुछ लोग मानते हैं कि इससे
छात्रों का ध्यान भटकता है। एक तरफ ऑनलाइन शिक्षा सबके लिए उपलब्ध है, दूसरी तरफ इसकी
गुणवत्ता हमेशा एक जैसी नहीं होती। इसलिए, संतुलन बनाना ज़रूरी है।**

*"In my opinion, technology has improved education. However, some people believe it
distracts students. On one hand, online education is accessible to everyone; on the
other hand, its quality isn't always consistent. Therefore, finding balance is important."*
"""},
        ],
        "quiz_type": "static", "pass_pct": 60, "n_questions": 4,
        "quiz_static": [
            {"prompt": "\"In my opinion\" is:", "options": ["मेरे विचार से", "इसलिए", "हालाँकि", "जबकि"], "answer": "मेरे विचार से"},
            {"prompt": "हालाँकि means:", "options": ["although / however", "therefore", "in addition", "because"], "answer": "although / however"},
            {"prompt": "इसलिए means:", "options": ["therefore", "however", "on one hand", "in my opinion"], "answer": "therefore"},
            {"prompt": "एक तरफ...दूसरी तरफ is used to:", "options": ["Present two contrasting sides of an argument", "Give a command", "Ask a question", "Report someone's speech"], "answer": "Present two contrasting sides of an argument"},
        ],
    },
    {
        "level": "C1", "title": "Reading Unadapted Text — Strategy",
        "hook": "A practical toolkit for tackling real newspapers, novels, or subtitles with no simplification.",
        "sections": [
            {"heading": "A reading strategy that actually works", "body": """
1. **Read the whole sentence once without stopping**, even if you don't understand
   every word — get the shape of it first (subject...eventually...verb at the end).
2. **Find the verb first**, since it's always at the end and tells you tense/mood,
   then work backward to attach the subject and object.
3. **Flag unfamiliar Sanskritized/Perso-Arabic vocabulary** rather than stopping to
   look each one up immediately — often 2-3 unknown words per sentence is still readable
   from context.
4. **Watch for passive voice and द्वारा** in news writing — it changes who's doing what.
5. Use this app's **Dictionary Search** for anything that blocks real comprehension,
   not every unfamiliar word.
"""},
            {"heading": "What to read next", "body": """
Once this chapter's quiz is passed, you've completed the full Storyline. From here,
real fluency comes from **volume of exposure**: news apps, subtitled shows, podcasts,
and conversation with native speakers — the app's Dictionary Search and Homework
generator remain useful tools to keep sharp indefinitely.
"""},
        ],
        "quiz_type": "static", "pass_pct": 60, "n_questions": 4,
        "quiz_static": [
            {"prompt": "When reading a difficult Hindi sentence, which word should you locate first?", "options": ["The verb (it's always last)", "The subject (it's always first)", "The first noun you see", "The postposition"], "answer": "The verb (it's always last)"},
            {"prompt": "A practical reading strategy for unfamiliar words is to:", "options": ["Flag them and keep reading for context, rather than stopping every time", "Stop and look up every single word immediately", "Skip the sentence entirely", "Only read sentences with zero unknown words"], "answer": "Flag them and keep reading for context, rather than stopping every time"},
            {"prompt": "Seeing द्वारा in a news sentence is a strong hint that the sentence is likely:", "options": ["Passive voice", "A question", "An idiom", "A conditional"], "answer": "Passive voice"},
            {"prompt": "After finishing this Storyline, ongoing fluency mainly comes from:", "options": ["Volume of real exposure — news, shows, conversation", "Re-reading only this app's material", "Memorizing the dictionary end to end", "Grammar drills alone"], "answer": "Volume of real exposure — news, shows, conversation"},
        ],
    },
    {
        "level": "C1", "title": "C1 Capstone — Free Conversation & Self-Assessment",
        "hook": "The final chapter — a full-spectrum check spanning everything from Vowels to Register.",
        "sections": [
            {"heading": "You've reached the end of the path", "body": """
This capstone mixes questions from every level of the Storyline — script, core grammar,
past tense, politeness, complex clauses, and register. Passing it is a genuine, honest
marker of reaching **CEFR C1**: you can read real Hindi text, follow native-speed
conversation and media on most topics, and express nuanced opinions — while still
having room to grow toward full native-level mastery (C2), which only comes from years
of immersion.

Well done getting here — this represents hundreds of hours of real learning.
"""},
        ],
        "quiz_type": "static", "pass_pct": 75, "n_questions": 10,
        "quiz_static": [
            {"prompt": "The ि matra is pronounced:", "options": ["After its consonant, though written before it", "Exactly where it's written", "Silently", "Only in conjuncts"], "answer": "After its consonant, though written before it"},
            {"prompt": "Hindi basic word order is:", "options": ["Subject-Object-Verb", "Subject-Verb-Object", "Verb-Subject-Object", "Free word order with no pattern"], "answer": "Subject-Object-Verb"},
            {"prompt": "\"I drank tea\" (मैंने चाय पी) uses the ने construction because पीना is:", "options": ["Transitive", "Intransitive", "A modal verb", "An irregular auxiliary"], "answer": "Transitive"},
            {"prompt": "The safest default \"you\" with strangers/elders is:", "options": ["आप", "तू", "तुम", "None — pronouns are optional"], "answer": "आप"},
            {"prompt": "जो...वह is used to build:", "options": ["Relative-correlative clauses", "The passive voice", "The future tense", "Discourse particles"], "answer": "Relative-correlative clauses"},
            {"prompt": "The Hindi passive voice is built with verb stem + या/ई/ए +:", "options": ["जाना", "होना", "करना", "सकना"], "answer": "जाना"},
            {"prompt": "द्वारा is a formal alternative to which postposition for marking the doer?", "options": ["से", "को", "में", "का"], "answer": "से"},
            {"prompt": "तत्सम words are borrowed directly from:", "options": ["Sanskrit", "Persian", "English", "Tamil"], "answer": "Sanskrit"},
            {"prompt": "मेरे विचार से means:", "options": ["In my opinion", "Therefore", "However", "On the other hand"], "answer": "In my opinion"},
            {"prompt": "This capstone chapter corresponds to reaching CEFR level:", "options": ["C1", "A1", "A2", "B1"], "answer": "C1"},
        ],
    },
]

# Attach stable ids/numbers derived from position in the list.
STORYLINE_CHAPTERS = []
for _i, _ch in enumerate(_CHAPTERS_RAW):
    _ch = dict(_ch)
    _ch["num"] = _i + 1
    _ch["id"] = f"ch{_i + 1:02d}"
    _ch.setdefault("pass_pct", 70)
    _ch.setdefault("n_questions", 6)
    STORYLINE_CHAPTERS.append(_ch)

STORYLINE_BY_ID = {c["id"]: c for c in STORYLINE_CHAPTERS}
STORYLINE_LEVELS = ["A1", "A2", "B1", "B2", "C1"]
