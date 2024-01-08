#rotate a matrix by 90 degrees
#this is a game, which involves going right, down, left, up.

class RotateMatrix():
    def __init__(self):
        self.matrix = [
            [0,1,2],
            [3,4,5],
            [6,7,8]
        ]
        self.matrix2 = self.matrix

    def matrix_rotator(self):
        return self.matrix


instance = RotateMatrix()



print("Matrix 1: ")
for array in instance.matrix:
    print(array)



def rotate_matrix():
    matrix_length = len(instance.matrix[0])
    x_coordinate = 0
    y_coordinate = 0
    x_min = 0
    x_max = matrix_length - 1
    #y_max =
    current_coordinate = [0,0]
    for x in range(len(instance.matrix)):
        if x == 0:
            y_coordinate = instance.matrix2[0][matrix_length - 1]

            instance.matrix2[x_coordinate][y_coordinate] = instance.matrix[x_coordinate][x]
            current_coordinate = [0,2]
            continue
        if(current_coordinate[0] == x_min):
            pass






rotate_matrix()
print("Matrix 2: ")
for array in instance.matrix2:
    print(array)