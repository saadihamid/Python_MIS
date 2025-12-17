# ميانگین عناصر روی قطر اصلی را بدست آورید
a = [[2,7,-3,0],[21,4,15,-6],[9,-17,0,2],[8,15,0,3]]

def average(a):
    sum=0
    for i in range(len(a)):
        sum += a[i][i]
    print(sum/len(a))    

average(a)
