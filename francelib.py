import colorlib
FR_ANGERS = u"Angers"
FR_BASTIA = u"Bastia"
FR_BORDEAUX = u"Girondins Bordeaux"
FR_CAEN = u"SM Caen"
FR_DIJON = u"Dijon FCO"
FR_GUINGAMP = u"Guingamp"
FR_LILLE = u"Lille OSC"
FR_LORIENT = u"FC Lorient"
FR_LYON = u"Lyon"
FR_MARSEILLE = u"Olympique Marseille"
FR_METZ = u"metz"
FR_MONACO = u"Monaco"
FR_MONTPELLIER = u"Montpellier HSC"
FR_NANCY = u"AS Nancy"
FR_NANTES = u"Nantes"
FR_NICE = u"OGC Nice"
FR_PARIS = u"Paris Saint Germain"
FR_RENNES = u"Stade Rennais"
FR_ST_ETIENNE = u"AS Saint-Etienne"
FR_TOULOUSE = u"Toulouse FC"


def getville(code):
    """Retourne la ville correspondant au code"""
    result = code
    if FR_ANGERS in code:
        result = colorlib.ecrire(colorlib.ENCRE_NOIRE, u"A")+u"n"+colorlib.ecrire(colorlib.ENCRE_NOIRE, u"g")
        result += u"e"+colorlib.ecrire(colorlib.ENCRE_NOIRE, u"r")+u"s"
    elif FR_BASTIA in code:
        result = u"Bastia"
    elif FR_BORDEAUX in code:
        result = u"Bordeaux"
    elif FR_CAEN in code:
        result = u"Caen"
    elif FR_DIJON in code:
        result = u"Dijon"
    elif FR_GUINGAMP in code:
        result = u"Guingamp"
    elif FR_LILLE in code:
        result = u"Lille"
    elif FR_LORIENT in code:
        result = colorlib.ecrire(colorlib.ENCRE_LORIENT, u"Lorient")
    elif FR_LYON in code:
        result = u"Lyon"
    elif FR_MARSEILLE in code:
        result = u"Marseille"
    elif FR_METZ in code:
        result = u"Metz"
    elif FR_MONACO in code:
        result = u"Monaco"
    elif FR_MONTPELLIER in code:
        result = u"Montpellier"
    elif FR_NANCY in code:
        result = u"Nancy"
    elif FR_NANTES in code:
        result = colorlib.ecrire(colorlib.ENCRE_NANTES, u"Nantes")
    elif FR_NICE in code:
        result = u"Nice"
    elif FR_PARIS in code:
        result = u"Paris"
    elif FR_RENNES in code:
        result = u"Rennes"
    elif FR_ST_ETIENNE in code:
        result = u"St Etienne"
    elif FR_TOULOUSE in code:
        result = u"Toulouse"
    return result


if __name__ == "__main__":
    print getville(FR_ANGERS)
    print getville(FR_BASTIA)
    print getville(FR_BORDEAUX)
    print getville(FR_CAEN)
    print getville(FR_DIJON)
    print getville(FR_ST_ETIENNE)
    print getville(FR_GUINGAMP)
    print getville(FR_LILLE)
    print getville(FR_LORIENT)
    print getville(FR_LYON)
    print getville(FR_MARSEILLE)
    print getville(FR_METZ)
    print getville(FR_MONTPELLIER)
    print getville(FR_MONACO)
    print getville(FR_NANTES)
    print getville(FR_NANCY)
    print getville(FR_NICE)
    print getville(FR_PARIS)
    print getville(FR_RENNES)
    print getville(FR_TOULOUSE)
