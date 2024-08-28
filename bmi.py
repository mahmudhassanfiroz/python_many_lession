
#Problem 6: BMI Calculator

weight = int(input())
feet = int(input())
inches = int(input())
height = feet * 0.3048 + inches * 0.0254
# height = float(input())
bmi = weight / (height ** 2)
# print(bmi)
if bmi < 18.5:
    print(bmi,"Underweight")
elif bmi >= 18.5:
    print(bmi,"Normal")
elif bmi >= 25:
    print(bmi,"Overweight")
elif bmi >= 30:
    print(bmi,"Obese")
else:
    print("Invalid BMI")

