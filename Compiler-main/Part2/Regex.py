def isLogical(text):
    if ord(text[0]) == ord("&") and ord(text[1]) == ord("&") \
            or ord(text[0]) == ord("|") and ord(text[1]) == ord("|"):
        return True
    else:
        return False


def isComparison(text):
    if len(text) == 1:
        if ord(text) == ord('<') or \
            ord(text) == ord('=') or \
                ord(text) == ord('>'):
            return True
        else:
            return False
    else:
        return False


def isLetter(letter):
    if len(letter) == 1 and ((ord('a') <= ord(letter) <= ord('z')) or (ord('A') <= ord(letter) <= ord('Z'))):
        return True
    else:
        return False


def isDigit(letter):
    if len(letter) != 1 or (ord('0') > ord(letter) or ord(letter) > ord('9')):
        return False
    else:
        return True


def isID(text):
    if isLetter(text[0]):
        for i in range(1, len(text)):
            if not (isLetter(text[i]) or isDigit(text[i]) or ord(text[i]) == ord('_')):
                return False
        return True
    else:
        return False


def isPosNumber(text):
    decimal_found = False

    if len(text) == 1 and ord(text[0]) == ord('.'):
        return False

    for x in text:
        if not (isDigit(x)) and (decimal_found and ord(x) == ord('.')):
            return False
        if ord(x) == ord('.'):
            decimal_found = True
    return True


def isNumber(text):
    if len(text) == 1 and ord(text[0]) == ord('-'):
        return False

    if ord(text[0]) == ord('-'):
        text = text[1:]
    return isPosNumber(text)


def isCV(text):
    if isLogical(text) or isComparison(text):
        return False
    elif ord(text[0]) == ord('!'):
        return False
    elif isNumber(text) or isID(text):
        return True
    else:
        return False


def isLOV(text):
    if isLogical(text) or isComparison(text):
        return False
    elif ord(text[0]) == ord('!') and (isNumber(text[1:]) or isID(text[1:])):
        return True
    else:
        return False
