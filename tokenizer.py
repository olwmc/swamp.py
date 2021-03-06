class Token(object):
    def __init__(self, token_type, value):
        """Initialize with token type and value"""
        self.token_type = token_type
        self.value = value
    
    def __eq__(self, other):
        return self.token_type == other.token_type and self.value == other.value
    def __str__(self):
        """String representation of the token"""
        return str(self.token_type) + "  |  " + str(self.value)


def get_token_type(string, types):
    """Match the token with it's type"""
    # Get the token type from the dictionary
    token_type = types.get(string)

    # If there's nothing, it's either an num literal or an identifier
    if token_type == None:
        try:
            float(string)
            return "NUM_LITERAL"
        except:
            return "IDENTIFIER"
    
    else:
        return token_type

def clean(arr):
    """Clean excess whitespace out of array"""
    for i in range(len(arr)):
         if(arr[i].isspace()):
             arr.pop(i)
             
def tokenize(program):
    """Splits the input program into a series of tokens"""
    program = program.split()
    clean(program)

    tokens = []
    inComment = False

    for string in program:
        # Check for (descriptor or comment) 
        if string[0] == "(":
            inComment = True
        elif string[-1] == ")":
            inComment = False
            continue
        
        # Otherwhise just make the token
        if not inComment:
            tokens.append(Token(get_token_type(string, types), string))  
    return tokens


types = {
       # Operations
       "+"         : "OP",                 "-"         : "OP",
       "/"         : "OP",                 "*"         : "OP",
       "dup"       : "OP",                 "drop"      : "OP",
       "swap"      : "OP",                 "over"      : "OP",
       "rot"       : "OP",                 "?"         : "OP",
       "emit"      : "OP",                 "cr"        : "OP",
       "="         : "OP",                 "."         : "OP", 
       ">"         : "OP",                 "<"         : "OP",
       "and"       : "OP",                 "or"        : "OP",
       "invert"    : "OP",                 "mod"       : "OP",
       "random"    : "OP",

       # Numeric input
       "input"       : "OP",

       # Conditional
       "if"        : "IF",                 "then"      : "THEN",
       "else"      : "ELSE",
       
       # Loops
       "do"        : "DO",                 "loop"      : "LOOP",
       "begin"     : "BEGIN",              "until"     : "UNTIL",

       # Variables and memory
       "variable"  : "VAR_DECLARATION",    "constant"  : "CONST_DECLARATION",
       "cells"     : "CELLS",              "alloc"     : "ALLOC",
       "!"         : "STORE_MEMORY",       "@"         : "FETCH_MEMORY",

       # Function declaration
       ":"         : "DEF_START",          ";"         : "DEF_END",
       
       # String output
       ".\""       : "QUOTE",
       
       # Import statement
       "import"    : "IMPORT",
       
       # Clear stack
       "clear"     : "OP",
       
       # Save results
       "save"      : "OP",

       # Exit
       "exit"      : "OP"
}