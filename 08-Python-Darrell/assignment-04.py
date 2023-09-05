num = int(input("Enter a number to convert: "))



m = ["", "M", "MM", "MMM"]
c = ["", "C", "CC", "CCC", "CD", "D",
        "DC", "DCC", "DCCC", "CM"]
x = ["", "X", "XX", "XXX", "XL", "L",
        "LX", "LXX", "LLXXX", "XC"]
i = ["", "I", "II", "III", "IV", "V",
     "VI", "VII", "VIII", "IX"]

thousands = m[num//1000]
hundreds = c[(num %1000) //1000]
tens = x[(num %100)//10]
ones = i[num %10]

ans = (thousands + hundreds + tens+ ones)

print(ans)

