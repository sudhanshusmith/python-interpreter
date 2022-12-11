lines = [] # initalise to empty list
with open('F:\IITD sem-1\COL Computer science\COL Assignment\Assignment 5\input_file.txt') as f:
    lines = f.readlines() # read all lines into a list of strings
n = len(lines)   # n is length of list 'lines'
print("The Number of Line in Your Input file is",n)  # printing number of lines in my input file
print (lines)  # showing the input text file line by line
print()   # Breaking the Output



Data = [] #Intialising our data center
print("Initial Data list is",Data) # printing initial data list
print() # Breaking the Output


def search_exp(x):   # it will search that a particular data x is already stored in the data or not
    # if it is not present it will return False and index at found None
    # if it is present it will return True and index at which data is present
    # Intialisation
    i = 0 # intialisng i by 0
    Data_len = len(Data) # finding lenth of Data
    found = False # intialising found by False
    found_at_index = None  # intialising found_at_index by None
    while (i < Data_len) and not found: # Termination: i will reaches to Data_len
        if Data[i] == x:  # if Data[i] is equal to x
            found = True  # changing value of found to True
            found_at_index = i  # setting value of found_at_index to i
        else:  # if Data[i] is not equal to x
            found = False # we will not change it here
            i = i+1 # increasing value of i by 1
            found_at_index = None # we will not change it here
    return (found, found_at_index)  # return statement of above function


def search_var(x):  # it will search that a particular var x is already mapped to some data or not
    # if it is not mapped it will return False and mapped to None and plzz ignore index value
    # if it is mapped it will return True and index to which data is mapped and at what index that variable with tuple is present
    # Intialisation
    i = 0   # intialisng i by 0
    Data_len = len(Data)  # finding lenth of Data
    found = False   # intialising found by False
    mapped_to = None  # intialising mapped_to by None
    while(i < Data_len) and not found:  # Termination: i will reaches to Data_len
        if type(Data[i]) == tuple:  # Checking type of Data at index i is tuple or not?
            if Data[i][0] == x: # If it is tuple we will check variable inside tuple is x or not?
                found = True  # If we found variable is x we will set found value to True
                mapped_to = Data[i][1]  # setting value of mapped_to to 1th index of tuple
            else:  # If Data is in the form of tuple but variable x is not found inside tuple
                found = False # we will not change it here
                i = i + 1  # increasing i by 1
                mapped_to = None # we will not change it here
        else:  # if Data is not in the form of tuple
            found = False  # we will not change it here
            i = i+1  # increasing i by 1
            mapped_to = None  # we will not change it here
    return (found,mapped_to,i)  # return of the above function


def operation():  # defining the function which is a helper function of doing operation whenever required
    if search_exp(token_list[2])[0]:  # checking that given data is present inside memory or not
        # print("We checked that Data is already present")
        if search_var(token_list[0])[0]: # checking that variable is already present inside memory or not
            # print("We checked that Variable is present & already mapped to some index")
            if Data[search_var(token_list[0])[1]] == token_list[2]:  # checking that variable is mapped to right index or not?
                None # doing nothing
                # print("Variable is already mapped to right index")
            else:  # if variable is not mapped to right index
                # print("Variable is not mapped to right index & We have mapped it at right index")
                y = list(Data[search_var(token_list[0])[2]])  # converting tuple to list
                y[1] = search_exp(token_list[2])[1]  # correcting the index
                Data[search_var(token_list[0])[2]] = tuple(y)  # converting list to tuple
        else: # if variable is not present inside memory
            # print("We checked that Variable is not present & not mapped to any index, We have added this new variable & mapped it for you")
            Data.append((token_list[0], search_exp(token_list[2])[1]))  # appending the new variable inside memory with it's mapped index
    else: # if given data is not present inside memory
        # print("We checked that data is not present, We have added data for you")
        Data.append(token_list[2]) # appending data inside the memory
        if search_var(token_list[0])[0]:  # checking that variable is already present inside memory or not
            # print("We checked that Variable is present & already mapped to some index")
            if Data[search_var(token_list[0])[1]] == token_list[2]:  # checking that variable is mapped to right index or not?
                None # doing nothing
                # print("Variable is already mapped to right index")
            else:  # if variable is not mapped to right index
                # print("Variable is not mapped to right index & We have mapped it at right index")
                y = list(Data[search_var(token_list[0])[2]])  # converting tuple to list
                y[1] = search_exp(token_list[2])[1]  # correcting the index
                Data[search_var(token_list[0])[2]] = tuple(y)  # converting list to tuple

        else:  # if variable is not present inside memory
            # print("We checked that Variable is not present & not mapped to any index, We have added this new variable & mapped it for you")
            Data.append((token_list[0], search_exp(token_list[2])[1]))  # appending the new variable inside memory with it's mapped index

    return ("This Operation has been excuted Succesfully")  # return of the helper function


