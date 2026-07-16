"""Grammar lesson content, organized as a curriculum of units and lessons."""

GRAMMAR_LESSONS = [
    {
        "title": "Word Order: Subject-Object-Verb",
        "content": """
Hindi puts the verb **last** in a sentence, unlike English/French (Subject-Verb-Object).

**मैं पानी पीता हूँ** (main paanee peetaa hoon)
literally *"I water drink"* → **I drink water.**

As you build sentences, always save the verb for the end.
""",
    },
    {
        "title": "Grammatical Gender",
        "content": """
Every Hindi noun is masculine or feminine (no neuter) — like French *le/la* — but in Hindi
the gender also changes the **verb ending**, which French does not do.

| Pattern | Gender | Examples |
|---|---|---|
| Nouns ending in **-आ (aa)** | usually masculine | लड़का (larkaa) boy, कमरा (kamraa) room |
| Nouns ending in **-ई (ii) / -िया** | usually feminine | लड़की (larkee) girl, चिड़िया (chiRiyaa) bird |
| Nouns ending in a consonant | either — no visual rule | किताब (kitaab, f.) book, घर (ghar, m.) house |

Exceptions exist — learn gender together with the word, just like French *le/la*.
""",
    },
    {
        "title": "Plural Nouns",
        "content": """
| Category | Rule | Example |
|---|---|---|
| Masculine, ends in -aa | -aa → -e | लड़का → लड़के (larkaa → larke) |
| Masculine, ends in consonant | no change | घर → घर |
| Feminine, ends in -ii/-iyaa | -ii/-iyaa → -iyaan | लड़की → लड़कियाँ |
| Feminine, ends in consonant | add -en | किताब → किताबें |
""",
    },
    {
        "title": "Postpositions (come AFTER the noun)",
        "content": """
Hindi has no prepositions — it uses **postpositions** that follow the noun.

| Hindi | Meaning | Example |
|---|---|---|
| में (mein) | in | घर में — in the house |
| पर (par) | on | मेज़ पर — on the table |
| से (se) | from / by / with | स्कूल से — from school |
| को (ko) | to / object marker | राम को — to Ram |
| का/की/के (kaa/kii/ke) | of / possessive (agrees with the following noun) | राम का घर — Ram's house |
| तक (tak) | until | कल तक — until tomorrow |
| के लिए (ke liye) | for | आपके लिए — for you |
| के साथ (ke saath) | with | दोस्त के साथ — with a friend |
| के बाद (ke baad) | after | खाने के बाद — after eating |
| से पहले (se pehle) | before | सोने से पहले — before sleeping |
| के पास (ke paas) | near / to have | मेरे पास किताब है — I have a book |
""",
    },
    {
        "title": "The Three Levels of 'You'",
        "content": """
| Hindi | Usage |
|---|---|
| तू (too) | very intimate — close friends, children, God |
| तुम (tum) | informal — friends, peers — like French *tu* |
| आप (aap) | formal/respectful — like French *vous*, always safe as default |

Default to **आप** with strangers, elders, or in professional settings.
""",
    },
    {
        "title": "Adjective Agreement",
        "content": """
Adjectives ending in **-आ (aa)** change to match the noun's gender and number,
just like French *grand/grande*:

अच्छा लड़का (achchhaa larkaa, good boy) → अच्छी लड़की (achchhee larkee, good girl)
→ अच्छे लड़के (achchhe larke, good boys)

Adjectives that don't end in -aa (like सुंदर, sundar, "beautiful") don't change form.
""",
    },
    {
        "title": "Present Habitual Tense",
        "content": """
Formed as: **verb stem + ता/ती/ते** (agreeing with gender/number) **+ a form of होना** (to be: हूँ/है/हो/हैं).

Example with जाना (jaanaa, "to go"):

- मैं जाता हूँ / जाती हूँ — I go (m/f)
- तुम जाते हो / जाती हो — you go (informal)
- वह जाता है / जाती है — he/she goes
- हम जाते हैं / जाती हैं — we go
- आप जाते हैं / जाती हैं — you go (formal)

Use the **Verb Trainer** page to drill this across 15 verbs.
""",
    },
    {
        "title": "Future Tense",
        "content": """
Formed as: **verb stem + ऊँगा/एगा/ओगे...** (agreeing with the subject).

Example with जाना:
- मैं जाऊँगा / जाऊँगी — I will go
- तुम जाओगे / जाओगी — you will go
- वह जाएगा / जाएगी — he/she will go

Use the **Verb Trainer** to practice future forms of all 15 verbs.
""",
    },
    {
        "title": "Simple Past & the ने (ne) Construction",
        "content": """
This is the biggest grammar surprise for English/French speakers.

In the simple past, **transitive verbs** (verbs that take a direct object, like "do" or "eat")
require the subject to take **ने (ne)**, and the **verb agrees with the OBJECT's gender/number**
instead of the subject's.

**मैंने चाय पी** (mainne chaay pee) = "I drank tea" — पी is feminine because *chaay* (tea) is
feminine, NOT because "I" am. This has no French/English equivalent — it takes real practice.

**Intransitive verbs** (जाना/to go, आना/to come, सोना/to sleep) do **NOT** use ने —
जाना's past is simply गया/गई/गए (gayaa/gaii/gae), agreeing with the subject as normal.
""",
    },
    {
        "title": "Negation",
        "content": """
Place **नहीं (naheen, "not")** directly before the verb:

मैं नहीं जाता हूँ (main naheen jaataa hoon) — I don't go.
""",
    },
    {
        "title": "Forming Questions",
        "content": """
Hindi word order usually doesn't change for questions. Add a question word
(क्या/कौन/कहाँ/कब/क्यों/कैसे/कितना) or simply raise your intonation at the end for
yes/no questions:

क्या आप जाते हैं? (kyaa aap jaate hain?) — Do you go?
""",
    },
]

CEFR_MILESTONES = [
    ("Beginner (A1)", "Read Devanagari slowly; introduce yourself; use survival phrases"),
    ("Elementary (A2)", "Build grammatically correct simple sentences in 3 tenses; ask/answer basic questions"),
    ("Intermediate (B1)", "Hold themed conversations (food, shopping, directions, family) without a script"),
    ("Upper-Intermediate (B1+)", "Read short unaided texts; write coherent paragraphs; follow connected speech at moderate pace"),
    ("Conversational (B2)", "Follow native-speed conversation on familiar topics; handle unscripted real-life situations"),
]
