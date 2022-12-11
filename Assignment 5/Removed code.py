elif token_list[2].isdigit():  # if 1st operand is number
print(search_exp(token_list[2]))
if search_exp(token_list[2])[0]:
    None
else:
    print("We have checked that any operands is not present in Data, Now We have added for you")
    Data.append(token_list[2])
    print(token_list[2])
print(token_list)
operand1 = int(token_list[2])  # our operand1
print(token_list[2])

if token_list[4].isdigit():  # IF 2nd operand is also number
    if search_exp(token_list[4])[0]:
        None
    else:  # if 2nd operand is string or (variable)
        print("We have checked that any operands is not present in Data, Now We have added for you")
        Data.append(token_list[4])
    operand2 = int(token_list[4])
    operator()

else:  # if 2nd operand is string
    if search_var(token_list[4])[0]:  # variable is defined from earlier
        operand2 = Data[search_var(token_list[4])[1]]
        operator()
    else:
        raise ValueError("Variable", token_list[4], "is not defined from earlier")

else:  # 1st operand is of variable type
if search_var(token_list[2])[0]:  # variable is defined from earlier
    operand1 = Data[search_var(token_list[2])[1]]
    if token_list[4].isdigit():  # 2nd operand is of number type
        if search_exp(token_list[4])[0]:
            None
        else:
            print("We have checked that any operands is not present in Data, Now We have added for you")
            Data.append(token_list[4])
        operand2 = float(token_list[4])
        operator()

    else:  # 2nd operand is also of variable type
        if search_var(token_list[4])[0]:  # variable is defined from earlier
            operand2 = Data[search_var(token_list[4])[1]]
            operator()
        else:  # variable is not defined from earlier
            raise ValueError("Variable", token_list[4], "is not defined from earlier")

else:  # variable is not defined from earlier
    raise ValueError("Variable", token_list[2], "is not defined from earlier")
