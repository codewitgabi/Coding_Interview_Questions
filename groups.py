def group(arr: list, size: int) -> list:
    output = []
    for i in range(0, len(arr), size):
        cont = []
        try:
            for j in range(i, i + size):
                cont.append(arr[j])
            output.append(cont)
        except IndexError:
            output.append(cont)
    return output


print(group([1, 2, 3, 4, 5, 6, 7, 8, 9], 4))
print(group([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
