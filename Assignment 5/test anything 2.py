def operator():
    if token_list[3] == '+':
        token_list[2] = operand1 + operand2
        if search_exp(token_list[2])[0]:
            print("We checked that Data is already present")
            if search_var(token_list[0])[0]:
                print("We checked that Variable is present & already mapped to some index")
                if Data[search_var(token_list[0])[1]] == token_list[2]:
                    print("Variable is already mapped to right index")
                else:
                    print("Variable is not mapped to right index & We have mapped it at right index")
                    y = list(Data[search_var(token_list[0])[2]])  # converting tuple to list
                    y[1] = search_exp(token_list[2])[1]  # correcting the index
                    Data[search_var(token_list[0])[2]] = tuple(y)  # converting list to tuple
            else:
                print(
                    "We checked that Variable is not present & not mapped to any index, We have added this new variable & mapped it for you")
                Data.append((token_list[0], search_exp(token_list[2])[1]))
        else:
            print("We checked that data is not present, We have added data for you")
            Data.append(token_list[2])
            if search_var(token_list[0])[0]:
                print("We checked that Variable is present & already mapped to some index")
                if Data[search_var(token_list[0])[1]] == token_list[2]:
                    print("Variable is already mapped to right index")
                else:
                    print("Variable is not mapped to right index & We have mapped it at right index")
                    y = list(Data[search_var(token_list[0])[2]])  # converting tuple to list
                    y[1] = search_exp(token_list[2])[1]  # correcting the index
                    Data[search_var(token_list[0])[2]] = tuple(y)  # converting list to tuple

            else:
                print(
                    "We checked that Variable is not present & not mapped to any index, We have added this new variable & mapped it for you")
                Data.append((token_list[0], search_exp(token_list[2])[1]))




    elif token_list[3] == '-':
        token_list[2] = operand1 - operand2
        if search_exp(token_list[2])[0]:
            print("We checked that Data is already present")
            if search_var(token_list[0])[0]:
                print("We checked that Variable is present & already mapped to some index")
                if Data[search_var(token_list[0])[1]] == token_list[2]:
                    print("Variable is already mapped to right index")
                else:
                    print("Variable is not mapped to right index & We have mapped it at right index")
                    y = list(Data[search_var(token_list[0])[2]])  # converting tuple to list
                    y[1] = search_exp(token_list[2])[1]  # correcting the index
                    Data[search_var(token_list[0])[2]] = tuple(y)  # converting list to tuple
            else:
                print(
                    "We checked that Variable is not present & not mapped to any index, We have added this new variable & mapped it for you")
                Data.append((token_list[0], search_exp(token_list[2])[1]))
        else:
            print("We checked that data is not present, We have added data for you")
            Data.append(token_list[2])
            if search_var(token_list[0])[0]:
                print("We checked that Variable is present & already mapped to some index")
                if Data[search_var(token_list[0])[1]] == token_list[2]:
                    print("Variable is already mapped to right index")
                else:
                    print("Variable is not mapped to right index & We have mapped it at right index")
                    y = list(Data[search_var(token_list[0])[2]])  # converting tuple to list
                    y[1] = search_exp(token_list[2])[1]  # correcting the index
                    Data[search_var(token_list[0])[2]] = tuple(y)  # converting list to tuple

            else:
                print(
                    "We checked that Variable is not present & not mapped to any index, We have added this new variable & mapped it for you")
                Data.append((token_list[0], search_exp(token_list[2])[1]))





    elif token_list[3] == '*':
        token_list[2] = operand1 * operand2
        if search_exp(token_list[2])[0]:
            print("We checked that Data is already present")
            if search_var(token_list[0])[0]:
                print("We checked that Variable is present & already mapped to some index")
                if Data[search_var(token_list[0])[1]] == token_list[2]:
                    print("Variable is already mapped to right index")
                else:
                    print("Variable is not mapped to right index & We have mapped it at right index")
                    y = list(Data[search_var(token_list[0])[2]])  # converting tuple to list
                    y[1] = search_exp(token_list[2])[1]  # correcting the index
                    Data[search_var(token_list[0])[2]] = tuple(y)  # converting list to tuple
            else:
                print(
                    "We checked that Variable is not present & not mapped to any index, We have added this new variable & mapped it for you")
                Data.append((token_list[0], search_exp(token_list[2])[1]))
        else:
            print("We checked that data is not present, We have added data for you")
            Data.append(token_list[2])
            if search_var(token_list[0])[0]:
                print("We checked that Variable is present & already mapped to some index")
                if Data[search_var(token_list[0])[1]] == token_list[2]:
                    print("Variable is already mapped to right index")
                else:
                    print("Variable is not mapped to right index & We have mapped it at right index")
                    y = list(Data[search_var(token_list[0])[2]])  # converting tuple to list
                    y[1] = search_exp(token_list[2])[1]  # correcting the index
                    Data[search_var(token_list[0])[2]] = tuple(y)  # converting list to tuple

            else:
                print(
                    "We checked that Variable is not present & not mapped to any index, We have added this new variable & mapped it for you")
                Data.append((token_list[0], search_exp(token_list[2])[1]))





    elif token_list[3] == '/':
        token_list[2] = operand1 / operand2
        if search_exp(token_list[2])[0]:
            print("We checked that Data is already present")
            if search_var(token_list[0])[0]:
                print("We checked that Variable is present & already mapped to some index")
                if Data[search_var(token_list[0])[1]] == token_list[2]:
                    print("Variable is already mapped to right index")
                else:
                    print("Variable is not mapped to right index & We have mapped it at right index")
                    y = list(Data[search_var(token_list[0])[2]])  # converting tuple to list
                    y[1] = search_exp(token_list[2])[1]  # correcting the index
                    Data[search_var(token_list[0])[2]] = tuple(y)  # converting list to tuple
            else:
                print(
                    "We checked that Variable is not present & not mapped to any index, We have added this new variable & mapped it for you")
                Data.append((token_list[0], search_exp(token_list[2])[1]))
        else:
            print("We checked that data is not present, We have added data for you")
            Data.append(token_list[2])
            if search_var(token_list[0])[0]:
                print("We checked that Variable is present & already mapped to some index")
                if Data[search_var(token_list[0])[1]] == token_list[2]:
                    print("Variable is already mapped to right index")
                else:
                    print("Variable is not mapped to right index & We have mapped it at right index")
                    y = list(Data[search_var(token_list[0])[2]])  # converting tuple to list
                    y[1] = search_exp(token_list[2])[1]  # correcting the index
                    Data[search_var(token_list[0])[2]] = tuple(y)  # converting list to tuple

            else:
                print(
                    "We checked that Variable is not present & not mapped to any index, We have added this new variable & mapped it for you")
                Data.append((token_list[0], search_exp(token_list[2])[1]))





    elif token_list[3] == '>':
        token_list[2] = operand1 > operand2
        if search_exp(token_list[2])[0]:
            print("We checked that Data is already present")
            if search_var(token_list[0])[0]:
                print("We checked that Variable is present & already mapped to some index")
                if Data[search_var(token_list[0])[1]] == token_list[2]:
                    print("Variable is already mapped to right index")
                else:
                    print("Variable is not mapped to right index & We have mapped it at right index")
                    y = list(Data[search_var(token_list[0])[2]])  # converting tuple to list
                    y[1] = search_exp(token_list[2])[1]  # correcting the index
                    Data[search_var(token_list[0])[2]] = tuple(y)  # converting list to tuple
            else:
                print(
                    "We checked that Variable is not present & not mapped to any index, We have added this new variable & mapped it for you")
                Data.append((token_list[0], search_exp(token_list[2])[1]))
        else:
            print("We checked that data is not present, We have added data for you")
            Data.append(token_list[2])
            if search_var(token_list[0])[0]:
                print("We checked that Variable is present & already mapped to some index")
                if Data[search_var(token_list[0])[1]] == token_list[2]:
                    print("Variable is already mapped to right index")
                else:
                    print("Variable is not mapped to right index & We have mapped it at right index")
                    y = list(Data[search_var(token_list[0])[2]])  # converting tuple to list
                    y[1] = search_exp(token_list[2])[1]  # correcting the index
                    Data[search_var(token_list[0])[2]] = tuple(y)  # converting list to tuple

            else:
                print(
                    "We checked that Variable is not present & not mapped to any index, We have added this new variable & mapped it for you")
                Data.append((token_list[0], search_exp(token_list[2])[1]))





    elif token_list[3] == '<':
        token_list[2] = operand1 < operand2
        if search_exp(token_list[2])[0]:
            print("We checked that Data is already present")
            if search_var(token_list[0])[0]:
                print("We checked that Variable is present & already mapped to some index")
                if Data[search_var(token_list[0])[1]] == token_list[2]:
                    print("Variable is already mapped to right index")
                else:
                    print("Variable is not mapped to right index & We have mapped it at right index")
                    y = list(Data[search_var(token_list[0])[2]])  # converting tuple to list
                    y[1] = search_exp(token_list[2])[1]  # correcting the index
                    Data[search_var(token_list[0])[2]] = tuple(y)  # converting list to tuple
            else:
                print(
                    "We checked that Variable is not present & not mapped to any index, We have added this new variable & mapped it for you")
                Data.append((token_list[0], search_exp(token_list[2])[1]))
        else:
            print("We checked that data is not present, We have added data for you")
            Data.append(token_list[2])
            if search_var(token_list[0])[0]:
                print("We checked that Variable is present & already mapped to some index")
                if Data[search_var(token_list[0])[1]] == token_list[2]:
                    print("Variable is already mapped to right index")
                else:
                    print("Variable is not mapped to right index & We have mapped it at right index")
                    y = list(Data[search_var(token_list[0])[2]])  # converting tuple to list
                    y[1] = search_exp(token_list[2])[1]  # correcting the index
                    Data[search_var(token_list[0])[2]] = tuple(y)  # converting list to tuple

            else:
                print(
                    "We checked that Variable is not present & not mapped to any index, We have added this new variable & mapped it for you")
                Data.append((token_list[0], search_exp(token_list[2])[1]))






    elif token_list[3] == '>=':
        token_list[2] = operand1 >= operand2
        if search_exp(token_list[2])[0]:
            print("We checked that Data is already present")
            if search_var(token_list[0])[0]:
                print("We checked that Variable is present & already mapped to some index")
                if Data[search_var(token_list[0])[1]] == token_list[2]:
                    print("Variable is already mapped to right index")
                else:
                    print("Variable is not mapped to right index & We have mapped it at right index")
                    y = list(Data[search_var(token_list[0])[2]])  # converting tuple to list
                    y[1] = search_exp(token_list[2])[1]  # correcting the index
                    Data[search_var(token_list[0])[2]] = tuple(y)  # converting list to tuple
            else:
                print(
                    "We checked that Variable is not present & not mapped to any index, We have added this new variable & mapped it for you")
                Data.append((token_list[0], search_exp(token_list[2])[1]))
        else:
            print("We checked that data is not present, We have added data for you")
            Data.append(token_list[2])
            if search_var(token_list[0])[0]:
                print("We checked that Variable is present & already mapped to some index")
                if Data[search_var(token_list[0])[1]] == token_list[2]:
                    print("Variable is already mapped to right index")
                else:
                    print("Variable is not mapped to right index & We have mapped it at right index")
                    y = list(Data[search_var(token_list[0])[2]])  # converting tuple to list
                    y[1] = search_exp(token_list[2])[1]  # correcting the index
                    Data[search_var(token_list[0])[2]] = tuple(y)  # converting list to tuple

            else:
                print(
                    "We checked that Variable is not present & not mapped to any index, We have added this new variable & mapped it for you")
                Data.append((token_list[0], search_exp(token_list[2])[1]))




    elif token_list[3] == '<=':
        token_list[2] = operand1 <= operand2
        if search_exp(token_list[2])[0]:
            print("We checked that Data is already present")
            if search_var(token_list[0])[0]:
                print("We checked that Variable is present & already mapped to some index")
                if Data[search_var(token_list[0])[1]] == token_list[2]:
                    print("Variable is already mapped to right index")
                else:
                    print("Variable is not mapped to right index & We have mapped it at right index")
                    y = list(Data[search_var(token_list[0])[2]])  # converting tuple to list
                    y[1] = search_exp(token_list[2])[1]  # correcting the index
                    Data[search_var(token_list[0])[2]] = tuple(y)  # converting list to tuple
            else:
                print(
                    "We checked that Variable is not present & not mapped to any index, We have added this new variable & mapped it for you")
                Data.append((token_list[0], search_exp(token_list[2])[1]))
        else:
            print("We checked that data is not present, We have added data for you")
            Data.append(token_list[2])
            if search_var(token_list[0])[0]:
                print("We checked that Variable is present & already mapped to some index")
                if Data[search_var(token_list[0])[1]] == token_list[2]:
                    print("Variable is already mapped to right index")
                else:
                    print("Variable is not mapped to right index & We have mapped it at right index")
                    y = list(Data[search_var(token_list[0])[2]])  # converting tuple to list
                    y[1] = search_exp(token_list[2])[1]  # correcting the index
                    Data[search_var(token_list[0])[2]] = tuple(y)  # converting list to tuple

            else:
                print(
                    "We checked that Variable is not present & not mapped to any index, We have added this new variable & mapped it for you")
                Data.append((token_list[0], search_exp(token_list[2])[1]))




    elif token_list[3] == '==':
        token_list[2] = operand1 == operand2
        if search_exp(token_list[2])[0]:
            print("We checked that Data is already present")
            if search_var(token_list[0])[0]:
                print("We checked that Variable is present & already mapped to some index")
                if Data[search_var(token_list[0])[1]] == token_list[2]:
                    print("Variable is already mapped to right index")
                else:
                    print("Variable is not mapped to right index & We have mapped it at right index")
                    y = list(Data[search_var(token_list[0])[2]])  # converting tuple to list
                    y[1] = search_exp(token_list[2])[1]  # correcting the index
                    Data[search_var(token_list[0])[2]] = tuple(y)  # converting list to tuple
            else:
                print(
                    "We checked that Variable is not present & not mapped to any index, We have added this new variable & mapped it for you")
                Data.append((token_list[0], search_exp(token_list[2])[1]))
        else:
            print("We checked that data is not present, We have added data for you")
            Data.append(token_list[2])
            if search_var(token_list[0])[0]:
                print("We checked that Variable is present & already mapped to some index")
                if Data[search_var(token_list[0])[1]] == token_list[2]:
                    print("Variable is already mapped to right index")
                else:
                    print("Variable is not mapped to right index & We have mapped it at right index")
                    y = list(Data[search_var(token_list[0])[2]])  # converting tuple to list
                    y[1] = search_exp(token_list[2])[1]  # correcting the index
                    Data[search_var(token_list[0])[2]] = tuple(y)  # converting list to tuple

            else:
                print(
                    "We checked that Variable is not present & not mapped to any index, We have added this new variable & mapped it for you")
                Data.append((token_list[0], search_exp(token_list[2])[1]))




    elif token_list[3] == '!=':
        token_list[2] = operand1 != operand2
        if search_exp(token_list[2])[0]:
            print("We checked that Data is already present")
            if search_var(token_list[0])[0]:
                print("We checked that Variable is present & already mapped to some index")
                if Data[search_var(token_list[0])[1]] == token_list[2]:
                    print("Variable is already mapped to right index")
                else:
                    print("Variable is not mapped to right index & We have mapped it at right index")
                    y = list(Data[search_var(token_list[0])[2]])  # converting tuple to list
                    y[1] = search_exp(token_list[2])[1]  # correcting the index
                    Data[search_var(token_list[0])[2]] = tuple(y)  # converting list to tuple
            else:
                print(
                    "We checked that Variable is not present & not mapped to any index, We have added this new variable & mapped it for you")
                Data.append((token_list[0], search_exp(token_list[2])[1]))
        else:
            print("We checked that data is not present, We have added data for you")
            Data.append(token_list[2])
            if search_var(token_list[0])[0]:
                print("We checked that Variable is present & already mapped to some index")
                if Data[search_var(token_list[0])[1]] == token_list[2]:
                    print("Variable is already mapped to right index")
                else:
                    print("Variable is not mapped to right index & We have mapped it at right index")
                    y = list(Data[search_var(token_list[0])[2]])  # converting tuple to list
                    y[1] = search_exp(token_list[2])[1]  # correcting the index
                    Data[search_var(token_list[0])[2]] = tuple(y)  # converting list to tuple

            else:
                print(
                    "We checked that Variable is not present & not mapped to any index, We have added this new variable & mapped it for you")
                Data.append((token_list[0], search_exp(token_list[2])[1]))





    elif token_list[3] == 'and':
        token_list[2] = operand1 and operand2
        if search_exp(token_list[2])[0]:
            print("We checked that Data is already present")
            if search_var(token_list[0])[0]:
                print("We checked that Variable is present & already mapped to some index")
                if Data[search_var(token_list[0])[1]] == token_list[2]:
                    print("Variable is already mapped to right index")
                else:
                    print("Variable is not mapped to right index & We have mapped it at right index")
                    y = list(Data[search_var(token_list[0])[2]])  # converting tuple to list
                    y[1] = search_exp(token_list[2])[1]  # correcting the index
                    Data[search_var(token_list[0])[2]] = tuple(y)  # converting list to tuple
            else:
                print(
                    "We checked that Variable is not present & not mapped to any index, We have added this new variable & mapped it for you")
                Data.append((token_list[0], search_exp(token_list[2])[1]))
        else:
            print("We checked that data is not present, We have added data for you")
            Data.append(token_list[2])
            if search_var(token_list[0])[0]:
                print("We checked that Variable is present & already mapped to some index")
                if Data[search_var(token_list[0])[1]] == token_list[2]:
                    print("Variable is already mapped to right index")
                else:
                    print("Variable is not mapped to right index & We have mapped it at right index")
                    y = list(Data[search_var(token_list[0])[2]])  # converting tuple to list
                    y[1] = search_exp(token_list[2])[1]  # correcting the index
                    Data[search_var(token_list[0])[2]] = tuple(y)  # converting list to tuple

            else:
                print(
                    "We checked that Variable is not present & not mapped to any index, We have added this new variable & mapped it for you")
                Data.append((token_list[0], search_exp(token_list[2])[1]))





    elif token_list[3] == 'or':
        token_list[2] = operand1 or operand2
        if search_exp(token_list[2])[0]:
            print("We checked that Data is already present")
            if search_var(token_list[0])[0]:
                print("We checked that Variable is present & already mapped to some index")
                if Data[search_var(token_list[0])[1]] == token_list[2]:
                    print("Variable is already mapped to right index")
                else:
                    print("Variable is not mapped to right index & We have mapped it at right index")
                    y = list(Data[search_var(token_list[0])[2]])  # converting tuple to list
                    y[1] = search_exp(token_list[2])[1]  # correcting the index
                    Data[search_var(token_list[0])[2]] = tuple(y)  # converting list to tuple
            else:
                print(
                    "We checked that Variable is not present & not mapped to any index, We have added this new variable & mapped it for you")
                Data.append((token_list[0], search_exp(token_list[2])[1]))
        else:
            print("We checked that data is not present, We have added data for you")
            Data.append(token_list[2])
            if search_var(token_list[0])[0]:
                print("We checked that Variable is present & already mapped to some index")
                if Data[search_var(token_list[0])[1]] == token_list[2]:
                    print("Variable is already mapped to right index")
                else:
                    print("Variable is not mapped to right index & We have mapped it at right index")
                    y = list(Data[search_var(token_list[0])[2]])  # converting tuple to list
                    y[1] = search_exp(token_list[2])[1]  # correcting the index
                    Data[search_var(token_list[0])[2]] = tuple(y)  # converting list to tuple

            else:
                print(
                    "We checked that Variable is not present & not mapped to any index, We have added this new variable & mapped it for you")
                Data.append((token_list[0], search_exp(token_list[2])[1]))

    return ("This Binary operator line excuted succesfully")