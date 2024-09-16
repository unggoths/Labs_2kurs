def convolution(v1, v2):
    result = [0] * (len(v1) + len(v2) - 1)
    for i in range(len(result)):
        for j in range(len(v2)):
            if 0 <= i - j < len(v1):
                result[i] += v1[i - j] * v2[len(v2) - 1 - j]
    return result


v1 = [8,1,0]
v2 = [5,6,9]

result = convolution(v1, v2)

print(v1)
print(v2)
print(result)
print("\n")

