firstNumber = input()
secondNumber = input()
thirdNumber = ''

for i in range(len(firstNumber)):
    if firstNumber[i] != secondNumber[i]:
        thirdNumber += '1'
    else:
        thirdNumber += '0'
print(thirdNumber)