import footParsing
import time
import datetime

start_time = time.time()
listePost = footParsing.getfeed()
# on fixe la date du jour a minuit
date = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

while (time.time() - start_time) < 148000:
    print('.')
    listePost = footParsing.getfeed()
    for post in listePost:
        timeCourant = datetime.datetime.strptime(post.published, "%a, %d %b %Y %H:%M:%S %Z")
        if date < timeCourant:
            footParsing.getdetail(post)
            date = timeCourant
            time.sleep(0.5)
        time.sleep(0.5)
    time.sleep(30)
print('----')
