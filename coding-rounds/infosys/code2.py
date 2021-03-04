x = int(input())
node_set = set()
node_dict = dict()
while True:
    raw_inp = input()
    if raw_inp == "":
        break
    i, j = [int(element) for element in raw_inp.split(" ")]
    if i not in node_set:
        node_set.add(i)
    if j not in node_set:
        node_set.add(j)
    if i not in node_dict:
        node_dict[i] = [
            j,
        ]
    else:
        node_dict[i].append(j)
    if j not in node_dict:
        node_dict[j] = [
            i,
        ]
    else:
        node_dict[j].append(i)
print(node_dict)
print(node_set)
