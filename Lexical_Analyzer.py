#!/usr/bin/env python
# coding: utf-8

import csv


def read_file(file_name: str) -> str:
    
    # "java_0_code_text_file.txt"
    # "Java_0_Complete_Program.txt"
    
    # open file as text_file
    with open(file_name, "r") as text_file: 
        
        # save all the data in the file in lines
        lines = text_file.read()
        
        # return lines converted to lowercase
        return lines.lower()


def get_csv(file_name: str) -> list:

    # initializing the following lists
    fields: list = []
    rows_list: list = []
    table: list = []

    # open the CSV file 
    with open(file_name, 'r') as csv_file:
        
        # save the data from csv_file to csv_reader
        csv_reader = csv.reader(csv_file)

        # save the fields row to fields
        fields = next(csv_reader)

        # get each row and save it to rows
        for row in csv_reader:
            rows_list.append(row)
 
    # add the fields to table
    table.append(fields)
    
    # get all the rows from rows_list and add them to table
    for row in rows_list:
        table.append(row)
         
    # returns the table
    return table


def get_dictionary(file_name: str) -> dict:

    # open the CSV file 
    with open(file_name, 'r') as csv_file:
        
        # get an ordered dictionary of the data
        ordered_dict = csv.DictReader(csv_file)
        
        # turn it into a common dictionary by putting it in a list
        into_dictionary = list(ordered_dict)
            
        # return the dictionary by itself
        return into_dictionary[0]


