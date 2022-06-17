def read(text):
    for character in text.replace('\r', '').replace('\n', ''):
        if character in data:
            data[character]['counts'] += 1
        else:
            data[character] = {'counts': 1}
    sorted_array = sorted(data, key=lambda x: data[x]['counts'], reverse=True)
    return sorted_array

def build(array):
    while len(array) != 1:
        merge_items = array.pop()
        second_item = array.pop()
        first_item_value = data[merge_items]['counts']
        second_value = data[second_item]['counts']
        merged_value = first_item_value + second_value
        felix[merge_items], felix[second_item] = data[merge_items], data[second_item]
        del data[merge_items], data[second_item]
        data[str(merge_items) + str(second_item)] = {'counts': merged_value, 'left': merge_items,'right': second_item}
        array = sorted(data, key=lambda x: data[x]['counts'], reverse=True)
        felix[list(data.keys())[0]] = list(data.values())[0]

    return array
def liczby(node, char, route):
    if 'left' in felix[node]:
        if char in felix[node]['left']:
            new_route = route + '0'
            liczby(felix[node]['left'], char, new_route)
    if 'right' in felix[node]:
        if char in felix[node]['right']:
            new_route = route + '1'
            liczby(felix[node]['right'], char, new_route)
    if 'left' not in felix[node]:
        if 'right' not in felix[node]:
            routes[char] = route


def string():
    with open('text.txt', 'r') as file:
        text = file.read().rstrip()

    return text

def dodaj(text):
    encoded_text = ""
    root_node = list(data.keys())[0]
    for char in root_node:
        liczby(root_node, char, '')

    for char in text.replace('\r', '').replace('\n', ''):
        encoded_text += routes[char]


    with open('text.bin', 'wb') as f:
        f.write(str.encode(encoded_text))
        f.close()

    with open('zerojedyn.txt', 'w') as f:
        f.write(str(routes))
        f.close()

data = {}
routes = {}
felix = {}
def main():
    text = string()
    sorted_array = read(text)
    build(sorted_array)
    dodaj(text)


main()