def check_operand1():  # defining helper function to check wether operand1 is already present inside memory or not?
    if search_exp(token_list[2])[0]:  # If operand1 is already present inside memory
        None  # doing nothing
    else: # If operand1 is not present inside memory
        # print("We have checked that 1st operand was not present in Data, Now We have added for you")
        Data.append(token_list[2])  # appending the operand1 inside memory


def check_operand2():  # defining helper function to check wether operand2 is already present inside memory or not?
    if search_exp(token_list[4])[0]: # If operand2 is already present inside memory
        None  # doing nothing
    else:  # If operand2 is not present inside memory
        # print("We have checked that 2nd operand was not present in Data, Now We have added for you")
        Data.append(token_list[4])  # appending the operand2 inside memory


for i in range (0,n): # each statement is on a separate line
    token_list = lines[i].split() # split a statement into a list of tokens
    p = len(token_list)  # p is length of token_list (i.e length of each line after splitting)
    print()  # breaking the output
    print("Reading Line number",(i+1),"......................................................")
    print ("Tokens:", token_list) # now process each statement
    # print("Total length of token_list is",p)


    #Checking for which case in Variable = Expression
    if p == 3:  # Expression is of 'Term' Type
        # print("Expression is of 'Term' Type")

        if token_list[2].isdigit():  # if data is of number type
            # print("Term is of Number Type")
            operation()  # calling helper function

        else:   # Expression may be of String Type
            if token_list[2] == 'True':   # Expression value is boolean
                # print("Term value is True")
                operation()  # calling helper function

            elif token_list[2] == 'False':   # Expression value is boolean
                # print("Term value is False")
                operation()   # calling helper function

            else:   # Expression is of String Type
                # print("Term is of purely String Type")
                if search_var(token_list[2])[0]: # Variable is defined from earlier
                    # print("Variable is defined from earlier")
                    token_list[2] = Data[search_var(token_list[2])[1]]  #accessing the value of variable
                    operation()   # calling helper function

                else:  # # Variable is not defined from earlier
                    raise ValueError("Variable", token_list[2], "is not defined")

        print("Current Updated Data list is", Data)






    elif p == 4: # Expression is of 'Unary_Operator' Type
        print("Expression is of 'Unary_Operator' Type")

        if token_list[2] == '-': # It's case of -2, -4 , -a  ......etc
            if token_list[3].isdigit():  # verifying that after minus there is integer or float only, not strings
                token_list[2] = str(-int(token_list[3]))  # converting in term type to apply that result
                operation()   # calling helper function

            else: # It means after '-' there is variable in form of strings
                if search_var(token_list[3])[0]: # Variable is defined from earlier
                    # print("Variable is defined from earlier")
                    token_list[2] = str(-int(Data[search_var(token_list[3])[1]]))   #accessing the value of variable
                    operation()   # calling helper function
                else:  # # Variable is not defined from earlier
                    raise ValueError("Variable", token_list[3], "is not defined")


        elif token_list[2] == 'not':  # If uniary operator is 'not'
            if token_list[3] == 'True':  # Its case of not True type
                token_list[2] = 'False'   # converting in term type to apply that result
                operation()   # calling helper function

            elif token_list[3] == 'False':  # It's case of not False type
                token_list[2] = 'True'  # converting in term type to apply that result
                operation()   # calling helper function

            else:  # It is the case of neither 'not True' and 'not False'
                raise ValueError("Unexpexted Input you have given, Kindly enter the valid input")


        else:  # token_list[2] is neither 'not' or '-'
            raise ValueError("Unexpexted Input you have given, Kindly enter the valid input")

        print("Current Updated Data list is", Data)






    elif p == 5:  # Expression is of 'Binary_Operator' Type
        # print("Expression is of 'Binary_Operator' Type")
        if token_list[2] == 'True':  # 1st operand value is True
            check_operand1()   # calling helper function
            if token_list[4] == 'True':  # 2nd operand value is True
                check_operand2()   # calling helper function
                token_list[2] = str(eval(token_list[2] + token_list[3] + token_list[4]))  # doing operations and converting into term type
                operation()   # calling helper function
            elif token_list[4] == 'False':   # 2nd operand value is False
                check_operand2()    # calling helper function
                token_list[2] = str(eval(token_list[2] + token_list[3] + token_list[4]))   # doing operations and converting into term type
                operation()   # calling helper function
            else:  #Unexpected Input given
                raise ValueError("Unexpected Input you have given, Kindly enter the valid input")


        elif token_list[2] == 'False': # 1st operand value is False
            check_operand1()    # calling helper function
            if token_list[4] == 'True':   # 2nd operand value is True
                check_operand2()   # calling helper function
                token_list[2] = str(eval(token_list[2] + token_list[3] + token_list[4]))   # doing operations and converting into term type
                operation()    # calling helper function
            elif token_list[4] == 'False':   # 2nd operand value is False
                check_operand2()   # calling helper function
                token_list[2] = str(eval(token_list[2] + token_list[3] + token_list[4]))    # doing operations and converting into term type
                operation()   # calling helper function
            else:  #Unexpected Input given
                raise ValueError("Unexpexted Input you have given, Kindly enter the valid input")




        elif token_list[2].isdigit():  # if 1st operand is number
            check_operand1()   # calling helper function
            if token_list[4].isdigit(): # IF 2nd operand is also number
                check_operand2()   # calling helper function
                token_list[2] = str(eval(str(token_list[2]) + token_list[3] + str(token_list[4])))   # doing operations and converting into term type
                operation()    # calling helper function
            else:  # if 2nd operand is string
                if search_var(token_list[4])[0]: # variable is defined from earlier
                    token_list[4] = Data[search_var(token_list[4])[1]]   # accessing the value of variable
                    token_list[2] = str(eval(str(token_list[2]) + token_list[3] + token_list[4]))    # doing operations and converting into term type
                    operation()   # calling helper function
                else:   #Unexpected Input given
                    raise ValueError("Variable", token_list[4],"is not defined from earlier")



        else: # 1st operand is of variable type
            if search_var(token_list[2])[0]:  # variable is defined from earlier
                token_list[2] = Data[search_var(token_list[2])[1]]    # accessing the value of variable
                if token_list[4].isdigit(): # 2nd operand is of number type
                    check_operand2()    # calling helper function
                    token_list[2] = str(eval(token_list[2] + token_list[3] + str(token_list[4])))    # doing operations and converting into term type
                    operation()    # calling helper function
                else: # 2nd operand is also of variable type
                    if search_var(token_list[4])[0]:  # variable is defined from earlier
                        token_list[4] = Data[search_var(token_list[4])[1]]   # accessing the value of variable
                        token_list[2] = str(eval(token_list[2] + token_list[3] + token_list[4]))    # doing operations and converting into term type
                        operation()   # calling helper function
                    else:  # variable is not defined from earlier
                        raise ValueError("Variable", token_list[4], "is not defined from earlier")

            else: # variable is not defined from earlier
                raise ValueError("Variable", token_list[2],"is not defined from earlier")

        print("Current Updated Data list is", Data)

    else:   #Unexpected Input given
        raise ValueError("Expression is neither of the 3 mentioned Types ('Term' Type , 'Unary_Operator' Type , 'Binary_Operator' Type)")

