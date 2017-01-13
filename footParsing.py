# coding: utf8
import feedparser
import re
import payslib
import messagelib
import liguelib
import sonlib
import weblib
import colorlib

regexFeed = '(\((.*?)[-](.*?)\))(.*)([v][s])(.*)(:)(.*?)([-])(.*?)([-])(.*)'
posts = []
url = 'http://www.scorespro.com/rss2/live-soccer.xml'
feed = feedparser.parse(url)
pays = ''
division = ''
equipe1 = ''
sco1 = ''
equipe2 = ''
sco2 = ''
information = ''


def getfeed():
    """Recuperation de l'ensemble du flux et stockage dans la liste des postes"""
    global feed
    global posts
    feed = feedparser.parse(url)
    for i in range(len(feed['entries']) - 1, -1, -1):
        posts.append(feed['entries'][i])
    return posts


def getfeedpays(pays_trigrame):
    """Recuperation de l'ensemble du flux pour un pays donnees et stockage dans la liste des postes"""
    global feed
    global posts
    posts = []
    feed = feedparser.parse(url)
    for i in range(len(feed['entries']) - 1, -1, -1):
        country, div, team1, team2, score1, score2, informa = getinfo(feed['entries'][i].summary)
        if country == pays_trigrame:
            posts.append(feed['entries'][i])
    return posts


def getdetail(info):
    """Affiche le detail du feed
    :type info: post rss
    """
    country, div, team1, team2, score1, score2, informa = getinfo(info.summary)
    print(colorlib.violet(info.id))
    print(colorlib.ecrire(colorlib.ENCRE_JAUNE_VIOLET, info.published))
    print (payslib.getpays(country))
    print("Division: " + liguelib.getdivision(div))

    if score1 == '0':
        print(colorlib.vert(team1 + ": ") + colorlib.jaune(score1))
    else:
        tmp = weblib.buteurs_home(info.id)
        chaine = colorlib.vert(team1 + ": ")
        chaine += colorlib.jaune(score1) + " -> " + ','.join(tmp)
        print(chaine)

    """si il y a des cartons on les affiche"""
    if len(weblib.jaune_home(info.id)) > 0:
        tmp = weblib.jaune_home(info.id)
        print("carton jaunes: " + ','.join(tmp))

    if len(weblib.red_home(info.id)) > 0:
        tmp = weblib.red_home(info.id)
        print("carton rouges: " + ','.join(tmp))

    if len(weblib.changement_home(info.id)) > 0:
        tmp = weblib.changement_home(info.id)
        print("remplacement: " + ','.join(tmp))

    if score2 == '0':
        print(colorlib.vert(team2 + ": ") + colorlib.jaune(score2))
    else:
        tmp = weblib.buteurs_ext(info.id)
        chaine = colorlib.vert(team2 + ": ")
        chaine += colorlib.jaune(score2) + "-> " + ','.join(tmp)
        print(chaine)

    if len(weblib.jaune_ext(info.id)) > 0:
        tmp = weblib.jaune_ext(info.id)
        print("carton jaunes: " + ','.join(tmp))

    if len(weblib.red_ext(info.id)) > 0:
        tmp = weblib.red_ext(info.id)
        print("carton rouges: " + ','.join(tmp))

    if len(weblib.changement_ext(info.id)) > 0:
        tmp = weblib.changement_ext(info.id)
        print("remplacement: " + ','.join(tmp))

    if messagelib.MSG_BUT in informa:
        sonlib.sonbut()
    print(colorlib.ecrire(colorlib.ENCRE_BLEU_VIOLET, messagelib.getmessage(informa)))
    print('')


def getinfo(info):
    """Parsing du feed post.summary"""
    match = re.search(regexFeed, info)
    country = u""
    divide = u""
    team1 = u""
    team2 = u""
    score1 = u""
    score2 = u""
    message = u""
    if match:
        country = match.group(2).strip()
        divide = match.group(3).strip()
        team1 = match.group(4).strip()
        team2 = match.group(6).strip()
        score1 = match.group(8).strip()
        score2 = match.group(10).strip()
        message = match.group(12).strip()
    return country, divide, team1, team2, score1, score2, message


if __name__ == "__main__":
    listInfo = getfeed()
    for post in listInfo:
        getdetail(post)
