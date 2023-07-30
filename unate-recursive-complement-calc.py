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


def main ():
    print('----------------***************************************----------------')
    print('Welcome to my mini project on Unate Recursive Paragidm (URP)')
    print('Treat it as a black box, it gives a complement of a Boolean Expression')
    print("Please have fun, I've tried to make the code very readable")
    print('----------------****************************************---------------')
    
    file_path = input('Enter input file path: ')
    input_file = open(file_path, 'r')
    
    num_of_vars, num_of_cubes, func = File_To_List_Converter(input_file)
    

main()