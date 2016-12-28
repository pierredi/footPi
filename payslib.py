import colorlib
PAYS_ALGERIE=u"ALG"
PAYS_ALLEMAGNE=u"GER"
PAYS_ANGLETERRE=u"ENG"
PAYS_ARABIE=u"KSA"
PAYS_ARGENTINE=u"ARG"
PAYS_AUSTRALIE=u"AUS"
PAYS_AZERBAIDJAN=u"AZE"
PAYS_BANGLADESH=u"BGD"
PAYS_BELGIQUE=u"BEL"
PAYS_BRESIL=u"BRA"
PAYS_ECOSSE=u"SCO"
PAYS_EGYPTE=u"EGY"
PAYS_EMIRATS=u"UAE"
PAYS_ESPAGNE=u"ESP"
PAYS_FRANCE=u"FRA"
PAYS_GALLES=u"WAL"
PAYS_GRECE=u"GRE"
PAYS_HONG_KONG=u"HKG"
PAYS_IRAN=u"IRN"
PAYS_ISRAEL=u"ISR"
PAYS_ITALIE=u"ITA"
PAYS_PAYS_BAS=u"NED"
PAYS_PORTUGAL=u"POR"
PAYS_QATAR=u"QAT"
PAYS_SENEGAL=u"sen"
PAYS_SURINAME=u"SUR"
PAYS_TAHITI=u"TAH"
PAYS_TRINITE_TOBAGO=u"TTO"
PAYS_TUNISIE=u"TUN"
PAYS_TURQUIE=u"TUR"
MATCH_AMICAL=u"FG"

def getpays(code):
    """Retourne le pays correspondant au code Pays"""
    result = code
    if PAYS_ESPAGNE in code:
        result = colorlib.ecrire(colorlib.ENCRE_ROUGE,u"Es")+colorlib.ecrire(colorlib.ENCRE_JAUNE,u"pa")+colorlib.ecrire(colorlib.ENCRE_ROUGE,u"gne")
    elif PAYS_ITALIE in code:
        result = colorlib.ecrire(colorlib.ENCRE_VERTE,u"It")+u"al"+colorlib.ecrire(colorlib.ENCRE_ROUGE,u"ie")
    elif PAYS_FRANCE in code:
        result = colorlib.ecrire(colorlib.ENCRE_BLEU,u"Fr")+u"an"+colorlib.ecrire(colorlib.ENCRE_ROUGE,u"ce")
    elif PAYS_ANGLETERRE in code:
        result = colorlib.ecrire(colorlib.ENCRE_ROUGE,u"Ang")+u"let"+colorlib.ecrire(colorlib.ENCRE_ROUGE,u"erre")
    elif PAYS_ALLEMAGNE in code:
        result = colorlib.ecrire(colorlib.ENCRE_NOIRE,u"All")+colorlib.ecrire(colorlib.ENCRE_ROUGE,u"ema")+colorlib.ecrire(colorlib.ENCRE_JAUNE,u"gne")
    elif PAYS_PORTUGAL in code:
        result = colorlib.ecrire(colorlib.ENCRE_VERTE,u"Por")+colorlib.ecrire(colorlib.ENCRE_ROUGE,u"tugal")
    elif PAYS_ALGERIE in code:
        result = colorlib.ecrire(colorlib.ENCRE_VERTE,u"Alg")+colorlib.ecrire(colorlib.ENCRE_ROUGE,u"\u00e9")+u"rie"
    elif PAYS_ARGENTINE in code:
        result = u"Argentine"
    elif PAYS_GRECE in code:
        result = u"Gr\u00e8ce"
    elif PAYS_EGYPTE in code:
        result = colorlib.ecrire(colorlib.ENCRE_ROUGE,u"Eg")+u"yp"+colorlib.ecrire(colorlib.ENCRE_NOIRE,u"te")
    elif PAYS_TAHITI in code:
        result = u"Tahiti"
    elif PAYS_BRESIL in code:
        result = u"Bresil"
    elif PAYS_SENEGAL in code:
        result = u"Senegal"
    elif PAYS_TRINITE_TOBAGO in code:
        result = u"Trinite et Tobago"
    elif PAYS_SURINAME in code:
        result = u"Suriname"
    elif PAYS_BANGLADESH in code:
        result = u"Bangladesh"
    elif PAYS_TUNISIE in code:
        result = colorlib.ecrire(colorlib.ENCRE_ROUGE,u"Tun")+u"i"+colorlib.ecrire(colorlib.ENCRE_ROUGE,u"sie")
    elif PAYS_ISRAEL in code:
        result = colorlib.ecrire(colorlib.ENCRE_BLEU,u"Is")+u"r"+colorlib.ecrire(colorlib.ENCRE_BLEU,u"\u2721")+u" \u00eb"+colorlib.ecrire(colorlib.ENCRE_BLEU,u"l")
    elif PAYS_TURQUIE in code:
        result = colorlib.ecrire(colorlib.ENCRE_ROUGE,u"Tur")+u"q"+colorlib.ecrire(colorlib.ENCRE_ROUGE,u"uie")
    elif PAYS_PAYS_BAS in code:
        result = u"Pays Bas"
    elif PAYS_IRAN in code:
        result = u"Iran"
    elif PAYS_HONG_KONG in code:
        result = u"Hong Kong"
    elif PAYS_ECOSSE in code:
        result = colorlib.ecrire(colorlib.ENCRE_BLEU,u"\u00c9")+u"c"+colorlib.ecrire(colorlib.ENCRE_BLEU,u"os")+u"s"+colorlib.ecrire(colorlib.ENCRE_BLEU,u"e")
    elif PAYS_GALLES in code:
        result = u"Pays de Galles"
    elif PAYS_AZERBAIDJAN in code:
        result = u"Azerba\u00efdjan"
    elif PAYS_QATAR in code:
        result = u"Qatar"
    elif PAYS_BELGIQUE in code:
        result = colorlib.ecrire(colorlib.ENCRE_NOIRE,u"Be")+colorlib.ecrire(colorlib.ENCRE_JAUNE,u"lgi")+colorlib.ecrire(colorlib.ENCRE_ROUGE,u"que")
    elif PAYS_AUSTRALIE in code:
        result = colorlib.ecrire(colorlib.ENCRE_BLEU,u"A")+u"u"+colorlib.ecrire(colorlib.ENCRE_ROUGE,u"s")+colorlib.ecrire(colorlib.ENCRE_BLEU,u"tralie")
    elif PAYS_ARABIE in code:
        result = colorlib.ecrire(colorlib.ENCRE_BLANC_VERT,u"Arabie Saoudite")
    elif PAYS_EMIRATS in code:
        result = u"Emirats Arabes Unis"
    elif MATCH_AMICAL in code:
        result = u"Match Amical"
    return result
