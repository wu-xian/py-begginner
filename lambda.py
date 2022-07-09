#
aa = [{'q': 1}, {'q': 2}, {'q': 3}]
cc = [a['q'] for a in aa if a['q'] >= 2]
print(cc)
print(aa)

for a in aa:
    print(a['q'])

print("=====")

# select


def f1(d): return d["val"]


d1 = [{'val': 1, 'haha': 22}, {'val': 33}, {'val': 999}]
dd1 = [f1(d) for d in d1]
print(dd1)

# where


def f2(d): return (d["val"] > 20)


d2 = [{'val': 1, 'haha': 22}, {'val': 33}, {'val': 999}]
dd2 = [d for d in d2 if f2(d)]
print(dd2)


# select many
d3 = [{'val': 1, 'haha': 22}, {'val': 33}, {'val': 999}]
dd3 = [{'a': d['val']} for d in d3]
print(dd3)

# select dict
d4 = {"val": 123, "haha": "jojo", "pupu": "jaja"}
dd4 = {v: k for (k,v) in d4.items()}
print(dd4)
