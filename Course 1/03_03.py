#Score Grading with try except block
score = input("Enter Score: ")

try:
    scoref = float(score)
except:
    print("Error Input")
    exit()

if((scoref<0)|(scoref>1)):
    print("Out of Range")
    exit()

if((scoref>=0.9)):
    grade="A"
elif(scoref>=0.8):
    grade="B"
elif(scoref>=0.7):
    grade="C"
elif(scoref>=0.6):
    grade="D"
elif(scoref>=0.0):
    grade="F"

print(grade)