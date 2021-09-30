# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 18:43:31 2021
@author: Andriy Kuzmych

"""

class a:
   def __init__(self, index, size):
        self.index = index
        self.size = size

list_memory = [] #list of elements(objects)

current_list_size = 0 #counter of total_size
          

def allocate(size): #push element to the list_memory
    global current_list_size
    real_size = size - 1 #decrease amount of 'x' because of dividing line '|'
    
    #finds place where to insert
    for i in range(len(list_memory)):
        if (i != 0) and\
            (list_memory[i].index - (list_memory[i-1].index + list_memory[i-1].size) >= real_size) and\
            (current_list_size + real_size <= total_size):
                
            list_memory.insert(i, a(list_memory[i-1].index + list_memory[i-1].size, size))
            current_list_size += size
            return list_memory[i-1].index + list_memory[i-1].index
        
        elif i == 0 and list_memory[i].index != 0:
            list_memory.insert(0, a(0, size))
            return 0
        
    #push element in the beginning
        
    if len(list_memory) == 0 and real_size < total_size and current_list_size + real_size <= total_size:
        list_memory.append(a(0, size))
        current_list_size += size
        return 0
    
    #push element in the end
    elif total_size - (list_memory[-1].index + list_memory[-1].size) >= real_size and current_list_size + real_size <= total_size:
        list_memory.append(a(list_memory[-1].index + list_memory[-1].size, size))
        current_list_size += size
        return list_memory[-1].index
    
    #report about error on other case
    else:
        return "No more free space"


def free(index): #delete element from list_memory
    global current_list_size
    
    #finds element to delete from list_memory
    for i in range(len(list_memory)):
        if index == list_memory[i].index:
            current_list_size -= list_memory[i].size #increase free memory
            del list_memory[i]
            return
    #report about error on other case
    print("Wrong index")


def print_memory(): #prints elements to the console
    out_string = "" #string that would be printed in the end of function execution
    k = 1 #count raw width
    l = 0 #count amount of raws
    local_size = 0 #identify size of index
    isFull = False #check if spaces were printed
    
    if len(list_memory) > 0:
        out_string += "|"
        
        i = 0
        while i < len(list_memory):
            
            #check wheather the difference between current and previous elements equals to zero
            #if yes then print elements
            if (i == 0 and list_memory[i].index == 0) or\
            (i != 0 and (list_memory[i].index - (list_memory[i-1].index + list_memory[i-1].size) == 0)) or\
            (list_memory[i].index - (list_memory[i-1].index + list_memory[i-1].size) > 0 and isFull) or\
                (i == 0 and isFull):
                
                #check size of index
                if list_memory[i].index < 10 and k + 1 <= total_width*2:
                    out_string += str(list_memory[i].index)
                    k += 1
                    local_size = 1
                elif list_memory[i].index >= 10 and k + 2 <= total_width*2:
                    out_string += str(list_memory[i].index)
                    k += 2
                    local_size = 2
                elif k == total_width*2:
                    out_string += "|\n|"
                    #???????
                    k = 1
                    l += 1
                else:
                    return "Error"
                
                #printing 'x'
                for j in range(list_memory[i].size*2 - local_size - 1):
                    if k + 1 <= total_width*2:
                        out_string += "x"
                        k += 1
                    elif k == total_width*2:
                        out_string += "|\n|"
                        k = 1
                        l += 1
                    else:
                        return "Error"
                    
                #print dividing line
                if k < total_width*2:
                    out_string += "|"
                    k += 1
                else:
                    out_string += "|\n|"
                    k = 1
                    l += 1
                isFull = False
                
            #if no then print spaces '-'
            elif (i == 0 and list_memory[i].index != 0) or\
                (i != 0 and (list_memory[i].index - (list_memory[i-1].index + list_memory[i-1].size)) > 0):
                if i == 0: #if it is the first element with some free space before
                    free_elem_index = 0
                else:
                    free_elem_index = list_memory[i-1].index + list_memory[i-1].size
                
                #local variable for comfortability
                size_difference = list_memory[i].index - free_elem_index
                real_size_difference = size_difference*2 - 1
                
                #printing spaces '-'
                for j in range(real_size_difference):
                    if k + 1 <= total_width*2:
                        out_string += "-"
                        k += 1
                    elif k == total_width*2:
                        out_string += "|\n|"
                        k = 1
                        l += 1
                    else:
                        return "Error"
                
                #print dividing line
                if k < total_width*2:
                    out_string += "|"
                    k += 1
                else:
                    out_string += "|\n|"
                    k = 1
                    l += 1
                    
                isFull = True #set True because spaces were printed
                
            #on other case it causes an error
            else:
                return "No such element"
            
            #iterate until spaces would be printed
            if isFull:
                i += 0
            else:
                i += 1
                
        #printing spaces after printing elements
        while l < int(total_size / total_width):
            
            while k < total_width*2:
                out_string += "-"
                k += 1
            if k == total_width*2:
                if l+1 < int(total_size / total_width):
                    out_string += "|\n|"
                    k = 1
                else:
                    out_string += "|"
            l += 1
            
    #if list_memory is empty     
    else:
        for i in range(int(total_size/total_width)):
            out_string += "|"
            for j in range(total_width*2-1):
                out_string += " "
            out_string += "|\n"
    
    print(out_string) #printing out_string
    
    
def defineAction(userString): #gives user opportunity to do some actions
    if(userString == "print"):
        print_memory()
    elif userString == "help":
        print("Available commands:\n\
        help  - show this help\n\
        exit  - exit this program\n\
        print  - print memory blocks map\n\
        allocate <num>  - allocate <num> cells. Returns block first cell number\n\
        free <num>  - free block with first cell number <num>")
    else:   
        action = ''
        for letter in userString:
            if letter == ' ':
                break
            else:
                action += letter
       
        #userNumber = int(userString[-1])
        userNumber = int(userString.split(" ")[1])
        if action == "allocate":
            print(allocate(userNumber))
        if action == "free":
            free(userNumber)
    
#main program
print("Please set memory size:")
total_size = int(input())

print("Please set width of output:")
total_width = int(input())

while True:
    
    userString = input()
    
    if(userString == "exit"):
        break
    else:
        defineAction(userString)
