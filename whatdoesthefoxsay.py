for t in range(int(input())):
    s = input().split()

    fox_string = []

    all_sounds = []
    i = input()

    while i != "what does the fox say?":
        all_sounds.append(i.split()[-1])
        i = input()

    for word in s:
        if not word in all_sounds:
            fox_string.append(word)
    print(" ".join(fox_string))