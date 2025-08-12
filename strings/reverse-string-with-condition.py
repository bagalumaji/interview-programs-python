from reverse_string import reverse


def reverse_string_with_condition(s: str) -> None:
    words = s.split(" ")
    result = ""
    for i in range(0, len(words)):
        if i % 2 == 0:
            result += reverse(words[i]) + " "
        else:
            result += words[i][1:len(words[i]) - 1] + " "

    print(result)


if __name__ == "__main__":
    reverse_string_with_condition("sayaji bagal pandharpur")
