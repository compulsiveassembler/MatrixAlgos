def get_matrix_from_input() -> list[list[float]]:

    entry: list[list[float]] = []

    loop_trigger: bool = True

    #TODO -> implement a less ugly loop
    while(True):
        input_string: str = input()
        
        if (input_string.upper() == "QUIT"):
            break       

        entry.append( [float(x) for x in input_string.split()] )
     
    return entry

#///Row Operations
#///


#mutates passed list
def swap_rows(matrix: list[list[float]], row_number: int): 


    return


#mutates passed list
def scale_row(matrix: list[list[float]], row: int, scalar: float):


    return


#mutates passed list
def combine_rows(matrix: list[list[float]], row_1: int, row_2: int):


    return



#TODO -> determine if this is optimal formatting for 80 char margins
def get_scaled_row(matrix: list[list[float]], row: int, scalar: float) \
                                                                -> list[float]:


    return 




#entry point for program
#TODO -> restructure to create API for other modules/programs
def program_start() -> None:
    
    #get matrix from input
    our_matrix: list[list[float]] = get_matrix_from_input()
    print(our_matrix)
    print(our_matrix[0][0])
    print(len(our_matrix[1]))

    #solve matrix

    return

program_start()

