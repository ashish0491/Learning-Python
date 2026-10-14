print('Hello')

name = "Ashish"
print(name[0:4])
print(name[0:4:2])
print(name[-6:0])


std_name = "Ashish"
math_marks = int(input("Enter your math marks: "))
science_marks = int(input("Enter your science marks: "))
eng_marks = int(input("Enter your English marks: "))
computer_marks = int(input("Enter your computer marks: "))

total_marks = math_marks + science_marks + eng_marks + computer_marks
percnt = (total_marks / 400) * 100

print("Total marks: ", total_marks)
print("Percentage: ", percnt)

if(percnt >= 90):
    print("Grade A")
elif(percnt >= 80):
    print("Grade B")
elif(percnt >= 70):
    print("Grade C")
elif(percnt >= 60):
    print("Grade D")
else:
    print("fail")

if(percnt >= 60):
    print("pass")
else:
    print("fail")