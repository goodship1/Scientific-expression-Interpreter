import ply.lex  as scanner
key_words = {"log":"LOG","cos":"COS","sin":"SIN","tan":"TAN","root":"ROOT","e":"E"}
tokens = ["equalequal","factorial","range","sumto","pow","equal","mod","plus","minus","times","integer","lessthan","greaterthan","divide","greaterthanequal","lessthanequal","open","closed"]+list(key_words.values())

def t_integer(t):
        #rules for lexing integers 
        r'\d+'
        t.type = key_words.get(int(t.value),"integer")
        return t


def t_range(t):
    r'\..'
    t.type = key_words.get(t.value,"range")
    return t

def t_sum_to(t):
    r'~'
    t.type = key_words.get(t.value,"sumto")
    return t


def t_lessthan(t):
        #token rule for lessthan
        r'\<'
        t.type = key_words.get(t.value,"lessthan")
        return t

t_ignore  = ' \t'

def t_greaterthanequal(t):
    r'\>='
    t.type =  key_words.get(t.value,"greaterthanequal")
    return t

def t_lessthanequal(t):
    r'\<='
    t.type = key_words.get(t.value,"lessthanequal")
    return t

def t_equalequal(t):
    r'=='
    t.type = key_words.get(t.value,"equal")
    return t

def t_mod(t):
    r'%'
    t.type = key_words.get(t.value,"mod")
    return t

def t_greaterthan(t):
        #token rule for greaterthan
        r'\>'
        t.type = key_words.get(t.value,"greaterthan")
        return t

def t_power(t):
    r'\^'
    t.type =  key_words.get(t.value,"pow")
    return t


def t_divide(t):
        #token rule for divide 
        r'\/'
        t.type = key_words.get(t.value,"divide")
        return t


def t_newline(t):
     r'\n+'
     t.lexer.lineno += len(t.value)


def t_error(t):
     print("Illegal character '%s'" % t.value[0])
     t.lexer.skip(1)
	

def t_times(t):
        #token rule for times 
        r'\*'
        t.type = key_words.get(t.value,"times")
        return t


def t_minus(t):
        #token rule for minus 
        r'\-'
        t.type = key_words.get(t.value,"minus")
        return t


def t_factorial(t):
    r'!'
    t.type =  key_words.get(t.value,"factorial")
    return t


def t_plus(t):
        #token rule for plus 
        r'\+'
        t.type = key_words.get(t.value,"plus")
        return t

def t_opening(t):
    r'\('
    t.type = key_words.get(t.value,"open")
    return t

def t_closing(t):
    r'\)'
    t.type = key_words.get(t.value,"closed")
    return t

def t_log(t):
        #Token rule for the Keyword log
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = key_words.get(t.value,"log")
        return t

def t_cos(t):
    #Token rule for the Keyword cos
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = key_words.get(t.value,"cos")
    return t

def t_sin(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type  = key_words.get(t.value,"sin")
    return t

def t_tan(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = key_words.get(t.value,"tan")
    return t

def t_root(p):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = key_words.get(t.value,"root")
    return t

def t_e(p):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = key_words.get(t.value,"e")
    return t 


scanner = scanner.lex()
