import footParsing
import time

start_time = time.time()
listePost = footParsing.getfeed()
date = time.strptime("Wed, 28 Dec 2016 10:44:12 GMT", "%a, %d %b %Y %H:%M:%S %Z")

while (time.time()-start_time) < 48000:
    print('.')
    listePost = footParsing.getfeed()
    for post in listePost:
        timeCourant = time.strptime(post.published, "%a, %d %b %Y %H:%M:%S %Z")
        if date < timeCourant:
            footParsing.getdetail(post)
            date = timeCourant
            time.sleep(2)
        time.sleep(2)
    time.sleep(20)
print('----')
