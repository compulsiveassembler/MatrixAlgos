#ENTRY POINT

#TODO -> restructure to create API for other modules/programs
def main() -> None:

    our_matrix: list[list[float]] = get_matrix_from_input()
    print(our_matrix)
    print(our_matrix[0][0])
    print(len(our_matrix[1]))

    

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

    row_length: int = len(matrix[0])
    number_of_rows: int = len(matrix)

    piv



    return

def swap_rows(
    matrix: list[list[float]], 
    row_number: int,
)-> list[list[float]]: 


    return


def scale_row(
    matrix: list[list[float]], 
    row: int, 
    scalar: float,
)-> list[list[float]]:


    return

def combine_rows(
    matrix: list[list[float]], 
    row_1: int, 
    row_2: int, 
    scalar: float,
)-> list[list[float]]:

    
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
