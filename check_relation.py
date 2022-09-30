"""Дан массив связей пользователей. Вам необходимо реализовать функцию,
которая принимает на вход три аргумента: информация о связях, как кортеж (tuple)
кортежей, первое имя (str), второе имя (str). Функция должна возвращать True, если
связь между любыми двумя заданными пользователями существует, например, если у
двух пользователей есть общие друзья или у их друзей есть общие друзья и т.д., иначе
False."""

def modification(net):
    vertices = set()
    for item in net:
        vertices.add(item[0])
        vertices.add(item[1])
    graph = dict()
    vertices = frozenset(vertices)
    for vertex in vertices:
        graph[vertex] = []
    for element in net:
        v1 = element[0]
        v2 = element[1]
        graph[v1].append(v2)
        graph[v2].append(v1)
    return graph

def check_relation(net, first, second, new_set=None):
    if not new_set:
        new_set = set()
    new_set.add(first)

    for element in set(net[first]) - new_set:
        check_relation(net, element, second, new_set)

    if second in new_set:
        return True

    return False

if __name__ == '__main__':
    net = (
    ("Ваня", "Лёша"), ("Лёша", "Катя"),
    ("Ваня", "Катя"), ("Вова", "Катя"),
    ("Лёша", "Лена"), ("Оля", "Петя"),
    ("Стёпа", "Оля"), ("Оля", "Настя"),
    ("Настя", "Дима"), ("Дима", "Маша")
    )

    net = modification(net)

assert check_relation(net, "Петя", "Стёпа") is True
assert check_relation(net, "Маша", "Петя") is True
assert check_relation(net, "Ваня", "Дима") is False
assert check_relation(net, "Лёша", "Настя") is False
assert check_relation(net, "Стёпа", "Маша") is True
assert check_relation(net, "Лена", "Маша") is False
assert check_relation(net, "Вова", "Лена") is True