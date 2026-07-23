import random

SKINS = [
    ("AK-47 | Redline", 120),
    ("AWP | Asiimov", 450),
    ("M4A1-S | Printstream", 900),
    ("Karambit | Doppler", 5000),
]

def open_case():
    return random.choice(SKINS)
