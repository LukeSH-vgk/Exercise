import matplotlib.pyplot as plt

fhand = open("StudentExercise.csv") #Luke Harnden and Lucas Hornbaker
next(fhand)
hours = []
for line in fhand:
    nums= line.split(",")
    exercise=nums[0]
    hours.append(exercise)
hours.sort()
hours = hours[1:]
for i in range(len(hours)):
    hours[i] = float(hours[i])
print = (hours)
plt.hist(hours,bins=14)

plt.ylabel("counts")
plt.title("frequency of exercise hours in a weeks")

plt.show()
