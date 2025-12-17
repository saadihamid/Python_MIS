# برنامه ايي بنويسيد که تشخيص دهد ماتریس متقارن است یا خیر
e = [[2,21,-3,8],[21,4,-17,-6],[-3,-17,0,2],[8,-6,2,3]]
def motegharen(a):
    for i in range(1,len(a)):
        for j in range(0,i):
            if a[i][j] != a[j][i]:
                print("ماتریس متقارن نیست")
                return
    print("ماتریس متقارن است")        

motegharen(e)

