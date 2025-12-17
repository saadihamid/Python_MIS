# برنامه ايي بنويسيد که تشخيص دهد ماتریس صفر است یا نه
b=  [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

def sefr(a):
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i][j] != 0:
                print ("ماتریس صفر نيست")
                return
                        
    print("ماتریس صفر است")

sefr(b)

