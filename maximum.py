# تابعی بنویسید که چندین عدد را گرفته ماکزیمم آنها را برگرداند
def maximum(*numbers):
    if len(numbers) == 0:
        return ("NO value")
    else:
        max = numbers[0]
        for k in numbers:
            if k>max: # اگر به جای علامت بزرگتر علامت کوچکتر قرار دهیم تابع مینیمم را بر می گرداند
                max = k
    return max
print (maximum(5,-34,89,54,0,-1,45))
