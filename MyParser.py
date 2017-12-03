#Tugas Tahap 1

operator = ['+','-','x',':']

def parse(inputan,index,output,hitungBuka,error):
    if error :
        return output

    if index is len(inputan):
        #if hitungBuka > 0:
        #   output += "error "
        return output

    count = index

    if inputan[count] is " ":
        index = index + 1
        return parse(inputan, index, output, hitungBuka,error)

    counter = 1

    while (count+1) is not len(inputan) and inputan[count+1] is not " " :
        counter = counter + 1
        count = count + 1


    if (counter > 1) :
        isNum = False
        before = 'none'
        count = count + 1
        for i in range(index,count):
            if before is 'none':
                if inputan[i].isdigit() :
                    before = 'num'
                    isNum = True
                elif inputan[i] is '+' or inputan[i] is '-':
                    before = 'plusmin'
                    isNum = False
                else:
                    isNum = False
                    break
            elif before is 'num' :
                if inputan[i].isdigit() :
                    before = 'num'
                    isNum = True
                elif inputan[i] is ',' :
                    before = 'com'
                    isNum = False
                elif inputan[i] is 'E' :
                    before = 'E'
                    isNum = False
                else:
                    isNum = False
                    break
            elif before is 'plusmin' :
                if inputan[i].isdigit() :
                    before = 'num'
                    isNum = True
                else:
                    isNum = False
                    break
            elif before is 'E':
                if inputan[i].isdigit() :
                    before = 'num'
                    isNum = True
                elif inputan[i] is '+' or inputan[i] is '-':
                    before = 'plusmin'
                    isNum = False
                else:
                    isNum = False
                    break
            elif before is 'com':
                if inputan[i].isdigit():
                    before = 'num'
                    isNum = True
                else:
                    isNum = False
                    break
            else:
                isNum = False
                break
        if isNum :
            output += 'num '
        else:
            output += 'error '
            error = True
        index = count
    else :
        if(inputan[count] in operator):
            output += 'opr '
        elif(inputan[count] is '('):
            output += 'kurbuka '
            hitungBuka = hitungBuka + 1
        elif(inputan[count] is ')'):
            output += 'kurtutup '
            hitungBuka = hitungBuka - 1
        elif(inputan[count].isdigit()):
            output += 'num '
        else:
            output += 'error '
            error = True
        index = index + 1


    return parse(inputan,index,output,hitungBuka,error)

def doParse(inputan):
    return parse(inputan,0,"",0,False)