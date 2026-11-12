"""VELOCITY LONGFORM - 16:9 chapter lesson, brand and motion constants."""

import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

OUTPUT_DIR = BASE_DIR / "output"
LESSONS_DIR = OUTPUT_DIR / "lessons"
HISTORY_DIR = OUTPUT_DIR / "history"
SCENE_DIR = BASE_DIR / "scene"

VIDEO_WIDTH = 1920
VIDEO_HEIGHT = 1080
FPS = 30

TARGET_CHAPTERS = 8
PHRASES_PER_CHAPTER = 7
TARGET_PHRASES = TARGET_CHAPTERS * PHRASES_PER_CHAPTER

# ---------------------------------------------------------------- brand

BRAND = "VELOCITY ITALIAN"
BRAND_LOCKUP_TOP = "VELOCITY"
BRAND_LOCKUP_BOTTOM = "ITALIAN"
HANDLE = "@velocityitalian"
MASCOT_NAME = "Velo"

# ==== LANGUAGE PACK START ====
LANGUAGE = {'code': 'it',
 'name': 'Italian',
 'native_name': 'Italiano',
 'history_key': 'italian',
 'english_voice': 'en-US-AvaNeural',
 'english_fallback_voice': 'en-US-GuyNeural',
 'native_voice': 'it-IT-DiegoNeural',
 'native_fallback_voice': 'it-IT-ElsaNeural',
 'native_engine': 'edge',
 'native_lang_code': 'it',
 'english_rate': '-4%',
 'native_rate': '-10%',
 'english_pitch': '+0Hz',
 'native_pitch': '+0Hz',
 'native_label': 'ITALIANO',
 'translit_label': 'SAY IT LIKE',
 'flag': 'it',
 'greeting': 'Ciao!',
 'encouragement': 'Fantastico!',
 'rtl': False,
 'char_tiles': False,
 'script_font': '',
 'glyphs': 'ABCDEFGHIJKLMNOPQRSTUVWXYZÀÈÉÌÒÙàèéìòù'}
# ==== LANGUAGE PACK END ====

# ==== CATEGORIES START ====
CATEGORIES = {'Motivation': 'Motivazione',
 'Love': 'Amore',
 'Success': 'Successo',
 'Wisdom': 'Saggezza',
 'Happiness': 'Felicità',
 'Self Improvement': 'Miglioramento Personale',
 'Gratitude': 'Gratitudine',
 'Friendship': 'Amicizia',
 'Hope': 'Speranza',
 'Creativity': 'Creatività',
 'Inner Peace': 'Pace Interiore',
 'Confidence': 'Fiducia',
 'Perseverance': 'Perseveranza',
 'Inspiration': 'Ispirazione',
 'Positive Life': 'Vita Positiva',
 'Courage': 'Coraggio',
 'Kindness': 'Gentilezza',
 'Patience': 'Pazienza',
 'Forgiveness': 'Perdono',
 'Strength': 'Forza',
 'Joy': 'Gioia',
 'Balance': 'Equilibrio',
 'Growth': 'Crescita',
 'Purpose': 'Scopo',
 'Mindfulness': 'Consapevolezza',
 'Travel & Airport': 'Viaggi e Aeroporto',
 'Ordering Food & Dining': 'Ordinare Cibo e Mangiare Fuori',
 'Shopping & Prices': 'Shopping e Prezzi',
 'Asking for Directions': 'Chiedere Indicazioni',
 'Hotel & Accommodation': 'Hotel e Alloggio',
 'Daily Routine': 'Routine Quotidiana',
 'Meeting People & Greetings': 'Incontrare Persone e Saluti',
 'Emergency & Health': 'Emergenze e Salute',
 'Public Transportation': 'Trasporti Pubblici',
 'Work & Office': 'Lavoro e Ufficio',
 'Weather & Small Talk': 'Meteo e Chiacchiere',
 'Coffee Shop & Bakery': 'Caffetteria e Pasticceria',
 'Family & Home': 'Famiglia e Casa',
 'Hobbies & Free Time': 'Hobby e Tempo Libero',
 'Dating & Romance': 'Incontri e Romanticismo',
 'Phone Calls & Messages': 'Telefonate e Messaggi',
 'Banking & Money': 'Banca e Denaro',
 'Doctor & Pharmacy': 'Medico e Farmacia',
 'Sports & Fitness': 'Sport e Fitness',
 'Celebrations & Parties': 'Celebrazioni e Feste',
 'Feelings & Emotions': 'Sentimenti ed Emozioni',
 'Agreeing & Disagreeing': "Essere d'Accordo e Non Esserlo",
 'Making Plans': 'Fare Piani',
 'Common Native Slang': 'Gergo Comune',
 'Cultural Traditions': 'Tradizioni Culturali'}
# ==== CATEGORIES END ====

CATEGORY_NAMES = list(CATEGORIES.keys())

AI_MODEL = os.getenv("AI_MODEL", "openai/gpt-5.4-nano")
AI_FALLBACK_MODEL = os.getenv("AI_FALLBACK_MODEL", "gemini-fast")
POLLINATIONS_API_KEY = os.getenv("POLLINATIONS_API_KEY", "")

# ---------------------------------------------------------------- timing (seconds)

INTRO_DURATION = 7.2
CHAPTER_INTRO_DURATION = 4.4
OUTRO_DURATION = 13.0

EN_CARD_IN = 0.70
GAP_EN_NATIVE = 0.60
NATIVE_CARD_LEAD = 0.40
GAP_BEFORE_REPEAT = 1.00
TAIL_HOLD = 1.30

# ---------------------------------------------------------------- palette

INK = "#30303A"
MUTED = "#8A8A8A"
CREAM = "#FFF8E7"
GREEN = "#58CC02"
GREEN_DARK = "#46A302"
GREEN_DEEP = "#3D8F00"
BLUE = "#1CB0F6"
PURPLE = "#7C5CFF"
ORANGE = "#FF7A00"
RED = "#FF4B4B"
YELLOW = "#F5A700"
TEAL = "#00A889"
PINK = "#E056A0"

# ==== HASHTAGS START ====
HASHTAGS = ['#learnitalian',
 '#italianlessons',
 '#italianforbeginners',
 '#languagelearning',
 '#italianvocabulary',
 '#velocityitalian',
 '#dailyitalian',
 '#italian',
 '#learnlanguages',
 '#speakitalian']
# ==== HASHTAGS END ====
