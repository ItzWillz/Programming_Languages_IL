from sys import *
import itertools

def parser(contents):
    lines = contents.split('\n')

    for line in lines:
        chars = list(line)
        tokens = []
        temp_str = ""
        quote_count = 0
        for char in chars:
            if char == '"' or char == "'":
                quote_count += 1

            if char == " " and quote_count % 2 == 0: #This would mean that the space is not in quotes
                tokens.append(temp_str)
                temp_str = ""
            else:
                temp_str += char
        tokens.append(temp_str)
        # End in Parsing Line

        instruction = tokens[0]
        tokens.remove(instruction)

        # String Output (Cat/Hello World? program) functionality takes string and outputs, string. idk if this qualifies as cat
        if(instruction == "SENTOUT"):
            combined_token = ""
            for token in tokens:
                token = token.replace('"', "", 2)
                token = token.replace("'", "", 2)
                combined_token += token + " "
            print(combined_token)
        
        # Math (multiply program) Functionality
        if(instruction == "EFFECTIVE"):
            result = 0
            if len(tokens) < 3:
                print("Error, expecting an additional argument.")
            elif tokens[0].isdigit == False:
                print("Error, argument following EFFECTIVE is not numeric.")
            elif tokens[2].isdigit == False:
                    print("Error, argument following EFFECTIVE X OPERATION is not numeric.")
            elif tokens[1] == "SUPER":
                result = int(tokens[0]) * int(tokens[2])
                print(result)
            elif tokens[1] == "NOT":
                result = int(tokens[0]) - int(tokens[2])
                print(result)
            elif tokens[1] == "NEUTRAL":
                result = int(tokens[0]) + int(tokens[2])
                print(result)
            elif tokens[1] == "RENOT":
                result = int(tokens[2]) - int(tokens[0])
                print(result)
            elif tokens[1] == "IMMUNE":
                result = int(tokens[0]) / int(tokens[2])
                print(result)
            elif tokens[1] == "REIMMUNE":
                result = int(tokens[2]) / int(tokens[0])
                print(result)
            
        # Reverse String Functionality
        if(instruction == "CATCH"):
            if(len(tokens) > 1):
                print("Error, too many arguments")
                break
            reversed_char = ''
            charlist = list(itertools.chain.from_iterable(tokens))
            for c in charlist:
                reversed_char = c + reversed_char
            print(reversed_char)
        
        # String Output (Hello World program) functionality
        if(instruction == "RELEASE"):
            if(tokens.count != 0):
                print("Too many additional arguments for 'RELEASE'")
            else:
                print("Hello World!")

        # Reapeat String Output functionality
        if(instruction == "PARTY"):
            combined_token = ""
            for token in tokens:
                if(token.isdigit()):
                    val = int(token)
                    while(val != 0):
                        print(combined_token)
                        val -= 1
                else:
                    token = token.replace('"', "", 2)
                    token = token.replace("'", "", 2)
                    combined_token += token + " "

            


def parse(file):
    contents = open(file, "r").read()
    parser(contents)

parse(argv[1])

