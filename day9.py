# BMI calculator
name = input("Enter your name : ")
weight = int(input("Enter your weight (lb) : ")) * 0.45
height = int(input("Enter your height (cm): ")) * 0.01

bmi =round( weight / (height * height), 2)


if bmi < 18.5 :
    health = "underweight"
elif 18.5 < bmi < 24.9 :
    health = "healthy weight"
elif 25.0 < bmi < 29.9 :
    health = "over weight"
elif bmi > 30.0 :
    health = "obesity"
else:
    print("Something wrong. Please try again.")



print(f'''
      
    -------------------------------------------------
    |                                                            
    |   Your name : {name.title()}                               
    |   Your BMI value is : {bmi}                     
    |   Your weight is in the {health} category      
    |                                                
    --------------------------------------------------

''')