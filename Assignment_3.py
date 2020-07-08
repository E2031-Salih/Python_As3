number = input("Enter a positive integer number :")
check = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", "-"]
i, j, t = 0, 0, 0
while j != 1:
    while t != 1:
        while i < len(number):
            if list(number)[i] not in check:
                print("Do not use any entries other than numeric values")
                number = input("Enter a positive integer number :")
                i = -1
            i +=1
        if float(number) > 0:
            t = 1
        else:
            print("Please enter a positive number")
            number = input("Enter a positive integer number :")
            i, t = 0, 0
    if (float(number) - (float(number) // 1)) == 0:
        j =1
    else:
        print("Please enter an integer number")
        number = input("Enter a positive integer number :")
        i, t, j = 0, 0, 0
Armstrong = 0
for i in range(len(number)):
    Armstrong += int(list(number)[i]) ** len(number)
print(f"{number} {int(number) == Armstrong and 'is' or 'is not'} an Armstrong number")
