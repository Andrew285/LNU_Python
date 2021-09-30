# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 18:43:31 2021

@author: User
"""

class a:
   def __init__(self, index, size):
        self.index = index
        self.size = size

list_memory = []
copy_list_memory = []
free_memory = []

total_size = 30
total_width = 10
current_list_size = 0

"""
def allocate_z(size):
    if len(list_memory) == 0 and size < total_size:
        list_memory.append(a(0, size))
        return 0
    elif list_memory[0].index <= size:
        #list_memory.insert(0, a(0, size))
        list_memory.append(a(0, size))
        return 0
    else:
        for i in range(len(list_memory)):
            if(list_memory[i+1].index - (list_memory[i].index+list_memory[i].size) >= size):
                list_memory.insert(i+1, a(list_memory[i+1].index + list_memory[i].size))
                return list_memory[i+1].index + list_memory[i].size
    if total_size - (list_memory[len(list_memory)-1].index + list_memory[len(list_memory)-1].size) <= size:
        list_memory.append(a(list_memory[len(list_memory)], size))
        return list_memory[-1].index + list_memory[-1].size
    return -1
"""
          
def allocate_z(size):
    global current_list_size
    if len(list_memory) == 0 and size < total_size and current_list_size + size <= total_size:
        list_memory.append(a(0, size))
        copy_list_memory.append(a(0, size))
        current_list_size += size
        return 0
    elif total_size - (list_memory[-1].index + list_memory[-1].size) >= size and current_list_size + size <= total_size:
        list_memory.append(a(list_memory[-1].index + list_memory[-1].size, size))
        copy_list_memory.append(a(copy_list_memory[-1].index + copy_list_memory[-1].size, size))
        current_list_size += size
        return list_memory[-1].index
    elif size > total_size or current_list_size > total_size:
        return "No more free space"
    else:
        for i in range(len(list_memory)):
            if (list_memory[i].index + list_memory[i].size) > size and current_list_size + size <= total_size:
                list_memory.insert(i, a(i, size))
                copy_list_memory.insert(i, a(i, size))
                current_list_size += size
                return i
    return "You can't add more elements"

def allocate(size):
    global current_list_size
    for i in range(len(list_memory)):
        if list_memory[i].index != 0 and list_memory[i].index - (list_memory[i-1].index + list_memory[i-1].size) >= size and current_list_size + size <= total_size:
            list_memory.insert(list_memory[i-1].index + list_memory[i-1].size, a(list_memory[i-1].index + list_memory[i-1].size, size))
            copy_list_memory.insert(copy_list_memory[i-1].index + copy_list_memory[i-1].size, a(copy_list_memory[i-1].index + list_memory[i-1].size, size))
            current_list_size += size
            return list_memory[i-1].index + list_memory[i-1].size
    if len(list_memory) == 0 and size < total_size and current_list_size + size <= total_size:
        list_memory.append(a(0, size))
        copy_list_memory.append(a(0, size))
        current_list_size += size
        return 0
    elif total_size - (list_memory[-1].index + list_memory[-1].size) >= size and current_list_size + size <= total_size:
        list_memory.append(a(list_memory[-1].index + list_memory[-1].size, size))
        copy_list_memory.append(a(copy_list_memory[-1].index + copy_list_memory[-1].size, size))
        current_list_size += size
        return list_memory[-1].index
    else:
        return "You can't add more elements"

def free(index):
    for i in range(len(list_memory)):
        if index == list_memory[i].index:
            free_memory.append(list_memory[i])
            del list_memory[i]
            return

def contains(list_mem, elem):
    for i in range(len(list_mem)):
        if elem.index == list_mem[i].index:
            return True
    return False

def print_memory():
    out_string = ""
    k = 1 #count raw width
    l = 1 #count amount of raws
    local_size = 0
   # t = 0
    if len(list_memory) > 0:
        out_string += "|"
        for i in range(len(list_memory)):
            if contains(list_memory, copy_list_memory[i]) == True:
                if copy_list_memory[i].index < 10 and k + 1 <= total_width*2:
                    out_string += str(copy_list_memory[i].index)
                    k += 1
                    local_size = 1
                elif copy_list_memory[i].index >= 10 and k + 2 <= total_width*2:
                    out_string += str(copy_list_memory[i].index)
                    k += 2
                    local_size = 2
                elif k == total_width*2:
                    out_string += "|\n|"
                    #???????
                    k = 1
                    l += 1
                else:
                    return "Error"
                #printing "x"
                
                for j in range((copy_list_memory[i].size-local_size)*2):
                    if k + 1 <= total_width*2:
                        out_string += "x"
                        k += 1
                    elif k == total_width*2:
                        out_string += "|\n|x"
                        k = 2
                        l += 1
                    else:
                        return "Error"
                    
                #????? 
                if k <= total_width*2:
                    out_string += "|"
                    k += 1
                
            elif contains(list_memory, copy_list_memory[i]) == False:
                if copy_list_memory[i].index < 10 and k + 1 <= total_width*2:
                    out_string += "-"
                    k += 1
                    local_size = 1
                elif copy_list_memory[i].index >= 10 and k + 2 <= total_width*2:
                    out_string += "--"
                    k += 2
                    local_size = 2
                elif k == total_width*2:
                    out_string += "|\n|"
                    #???????
                    k = 1
                    l += 1
                else:
                    return "Error"
                #printing "x"
                
                for j in range((copy_list_memory[i].size-local_size)*2):
                    if k + 1 <= total_width*2:
                        out_string += "-"
                        k += 1
                    elif k == total_width*2:
                        out_string += "|\n|-"
                        k = 2
                        l += 1
                    else:
                        return "Error"
                    
                #????? 
                if k <= total_width*2:
                    if i < len(copy_list_memory)-1 and contains(list_memory, copy_list_memory[i+1]) == False:
                        
                        out_string += "-"
                    else:
                        out_string += "|"
                    k += 1
                    
            else:
                return "No such element"
                
            #printing spaces
            
        while l <= int(total_size / total_width):
            
            while k < total_width*2:
                out_string += "-"
                k += 1
            if l + 1 <= int(total_size / total_width):
                if k <= total_width*2:
                    out_string += "|\n|"
                else:
                    out_string += "\n|"
            elif k == total_width*2:
                out_string += "|"
            else:
                out_string += "\n|"
            #?????
            k = 1
            l += 1
            
    else:
        for i in range(int(total_size/total_width)):
            out_string += "|"
            for j in range(total_width*2-1):
                out_string += " "
            out_string += "|\n"
    
    print(out_string)
    
#isRunProgram = True
    
def defineAction(userString):
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
    
#print("Please set memory size:")
#total_size = 30

#print("Please set width of output:")
#total_width = 10

print("Size: 30", "Width: 10")

while True:
    

    userString = input()
    
    if(userString == "exit"):
        break
    else:
        defineAction(userString)
       
        """
        print("\n")
        for i in range(len(list_memory)):
            print(list_memory[i].index, list_memory[i].size)
            print(copy_list_memory[i].index, list_memory[i].size)
            """
