"""
Napisz kod kt�ry sprawdzi zbalansowanie nawias�w, tzn. czy ilo�� otwieranych nawias�w jest r�wna ilo�ci nawias�w
zamykanych. Zw�r� uwag�, �e mog� by� cztery typy nawias�w:
- okr�g�e: ( i )
- kwadratowe: [ i ]
- klamrowe { i }
- tr�jk�tne < i >
"""

NAWIASY_OTWIERAJACE = ('(', '{', '[', '<')
NAWIASY_ZAMYKAJACE = (')', '}', ']', '>')
PARA = dict(zip(NAWIASY_OTWIERAJACE, NAWIASY_ZAMYKAJACE))


def _czy_pasujace(otwarte, nawias_zamykajacy):
    if otwarte:
        nawias_otwierajacy = otwarte.pop()
        return PARA[nawias_otwierajacy] == nawias_zamykajacy
    else:
        return False


def zbalansowanie_nawiasow(ciag):
    """
    >>> zbalansowanie_nawiasow('{}')
    True
    >>> zbalansowanie_nawiasow('()')
    True
    >>> zbalansowanie_nawiasow('[]')
    True
    >>> zbalansowanie_nawiasow('<>')
    True
    >>> zbalansowanie_nawiasow('')
    True
    >>> zbalansowanie_nawiasow('(')
    False
    >>> zbalansowanie_nawiasow('}')
    False
    >>> zbalansowanie_nawiasow('(]')
    False
    >>> zbalansowanie_nawiasow('([)')
    False
    >>> zbalansowanie_nawiasow('[()')
    False
    >>> zbalansowanie_nawiasow('{()[]}')
    True
    >>> zbalansowanie_nawiasow('() [] () ([]()[])')
    True
    >>> zbalansowanie_nawiasow("( (] ([)]")
    False
    """
    otwarte = []
    for znak in ciag:
        if znak in NAWIASY_OTWIERAJACE:
            otwarte.append(znak)
        elif znak in NAWIASY_ZAMYKAJACE:
            if not _czy_pasujace(otwarte, znak):
                return False
    return not otwarte
