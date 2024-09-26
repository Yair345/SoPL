def sortedzip(lists):
    if not lists:
        return []
    sorted_first = sorted(lists[0])
    rest_sorted_zip = sortedzip(lists[1:])

    return zip(sorted_first, *rest_sorted_zip)


result = sortedzip([[3, 1, 2], [5, 6, 4], ['a', 'b', 'c']])
print(list(result))
