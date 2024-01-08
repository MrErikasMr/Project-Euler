from rotateMatrix import RotateMatrix


instance = RotateMatrix()

matrix = instance.matrix


def test_matrix_rotator():
    assert type(instance.matrix_rotator()) is list


def test_matrix_is_matrix():
    for item in instance.matrix_rotator():
        assert type(item) is list

