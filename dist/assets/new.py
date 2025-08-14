from datetime import datetime

def con(t):
    var=datetime.strptime(t,'%I:%M:%S %p')
    var1=datetime.strftime(var,'%H:%M:%S')
    print(var1)
a=(input("enter the number in 12 hour format: "))
b=con(a)
print(b)
