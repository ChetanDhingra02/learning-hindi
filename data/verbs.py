"""Full conjugation paradigms for core Hindi verbs.
PRONOUNS order: main, tu, tum, vah, hum, aap, ve
Each tense dict maps pronoun -> (masculine_form, feminine_form)
Past tense forms shown are the participle used with ने (ne) for transitive verbs,
or the plain intransitive past for verbs like jaana/aana/sona.
"""

PRONOUNS = ["main", "tu", "tum", "vah", "hum", "aap", "ve"]
PRONOUN_LABELS = {
    "main": "मैं (I)", "tu": "तू (you, intimate)", "tum": "तुम (you, informal)",
    "vah": "यह/वह (he/she/it)", "hum": "हम (we)", "aap": "आप (you, formal)", "ve": "ये/वे (they)",
}
# whether the subject is grammatically singular(1) or plural(0) form of verb used
PRONOUN_NUMBER = {"main": "sg", "tu": "sg", "tum": "pl", "vah": "sg", "hum": "pl", "aap": "pl", "ve": "pl"}


def _present(stem_m_sg, stem_f_sg, stem_m_pl, stem_f_pl):
    """Build present-habitual paradigm given the four base forms (stem+taa etc. already conjugated)."""
    return {
        "main": (stem_m_sg + " हूँ", stem_f_sg + " हूँ"),
        "tu":   (stem_m_sg + " है", stem_f_sg + " है"),
        "tum":  (stem_m_pl + " हो", stem_f_sg + " हो"),
        "vah":  (stem_m_sg + " है", stem_f_sg + " है"),
        "hum":  (stem_m_pl + " हैं", stem_f_pl + " हैं"),
        "aap":  (stem_m_pl + " हैं", stem_f_pl + " हैं"),
        "ve":   (stem_m_pl + " हैं", stem_f_pl + " हैं"),
    }

def _future(m_sg, f_sg, m_sg2, f_sg2, m_pl2, f_pl2, m_pl, f_pl):
    return {
        "main": (m_sg, f_sg),
        "tu":   (m_sg2, f_sg2),
        "tum":  (m_pl2, f_pl2),
        "vah":  (m_sg2, f_sg2),
        "hum":  (m_pl, f_pl),
        "aap":  (m_pl, f_pl),
        "ve":   (m_pl, f_pl),
    }

def _past(m_sg, f_sg, m_pl, f_pl, needs_ne=True):
    subj_labels = {
        "main": "मैंने" if needs_ne else "मैं", "tu": "तूने" if needs_ne else "तू",
        "tum": "तुमने" if needs_ne else "तुम", "vah": "उसने" if needs_ne else "वह/यह",
        "hum": "हमने" if needs_ne else "हम", "aap": "आपने" if needs_ne else "आप",
        "ve": "उन्होंने" if needs_ne else "वे/ये",
    }
    return {
        "main": (m_sg, f_sg), "tu": (m_sg, f_sg), "tum": (m_sg, f_sg),
        "vah": (m_sg, f_sg), "hum": (m_pl, f_pl), "aap": (m_sg, f_sg), "ve": (m_pl, f_pl),
    }, subj_labels


VERBS = {}

def add_verb(key, hi, translit, meaning, present, future, past, past_needs_ne=True, note=""):
    p_forms, p_labels = past
    VERBS[key] = {
        "hi": hi, "translit": translit, "meaning": meaning, "note": note,
        "present": present, "future": future, "past": p_forms, "past_subject_labels": p_labels,
        "past_needs_ne": past_needs_ne,
    }

add_verb("karna", "करना", "karnaa", "to do",
    _present("करता", "करती", "करते", "करती"),
    _future("करूँगा", "करूँगी", "करेगा", "करेगी", "करोगे", "करोगी", "करेंगे", "करेंगी"),
    _past("किया", "की", "किये", "कीं"))

add_verb("jaana", "जाना", "jaanaa", "to go",
    _present("जाता", "जाती", "जाते", "जाती"),
    _future("जाऊँगा", "जाऊँगी", "जाएगा", "जाएगी", "जाओगे", "जाओगी", "जाएंगे", "जाएंगी"),
    _past("गया", "गई", "गए", "गईं"), past_needs_ne=False,
    note="Irregular past (gayaa/gaii); does NOT take ने because it's intransitive.")

add_verb("khaana", "खाना", "khaanaa", "to eat",
    _present("खाता", "खाती", "खाते", "खाती"),
    _future("खाऊँगा", "खाऊँगी", "खाएगा", "खाएगी", "खाओगे", "खाओगी", "खाएंगे", "खाएंगी"),
    _past("खाया", "खाई", "खाए", "खाईं"))

