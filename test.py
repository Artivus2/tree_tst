def to_tree(source: list):  #входящий лист
    i = 0
    result = dict() #выход словарь
    node = result
    while i < len(source):
        parent = source[i][0]
        child = source[i][1]
        if parent is None:
            result.update({child: {}})
            i += 1

        else:
            node[parent].update({child: {}})
            if i != len(source) - 1 and source[i+1][0] in result:
                node = result
            elif i != len(source) - 1 and source[i+1][0] != parent:
                node = node[parent]
            i += 1

    return result


expected = {
    'a': {'a1': {}, 'a2': {'a21': {}, 'a22': {}}},
    'b': {'b1': {'b11': {'b111': {}}}, 'b2': {}},
    'c': {'c1': {}},
}

source = [
    (None, 'a'),
    (None, 'b'),
    (None, 'c'),
    ('a', 'a1'),
    ('a', 'a2'),
    ('a2', 'a21'),
    ('a2', 'a22'),
    ('b', 'b1'),
    ('b1', 'b11'),
    ('b11', 'b111'),
    ('b', 'b2'),
    ('c', 'c1'),
]

if __name__ == '__main__':
    assert to_tree(source) == expected

print(to_tree(source))