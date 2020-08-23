from collections import Counter

# print(Counter([1,2,3,1,1,1]))
ctr1 = Counter((3,1,2,3,1,1,1))

# print(ctr1)

# print(ctr1.most_common(1))
# print(ctr1.most_common(2))


ctr2 = Counter({'a':3, 'b':7, 'c':6})
# print(ctr2.most_common(1))
# print(ctr2['a'])

# print(dir(Counter))

# data = [3,2,6,4,1,5]
# print(Counter(data).most_common(1)[0][1])

data = [6,2,6,4,6,5]
print(Counter(data).most_common(1)[0])
