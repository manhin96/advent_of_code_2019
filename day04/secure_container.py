minLimit = 156218
maxLimit = 652527

def check_two_adjecending_numbers(number):
    numberList = list(str(number))

    for x in range(0, len(numberList)):
        try:
            if numberList[x] == numberList[x + 1]:
                #print("numbers are the same")
                return True
        except IndexError as e:
            #print("critera hasn't been met")
            return False


def check_increase_or_same(number):
    numberList = list(str(number))

    for x in range(0, len(numberList)):
        try:
            if int(numberList[x]) <= int(numberList[x + 1]):
                #print("next number is bigger or the same as the current one")
                continue
            else: 
                #print("a number is smaller then the previous number")
                return False
        except IndexError as e:
            return True



if __name__ == '__main__':
    validPasswordCounter = 0
    for item in range(minLimit, maxLimit + 1):
        if check_two_adjecending_numbers(item) and check_increase_or_same(item):
            print("checking {}".format(item))
            validPasswordCounter += 1
    print("amount of valid passwords are: {}".format(validPasswordCounter))

    # for x in range(minLimit, maxLimit + 1):
    #     print(x)

