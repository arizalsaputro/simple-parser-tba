"""
rule
S->E
E->E O E
E->(E)
E->num
O->opr
"""


def getToken(token, index, stack):
    if index is len(token):
        return stack
    if token[index] is " ":
        index = index + 1
        return getToken(token, index, stack)
    text = ''
    count = index
    while (count + 1) is not len(token) and token[count] is not " ":
        text = text + token[count]
        count = count + 1

    stack.append(text)

    index = count + 1
    return getToken(token, index, stack)


def check(token, index, valid):
    if index + 1 < len(token) and index + 2 < len(token):
        if token[index] == 'num' and token[index + 1] == 'opr' and token[index + 2] == 'num':
            valid = True
        elif token[index+2] == 'kurbuka':
            if token[index] == 'num' and token[index+1] == 'opr':
                valid = True
            pass
        else:
            valid = False
    elif index + 1 < len(token):
        if token[index] == 'num' and token[index + 1] == 'opr':
            valid = False
        if token[index] == 'opr' and token[index + 1] == 'opr':
            valid = False
    else:
        if token[index] == 'num' or token[index] == 'opr':
            valid = True
    return valid


def validate(token, index, kurbuka, startbuka, valid):
    if index is len(token):
        if kurbuka is not 0:
            return False
        return valid

    if token[index] == 'kurbuka':
        if kurbuka is 0:
            startbuka = index
        kurbuka = kurbuka + 1
    elif token[index] == 'kurtutup':
        kurbuka = kurbuka - 1
        if kurbuka is 0:
            valid = validate(token[startbuka + 1:index], 0, 0, 0, valid)
            if valid is False:
                return valid
    elif kurbuka == 0:
        if token[index] == 'num':
            valid = check(token, index, valid)
            if valid is False:
                return valid

    index = index + 1
    return validate(token, index, kurbuka, startbuka, valid)


def checkToken(token):
    token = getToken(token, 0, [])
    if 'error' in token:
        return "TIDAK VALID"
    else:
        if validate(token, 0, 0, 0, False):
            return "VALID"
        else:
            return "TIDAK VALID"
