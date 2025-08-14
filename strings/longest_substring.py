def longest_substring(val) -> int:
    s = set()
    left = 0
    cnt = 0
    for right in range(0, len(val)):
        while val[right] in s:
            s.remove(val[left])
            left += 1

        s.add(val[right])
        cnt = max(cnt, len(s))

    return cnt


if __name__ == "__main__":
    print(longest_substring("abcabcd"))
