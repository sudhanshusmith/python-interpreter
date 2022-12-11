# Name: Sudhanshu Kumar
# Entry Number: 2021CE10518
# Assignment-5(part 2)




lines = [] # initalise to empty list
with open("F:\IITD sem-1\COL Computer science\COL Assignment\Assignment 5b\Assignment 5 - part 2-20220306\input of Assignment 5b.txt") as f:
    lines = f.readlines() # read all lines into a list of strings
n = len(lines)   # n is length of list 'lines'
print("The Number of Line in Your Input file is",n)  # printing number of lines in my input file
print (lines)  # showing the input text file line by line
print()   # Breaking the Output

Instructions_list = []   # Initialising our Instructions_list
Data = [] #Intialising our data center
print("Initial Data list is",Data) # printing initial data list
print() # Breaking the Output


def conditional_evaluation():
    #INPUT: It does not take any Input
    #Output: It doesn't return as such anything, but do a lot's of computation inside this function for what it is designed
    #Purpose of the Function: It check the conditional of While loop, that it is True or False
    # print("Expression is of 'Binary_Operator' Type")
    if token_list[2] == 'True':  # 1st operand value is True
        check_operand1()  # calling helper function
        if token_list[4] == 'True':  # 2nd operand value is True
            check_operand2()  # calling helper function
            token_list[2] = str(
                eval(token_list[2] + token_list[3] + token_list[4]))  # doing operations and converting into term type
            # operation()  # calling helper function
        elif token_list[4] == 'False':  # 2nd operand value is False
            check_operand2()  # calling helper function
            token_list[2] = str(
                eval(token_list[2] + token_list[3] + token_list[4]))  # doing operations and converting into term type
            # operation()  # calling helper function
        else:  # Unexpected Input given
            raise ValueError("Unexpected Input you have given, Kindly enter the valid input")


    elif token_list[2] == 'False':  # 1st operand value is False
        check_operand1()  # calling helper function
        if token_list[4] == 'True':  # 2nd operand value is True
            check_operand2()  # calling helper function
            token_list[2] = str(
                eval(token_list[2] + token_list[3] + token_list[4]))  # doing operations and converting into term type
            # operation()  # calling helper function
        elif token_list[4] == 'False':  # 2nd operand value is False
            check_operand2()  # calling helper function
            token_list[2] = str(
                eval(token_list[2] + token_list[3] + token_list[4]))  # doing operations and converting into term type
            # operation()  # calling helper function
        else:  # Unexpected Input given
            raise ValueError("Unexpexted Input you have given, Kindly enter the valid input")




    elif token_list[2].isdigit():  # if 1st operand is number
        check_operand1()  # calling helper function
        if token_list[4].isdigit():  # IF 2nd operand is also number
            check_operand2()  # calling helper function
            token_list[2] = str(eval(str(token_list[2]) + token_list[3] + str(
                token_list[4])))  # doing operations and converting into term type
            # operation()  # calling helper function
        else:  # if 2nd operand is string
            if search_var(token_list[4])[0]:  # variable is defined from earlier
                token_list[4] = Data[search_var(token_list[4])[1]]  # accessing the value of variable
                token_list[2] = str(eval(str(token_list[2]) + token_list[3] + token_list[
                    4]))  # doing operations and converting into term type
                # operation()  # calling helper function
            else:  # Unexpected Input given
                raise ValueError("Variable", token_list[4], "is not defined from earlier")



    else:  # 1st operand is of variable type
        if search_var(token_list[2])[0]:  # variable is defined from earlier
            token_list[2] = Data[search_var(token_list[2])[1]]  # accessing the value of variable
            if token_list[4].isdigit():  # 2nd operand is of number type
                check_operand2()  # calling helper function
                token_list[2] = str(eval(token_list[2] + token_list[3] + str(
                    token_list[4])))  # doing operations and converting into term type
                # operation()  # calling helper function
            else:  # 2nd operand is also of variable type
                if search_var(token_list[4])[0]:  # variable is defined from earlier
                    token_list[4] = Data[search_var(token_list[4])[1]]  # accessing the value of variable
                    token_list[2] = str(eval(token_list[2] + token_list[3] + token_list[
                        4]))  # doing operations and converting into term type
                    # operation()  # calling helper function
                else:  # variable is not defined from earlier
                    raise ValueError("Variable", token_list[4], "is not defined from earlier")

        else:  # variable is not defined from earlier
            raise ValueError("Variable", token_list[2], "is not defined from earlier")

    print("Current Updated Data list is", Data)


