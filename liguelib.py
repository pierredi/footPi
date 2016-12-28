DIV_LIGUE_1=u"L1"
DIV_LIGUE_2=u"L2"
MSG_MI_TEMPS=u"Ligue 2"

def getdivision(code):
    """Retourne la division correspondant au code"""
    result = code
    if DIV_LIGUE_1 in code:
        result = u"Ligue 1"
    elif DIV_LIGUE_2 in code:
        result = u"Ligue 2"
    return result