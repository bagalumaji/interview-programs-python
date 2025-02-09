def find_substring_in_string(s:list[str])->str:
    main_string = s[0]
    words = s[1].split(",")
    part1 = ''
    part2 = ''

    for word in words:
        l = len(word)
        if main_string.startswith(word) and len(part1) < l:
            part1 = word
        elif main_string.endswith(word) and len(part2) < l:
            part2 =  word

    return part1+","+part2

strings = ["baseball",'a,base,all,ball']
print(find_substring_in_string(strings))
