from rotateMatrix import RotateMatrix


instance = RotateMatrix()

matrix = instance.matrix


def test_matrix_rotator():
    assert type(instance.matrix_rotator()) is list


def test_matrix_is_matrix():
    for item in instance.matrix_rotator():
        assert type(item) is list




def test_3_by_3():
    result = [[8, 4, 0],
        [9, 0, 1],
        [10, 6, 2]]

    assert result == instance.rotate_matrix()


def test_4_by_4():
    pass
    result = [[12, 8, 4, 0],
        [13, 0, 0, 1],
        [14, 0, 0, 2],
        [15, 11, 7, 3]]

    assert result == instance.rotate_matrix()




