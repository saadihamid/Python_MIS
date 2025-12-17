# برنامه ايي بنويسيد که تشخيص دهد ماتریس پايين مثلثی است یا خیر
d=  [[0,0,0,0],[7,0,0,0],[-9,4,0,0],[0,0,0,0]]

def paiinmosalasi(a):
    for i in range(0,len(a)-1):
        for j in range(i+1,len(a)):
            if a[i][j] != 0:
                print("ماتریس پايين مثلثی نیست")
                return
    print("ماتریس پايين مثلثی است")        

paiinmosalasi(d)

