import unittest


def find_multiples(l, index):
    current_divider = l[index]
    return [item for item in l[index + 1:] if item % current_divider == 0]


def find_dividers(l, index):
    current_dividend = l[index]
    return [item for item in l[:index] if current_dividend % item == 0]


def solution(l):
    list_size = len(l)
    count = 0
    while list_size >= 2:
        list_size -= 1
        count += len(find_dividers(l, list_size)) * len(find_multiples(l, list_size))

    return count