def java_0_DFSM(string: str) -> list:
    
    # variables to help parse 'string'
    current_token: str = ""
        
    token_list: list = []
    current_state: str = "0"
    previous_state: str = "0"
    comment_flag: bool = False
        
    table: list = get_csv("Java_0_DFSA_Table.csv")
    
    any_symbol: list = [" ", "\n"] + table[0][5:19]
        
    # this addresses an edge case without the need to add a new condition
    string += " "

    print("String being parsed: \n\n'" + string + "'")
    
    # going over each individual character in 'string'
    for character in string:

        previous_state = current_state

        
        # COMMENT AND OPERATORS  --------------------------------------------------------


        # if comment_flag is True and previous_state is 11
        if comment_flag and previous_state == "11":
            
            # keep current_state = 11
            current_state = table[12][1]
            
            # if the character is '*' add it to current_token 
            # and set current_state to 12 (go to state 12)
            if character == "*":
                current_token += character
                current_state = table[12][7]
                

            # or current_token is '*' and character is '/' 
            # add '/' to current_token and set current_state to 12 
            # now in state 12 we meet the condition that the comment has ended (go to state 12)
            elif current_token == "*" and character == "/":
                current_token += character
                current_state = table[12][7]
                
                
        # if current_token is '/' and character is anything except '*' (go to state 10)
        elif current_token == "/" and character != "*":
            
            # if current_token is not whitespace add current_token to token_list
            if current_token != " ":
                token_list.append(current_token)
        
            # reset current_token then add character to token_list
            # set current_state = state 10
            current_token = ""
            current_token += character
            current_state = table[10][1]
            
            
        # if current_token is '=' and character is not '=' (go to state 14)
        elif current_token == "=" and character != "=":
            
            # if current_token is not whitespace add current_token to token_list
            if current_token != " ":
                token_list.append(current_token)
        
            # reset current_token then add character to token_list
            # set current_state = state 14
            current_token = ""
            current_token += character
            current_state = table[14][1]
            
            
        # if current_token is '<' and character is not '=' (go to state 17)
        elif current_token == "<" and character != "=":
            
            # if current_token is not whitespace add current_token to token_list
            if current_token != " ":
                token_list.append(current_token)
            
            # reset current_token then add character to token_list
            # set current_state = state 17
            current_token = ""
            current_token += character
            current_state = table[17][1]
            
            
        # if current_token is '>' and character is not '=' (go to state 20)
        elif current_token == ">" and character != "=":
            
            # if current_token is not whitespace add current_token to token_list
            if current_token != " ":
                token_list.append(current_token)
            
            # reset current_token then add character to token_list
            # set current_state = state 20
            current_token = ""
            current_token += character
            current_state = table[20][1]
            
            
        # if current_token is '!' and character is not '=' (go to state 1)
        elif current_token == "!" and character != "=":
            
            # reset current_token then add character to token_list
            # set current_state = state 1
            current_token = ""
            current_state = table[23][1]


        # LETTERS, DIGITS, AND SYMBOLS IF LETTER/DIGIT ADJACENT ----------------------

    
        # if we have a character from any_symbol following a letter (go to state 3)
        elif character in any_symbol and previous_state == "2": 
            
            # if a character from any_symbol is encountered we add the current_token
            # to token_list and proceed with this state to get the symbol individually
            # so long as character is not whitespace
            if character != " ":
                token_list.append(current_token)
                current_token = ""
                current_token += character

            # we have a <variable identifier> set current_state = state 3
            current_state = table[3][1]


        # if we have a digit following a letter (go to state 2)
        elif character.isdigit() and current_state == "2":
            
            # add the character to current_token
            # set current_state = state 2
            current_token += character
            current_state = table[1][3] 

            
        # if we have a letter (state 2)
        elif character.isalpha():
            
            # add the character to current_token
            # set current_state = state 2 
            current_token += character
            current_state = table[1][3]


        # if we have a character from any_symbol following a digit (go to state 4)
        elif character in any_symbol and previous_state == "4": # state 4: digit
            
            # if a character from any_symbol is encountered we add the current_token
            # to token_list and proceed with this state to get the symbol individually
            # so long as character is not whitespace
            if character != " ":
                token_list.append(current_token)
                current_token = ""
                current_token += character
            
            # we have an <integer> set current_state = state 5
            current_state = table[5][1]


        # if we have a digit (go to state 4)
        elif character.isdigit():
            
            # add the digit to current_token
            # set current_state = state 4
            current_token += character
            current_state = table[1][4]
            
        
        # OPERATORS AND COMMENTS ---------------------------------------------------
        
        
        # if we have '/*' as a token and previous_state is 9 (go to state 11)
        elif current_token == "/" and character == "*" and previous_state == "9":
            
            # add the '*' to current_token
            # set current_state = state 11
            current_token += character
            current_state = table[10][7]
            

        # if we have '==' as a token and previous_state is 13 (go to state 15)
        elif current_token == "=" and character == "=" and previous_state == "13":
            
            # add the '=' to current_token
            # set current_state = state 15
            current_token += character 
            current_state = table[14][9]
            
            
        # if we have '<=' as a token and previous_state is 16 (go to state 18)
        elif current_token == "<" and character == "=" and previous_state == "16":
            
            # add the '=' to current_token
            # set current_state = state 18
            current_token += character 
            current_state = table[17][9]
            
            
        # if we have '>=' as a token and previous_state is 19 (go to state 21)
        elif current_token == ">" and character == "=" and previous_state == "19":
            
            # add the '=' to current_token
            # set current_state = state 21
            current_token += character 
            current_state = table[20][9]
            
            
        # if we have '!=' as a token and previous_state is 22 (go to state 23)
        elif current_token == "!" and character == "=" and previous_state == "22":
            
            # add the '=' to current_token
            # set current_state = state 23
            current_token += character 
            current_state = table[23][9]
            
            
        # if we have a '+' sign (go to state 6)
        elif character == "+": 
            
            # add '+' to current_token
            # set current_state = state 6
            current_token += character
            current_state = table[1][5]
            
            
        # if we have a '-' sign (go to state 7)
        elif character == "-": 
            
            # add '-' to current_token
            # set current_state = state 7
            current_token += character
            current_state = table[1][6]

        
        # if we have a '*' sign (go to state 8)
        elif character == "*": 
            
            # add '*' to current_token
            # set current_state = state 8
            current_token += character
            current_state = table[1][7]
            
        
        # if we have a '/' sign (go to state 9)
        elif character == "/": 
            
            # add '/' to current_token 
            # set current_state = state 9
            current_token += character
            current_state = table[1][8]
              
        
        # if we have a '=' sign (go to state 13)
        elif character == "=":
            
            # add '=' to current_token
            # set current_state = state 13
            current_token += character
            current_state = table[1][9]
            
        
        # if we have a '<' sign (go to state 16)
        elif character == "<":
            
            # add '<' to current_token
            # set current_state = state 16
            current_token += character
            current_state = table[1][10]
            
        
        # if we have a '>' sign (go to state 19)
        elif character == ">":
            
            # add '>' to current_token
            # set current_state = state 19
            current_token += character
            current_state = table[1][11]
            
            
        # if we have a '!' sign (go to state 22)
        elif character == "!":
            
            # add '!' to current_token
            # set current_state = state 22
            current_token += character
            current_state = table[1][12]
            
            
        # PARENTHESIS AND BRACES ---------------------------------------------------
        
        
        # if we have a '(' sign (go to state 24)
        elif character == "(": 
            
            # add '(' to current_token
            # set current_state = state 24
            current_token += character
            current_state = table[1][13]
            
        
        # if we have a ')' sign (go to state 25)
        elif character == ")": 
            
            # add ')' to current_token
            # set current_state = state 25
            current_token += character
            current_state = table[1][14]
           
        
        # if we have a '{' sign (go to state 26)
        elif character == "{": 
            
            # add '{' to current_token
            # set current_state = state 26
            current_token += character
            current_state = table[1][15]
            
            
        # if we have a '}' sign (go to state 27)
        elif character == "}": 
            
            # add '}' to current_token
            # set current_state = state 27
            current_token += character
            current_state = table[1][16]
            
        
        # COMMA AND SEMICOLON ------------------------------------------------------
        
        
        # if we have a ',' sign (go to state 28)
        elif character == ",": 
            
            # add ',' to current_token
            # set current_state = state 28
            current_token += character
            current_state = table[1][15]
            
            
        # if we have a ';' sign (go to state 29)
        elif character == ";": 
            
            # add ';' to current_token
            # set current_state = state 29
            current_token += character
            current_state = table[1][16]
        
            
        # SPACE AND UNIDENTIFIED SYMBOLS -------------------------------------------
            
            
        # if we have whitespace (go to state 0)
        elif character == " " or character == "\n":
            
            # set current_state = state 0
            current_state = table[1][1]
            
            
        # otherwise we have an unidentified symbol (go to state 1)
        else:
            
            # set current_state = state 1
            print(character)
            current_state = table[1][2]
            
            
        # CASE STATEMENTS FOR current_state ---------------------------------------
    
    
        # we check current_state and proceed accordingly
        match current_state:

            
            # case 0
            case "0":
                current_token = ""

                
            # case 1
            case "1":
                print("Illegal character")
                break

                
            # case 2 
            case "2":
                pass

                
            # case 3 ( [a-zA-Z] )
            case "3":
                if current_token != "\n":
                    token_list.append(current_token)
                
                current_token = ""
                current_state = "0"

                
            # case 4
            case "4":
                pass

                
            # case 5 ( [0-9] )
            case "5":
                if current_token != "\n":
                    token_list.append(current_token)
                    
                current_token = ""
                current_state = "0"

                
            # case 6 ( + )
            case "6":
                token_list.append(current_token)
                current_token = ""
                current_state = "0"
                
            
            # case 7 ( - )
            case "7":
                token_list.append(current_token)
                current_token = ""
                current_state = "0"
                
            
            # case 8 ( * )
            case "8":
                token_list.append(current_token)
                current_token = ""
                current_state = "0"
                
            
            # case 9 
            case "9":
                pass
                
            
            # case 10 ( / )
            case "10":
                if current_token != " ":
                    token_list.append(current_token)
                    
                current_token = ""
                current_state = "0"
                

            # case 11 ( /* )
            case "11":
                comment_flag = True
                current_token = ""
                current_state = "11"
                
                
            # case 12 ( */ )
            case "12":
                if current_token == "*/":
                    current_token = ""
                    current_state = "0"
                    comment_flag = False
                    
                else:
                    current_state = "11"
                    
                    
            # case 13
            case "13":
                pass

            
            # case 14 ( = )
            case "14":
                if current_token != " ":
                    token_list.append(current_token)
                    
                current_token = ""
                current_state = "0"
                    
            
            # case 15 ( == )
            case "15":
                token_list.append(current_token)
                current_token = ""
                current_state = "0"
                
                               
            # case 16
            case "16":
                pass

            
            # case 17 ( < )
            case "17":
                if current_token != " ":
                    token_list.append(current_token)
                    
                current_token = ""
                current_state = "0"
                    
            
            # case 18 ( <= )
            case "18":
                token_list.append(current_token)
                current_token = ""
                current_state = "0"
                
                
            # case 19
            case "19":
                pass


            # case 20 ( > )
            case "20":
                if current_token != " ":
                    token_list.append(current_token)
                    
                current_token = ""
                current_state = "0"
                    
            
            # case 21 ( >= )
            case "21":
                token_list.append(current_token)
                current_token = ""
                current_state = "0"
                
            
            # case 22
            case "22":
                pass

                
            # case 23 ( != )
            case "23":
                token_list.append(current_token)
                current_token = ""
                current_state = "0"
                
            
            # case 24 ( ( )
            case "24":
                token_list.append(current_token)
                current_token = ""
                current_state = "0"
                
            
            # case 25 ( ) )
            case "25":
                token_list.append(current_token)
                current_token = ""
                current_state = "0"
                
                
            # case 26 ( { )
            case "26":
                token_list.append(current_token)
                current_token = ""
                current_state = "0"
                
            
            # case 27 ( } )
            case "27":
                token_list.append(current_token)
                current_token = ""
                current_state = "0"
                
                
            # case 28 ( , )
            case "28":
                token_list.append(current_token)
                current_token = ""
                current_state = "0"
                
            
            # case 29 ( ; )
            case "29":
                token_list.append(current_token)
                current_token = ""
                current_state = "0"
                
                
            # unidentified case
            case unknown_command:
                print("Invalid input.")
            
    
        # END OF CASE STATEMENTS FOR current_state -------------------------------
    
    # return the token list
    return token_list


