def formatWholeNumber(num):
    if num > 999:
        divided = []

        ourNums = list(str(num))[::-1]
        while num > 999:
            divided.append(str(int(num / 1000)))
            num = int(num / 1000)
        separated = ""

        newList = list(map(lambda nums: list(nums), divided))
        onlyOnce = True

        for _ in newList[len(newList) - 1]:
            if onlyOnce:
                tempCount = len(newList[len(newList) - 1]) - 1
                while tempCount >= 0:
                    separated += newList[len(newList) - 1][::-1][tempCount]

                    tempCount -= 1
                separated += ","
                onlyOnce = False

        listCopy = [x for x in ourNums]

        for num in range(len(newList[len(newList) - 1]), 0, -1):
            ourNums.pop()
            listCopy.pop()

        listCopy = listCopy[::-1]

        ourNumsLength = len(ourNums) // 3

        generalCounter = 0

        for inGeneral in range(ourNumsLength, 0, -1):
            countTo3 = 0

            for eachDigit in range(generalCounter, len(listCopy)):
                if countTo3 != 3:
                    separated += listCopy[generalCounter]
                    generalCounter += 1
                    countTo3 += 1

            separated += ","

        return str(separated.strip(","))

    return str(num)

