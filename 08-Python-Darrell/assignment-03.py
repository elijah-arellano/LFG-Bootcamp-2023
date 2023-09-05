def calculate_resistorVal(colors):
    colorVals = {
        "Black": 0,
        "Brown": 1,
        "Red": 2,
        "Orange": 3,
        "Yellow": 4,
        "Green": 5,
        "Blue": 6,
        "Violet": 7,
        "Grey": 8,
        "White": 9
    }

    value = 0

    for color in colors[:2]:
        value = value * 10 + colorVals.get(color, 0)

    return value

input_colors = input("Enter the band colors: ")

resistor_val = calculate_resistorVal(input_colors)

print(f"Resistor value is: {resistor_val:02}")

######################

fruits = ("apple", "grape", "orange")

for fruit in fruits:
    print(fruit)