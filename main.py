#ENTRY POINT

#TODO -> restructure to create API for other modules/programs
def main() -> None:
    
    our_matrix: list[list[float]] = get_matrix_from_input()
    print(our_matrix)
    print(our_matrix[0][0])
    print(len(our_matrix[1]))

    print("Pick row to scale")
    chosen_row: int = int(input())
    print(f"You will be printing the following row: { our_matrix[chosen_row] }")

    print("Pick a number to scale this row by")
    scalar: float = float(input())

    print("This is the scaled row V V V")
    print( get_scaled_row(our_matrix, chosen_row, scalar) )

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

#///Row Operations
#///



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
