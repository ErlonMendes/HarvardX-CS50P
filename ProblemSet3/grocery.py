import operator
groc_list = dict()
while True:
    try:
        item = input().strip().upper()
        if item in groc_list:
            groc_list[item] += 1
        else:
            groc_list[item] = 1
    except (EOFError, KeyError):
        sorted_list = sorted(groc_list.items(), key=operator.itemgetter(0))
        sorted_list = dict(sorted_list)
        for item in sorted_list:
            print(sorted_list[item], item)
        break
