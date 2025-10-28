import re

def isValidNumber(card_number):
    return card_number.isdigit() and len(card_number) in [13, 15, 16]


def getCheckSum(card_number):
    checkSum = 0
    for i in reversed(range(0, len(card_number) - 1, 2)):
        digit = int(card_number[i]) * 2
        if digit > 9:
            checkSum += (digit % 10) + (digit // 10)
        else:
            checkSum += digit
    for i in reversed(range(1, len(card_number), 2)):
        checkSum += int(card_number[i])
    return checkSum

def getCardType(card_number):
    if (len(card_number) == 13 or len(card_number) == 16) and card_number.startswith("4"):
        return "Visa"
    if len(card_number) == 15 and (card_number.startswith("34") or card_number.startswith("37")):
        return "American Express"
    if len(card_number) == 16 and re.match(r'5[1-5]', card_number[:2]):
        return "MasterCard"
    else:
        return "Invalid"

cardNumber = input("Введите номер банковской карты: ")
if isValidNumber(cardNumber):
    if getCheckSum(cardNumber) % 10 == 0:
        print(getCardType(cardNumber))
    else:
        print("Invalid")
else:
    print("Invalid")