add_verb("peena", "पीना", "peenaa", "to drink",
    _present("पीता", "पीती", "पीते", "पीती"),
    _future("पीऊँगा", "पीऊँगी", "पीएगा", "पीएगी", "पीओगे", "पीओगी", "पीएंगे", "पीएंगी"),
    _past("पिया", "पी", "पिए", "पीं"))

add_verb("dekhna", "देखना", "dekhnaa", "to see / watch",
    _present("देखता", "देखती", "देखते", "देखती"),
    _future("देखूँगा", "देखूँगी", "देखेगा", "देखेगी", "देखोगे", "देखोगी", "देखेंगे", "देखेंगी"),
    _past("देखा", "देखी", "देखे", "देखीं"))

add_verb("sunna", "सुनना", "sunnaa", "to hear / listen",
    _present("सुनता", "सुनती", "सुनते", "सुनती"),
    _future("सुनूँगा", "सुनूँगी", "सुनेगा", "सुनेगी", "सुनोगे", "सुनोगी", "सुनेंगे", "सुनेंगी"),
    _past("सुना", "सुनी", "सुने", "सुनीं"))

add_verb("bolna", "बोलना", "bolnaa", "to speak",
    _present("बोलता", "बोलती", "बोलते", "बोलती"),
    _future("बोलूँगा", "बोलूँगी", "बोलेगा", "बोलेगी", "बोलोगे", "बोलोगी", "बोलेंगे", "बोलेंगी"),
    _past("बोला", "बोली", "बोले", "बोलीं"))

add_verb("aana", "आना", "aanaa", "to come",
    _present("आता", "आती", "आते", "आती"),
    _future("आऊँगा", "आऊँगी", "आएगा", "आएगी", "आओगे", "आओगी", "आएंगे", "आएंगी"),
    _past("आया", "आई", "आए", "आईं"), past_needs_ne=False,
    note="Intransitive; does not take ने.")

add_verb("lena", "लेना", "lenaa", "to take",
    _present("लेता", "लेती", "लेते", "लेती"),
    _future("लूँगा", "लूँगी", "लेगा", "लेगी", "लोगे", "लोगी", "लेंगे", "लेंगी"),
    _past("लिया", "ली", "लिए", "लीं"))

add_verb("dena", "देना", "denaa", "to give",
    _present("देता", "देती", "देते", "देती"),
    _future("दूँगा", "दूँगी", "देगा", "देगी", "दोगे", "दोगी", "देंगे", "देंगी"),
    _past("दिया", "दी", "दिए", "दीं"))

add_verb("padhna", "पढ़ना", "paDhnaa", "to read / study",
    _present("पढ़ता", "पढ़ती", "पढ़ते", "पढ़ती"),
    _future("पढ़ूँगा", "पढ़ूँगी", "पढ़ेगा", "पढ़ेगी", "पढ़ोगे", "पढ़ोगी", "पढ़ेंगे", "पढ़ेंगी"),
    _past("पढ़ा", "पढ़ी", "पढ़े", "पढ़ीं"))

add_verb("likhna", "लिखना", "likhnaa", "to write",
    _present("लिखता", "लिखती", "लिखते", "लिखती"),
    _future("लिखूँगा", "लिखूँगी", "लिखेगा", "लिखेगी", "लिखोगे", "लिखोगी", "लिखेंगे", "लिखेंगी"),
    _past("लिखा", "लिखी", "लिखे", "लिखीं"))

add_verb("sona", "सोना", "sonaa", "to sleep",
    _present("सोता", "सोती", "सोते", "सोती"),
    _future("सोऊँगा", "सोऊँगी", "सोएगा", "सोएगी", "सोओगे", "सोओगी", "सोएंगे", "सोएंगी"),
    _past("सोया", "सोई", "सोए", "सोईं"), past_needs_ne=False,
    note="Intransitive; does not take ने.")

add_verb("khelna", "खेलना", "khelnaa", "to play",
    _present("खेलता", "खेलती", "खेलते", "खेलती"),
    _future("खेलूँगा", "खेलूँगी", "खेलेगा", "खेलेगी", "खेलोगे", "खेलोगी", "खेलेंगे", "खेलेंगी"),
    _past("खेला", "खेली", "खेले", "खेलीं"))

add_verb("samajhna", "समझना", "samajhnaa", "to understand",
    _present("समझता", "समझती", "समझते", "समझती"),
    _future("समझूँगा", "समझूँगी", "समझेगा", "समझेगी", "समझोगे", "समझोगी", "समझेंगे", "समझेंगी"),
    _past("समझा", "समझी", "समझे", "समझीं"))
