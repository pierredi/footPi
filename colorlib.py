ENCRE_ROUGE = [str(1), str(31), str(40)]
ENCRE_VERTE = [str(1), str(32), str(40)]
ENCRE_JAUNE = [str(1), str(33), str(40)]
ENCRE_ORANGE = [str(3), str(30), str(43)]
ENCRE_JAUNE_VIOLET = [str(1), str(33), str(45)]
ENCRE_BLEU_VIOLET = [str(1), str(36), str(45)]
ENCRE_BLEU_BLANC = [str(4), str(34), str(47)]
ENCRE_BLANC_BLEU = [str(1), str(37), str(44)]
ENCRE_BLANC_ORANGE = [str(1), str(37), str(43)]
ENCRE_VERT_BLANC = [str(5), str(32), str(47)]
ENCRE_BLANC_VERT = [str(7), str(32), str(47)]
ENCRE_BLANC = [str(1), str(37), str(40)]
ENCRE_BLEU = [str(1), str(34), str(40)]
ENCRE_VIOLET = [str(1), str(35), str(40)]
ENCRE_NOIRE = [str(7), str(37), str(40)]
ENCRE_BLANC_ROUGE_U = [str(4), str(31), str(47)]
ENCRE_ROUGE_BLANC = [str(7), str(31), str(47)]
ENCRE_NANTES = [str(1), str(33), str(42)]
ENCRE_LORIENT = [str(7), str(30), str(43)]


def liste_couleur():
    print(u"test de couleur")
    print(u"Style, Foreground, Background")
    for style in range(8):
        for fg in range(30, 38):
            s1 = ''
            for bg in range(40, 48):
                format = ';'.join([str(style), str(fg), str(bg)])
                s1 += "\x1b[%sm %s \x1b[0m" % (format, format)
            print s1
        print('\n')
    print("fin test couleur")


def ecrire(couleur, phrase):
    tableau_couleur = ';'.join(couleur)
    return "\x1b[%sm%s\x1b[0m" % (tableau_couleur, phrase)


if __name__ == "__main__":
    liste_couleur()
