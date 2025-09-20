w = int(input("Your weight(kg): "))
h = int(input("Your height(cm): "))
BMI = w / (h/100)**2
if BMI <= 18.4:
    print("Underweight")
elif BMI <= 24.9:
    print("Healthy")
elif BMI <= 29.9:
    print("Overweight")
elif BMI <= 34.9:
    print("Severly Overweight")
elif BMI <= 39.9:
    print("Obese")
else:
    print("BOOM")
    