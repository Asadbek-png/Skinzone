import random

def open_case():
    skins = [
        ("AK-47 | Redline", 100),
        ("AWP | Asiimov", 500),
        ("M4A1-S | Printstream", 1000),
        ("Karambit | Doppler", 5000)
    ]
    return random.choice(skins)
