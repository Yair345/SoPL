def add3dicts(d1, d2, d3):
    return add2dicts(add2dicts(d1, d2), d3)


def add2dicts(d1, d2):
    return {key: tuple(set(tuple(d1[key]) + tuple(d2[key])))
            if key in d1.keys() and key in d2.keys()
            else tuple(d1[key])
                if key in d1.keys()
                else tuple(d2[key])
            for key in tuple(list(d1.keys()) + list(d2.keys()))}


def test_add2dicts():
    d1 = {1: [1, 2], 2: [3, 4]}
    d2 = {2: [5], 3: [6]}

    # איחוד דוגמה פשוטה
    result = add2dicts(d1, d2)
    assert result == {1: (1, 2), 2: (3, 4, 5), 3: (6,)}, f"Test failed: {result}"

    # מקרה שבו אין מפתחות משותפים
    d1 = {1: [1, 2]}
    d2 = {2: [3, 4]}
    result = add2dicts(d1, d2)
    assert result == {1: (1, 2), 2: (3, 4)}, f"Test failed: {result}"

    # מקרה שבו אחד המילונים ריק
    d1 = {}
    d2 = {2: [3, 4]}
    result = add2dicts(d1, d2)
    assert result == {2: (3, 4)}, f"Test failed: {result}"

    # מקרה שבו שני המילונים ריקים
    d1 = {}
    d2 = {}
    result = add2dicts(d1, d2)
    assert result == {}, f"Test failed: {result}"

    print("All add2dicts tests passed!")


def test_add3dicts():
    d1 = {1: [1, 2], 2: [3, 4]}
    d2 = {2: [5], 3: [6]}
    d3 = {1: [7], 4: [8]}

    # איחוד של שלושה מילונים
    result = add3dicts(d1, d2, d3)
    assert result == {1: (1, 2, 7), 2: (3, 4, 5), 3: (6,), 4: (8,)}, f"Test failed: {result}"

    # מקרה שבו אחד המילונים ריק
    d1 = {1: [1, 2], 2: [3, 4]}
    d2 = {}
    d3 = {2: [5], 3: [6]}
    result = add3dicts(d1, d2, d3)
    assert result == {1: (1, 2), 2: (3, 4, 5), 3: (6,)}, f"Test failed: {result}"

    # מקרה שבו כל המילונים ריקים
    d1 = {}
    d2 = {}
    d3 = {}
    result = add3dicts(d1, d2, d3)
    assert result == {}, f"Test failed: {result}"

    print("All add3dicts tests passed!")


# הרצת הבדיקות
test_add2dicts()
test_add3dicts()

