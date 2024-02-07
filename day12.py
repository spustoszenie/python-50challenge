def count_dots(s):
    kropki = []
    for i in s:
        if i == '.':
            kropki.append(i)
    stringkropek = ''.join(map(str, kropki))
    return stringkropek

print(count_dots('h.e.l.p.'))