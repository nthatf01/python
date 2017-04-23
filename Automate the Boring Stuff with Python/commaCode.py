def listToString(listParameter):
    for i in range(len(listParameter)):
        if (i != len(listParameter) - 1):
            print(listParameter[i] + ', ', end = '')
        else:
            print('and ' + listParameter[i])
        
spam = ['apples', 'bananas', 'tofu', 'cats']
listToString(spam)