print()    # breaking the output
print("Final Data list is",Data)    # final data list is Here
print()   # breaking the output


print("OUTPUT Results are Here......................")
# OUTPUT code starts here
# Initialisation
tuple_index_mapped_to = []  # Intialising by empty list
non_tuple_index = []   # Intialising by empty list
Data_len = len(Data)   # length of Final Data
for i in range (0,Data_len):   # Termination: i will reach to Data_len
    if type(Data[i]) == tuple:   # if at index i Data is of tuyple type
        print("The Final Value of",Data[i][0],"is",Data[Data[i][1]])
        tuple_index_mapped_to.append(Data[i][1])   # appending
    else:   # if at index i Data is not of tuyple type
        non_tuple_index.append(i)   # appending
        i = i + 1   # increasing i by 1


# print(tuple_index_mapped_to)  # Intial collected list tuple_index_mapped_to
tuple_index_mapped_to.sort()   # sorting the list tuple_index_mapped_to
tuple_index_mapped_to = list(dict.fromkeys(tuple_index_mapped_to))  # deleting the duplicate from the list tuple_index_mapped_to
# print(non_tuple_index)
# print(tuple_index_mapped_to)
print()   # breaking the output


print("Garbage Values are Here......................")
garbage_index = list(set(tuple_index_mapped_to) - set(non_tuple_index)) + list(set(non_tuple_index) - set(tuple_index_mapped_to))  # Code to get difference of two lists Using set()
# print("Garbage indexes are", garbage_index)
garbage_index_len = len(garbage_index)   # length of garbage_index
for i in range (0,garbage_index_len):   # for loop for identifing and printing all the garbage values
    print("One of the Garbage Value in Data is",Data[garbage_index[i]],", Which is present at index",garbage_index[i])

# Code Ends Here