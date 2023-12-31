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
 
    for column in range(0, row_length):
        matrix[row_2][column] = matrix[row_2][column] + scaled_row[column]

    return

################################################################################
main()

if __name__ == '__main__':
    main()
