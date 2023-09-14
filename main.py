#ENTRY POINT

#TODO -> restructure to create API for other modules/programs
def main() -> None:

    our_matrix: list[list[float]] = get_matrix_from_input()
    print(our_matrix)
 
    solve_matrix(our_matrix)
    

    return

################################################################################
def get_matrix_from_input() -> list[list[float]]:

    entry: list[list[float]] = []

    #TODO -> implement a less ugly loop
    while(True):
        input_string: str = input()
        
        if (input_string.upper() == "QUIT"):
            break       

        entry.append( [float(x) for x in input_string.split()] ) 
            
    return entry

def solve_matrix(matrix: list[list[float]]) -> list[list[float]]:

    row_length: int =     len(matrix[0])
    number_of_rows: int = len(matrix)

    pivot_row: int =    0
    pivot_column: int = 0

    while(true):

        if (matrix[pivot_row][pivot_column] == 0):
            
            for x in range(pivot_row, number_of_rows):
                if matrix[x][pivot_column] != 0:
                    matrix = swap_rows(matrix, pivot_row, x)
            continue
        


    return

def swap_rows(
    matrix: list[list[float]], 
    first_row_number: int,
    second_row_number: int,
)-> list[list[float]]: 

    return


def scale_row(
    matrix: list[list[float]], 
    row: int, 
    scalar: float,
)-> list[list[float]]:

    matrix[row] = [x*scalar for x in matrix[row]]

    return

def combine_rows(
    matrix: list[list[float]], 
    row_1: int, 
    row_2: int, 
    scalar: float,
)-> list[list[float]]:

    matrix = scale_row(matrix, row_1, scalar)
 
    for x in range()

    return

#TODO -> determine if this is optimal formatting for 80 char margins
def get_scaled_row(
    matrix: list[list[float]], 
    row: int, 
    scalar: float,
)-> list[float]:
    
    return [x*scalar for x in matrix[row]]


################################################################################
main()

if __name__ == '__main__':
    main()
