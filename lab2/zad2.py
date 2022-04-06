newfile = []
f = open('zadanie2.csv')
for line in f:
    x = line.split(',', 1)
    if '\n' in x:
        continue
    else:
        newfile.append(line)
f.close()

list = []
i = 0
for line in newfile:
    if i == 0:
        i += 1
        continue
    t = line.split(',')
    d = {'key':int(t[0]), 'val':t[1]}
    list.append(d)
list = sorted(list, key = lambda d: d['key'])
deleted = []

for line in list:
    line['key'] = i
    line['val'] = line['val'].lower()
    a = line['val'].split()
    for l in range(len(a)):
        if len(a[l]) == 1:
            continue
        if ord(a[l][0]) == ord(a[l][1]) + 1 or ord(a[l][0]) == ord(a[l][1]) - 1:
            line['val'].strip(a[l])
            temp = str(line['key']) + ': ' + a[l]
            deleted.append(temp)
        i += 1
print(newfile)
print('------------------------')
print(deleted)