def assignment5():
    # INPUT: It does not take any Input
    # Output: It doesn't return as such anything, but do a lot's of computation inside this function for what it is designed
    # Purpose of the Function: It's code of Assignment-5 and it will be now used as a helper function
    # token_list = token_list_while
    # print(token_list)
    p = len(token_list)
    # Checking for which case in Variable = Expression
    if p == 3:  # Expression is of 'Term' Type
        # print("Expression is of 'Term' Type")

        if token_list[2].isdigit():  # if data is of number type
            # print("Term is of Number Type")
            operation()  # calling helper function

        else:  # Expression may be of String Type
            if token_list[2] == 'True':  # Expression value is boolean
                # print("Term value is True")
                operation()  # calling helper function

            elif token_list[2] == 'False':  # Expression value is boolean
                # print("Term value is False")
                operation()  # calling helper function

            else:  # Expression is of String Type
                # print("Term is of purely String Type")
                if search_var(token_list[2])[0]:  # Variable is defined from earlier
                    # print("Variable is defined from earlier")
                    token_list[2] = Data[search_var(token_list[2])[1]]  # accessing the value of variable
                    operation()  # calling helper function

                else:  # # Variable is not defined from earlier
                    raise ValueError("Variable", token_list[2], "is not defined")

        print("Current Updated Data list is", Data)






    elif p == 4:  # Expression is of 'Unary_Operator' Type
        print("Expression is of 'Unary_Operator' Type")

        if token_list[2] == '-':  # It's case of -2, -4 , -a  ......etc
            if token_list[3].isdigit():  # verifying that after minus there is integer or float only, not strings
                token_list[2] = str(-int(token_list[3]))  # converting in term type to apply that result
                operation()  # calling helper function

            else:  # It means after '-' there is variable in form of strings
                if search_var(token_list[3])[0]:  # Variable is defined from earlier
                    # print("Variable is defined from earlier")
                    token_list[2] = str(-int(Data[search_var(token_list[3])[1]]))  # accessing the value of variable
                    operation()  # calling helper function
                else:  # # Variable is not defined from earlier
                    raise ValueError("Variable", token_list[3], "is not defined")


        elif token_list[2] == 'not':  # If uniary operator is 'not'
            if token_list[3] == 'True':  # Its case of not True type
                token_list[2] = 'False'  # converting in term type to apply that result
                operation()  # calling helper function

            elif token_list[3] == 'False':  # It's case of not False type
                token_list[2] = 'True'  # converting in term type to apply that result
                operation()  # calling helper function

            else:  # It is the case of neither 'not True' and 'not False'
                raise ValueError("Unexpexted Input you have given, Kindly enter the valid input")


        else:  # token_list[2] is neither 'not' or '-'
            raise ValueError("Unexpexted Input you have given, Kindly enter the valid input")

        print("Current Updated Data list is", Data)






    elif p == 5:  # Expression is of 'Binary_Operator' Type
        # print("Expression is of 'Binary_Operator' Type")
        if token_list[2] == 'True':  # 1st operand value is True
            check_operand1()  # calling helper function
            if token_list[4] == 'True':  # 2nd operand value is True
                check_operand2()  # calling helper function
                token_list[2] = str(eval(
                    token_list[2] + token_list[3] + token_list[4]))  # doing operations and converting into term type
                operation()  # calling helper function
            elif token_list[4] == 'False':  # 2nd operand value is False
                check_operand2()  # calling helper function
                token_list[2] = str(eval(
                    token_list[2] + token_list[3] + token_list[4]))  # doing operations and converting into term type
                operation()  # calling helper function
            else:  # Unexpected Input given
                raise ValueError("Unexpected Input you have given, Kindly enter the valid input")


        elif token_list[2] == 'False':  # 1st operand value is False
            check_operand1()  # calling helper function
            if token_list[4] == 'True':  # 2nd operand value is True
                check_operand2()  # calling helper function
                token_list[2] = str(eval(
                    token_list[2] + token_list[3] + token_list[4]))  # doing operations and converting into term type
                operation()  # calling helper function
            elif token_list[4] == 'False':  # 2nd operand value is False
                check_operand2()  # calling helper function
                token_list[2] = str(eval(
                    token_list[2] + token_list[3] + token_list[4]))  # doing operations and converting into term type
                operation()  # calling helper function
            else:  # Unexpected Input given
                raise ValueError("Unexpexted Input you have given, Kindly enter the valid input")




        elif token_list[2].isdigit():  # if 1st operand is number
            check_operand1()  # calling helper function
            if token_list[4].isdigit():  # IF 2nd operand is also number
                check_operand2()  # calling helper function
                token_list[2] = str(eval(str(token_list[2]) + token_list[3] + str(
                    token_list[4])))  # doing operations and converting into term type
                operation()  # calling helper function
            else:  # if 2nd operand is string
                if search_var(token_list[4])[0]:  # variable is defined from earlier
                    token_list[4] = Data[search_var(token_list[4])[1]]  # accessing the value of variable
                    token_list[2] = str(eval(str(token_list[2]) + token_list[3] + token_list[
                        4]))  # doing operations and converting into term type
                    operation()  # calling helper function
                else:  # Unexpected Input given
                    raise ValueError("Variable", token_list[4], "is not defined from earlier")



        else:  # 1st operand is of variable type
            if search_var(token_list[2])[0]:  # variable is defined from earlier
                token_list[2] = Data[search_var(token_list[2])[1]]  # accessing the value of variable
                if token_list[4].isdigit():  # 2nd operand is of number type
                    check_operand2()  # calling helper function
                    token_list[2] = str(eval(token_list[2] + token_list[3] + str(
                        token_list[4])))  # doing operations and converting into term type
                    operation()  # calling helper function
                else:  # 2nd operand is also of variable type
                    if search_var(token_list[4])[0]:  # variable is defined from earlier
                        token_list[4] = Data[search_var(token_list[4])[1]]  # accessing the value of variable
                        token_list[2] = str(eval(token_list[2] + token_list[3] + token_list[
                            4]))  # doing operations and converting into term type
                        operation()  # calling helper function
                    else:  # variable is not defined from earlier
                        raise ValueError("Variable", token_list[4], "is not defined from earlier")

            else:  # variable is not defined from earlier
                raise ValueError("Variable", token_list[2], "is not defined from earlier")

        print("Current Updated Data list is", Data)

    else:  # Unexpected Input given
        raise ValueError(
            "Expression is neither of the 3 mentioned Types ('Term' Type , 'Unary_Operator' Type , 'Binary_Operator' Type)")


