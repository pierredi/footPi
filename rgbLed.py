import pigpio
import time

PIN_RED =  17
PIN_GREEN = 22
PIN_BLUE = 24

COULEUR_ROUGE = [255,0,0]
COULEUR_ORANGE = [200,64,0]
COULEUR_JAUNE = [200,128,0]
COULEUR_VERT = [0,255,0]
COULEUR_BLEU_VERT = [0,128,128]
COULEUR_BLEU = [0,0,255]
COULEUR_VIOLET = [255,0,255]
COULEUR_BLANC = [255,255,255]

pi = pigpio.pi()

def led_couleur(couleur):
    pi.set_PWM_dutycycle(PIN_RED,couleur[0])
    pi.set_PWM_dutycycle(PIN_GREEN,couleur[1])
    pi.set_PWM_dutycycle(PIN_BLUE,couleur[2])

def led_off():
    pi.set_PWM_dutycycle(PIN_RED,0)
    pi.set_PWM_dutycycle(PIN_GREEN,0)
    pi.set_PWM_dutycycle(PIN_BLUE,0)

def led_clignotante(couleur):
    for cpt in range(10):
        led_couleur(couleur)
        time.sleep(0.2)
        led_off()
        time.sleep(0.2)
    led_off()

def led_nantes():
    for cpt in range(10):
        led_couleur(COULEUR_JAUNE)
        time.sleep(0.2)
        led_couleur(COULEUR_VERT)
        time.sleep(0.2)
    led_off()

def led_paris():
    for cpt in range(10):
        led_couleur(COULEUR_BLEU)
        time.sleep(0.2)
        led_couleur(COULEUR_ROUGE)
        time.sleep(0.2)
    led_off()

def led_france():
    for cpt in range(10):
        led_couleur(COULEUR_BLEU)
        time.sleep(0.2)
        led_couleur(COULEUR_BLANC)
        time.sleep(0.2)
        led_couleur(COULEUR_ROUGE)
        time.sleep(0.2)
    led_off()


def led_espagne():
    for cpt in range(10):
        led_couleur(COULEUR_JAUNE)
        time.sleep(0.2)
        led_couleur(COULEUR_ROUGE)
        time.sleep(0.2)
    led_off()

def led_italie():
    for cpt in range(10):
        led_couleur(COULEUR_VERT)
        time.sleep(0.2)
        led_couleur(COULEUR_BLANC)
        time.sleep(0.2)
        led_couleur(COULEUR_ROUGE)
        time.sleep(0.2)
    led_off()

def led_pays(infopays):
    if 'ESP' in infopays:
        led_espagne()
    elif 'ITA' in infopays:
        led_italie()
    elif 'FRA' in infopays:
        led_france()


if __name__ == "__main__":
    led_nantes()
    led_paris()
    led_italie()
    led_espagne()
    led_france()

