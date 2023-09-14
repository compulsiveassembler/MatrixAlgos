#ENTRY POINT

#TODO -> restructure to create API for other modules/programs
def main() -> None:

    our_matrix: list[list[float]] = get_matrix_from_input()
    print(our_matrix)
 
    solve_matrix(our_matrix)

 
    print(our_matrix)

    return

################################################################################
def get_matrix_from_input() -> list[list[float]]:

    entry: list[list[float]] = []

    #TODO -> implement a less ugly loop
    while(True):
        input_string: str = input()
        
        if (input_string.upper() == "QUIT"):
            break       
        else:
            entry.append( [float(x) for x in input_string.split()] ) 
            
    return entry

def solve_matrix(matrix: list[list[float]]) -> list[list[float]]:

    row_length: int     = len(matrix[0])
    number_of_rows: int = len(matrix)

    pivot_row: int    = 0
    pivot_column: int = 0

    target_row: int   = pivot_row + 1

    while(True):

        print(matrix)

        if (pivot_row == number_of_rows or pivot_column == row_length):
            break

        if (matrix[pivot_row][pivot_column] == 0):
            
            for x in range(pivot_row, number_of_rows):
                if matrix[x][pivot_column] != 0:
                    swap_rows(matrix, pivot_row, x)
            continue
        else:
            
            if (target_row != number_of_rows):
                scalar: float = (1\
                                /matrix[pivot_row][pivot_column])\
                                *-matrix[target_row][pivot_column]
                print(scalar)

                combine_rows(matrix, pivot_row, target_row, scalar)
                target_row = target_row + 1
            else:
#                pivot_row = pivot_row + 1
                pivot_column = pivot_column + 1
                target_row = target_row + 1
                continue



    return

def swap_rows(
    matrix: list[list[float]], 
    first_row_number: int,
    second_row_number: int
): 

    row_length: int     = len(matrix[0])
    number_of_rows: int = len(matrix)

    first_row: list[float] = matrix[first_row_number]

    matrix[first_row_number]  = matrix[second_row_number]
    matrix[second_row_number] = first_row

    return 


def scale_row(
    matrix: list[list[float]], 
    row: int, 
    scalar: float,
)-> list[list[float]]:

    return [x*scalar for x in matrix[row]]

def combine_rows(
    matrix: list[list[float]], 
    row_1: int, 
    row_2: int, 
    scalar: float
):

    row_length: int     = len(matrix[0])
    number_of_rows: int = len(matrix)

    scaled_row = scale_row(matrix, row_1, scalar)

    print(f"scaled row is {scaled_row}")
 
    for x in range(0, row_length):
        matrix[row_2][x] = matrix[row_2][x] + scaled_row[x]

    return

################################################################################
main()

if __name__ == '__main__':
    main()
