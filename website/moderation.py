import re

BANNED_WORDS = [
    "fuck",
    "fucking",
    "fucker",
    "shit",
    "bullshit",
    "bitch",
    "bastard",
    "asshole",
    "dick",
    "pussy",
    "cunt",
    "motherfucker",
    "whore",
    "slut",
    "retard",
    "retarded",
    "nigger",
    "nigga",
    "faggot",
    "dyke",
    "tranny",
    "kike",
    "spic",
    "chink",
    "gook",
    "cracker",
    "wetback",
    "twat",
    "jackass",
    "douche",
    "douchebag",
    "cock",
    "cum",
    "jizz",
    "penis",
    "vagina",
    "rape",
    "rapist",
    "pedo",
    "pedophile",
    "molest",
    "suicide",
    "kill yourself",
    "kys",
    "idiot",
    "moron",
    "loser",
    "dipshit",
    "piece of shit",
    "scumbag",
    "jew",
]


def normalize_text(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    text = re.sub(r"\s+", "", text)
    
    return text

def contains_banned_words(text):
    normalized_text = normalize_text(text)
    
    for word in BANNED_WORDS:
        normalized_word = normalize_text(word)
        
        if normalized_word in normalized_text:
            return True
        
    return False