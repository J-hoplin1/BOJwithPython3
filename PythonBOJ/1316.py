words = int(input())
wordCount = 0
for e in range(words):
    word = input()
    if list(word) == list(sorted(word,key = word.find)): #key 매개변수에 word.find를 하게 되면 sorted() 함수는 알파벳 순 정렬이 아닌 word라는 문자열에서 가장 처음으로 발견되는 문자부터 정렬해 나간다.
        wordCount += 1
    else:
        pass
print(wordCount)