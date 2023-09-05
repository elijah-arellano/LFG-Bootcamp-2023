
no = int(input("Enter the number : "))

if no % 2 == 0:
    print("calculation done and the result is")
    print(f"{no} is an even number")
elif no % 3 == 0:
    print("another calculation done and the result is")
    print(f"{no} is divisible by 3")
else:
    print("final calculation done")
    print(f"{no} is not divisible by 2 or 3")

""" 
if [1]:
    print("true")
else:
    print("false") 
"""