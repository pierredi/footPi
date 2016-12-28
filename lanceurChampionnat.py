import sys
import footParsing
import time
import voicelib

start_time = time.time()
listePost = footParsing.getfeed()
date = time.strptime("Mon, 19 Dec 2016 00:00:01 GMT","%a, %d %b %Y %H:%M:%S %Z")

print (sys.argv[1])
voicelib.speakfr7()

while (time.time()-start_time)<48000:
    print('.')
    listePost = footParsing.getfeedpays(sys.argv[1])
    for post in listePost:
        timeCourant = time.strptime(post.published,"%a, %d %b %Y %H:%M:%S %Z")
        if date<timeCourant:
            footParsing.getdetail(post)
            date=timeCourant
            time.sleep(2)
        time.sleep(2)
    time.sleep(20)
print('----')