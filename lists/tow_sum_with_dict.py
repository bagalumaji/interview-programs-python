def find_two_sum(arr: list, target: int) -> dict:
    res = {}
    for i in range(len(arr)):
        v = target - arr[i]
        if not v in res:
            res[arr[i]] = v

    return res


if __name__ == "__main__":
    lst1 = [2, 4, 5, 7, 3, 6, 8, 2]
    result = find_two_sum(lst1, 9)
    print(result)
