def dectobin(val):
    binnums = []
    while val != 0:
        binnums.append(str(int(val) % 2))
        val = int(val) // 2

    binnum = "".join(binnums[::-1])

    print(binnum)

def bintodec(val):
    decnum = 0

    for i in range(len(val)):
        decnum += int(val[i]) * 2 ** (len(val) - i - 1)

    print(decnum)

print("1. Decimal to Binary")
print("2. Binary to Decimal")
choice = input("Enter your choice: ")

val = input('Enter a decimal number: ' if choice == "1" else 'Enter a binary number: ')

if choice == "1":
    dectobin(val)
elif choice == "2":
    bintodec(val)
    