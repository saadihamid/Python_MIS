# معرفی تابع ها
# ارسال لیست به عنوان پارامترهای تابع
def fun01(cars): # آرگومان تابع (cars) از نوع لیست است
    for i in cars:
       print(i)

car_list = ['t','Benz', 'BMW', 'Pegout']
fun01(cars=car_list) # در اینجا پارامتر تابع از نوع لیست است
