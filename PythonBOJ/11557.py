testCase = int(input())

result = list()
for e in range(testCase):
    schoolCount = int(input())
    maxSchoolName = None
    maxAmount = 0
    for y in range(schoolCount):
        schoolName, amount = input().split()
        if y == 1:
            maxSchoolName = schoolName
            maxAmount = int(amount)
        else:
            if maxAmount < int(amount):
                maxSchoolName = schoolName
                maxAmount = int(amount)
            else:
                pass
    result.append(maxSchoolName)

for t in result:
    print(t)
