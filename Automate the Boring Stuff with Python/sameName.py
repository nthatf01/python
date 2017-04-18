def spam():
    eggs = 'spam local'
    #prints 'spam local'
    print(eggs)

def bacon():
    eggs = 'bacon local'
    #prints 'bacon local'
    print(eggs)
    spam()
    #prints 'bacon local'
    print(eggs)

eggs = 'global'
bacon()
#prints 'global'
print(eggs)
