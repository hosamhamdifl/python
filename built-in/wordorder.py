n = int(input())
words = []
word_count = 0
word_order = 0
od = {}
for _ in range(n):
    words.append(input().split())
for i in range(len(words)):
    if str(words[i]) not in od.keys():
        od[str(words[i])]=1
    else:
        od[str(words[i])]+=1
for key in od.keys():
    word_count+=1
print(word_count)
for value in od.values():
    # word_count+=int(value)
    print(value,end=' ')