def token_classification_table(token_list: list) -> list:
    
    # variables to help get the token_classification_list
    token_clasification_list: list = []
    program_name_flag: bool = False
    constant_type_flag: bool = False
    
    # get the dictionaries of reserved words and symbols
    reserved: list = get_dictionary("Reserved_Words.csv")
    symbols: list = get_dictionary("Reserved_Symbols.csv")
    
    
    # we go through each token 
    for token in token_list:
        
        
        # first we check if the token is a reserved word
        if token in reserved:
            
            # if so we add it to the token_classification_list along with the classification
            token_clasification_list.append((token, reserved[token]))
            
            # the token is 'class' we turn on program_name_flag
            if token == "class":
                program_name_flag = True
                
            # the token is 'const' we turn on constant_type_flag
            if token == "const":
                constant_type_flag = True
            
        
        # if program_name_flag is on we add the token and the clasification to token_classification_list
        # and turn off program_name_flag
        elif program_name_flag:
            token_clasification_list.append((token, "<program name>"))
            program_name_flag = False
    
        
        # we check that constant_type_flag is on and that the token is not a digit or symbol
        # and we add the token and the clasification to token_classification_list
        elif (constant_type_flag and token not in symbols and not token.isdigit()):
            token_clasification_list.append((token, "<constant identifier>"))
            
        
        # if the token is a digit add the token and the clasification to token_classification_list
        elif token.isdigit():
            token_clasification_list.append((token, "<numeric literal>"))
            
            
        # if the token has letters and digits add the token and the clasification to token_classification_list
        elif token.isalnum():
            token_clasification_list.append((token, "<variable identifier>"))
            
            
        # if the token is a reserved symbol
        elif token in symbols:
            
            # if the token is a semicolon we turn off the constant_type_flag
            if token == ";":
                constant_type_flag = False
            
            # we add the token and the clasification to token_classification_list
            token_clasification_list.append((token, symbols[token]))
            
        # otherwise print that the token has no classification 
        else:
            print("No classification for:", token)

    
    # return the token classification list
    return token_clasification_list


