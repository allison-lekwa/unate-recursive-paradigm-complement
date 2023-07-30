# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 08:35:02 2023

@author: user
"""

from datetime import datetime

# Parses input File in List seperated by lines.
def File_To_List_Converter (input_file):
    file=input_file.read() # Read input file
    file=file.split("\n") # Split file
    list_inputs=[[int(i) for i in x.split(" ")  if i != ""] for x in file if x != '' ]
    num_of_vars = list_inputs.pop(0)[0]
    num_of_cubes = list_inputs.pop(0)[0]
    func = list_inputs
    print(func)
    return num_of_vars, num_of_cubes, func

# this was not stipulated, so you can leave it out
def ValidateFunc(num_of_cubes, func):
    if num_of_cubes != len(func):
        return False, 'invalid function!!! Cubelist must be equal'\
            ' to number of individual expressions'
    else:
        for i in range(0, len(func)):
            if func[i][0] != len(func[i]) - 1:
                return False, 'Invalid!!! number of dont cares do not equal '\
                        'to number of variables for' + func[i] + 'check line' + i
        return True, 'valid'
    
# handles when we have at least a dont care cube    
def Check_Cube_List_With_Dont_Cares(num_of_cubes, func):
    dont_care_flag = False # set initial state of number of dont care cube list to false
    for i in range(0, len(func)):
        if func[i][0] == 0: #check if the number of "not dont care" is zero
            return not(dont_care_flag)
    return dont_care_flag

def Complement(num_of_vars, num_of_cubes, func):
    print(len(func))
    if len(func) == 0: # function has empty cube list
        return [[ '11' for i in range(0, num_of_vars)]] # Complement zeros
    
    dont_care_flag = Check_Cube_List_With_Dont_Cares(num_of_cubes, func)
    if dont_care_flag: #function has at least a cube with dont cares
        return [[ '00' for i in range(0, num_of_vars)]] # Complement dont cares i.e '1'
    else:
        return

def Output_To_File(num_of_vars, func_complement, isValid, reason):
    now = datetime.now() # current date and time
    file=open("Output"+now,"w")
    file.write(str(num_of_vars)+"\n")
    file.write(str(len(func_complement))+"\n")
    for x in func_complement:
        y=[i for i in x if i != "11"]
        file.write(str(len(y))+" ")
        for i in range(0,len(y)):
            if y[i] == "01":
                file.write(str(i+1))
            elif y[i] == "10":
                file.write(str(-(i+1)))
            if i != len(y)-1:
                file.write(" ")
        file.write("\n")
    if not(isValid):
        file.write(str(reason))
    file.close()

def main ():
    print('----------------***************************************----------------')
    print('Welcome to my mini project on Unate Recursive Paragidm (URP)')
    print('Treat it as a black box, it gives a complement of a Boolean Expression')
    print("Please have fun, I've tried to make the code very readable")
    print('----------------****************************************---------------')
    
    file_path = input('Enter input file path: ')
    input_file = open(file_path, 'r')
    
    num_of_vars, num_of_cubes, func = File_To_List_Converter(input_file)
    isValid, reason = ValidateFunc(num_of_cubes, func)
    if isValid:
        func = Complement(num_of_vars, num_of_cubes, func)
        
    Output_To_File(num_of_vars, func, isValid, reason)
    print("--BOOLEAN FUNCTION PCN COMPLEMENT ---")
    for i in func:
        print(i)
    print(reason)
    input_file.close()

main()