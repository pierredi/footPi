from subprocess import call

def speaktext():
    call(["espeak","-s140 -ven+18 -z","Hello from Mike"])


def speakfr():
    call(["espeak","-s140 -v mb-fr1 ","salut les amis"])

def speakfr2():
    call(["espeak","-s165 -v fr ","bonjour, je suis une voix artificielle. Je m'appelle lucien"])

def speakfr3():
    call(["espeak","-s160 -v mb/mb-fr4 ","bonjour, je suis une voix artificielle. Je m'appelle lucien"])

def speakfr4():
    call(["espeak","-s150 -v mb/mb-en1 ","bonjour, je suis une voix artificielle. Je m'appelle lucien"])

def speakfr5():
    call(["espeak","-s160 -v mb/mb-fr4 ","bonjour, je suis une voix artificielle. Je m'appelle lucien"])

def speakfr6():
    call(["espeak","-s170 -v mb/mb-fr4 ","bonjour, je suis une voix artificielle. Je m'appelle lucien"])

def speakfr7():
    call(["espeak","-s160 -v /usr/lib/x86_64-linux-gnu/espeak-data/voices/mb/mb-fr4 ",u"bonjour, je suis une voix artificielle. Je m'appelle lucien"])