def search_exp(x):
    # Purpose of Function: It will search that a particular data x is already stored in the data or not
    # INPUT: It takes expression as a input
    # OUTPUT:
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


def search_var(x):
    # Purpose of the Function: It will search that a particular var x is already mapped to some data or not
    # Input: It will take Variable as a input
    # Output:
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


def operation():
    # Purpose of the Function: defining the function which is a helper function of doing operation whenever required
    # INPUT: It does not take any Input
    # Output: It doesn't return as such anything, but do a lot's of computation inside this function for what it is designed
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

    return ("This Operation has been executed Succesfully")  # return of the helper function


def check_operand1():
    #Purpose of the Function: defining helper function to check wether operand1 is already present inside memory or not?
    # INPUT: It does not take any Input
    # Output: It doesn't return as such anything, but do a lot's of computation inside this function for what it is designed
    if search_exp(token_list[2])[0]:  # If operand1 is already present inside memory
        None  # doing nothing
    else: # If operand1 is not present inside memory
        # print("We have checked that 1st operand was not present in Data, Now We have added for you")
        Data.append(token_list[2])  # appending the operand1 inside memory


def check_operand2():
    # Purpose of the Function: defining helper function to check wether operand2 is already present inside memory or not?
    # INPUT: It does not take any Input
    # Output: It doesn't return as such anything, but do a lot's of computation inside this function for what it is designed
    if search_exp(token_list[4])[0]: # If operand2 is already present inside memory
        None  # doing nothing
    else:  # If operand2 is not present inside memory
        # print("We have checked that 2nd operand was not present in Data, Now We have added for you")
        Data.append(token_list[4])  # appending the operand2 inside memory


