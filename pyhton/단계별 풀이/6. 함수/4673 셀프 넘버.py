def d(a:int):
    A = list(str(a))
    for i in A:
        a = a + int(i)
    return a

def createarray(n:int):
    array =[]
    for i in range(1, n + 1):
        array.append(i)
    return array

def selfnumbersundern(n):#n 이하의 셀프넘버 배열 리턴
    numbers = createarray(n)

    ds = 1
    selfnumber = 1

    while selfnumber <= n:

        ds = selfnumber

        while ds <= n:
            ds = d(ds)
            if ds in numbers:
                numbers.remove(ds)

        if numbers.index(selfnumber) == len(numbers) - 1:
            selfnumber = n + 1
            #outofrange참조 방지
        else:
            selfnumber = numbers[numbers.index(selfnumber) + 1]

    return numbers

selfnumbersunder10000 = selfnumbersundern(10000)

for i in selfnumbersunder10000:
    print(i)

##시간초과