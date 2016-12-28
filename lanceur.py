import footParsing
import time
import voicelib
import payslib
import colorlib

start_time = time.time()
listePost = footParsing.getfeed()
date = time.strptime("Wed, 28 Dec 2016 10:44:12 GMT","%a, %d %b %Y %H:%M:%S %Z")

#voicelib.speakfr7()

print payslib.getpays(u"FRA")
print payslib.getpays(u"ESP")
print payslib.getpays(u"ITA")
print payslib.getpays(u"ENG")
print payslib.getpays(u"GER")
print payslib.getpays(u"POR")
print payslib.getpays(u"ALG")
print payslib.getpays(u"BEL")
print payslib.getpays(u"TUN")
print payslib.getpays(u"TUR")
print payslib.getpays(u"ISR")
print payslib.getpays(u"SCO")
print payslib.getpays(u"KSA")
print payslib.getpays(u"AUS")
print payslib.getpays(u"EGY")

#colorlib.liste_couleur()

while (time.time()-start_time)<48000:
    print('.')
    listePost = footParsing.getfeed()
    for post in listePost:
        timeCourant = time.strptime(post.published,"%a, %d %b %Y %H:%M:%S %Z")
        if date<timeCourant:
            footParsing.getdetail(post)
            date=timeCourant
            time.sleep(2)
        time.sleep(2)
    time.sleep(20)
print('----')