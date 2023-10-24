# Input: a string that might have multiple extra white spaces:
# "    Aditya went to       Padua    "
# Output: "Aditya went to Padua"


def remove_extra_whitespaces(line: str) -> str:
    # c.isalpha() means if c is an actual character (alphanumeric) ELSE whitespace
    # IDEA is to capture all possible cases: there are two va;ues for state - 0 or 1 (2 values),
    # similarly there are two values for c - either it's a character or a whitespace (2 values):
    # TOTAL: 2 x 2 values (4 conditions or states to capture)
    # Notice the 4 case statements checking for these 4 conditions.
    # for each iteration ONLY 1 condition will be true/
    # When we reach that condition we DO WORK
    STATE = 0  # state is one when you have seen a character (previous character) else it's 0 (previous char was whitespace)
    new_l = ""
    for c in line:
        match c:
            case x if c.isalpha() and STATE == 0:
                STATE = 1
                new_l += x
            case x if not c.isalpha() and STATE == 1:
                STATE = 0
                new_l += x
            case x if not c.isalpha() and STATE == 0:
                pass
            case x if c.isalpha() and STATE == 1:
                new_l += x
            case _:
                pass
    return new_l

# NOW write the same program using if else

# def RemoveExtraWhiteSpaces(line: str) -> str:
#     # Write the body of the function below
#     if line == " " or line.find(" ") == -1:
#         return line
    





    

def RemoveExtraWhiteSpace(line: str):
    # Write the body of the function below
    s = ""
    if line == " ":
        s = line
        return s
    else:
        if line[0] != " ":
            s = s+ line[0]
        for i in range(1,(len(line)-1),1):
            if line[i] != " ":
                s = s + line[i]
            else:
                 if line[i] == " " and (line[i+1] != " " and line[i-1] != " "):
                    s = s + line[i]
        if line[len(line)-1] != " ":
         s = s+ line[len(line)-1]    
        return s
    # new_l = ""
    # for idx, elem in enumerate(line):
    #     match elem:
    #         case x if idx == 0 and not elem.isalnum():
    #             pass
    #         case x if idx >= 1 and not elem.isalnum() and not (line[idx-1]).isalnum():
    #             pass
    #         case x if idx >= 1 and not elem.isalnum() and (line[idx-1]).isalnum():
    #             new_l += x
    #         case x if idx >= 1 and elem.isalnum() and (line[idx-1]).isalnum():
    #             new_l += x
    #         case _:
    #             new_l += elem 
    # return new_l



if __name__ == "__main__":
    IN: str = "    Aditya went to       Padua    "
    print(remove_extra_whitespaces(IN))
    print(remove_extra_whitespaces("     "))                  
    print(RemoveExtraWhiteSpace("  aditya is a funny boy  "))                 
    print(remove_extra_whitespaces("  aditya is a funny boy  "))
    print(RemoveExtraWhiteSpace("aditya"))

        
    





    
