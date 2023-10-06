grades = {}

score = 0
name = ''
while (name!='-999'):
    if(name!='-999'):
       name = input("Please enter your name (or -999 to quit): ")
       score = int(input("Please enter your score: "))
       grades[name] = score
    else:
        break
print(grades.items())