# collecting all lines number which are in intendation with tab
tabs_info = [0]  # Initialisation
for i in range (0,n):   # loop for collecting all lines number which are in intendation with tab
    tabs = 0   # Initialisation
    while lines[i][tabs] == '\t':   # checking that tab is present or not
        tabs += 1    # increasing value of tab by 1
    tabs_info.append((f'lines{i + 1}', tabs))   # appending all lines number which are in intendation with tab in a tabs_info
# print(tabs_info)


loop_body_lines_number = []   # Initialisation   [4,5,9]
all_loops_lines = []    # Initialisation   ['x = x + 1', 'y = 3', 'i = i + 1']
while_all_loop_body_in_tuple =[]    # Initialisation   [('x = x + 1', 'y = 3'), ('i = i + 1')]
particular_loop_body_in_tuple = []   # Initialisation ['x = x + 1', 'y = 3']

i = 0    # Initialisation
while i < n:
    if tabs_info[(i + 1)][1] == 1:   # checking that if tab == 1
        loop_body_lines_number.append(i + 1)   # appending
        all_loops_lines.append(lines[i])    # appending
        particular_loop_body_in_tuple.append(lines[i])    # appending
        if i == n-1 and particular_loop_body_in_tuple != []:   # checking
            while_all_loop_body_in_tuple.append(particular_loop_body_in_tuple)   # appending

        i = i + 1  # increasing i by 1
    else:   # if tab is not equal to 1
        i = i + 1   # increasing i by 1
        if particular_loop_body_in_tuple != []:   # checking that it is not empty list?
            while_all_loop_body_in_tuple.append(particular_loop_body_in_tuple)   # appending
        particular_loop_body_in_tuple = []   # again assigning it as a empty list


# print(loop_body_lines_number)
# print(all_loops_lines)
# print(while_all_loop_body_in_tuple)
# print(particular_loop_body_in_tuple)



count = 0   # Intialisation


