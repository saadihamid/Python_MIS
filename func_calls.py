# دو تابع بنويسيد که تابع دوم تابع اول را فراخوانی کند
def f1(x=2):
    return 2*x

def f2():
    y=4
    return f1(y)

print (f2())

