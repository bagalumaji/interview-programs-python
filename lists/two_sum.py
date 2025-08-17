lst1 = [2, 4, 5, 7, 3, 6, 8, 2]


def find_first_two_sum(lst: list, target: int) -> tuple | None:
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] + lst[j] == target:
                print(i, j)
                print(lst[i], lst[j])
                return i, j, lst[i], lst[j]

    return None


result = find_first_two_sum(lst1, 9)
i, j, val1, val2 = result
print(f"indices : {i}, {j} | values : {val1},{val2}")
