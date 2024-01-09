#rotate a matrix by 90 degrees
#this is a game, which involves going right, down, left, up.

#successfully rotated the outside of the matrix, now we have to delve deeper and rotate the insides
class RotateMatrix():
    def __init__(self):
        self.matrix = [
            [0,1,2],
            [4,5,6],
            [8,9,10]


        ]
        self.matrix2 = [
            [0,0,0],
            [0,0,0],
            [0,0,0],


        ]

    def matrix_rotator(self):
        return self.matrix

    def rotate_matrix(self):
        matrix_length = len(instance.matrix[0])
        matrix_width = len(instance.matrix)
        matrix_dimension = matrix_length * matrix_width
        #  print(len(instance.matrix))
        x_coordinate = 0
        y_coordinate = 0
        x_rotation = 0
        y_rotation = 0
        x_min = 0
        y_min = 0
        x_max = matrix_length - 1

        y_max = matrix_width - 1
        current_coordinate = [0, 0]
        going_right = True
        going_down = False
        going_left = False
        going_up = False
        print("X max:", x_max)

        for x in range(matrix_dimension + 15):
            try:

                if x == 0:
                    number = int(instance.matrix[y_coordinate][x_coordinate])
                    y_rotation = 0
                    x_rotation = x_max
                    instance.matrix2[y_rotation][x_rotation] = number
                    x_coordinate += 1
                    y_coordinate = 0
                    y_rotation += 1
                    continue

                if going_right:
                    if x_coordinate > x_max:
                        going_right = False
                        going_down = True
                        x_coordinate = x_max
                        y_coordinate += 1
                        y_rotation -= 1
                        x_rotation -= 1

                        continue

                    number = int(instance.matrix[y_coordinate][x_coordinate])
                    instance.matrix2[y_rotation][x_rotation] = number
                    x_coordinate += 1
                    y_rotation += 1
                    print(x_coordinate)

                if going_down:
                    if y_coordinate > y_max:
                        going_down = False
                        going_left = True
                        y_coordinate = y_max
                        x_coordinate -= 1
                        x_rotation = 0
                        y_rotation -= 1
                        continue

                    #    print(y_coordinate, x_coordinate)
                    number = int(instance.matrix[y_coordinate][x_coordinate])
                    instance.matrix2[y_rotation][x_rotation] = number
                    x_rotation -= 1
                    y_coordinate += 1

                if going_left:
                    if x_coordinate < x_min:
                        going_left = False
                        going_up = True
                        x_coordinate = x_min
                        y_coordinate -= 1

                        y_rotation = 0
                        x_rotation += 1
                        continue

                    number = int(instance.matrix[y_coordinate][x_coordinate])
                    instance.matrix2[y_rotation][x_rotation] = number
                    y_rotation -= 1
                    x_coordinate -= 1

                if going_up:
                    if y_coordinate < y_min:

                        return instance.matrix2
                    number = int(instance.matrix[y_coordinate][x_coordinate])
                    instance.matrix2[y_rotation][x_rotation] = number
                    x_rotation += 1
                    y_coordinate -= 1








            except IndexError:
                print("indexError")
                continue


instance = RotateMatrix()



print("Matrix 1: ")
for array in instance.matrix:
    print(array)












instance.rotate_matrix()
print("Matrix 2: ")
for array in instance.matrix2:
    print(array)

print("")
print("Matrix 1: ")
for array in instance.matrix:
    print(array)
