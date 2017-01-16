# coding: utf8
import colorlib
XIANGQI = u"XIA"


def affiche_echiquier():
    """affiche l'echiquier"""
    result = u"G\u00e9n\u00e9ral :"
    result += colorlib.ecrire(colorlib.ENCRE_NOIRE, u"\U00005C07")
    result += colorlib.ecrire(colorlib.ENCRE_ROUGE, u"\U00005E25") + u"\n"
    result += u"Gardes :"
    result += colorlib.ecrire(colorlib.ENCRE_NOIRE, u"\U000058EB")
    result += colorlib.ecrire(colorlib.ENCRE_ROUGE, u"\U00004ED5") + u"\n"
    result += u"\u00c9l\u00e9phants :"
    result += colorlib.ecrire(colorlib.ENCRE_NOIRE, u"\U00008C61")
    result += colorlib.ecrire(colorlib.ENCRE_ROUGE, u"\U000076F8") + u"\n"
    result += u"Chevaux :"
    result += colorlib.ecrire(colorlib.ENCRE_NOIRE, u"\U000099ac")
    result += colorlib.ecrire(colorlib.ENCRE_ROUGE, u"\U0000508C") + u"\n"
    result += u"Bombardes :"
    result += colorlib.ecrire(colorlib.ENCRE_NOIRE, u"\U00007832")
    result += colorlib.ecrire(colorlib.ENCRE_ROUGE, u"\U000070AE") + u"\n"
    result += u"Chariots :"
    result += colorlib.ecrire(colorlib.ENCRE_NOIRE, u"\U00008eca")
    result += colorlib.ecrire(colorlib.ENCRE_ROUGE, u"\U00008f66") + u"\n"
    result += u"Soldats :"
    result += colorlib.ecrire(colorlib.ENCRE_NOIRE, u"\U00005352")
    result += colorlib.ecrire(colorlib.ENCRE_ROUGE, u"\U00005175") + u"\n"

    result += colorlib.ecrire(colorlib.ENCRE_NOIRE, u" \U00008eca \U000099ac \U00008C61 \U000058EB \U00005C07")
    result += colorlib.ecrire(colorlib.ENCRE_NOIRE, u" \U000058EB \U00008C61 \U000099ac \U00008eca") + u"\n"
    result += colorlib.ecrire(colorlib.ENCRE_NOIRE, u"                           \n")
    result += colorlib.ecrire(colorlib.ENCRE_NOIRE, u"    \U00007832                \U00007832   ") + u"\n"
    result += colorlib.ecrire(colorlib.ENCRE_NOIRE, u" \U00005352    \U00005352    \U00005352    \U00005352")
    result += colorlib.ecrire(colorlib.ENCRE_NOIRE, u"    \U00005352") + u"\n"
    result += colorlib.ecrire(colorlib.ENCRE_ROUGE, u" \U00005175    \U00005175    \U00005175    \U00005175")
    result += colorlib.ecrire(colorlib.ENCRE_ROUGE, u"    \U00005175") + u"\n"
    result += colorlib.ecrire(colorlib.ENCRE_ROUGE, u"    \U000070AE                \U000070AE   ") + u"\n"
    result += colorlib.ecrire(colorlib.ENCRE_ROUGE, u"                           \n")
    result += colorlib.ecrire(colorlib.ENCRE_ROUGE, u" \U00008f66 \U0000508C \U000076F8 \U00004ED5 \U00005E25")
    result += colorlib.ecrire(colorlib.ENCRE_ROUGE, u" \U00004ED5 \U000076F8 \U0000508C \U00008f66") + u"\n"
    return result


if __name__ == "__main__":
    print affiche_echiquier()
