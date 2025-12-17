# تابعی بنویسید که تعداد واحدها و نمرات دروس را گرفته معدل را نمایش دهد

def average(unit,score):
  sum =0
  unit_sum = 0
  for i in range(len(unit)):
    sum += unit[i]* score[i]
    unit_sum += unit[i]
  return sum / unit_sum

unit=[]
score=[]
for i in range(2):
  unit.append(int(input()))
  score.append(float(input()))
print(average(unit,score))