def write_to_csv(token_clasification_list: list) -> list:
    
    # create the CSV file
    with open('Token_Classification_Table.csv', 'w', newline='') as csv_file:
            
        # get the header
        header = ["Token", "Classification"]
        
        # set up our writer object
        writer = csv.writer(csv_file)
        
        # write the header to the CSV file
        writer.writerow(header)
        
        # we write each token along with its classification in the CSV file
        for token in token_clasification_list:
            writer.writerow([token[0], token[1]])


def token_symbol_table(token_classification_list: list) -> list:
    
    # some variables to help us
    row_number: int = 1
    temp_counter: int = 1
    address_counter: int = 0
    token_classifications: list = []
    symbol_table: list = []
    variable_list: list = []
    header: list = []
    
    # we get the classifications
    token_classifications = token_classification_list
        
    # we create the symbol table
    with open("Symbol_Table.csv", 'w', newline='') as csv_file:
            
        # we get the header
        header = [" ", "Symbol", "Classification", "Value", "Address", "Segment"]
        
        # we get our writer object
        writer = csv.writer(csv_file)
        
        
        # we get the data needed into the table ----------------------------------------------
        
        
        # we go through every token in the classification table
        for index, token in enumerate(token_classifications):
            
            
            # if the token is classified as the program name
            if token[1] == "<program name>":
                
                # we add the data to symbol_table
                symbol_table.append(list([row_number, token[0], token[1], "", "0", "CS"]))
                
            
            # if the token is a variable or constant identifier and the next token is a '='
            # and the token next to it is a digit
            if ((token[1] == "<variable identifier>" or token[1] == "<constant identifier>") and 
                  token_classifications[index + 1][0] == "=" and 
                  token_classifications[index + 2][0].isdigit()):

                # add the variable to the list
                variable_list.append(token[0])
                
                # we add the data to symbol_table
                symbol_table.append(
                    list([row_number, token[0], token[1], token_classifications[index + 2][0], "0", "DS"])
                )
                
                
            # if the token is a variable identifier and the token is not in variable_list
            elif token[1] == "<variable identifier>" and token[0] not in variable_list:
                variable_list.append(token[0])
                
                # we add the data to symbol_table
                symbol_table.append(list([row_number, token[0], token[1], "", "0", "DS"]))

            
            # if the token is a numeric literal and the token before it is not a '='
            if token[1] == "<numeric literal>" and token_classifications[index - 1][0] != "=":
                
                # we add the data to symbol_table
                symbol_table.append(list([row_number, token[0], token[1], token[0], "0", "DS"]))
                
                
            # if the token is an addition, subtraction, mupltiplication, or division operator
            if (token[1] == "<addition operator>" or 
                token[1] == "<multiplication operator>" or
                token[1] == "<subtraction operator>" or 
                token[1] == "<division operator>" or 
                token[1] == "<equality operator>" or
                token[1] == "<less than operator>" or 
                token[1] == "<greater than operator>" or
                token[1] == "<less than equals operator>" or
                token[1] == "<greater than equals operator>" or 
                token[1] == "<not equals operator>"):
                
                # we add the data to symbol_table
                symbol_table.append(list([row_number, "temp", "", "", "" ""]))

                
        # now we format the symbol table -------------------------------------------------
        
        
        # we check every row for the ones holding 'temp' in the symbol column
        for row in symbol_table:
            if "temp" in row[1]:
                
                # we move the row to the bottom of the list
                symbol_table.append(symbol_table.pop(symbol_table.index(row)))
                
        
        # if a row has 'temp' in the symbol column we modify them by adding numbers 
        # to them in ascending order
        for row in symbol_table:
            if "temp" in row[1]:
                row[1] += str(temp_counter)
                temp_counter += 1
                
                
        # we add the proper row number to each row
        for row in symbol_table:
            row[0] = row_number
            row_number += 1
            
            
        # we fix the address counter to each row
        for row in symbol_table[1:]:
            if row[4] == "0":
                row[4] = address_counter
                address_counter += 2
                
                
        # we insert the header at the top 
        symbol_table.insert(0, header)
        
        
        # finally we write the table to the CSV file
        for row in symbol_table:
            writer.writerow(row)


def lexical_analyzer(file_name: str) -> str:
    
    # we declare the variable for the token list and its classifications, and the symbol table
    token_list: list = []
    token_classifications: list = []
    symbol_table: list = []

    # we save the token list and its classifications to the respective variable 
    token_list = java_0_DFSM(read_file(file_name))
    token_classifications = token_classification_table(token_list)
    
    # we write the token classification and symbol table into a CSV file
    write_to_csv(token_classifications)
    symbol_table = token_symbol_table(token_classifications)
    
    return "Lexical analysis complete."


if __name__ == "__main__":
    lexical_analyzer("java_0_code_text_file.txt") # java_0_code_text_file.txt
    