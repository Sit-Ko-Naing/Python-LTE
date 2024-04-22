name = input("Enter your name : ")
weight = int(input("Enter your weight (lb) : ")) * 0.45      #kg
height = int(input("Enter your height (cm) :")) / 100  #meter


bmi = weight / height**2 
bmi = round(bmi,2)

if bmi < 18.5:
    print("Your weight is under weight.")
elif 18.5 < bmi < 24.9:
    print("Your weight is Healthy weight.")
elif 25.0 < bmi < 29.9:
    print("Your weight is Overweight.")
elif bmi > 30.0:
    print("Your weight is obesity.")
else:
    print("Something wrong.")

print(f"Your BMI value is {bmi}")