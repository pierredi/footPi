# coding: utf8
MSG_DEBUT = u"Kick Off"
MSG_MI_TEMPS = u"Halftime"
MSG_FIN = u"Match Finished"
MSG_REPRISE = u"2nd Half Started"
MSG_REPORTE = u"Match Postponed"
MSG_BUT = u"Goal for"


def getmessage(code):
    """Retourne le pays correspondant au code Pays"""
    result = code
    if MSG_DEBUT in code:
        result = u"coup d\u00b4envoi"
    elif MSG_MI_TEMPS in code:
        result = u"Mi-temps"
    elif MSG_FIN in code:
        result = u"Match termin\u00e9"
    elif MSG_REPORTE in code:
        result = u"Match report\u00e9"
    elif MSG_REPRISE in code:
        result = u"Reprise de la deuxi\u00e8me mi-temps"
    return result

if __name__ == "__main__":
    print getmessage(MSG_DEBUT)
    print getmessage(MSG_BUT)
    print getmessage(MSG_FIN)
    print getmessage(MSG_MI_TEMPS)
    print getmessage(MSG_REPRISE)
    print getmessage(MSG_REPORTE)