for i in range (0,n): # each statement is on a separate line
    token_list = lines[i].split() # split a statement into a list of tokens
    p = len(token_list)  # p is length of token_list (i.e length of each line after splitting)
    print()  # breaking the output
    print("Reading Line number",(i+1),"......................................................")
    print ("Tokens:", token_list) # now process each statement
    # print("Total length of token_list is",p)

    tabs = 0   # Intialisation
    while lines[i][tabs] == '\t':   # checking line have tabs or not
        tabs += 1   # increasing tabs by 1
    print("tabs: ", tabs)


    if lines[i] in all_loops_lines:   # skiping the lines which are in intendation
        print("skipped this line as it's a loop body part and handeled it seperately")
        continue   # skkiping

    #Checking for which cases

    if token_list[0] == 'while':   # code for intrepreating a while loop

        token_list.insert(1,'=')  # inserting '=' in a token list at index 1

        # resolving the issue of semicolumn(:) after space or without space
        w = len(token_list[4])   # length of token_list[4]
        if token_list[4][w-1] == ':' :   # checking
            token_list[4] = token_list[4][0:(w-1)]  # re-assigning
        else:
            None   # skkiping


        # checking operator which is used in conditional
        if token_list[3] == '<=':
            r = ('BLE', token_list[2], token_list[4], (i + 2 + len(while_all_loop_body_in_tuple[count])))
        elif token_list[3] == '>=':
            r = ('Not BLE', token_list[2], token_list[4], (i + 2 + len(while_all_loop_body_in_tuple[count])))
        elif token_list[3] == '<':
            r = ('BLT', token_list[2], token_list[4], (i + 2 + len(while_all_loop_body_in_tuple[count])))
        elif token_list[3] == '>':
            r = ('Not BLT', token_list[2], token_list[4], (i + 2 + len(while_all_loop_body_in_tuple[count])))
        elif token_list[3] == '=':
            r = ('BE', token_list[2], token_list[4], (i + 2 + len(while_all_loop_body_in_tuple[count])))
        else:
            r = (token_list[3], token_list[2], token_list[4], (i + 2 + len(while_all_loop_body_in_tuple[count])))
        Instructions_list.append(r)   # appending in Instructions_list

        conditional_evaluation()  # calling helper function

        if token_list[2] == 'True':   # if conditional states True
            token_list[2] = True
        else:   # if conditional states False
            token_list[2] = False


        lines_while = while_all_loop_body_in_tuple[count]
        len_of_lines_while = len(lines_while)

        while token_list[2]:   # handling the statement of loop body
            for  j in range(0,len_of_lines_while):
                token_list_while = lines_while[j].split()

                if j == len_of_lines_while - 1:
                    token_list = token_list_while

                    if token_list not in Instructions_list:
                        Instructions_list.append(tuple(token_list))

                    assignment5()   # calling helper function

                    token_list = lines[i].split()
                    token_list.insert(1, '=')

                    # resolving the issue of semicolumn(:) after space or without space
                    w = len(token_list[4])  # length of token_list[4]
                    if token_list[4][w - 1] == ':':  # checking
                        token_list[4] = token_list[4][0:(w - 1)]  # re-assigning
                    else:
                        None  # skkiping

                else:
                    token_list = token_list_while

                    if token_list not in Instructions_list:
                        Instructions_list.append(tuple(token_list))

                    assignment5()   # calling helper function

            conditional_evaluation()   # calling helper function

            if token_list[2] == 'True':  # if conditional states True
                token_list[2] = True
            else:  # if conditional states False
                token_list[2] = False

        index = Instructions_list.index(r)  # getting the index via searching
        # Instructions_list.append(("Branch",index))
        Instructions_list.append(("Branch", i))   # appending
        count = count + 1  # increasing by 1



    else:
        Instructions_list.append(tuple(token_list))   # appending
        assignment5()   # calling helper function


print()
print()    # breaking the output
print("Final Data list is",Data)    # final data list is Here
print()   # breaking the output
print()


# Removing the duplicacy from Instruction_list
res = []   # Initialisation
for h in Instructions_list:  # checking
    if h not in res:   # checking
        res.append(h)  # appending

print("Instructions List are Here......................")
print(res)  # printing Instruction_list
print()
print()

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
print()

print("Garbage Values are Here......................")
garbage_index = list(set(tuple_index_mapped_to) - set(non_tuple_index)) + list(set(non_tuple_index) - set(tuple_index_mapped_to))  # Code to get difference of two lists Using set()
# print("Garbage indexes are", garbage_index)
garbage_index_len = len(garbage_index)   # length of garbage_index
for i in range (0,garbage_index_len):   # for loop for identifing and printing all the garbage values
    print("One of the Garbage Value in Data is",Data[garbage_index[i]],", Which is present at index",garbage_index[i])

# Code Ends Here