import
# program, clause-list, clause, query 
# bowen

#global
global lex_index, token, nextChar, Lexeme, NextToken, File, error, charClass
File = None
number_of_lines = -1
token = -1
Lexeme = []
error = []
nextChar = ''


#character classes
UPPER_CHAR, LOWER_CHAR, DIGIT, SPECIAL, UNKNOWN= 0,1,2,3,99

#token codes
ADD_OP, SUB_OP, MULT_OP, DIV_OP = 21,22,23,24
BACK_SLASH, CIRCUMFLEX, TILDE, COLON, PERIOD =25,26,27,28,29
QUESTION, SPACE, HASHTAG, DOLLAR, AMPERSAND = 30,31,32,33,34,35
LEFT_PAREN, RIGHT_PAREN = 36, 37
QUOTATION = 38
EOF = -1

#main driver
def main():
    global File
    i = 1
    while()
        File = open(str(i)+'1.txt', 'r')
        get_char()

        while(NextToken != EOF):
            Lex()

        #print error
        #reset the variables

# Lookup() - function to lookup operators and return the token
def lookup(char):

    global next_token
    if char == "(":
        add_char()
        next_token = LEFT_PAREN
    elif char == ")":
        add_char()
        next_token = RIGHT_PAREN
    elif char == "+":
        add_char()
        next_token = ADD_OP
    elif char == "-":
        add_char()
        next_token = SUB_OP
    elif char == "*":
        add_char()
        next_token = MULT_OP
    elif char == "/":
        add_char()
        next_token = DIV_OP
    elif char == "\\":
        add_char()
        next_token = BACK_SLASH
    elif char == "^":
        add_char()
        next_token = CIRCUMFLEX
    elif char == "~":
        add_char()
        next_token = TILDE
    elif char == ":":
        add_char()
        next_token = COLON
    elif char == ".":
        add_char()
        next_token = PERIOD
    elif char == "?":
        add_char()
        next_token = QUESTION
    elif char == " ":
        add_char()
        next_token = SPACE
    elif char == "#":
        add_char()
        next_token = HASHTAG
    elif char == "$":
        add_char()
        next_token = DOLLAR
    elif char == "&":
        add_char()
        next_token = AMPERSAND
    elif char == '\'':
        add_char()
        next_token = QUOTATION
    else:
        add_char()
        next_token = EOF

    return next_token

#add next char to lexeme
def add_char():
    Lexeme.append(nextChar)

#to get the next character of input and determine its character and class
def get_char():
    global nextChar, charClass
    nextChar = File.read(1)
    if nextChar != EOF:
        if re.match()
            charClass = LETTER
        elif nextChar.isdigit():
            charClass = DIGIT
        else:
            charClass = UNKNOWN
    else:
        charClass = EOF



# Lex() - lexical analyzer
#numeral, atom, variable
def Lex():
    NextToken = (lex, token)
   while char.isdigit():
       lex+=char
       token = 'numeral'
       NextToken = (lex, token)
       char = next(Next)
       break

    if char.islower():
        lex+=char
        token = ''



#---------Syntax analysis-----------

# <program> -> <clause-list> <query> | <query>

def Program():
    global error
    if NextToken == QUESTION:
        Query()
    elif NextToken == LOWER_CHAR:
        ClauseList()
        if NextToken == QUESTION:
            Query()
        else:
            print("Clause_List must come before Query", number_of_lines,token))
            get_char()
            Lex()            
            
# <clause-list> -> <clause> | <clause> <clause-list>

def Clause_List():
    global error
    Clause()
    if NextToken == QUOTATION:
        Clause_List()
        
# <clause> -> <predicate> . | <predicate> :- <predicate-list> .

def Clause():
    global error
    Predicate()

    if NextToken == PERIOD:
        Lex()
    elif NextToken == COLON:
        Lex()
        if NextToken == DASH:
            lex()
            Predicate_List()
            if NextToken == PERIOD:
                lex()
            else:
                print("Missing PERIOD", number_of_lines,token)
                get_char()
                Lex()
        else:
            print("Missing COLON", number_of_lines,token)
            get_char()
            Lex()
    else:
        print("Invalid Clause", number_of_lines,token)
        get_char()
        Lex()
        
# <query> -> ?- <predicate-list> .

def Query():
    global error
    if NextToken == QUESTION:
        Lex()
        if NextToken == DASH:
            Lex()
            Predicate_List()
            if NextToken == PERIOD:
                Lex()
            else:
                print("Missing PERIOD",number_of_lines,token)
                get_char()
                Lex()
        else:
            print("Missing DASH", number_of_lines,token)
            get_char()
            Lex()
    else:
        print("Missing QUESTION MARK", number_of_lines,token)
        get_char()
        lex()

# <predicate-list> -> <predicate> | <predicate> , <predicate-list>

def PredicateList():
    Predicate()
    if NextToken == COMMA:
        Lex()
        PredicateList()
        
# <predicate> -> <atom> | <atom> ( <term-list> )

def Predicate():
    atom_func()
    if NextToken == LEFT_PAREN:
        Lex()
        TermList()
        if NextToken == RIGHT_PAREN:
            Lex()
        else:
            print("Missing RIGHT Parenthesis")
            get_char()
            Lex()
            
# <term-list> -> <term> | <term> , <term-list>

def TermList():
    Term()
    if NextToken == COMMA:
        Lex()
        TermList()
        
# <term> -> <atom> | <variable> | <structure> | <numeral>

def Term():
    if NextToken == DIGIT:
        numeral()
    elif NextToken == UPPER_CHAR:
        variable()
    elif NextToken == LOWER_CHAR or quotation:
        structure()
    else:
        print("Invalid Term")
        Lex()

# <structure> -> <atom> ( <term-list> )


# <atom> -> <small-atom> | ' <string> '

# <small-atom> -> <lowercase-char> | <lowercase-char> <character-list>

# <variable> -> <uppercase-char> | <uppercase-char> <character-list>

# <character-list> -> <alphanumeric> | <alphanumeric> <character-list>

# <alphanumeric> -> <lowercase-char> | <uppercase-char> | <digit>

# <numeral> -> <digit> | <digit> <numeral>


# <string> -> <character> | <character> <string>

# <character> -> <alphanumeric> | <special>
