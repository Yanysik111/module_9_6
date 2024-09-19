def all_variants(text):
    for i in range(len(text)):
        yield text[i]

    for j in range(len(text)):
        if j == (len(text) - 1):
            yield text[j - 1] + text[j]

        if j == (len(text) - 2):
            yield text[j-1] + text[j]

        if j == len(text) - 1:
            yield text


a = all_variants("abc")
for i in a:
    print(i)