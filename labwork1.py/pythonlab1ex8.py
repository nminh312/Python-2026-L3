def extract_even(l):
    l = [1, 4, 5, -1, 10]
    result = []
    for i in l:
        if i%2 ==0:
            result.append(i)
    return result
print(extract_even)

