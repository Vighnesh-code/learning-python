height = 1.65
weight = 84

# BMI is calculated by dividing person's weight by square of his height
bmi = weight / pow(height, 2)

print("Long Number Format: " + str(bmi))
print("Integer: " + str(int(bmi)))
print("Rounded: " + str(round(bmi)))
print("Rounded: " + str(round(bmi, 2)))

# template literals are called fstrings in python
print(f"Your BMI Index is: {str(round(bmi, 2))}")
