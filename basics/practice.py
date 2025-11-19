text = "thanksgivingday"
data = {}

for index, char in enumerate(text, start=1):
    data[char] = data.get(char, 0) + 1

print(data)
