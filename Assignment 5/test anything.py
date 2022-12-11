def all_operators():
    if token_list[3] == '+':
        token_list[2] = operand1 + operand2
        found1 = finding_expression(token_list[2])[0]  # We checked presence of data
        found2 = finding_variable(token_list[0])[0]  # we checked presence of variable
        if found1 == True:  # if data is present
            None
        else:  # if data is not present
            data_list.append(token_list[2])  # we add data to datalist

        if found2 == True:  # we checked presence of variable
            None
        else:  # if variable is not present we append variable and assign data index to this variable
            data_list.append((token_list[0], finding_expression(token_list[2])[1]))

        if data_list[finding_variable(token_list[0])[1]] == token_list[2]:  # we checked it is mapping correct or not
            None
        else:
            Q = list(data_list[finding_variable(token_list[0])[2]])  # conversion from tuple to list format
            Q[1] = finding_expression(token_list[2])[1]  # index got corrected here
            data_list[finding_variable(token_list[0])[2]] = tuple(Q)  # conversion list into tuple format

    if token_list[3] == '-':
        token_list[2] = operand1 - operand2
        found1 = finding_expression(token_list[2])[0]  # We checked presence of data
        found2 = finding_variable(token_list[0])[0]  # we checked presence of variable
        if found1 == True:  # if data is present
            None
        else:  # if data is not present
            data_list.append(token_list[2])  # we add data to datalist

        if found2 == True:  # we checked presence of variable
            None
        else:  # if variable is not present we append variable and assign data index to this variable
            data_list.append((token_list[0], finding_expression(token_list[2])[1]))

        if data_list[finding_variable(token_list[0])[1]] == token_list[2]:  # we checked it is mapping correct or not
            None
        else:
            Q = list(data_list[finding_variable(token_list[0])[2]])  # conversion from tuple to list format
            Q[1] = finding_expression(token_list[2])[1]  # index got corrected here
            data_list[finding_variable(token_list[0])[2]] = tuple(Q)  # conversion list into tuple format

    if token_list[3] == '*':
        token_list[2] = operand1 * operand2
        found1 = finding_expression(token_list[2])[0]  # We checked presence of data
        found2 = finding_variable(token_list[0])[0]  # we checked presence of variable
        if found1 == True:  # if data is present
            None
        else:  # if data is not present
            data_list.append(token_list[2])  # we add data to datalist

        if found2 == True:  # we checked presence of variable
            None
        else:  # if variable is not present we append variable and assign data index to this variable
            data_list.append((token_list[0], finding_expression(token_list[2])[1]))

        if data_list[finding_variable(token_list[0])[1]] == token_list[2]:  # we checked it is mapping correct or not
            None
        else:
            Q = list(data_list[finding_variable(token_list[0])[2]])  # conversion from tuple to list format
            Q[1] = finding_expression(token_list[2])[1]  # index got corrected here
            data_list[finding_variable(token_list[0])[2]] = tuple(Q)  # conversion list into tuple format

    if token_list[3] == '/':
        token_list[2] = operand1 / operand2
        found1 = finding_expression(token_list[2])[0]  # We checked presence of data
        found2 = finding_variable(token_list[0])[0]  # we checked presence of variable
        if found1 == True:  # if data is present
            None
        else:  # if data is not present
            data_list.append(token_list[2])  # we add data to datalist

        if found2 == True:  # we checked presence of variable
            None
        else:  # if variable is not present we append variable and assign data index to this variable
            data_list.append((token_list[0], finding_expression(token_list[2])[1]))

        if data_list[finding_variable(token_list[0])[1]] == token_list[2]:  # we checked it is mapping correct or not
            None
        else:
            Q = list(data_list[finding_variable(token_list[0])[2]])  # conversion from tuple to list format
            Q[1] = finding_expression(token_list[2])[1]  # index got corrected here
            data_list[finding_variable(token_list[0])[2]] = tuple(Q)  # conversion list into tuple format

    if token_list[3] == '>':
        token_list[2] = operand1 > operand2
        found1 = finding_expression(token_list[2])[0]  # We checked presence of data
        found2 = finding_variable(token_list[0])[0]  # we checked presence of variable
        if found1 == True:  # if data is present
            None
        else:  # if data is not present
            data_list.append(token_list[2])  # we add data to datalist

        if found2 == True:  # we checked presence of variable
            None
        else:  # if variable is not present we append variable and assign data index to this variable
            data_list.append((token_list[0], finding_expression(token_list[2])[1]))

        if data_list[finding_variable(token_list[0])[1]] == token_list[2]:  # we checked it is mapping correct or not
            None
        else:
            Q = list(data_list[finding_variable(token_list[0])[2]])  # conversion from tuple to list format
            Q[1] = finding_expression(token_list[2])[1]  # index got corrected here
            data_list[finding_variable(token_list[0])[2]] = tuple(Q)  # conversion list into tuple format

    if token_list[3] == '<':
        token_list[2] = operand1 < operand2
        found1 = finding_expression(token_list[2])[0]  # We checked presence of data
        found2 = finding_variable(token_list[0])[0]  # we checked presence of variable
        if found1 == True:  # if data is present
            None
        else:  # if data is not present
            data_list.append(token_list[2])  # we add data to datalist

        if found2 == True:  # we checked presence of variable
            None
        else:  # if variable is not present we append variable and assign data index to this variable
            data_list.append((token_list[0], finding_expression(token_list[2])[1]))

        if data_list[finding_variable(token_list[0])[1]] == token_list[2]:  # we checked it is mapping correct or not
            None
        else:
            Q = list(data_list[finding_variable(token_list[0])[2]])  # conversion from tuple to list format
            Q[1] = finding_expression(token_list[2])[1]  # index got corrected here
            data_list[finding_variable(token_list[0])[2]] = tuple(Q)  # conversion list into tuple format

    if token_list[3] == '>=':
        token_list[2] = operand1 >= operand2
        found1 = finding_expression(token_list[2])[0]  # We checked presence of data
        found2 = finding_variable(token_list[0])[0]  # we checked presence of variable
        if found1 == True:  # if data is present
            None
        else:  # if data is not present
            data_list.append(token_list[2])  # we add data to datalist

        if found2 == True:  # we checked presence of variable
            None
        else:  # if variable is not present we append variable and assign data index to this variable
            data_list.append((token_list[0], finding_expression(token_list[2])[1]))

        if data_list[finding_variable(token_list[0])[1]] == token_list[2]:  # we checked it is mapping correct or not
            None
        else:
            Q = list(data_list[finding_variable(token_list[0])[2]])  # conversion from tuple to list format
            Q[1] = finding_expression(token_list[2])[1]  # index got corrected here
            data_list[finding_variable(token_list[0])[2]] = tuple(Q)  # conversion list into tuple format

    if token_list[3] == '<=':
        token_list[2] = operand1 <= operand2
        found1 = finding_expression(token_list[2])[0]  # We checked presence of data
        found2 = finding_variable(token_list[0])[0]  # we checked presence of variable
        if found1 == True:  # if data is present
            None
        else:  # if data is not present
            data_list.append(token_list[2])  # we add data to datalist

        if found2 == True:  # we checked presence of variable
            None
        else:  # if variable is not present we append variable and assign data index to this variable
            data_list.append((token_list[0], finding_expression(token_list[2])[1]))

        if data_list[finding_variable(token_list[0])[1]] == token_list[2]:  # we checked it is mapping correct or not
            None
        else:
            Q = list(data_list[finding_variable(token_list[0])[2]])  # conversion from tuple to list format
            Q[1] = finding_expression(token_list[2])[1]  # index got corrected here
            data_list[finding_variable(token_list[0])[2]] = tuple(Q)  # conversion list into tuple format

    if token_list[3] == '==':
        token_list[2] = operand1 == operand2
        found1 = finding_expression(token_list[2])[0]  # We checked presence of data
        found2 = finding_variable(token_list[0])[0]  # we checked presence of variable
        if found1 == True:  # if data is present
            None
        else:  # if data is not present
            data_list.append(token_list[2])  # we add data to datalist

        if found2 == True:  # we checked presence of variable
            None
        else:  # if variable is not present we append variable and assign data index to this variable
            data_list.append((token_list[0], finding_expression(token_list[2])[1]))

        if data_list[finding_variable(token_list[0])[1]] == token_list[2]:  # we checked it is mapping correct or not
            None
        else:
            Q = list(data_list[finding_variable(token_list[0])[2]])  # conversion from tuple to list format
            Q[1] = finding_expression(token_list[2])[1]  # index got corrected here
            data_list[finding_variable(token_list[0])[2]] = tuple(Q)  # conversion list into tuple format

    if token_list[3] == '!=':
        token_list[2] = operand1 != operand2
        found1 = finding_expression(token_list[2])[0]  # We checked presence of data
        found2 = finding_variable(token_list[0])[0]  # we checked presence of variable
        if found1 == True:  # if data is present
            None
        else:  # if data is not present
            data_list.append(token_list[2])  # we add data to datalist

        if found2 == True:  # we checked presence of variable
            None
        else:  # if variable is not present we append variable and assign data index to this variable
            data_list.append((token_list[0], finding_expression(token_list[2])[1]))

        if data_list[finding_variable(token_list[0])[1]] == token_list[2]:  # we checked it is mapping correct or not
            None
        else:
            Q = list(data_list[finding_variable(token_list[0])[2]])  # conversion from tuple to list format
            Q[1] = finding_expression(token_list[2])[1]  # index got corrected here
            data_list[finding_variable(token_list[0])[2]] = tuple(Q)  # conversion list into tuple format

    if token_list[3] == 'and':
        token_list[2] = operand1 and operand2
        found1 = finding_expression(token_list[2])[0]  # We checked presence of data
        found2 = finding_variable(token_list[0])[0]  # we checked presence of variable
        if found1 == True:  # if data is present
            None
        else:  # if data is not present
            data_list.append(token_list[2])  # we add data to datalist

        if found2 == True:  # we checked presence of variable
            None
        else:  # if variable is not present we append variable and assign data index to this variable
            data_list.append((token_list[0], finding_expression(token_list[2])[1]))

        if data_list[finding_variable(token_list[0])[1]] == token_list[2]:  # we checked it is mapping correct or not
            None
        else:
            Q = list(data_list[finding_variable(token_list[0])[2]])  # conversion from tuple to list format
            Q[1] = finding_expression(token_list[2])[1]  # index got corrected here
            data_list[finding_variable(token_list[0])[2]] = tuple(Q)  # conversion list into tuple format

    if token_list[3] == 'or':
        token_list[2] = operand1 or operand2
        found1 = finding_expression(token_list[2])[0]  # We checked presence of data
        found2 = finding_variable(token_list[0])[0]  # we checked presence of variable
        if found1 == True:  # if data is present
            None
        else:  # if data is not present
            data_list.append(token_list[2])  # we add data to datalist

        if found2 == True:  # we checked presence of variable
            None
        else:  # if variable is not present we append variable and assign data index to this variable
            data_list.append((token_list[0], finding_expression(token_list[2])[1]))

        if data_list[finding_variable(token_list[0])[1]] == token_list[2]:  # we checked it is mapping correct or not
            None
        else:
            Q = list(data_list[finding_variable(token_list[0])[2]])  # conversion from tuple to list format
            Q[1] = finding_expression(token_list[2])[1]  # index got corrected here
            data_list[finding_variable(token_list[0])[2]] = tuple(Q)  # conversion list into tuple format


    return("Done")