def sortedzip(lists):
    if not all(lists):
        return []

    min_vals = [min(l) for l in lists]
    # print(min_vals)

    return [tuple(min_vals)] + sortedzip([[x for x in l if x != min_vals[i]] for i, l in enumerate(lists)])


result = sortedzip([[3, 1, 2], [5, 6, 4], ['a', 'b', 'c']])
print(list(result))


def sortedzip_tail(lists):
    def sortedzip_tail_helper(lists, result):
        if not all(lists):
            return result

        min_vals = [min(l) for l in lists]

        return sortedzip_tail_helper([[x for x in l if x != min_vals[i]] for i, l in enumerate(lists)], result + [tuple(min_vals)])

    return sortedzip_tail_helper(lists, [])

result = sortedzip_tail([[3, 1, 2], [5, 6, 4], ['a', 'b', 'c']])
print(list(result))
