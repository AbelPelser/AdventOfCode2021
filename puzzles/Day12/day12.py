from collections import defaultdict

from util import *


def do_stuff(graph, paths, current_path):
    for t in graph[current_path[-1]]:
        new_path = current_path + [t]
        if t != 'end':
            if t.upper() == t or t not in current_path:
                do_stuff(graph, paths, new_path)
        else:
            paths.append(new_path[:])


def do_stuff2(graph, paths, current_path):
    for t in graph[current_path[-1]]:
        new_path = current_path + [t]
        if t != 'end':
            has_dup = False
            for r in current_path:
                if current_path.count(r) > 1 and r.lower() == r:
                    has_dup = True
            if t.upper() == t or t not in current_path or (not has_dup and t != 'start'):
                do_stuff2(graph, paths, new_path)
        else:
            paths.append(new_path[:])


def part1():
    lines = read_input_as_lines()
    graph = defaultdict(list)
    for line in lines:
        f, t = line.split('-')
        graph[f].append(t)
        graph[t].append(f)
    p = []
    do_stuff(graph, p, ['start'])
    return len(p)


def part2():
    lines = read_input_as_lines()
    graph = defaultdict(list)
    for line in lines:
        f, t = line.split('-')
        graph[f].append(t)
        graph[t].append(f)
    p = []
    do_stuff2(graph, p, ['start'])
    return len(p)


if __name__ == '__main__':
    print(part1())
    print(part2())
