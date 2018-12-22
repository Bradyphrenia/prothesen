import unittest


def test_format_winkel(text):
    text = text.strip()
    if text == 'Null' or text == '.':  # leer?
        return ''
    if text == '':
        return text
    if '.' not in text and text[0:1] not in ('+', '-'):  # nur 3 Ziffern
        text = '+' + text[0:2] + '.' + text[2:]
        return test_format_winkel(text)  # Rekursion
    if text[0:1] not in ('+', '-'):  # kein Vorzeichen
        text = '+' + text
        return test_format_winkel(text)  # Rekursion
    if text[0:1] in ('+', '-') and '.' not in text:  # Vorzeichen, kein Punkt
        text = text[0:3] + '.'
        return test_format_winkel(text)  # Rekursion
    if text[2:3] == '.':  # einstellig vor Punkt, Punkt nach hinten
        text = text[0:1] + ' ' + text[1:]
        return test_format_winkel(text)  # Rekursion
    if len(text) < 5:  # leer nach Punkt, .0
        text += '0'
    if text[1:2] == '0':  # zwei führende Nullen vor Punkt
        text = text[0:1] + ' ' + text[2:]
    if text[2:3] == ' ':  # Lehrstelle vor Punkt
        text = text[0:2] + text[3:]
        return test_format_winkel(text)  # Rekursion
    return text


assert test_format_winkel('2') == '+2.2'
