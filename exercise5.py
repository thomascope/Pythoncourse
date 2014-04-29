# Part 1 of task:

age = 75
if age >=18 and age <=60:
    print("Great, you're the perfect age!")
elif age<18:
    print("Oh dear, you're too young!")
else:
    print("Oh dear, you must be too old!")

# Part 2 of task:

trialdictionary = {'correctAnswer': 'up', 'subjectAnswer': 'left'}
if trialdictionary['correctAnswer'] == trialdictionary['subjectAnswer']:
    print("That's great!")
else:
    print("You're a dimwit")

# Part 3 of task:

for count in range(20):
    print('trial %i' %(count))
    if (count+1)%3==0:
        print('... and now a break. Cheers!')
