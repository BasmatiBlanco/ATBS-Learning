def vowel_count(word):
    dic_vow = {"a":0, "e":0, "i":0, "o":0, "u":0, "y":0}
    for i in word:
        if i in dic_vow:
            dic_vow[i] += 1
    print(dic_vow)

vowel_count("armageddon")