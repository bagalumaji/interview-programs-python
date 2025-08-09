s = "python programming"

count_of_chars = dict()

for char in s:
    if char in count_of_chars:
        count_of_chars[char] += 1
    else:
        count_of_chars[char] = 1

print(count_of_chars)