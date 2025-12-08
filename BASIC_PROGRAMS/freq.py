def char_frequency(s):
    fr = {}
    for i in s:
        if i in fr:
            fr[i] += 1
        else:
            fr[i] = 1
    return fr

s = input()
print(char_frequency(s))

        