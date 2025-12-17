# تابعی به صورت بازگشتی بنويسيد که فیبوناچی يک عدد را محاسبه کند
def fib(n):
    if n==0 or n==1:
        return n
    else:
        return fib(n-1)+fib(n-2)
    
print(fib(int(input())))    

