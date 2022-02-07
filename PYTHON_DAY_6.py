
def div(a,b):
    print(a//b)


def mod_div(fun): 
    def inner(a,b):
        if a<b:
            a,b=b,a
        fun(a,b)
    return inner
a,b=(int(i) for i in input('Enter Two numbers: ').split())
div=mod_div(div)
div(a,b) 