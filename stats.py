import matplotlib.pyplot as plt

fhand = open("StudentExercise.csv") #Luke Harnden and Lucas Hornbaker
next(fhand)
hours = []
for line in fhand:
    nums= line.split(",")
    exercise=nums[0]
    if(exercise != ''):
        hours.append(exercise)
hours = hours[1:]
for i in range(len(hours)):
    hours[i] = float(hours[i])
hours.sort()
print(hours)
plt.hist(hours,bins=14)

plt.ylabel("counts")
plt.title("frequency of exercise hours in a weeks")

plt.show()

count = 0
total = 0
for hour in hours:
    total = total + hour
    count = count + 1
avg = total/count
print(avg)

count_2 = 0
for hour in hours:
    if hour >= avg:
        count_2 = count_2 + 1
prop_above = count_2/count
print(prop_above)

median = hours[len(hours)//2]
print(median)
