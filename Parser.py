from Lexer import tokens
import ply.yacc as yacc
from AST import Node




def p_term_plus(p):
    'expr : term plus term'
    p[0] = Node("add",[p[1],p[3]],p[2])



def p_cos_term(p):
    'expr : COS opening term closing'
    p[0] =  Node("cos",[p[3],p[3]],"cos")

def p_sin_term(p):
    'expr : SIN opening term closing'
    p[0] = Node("sin",[p[3],p[3]],"sin")


def p_tan_term(p):
    'expr : TAN opening term closing'
    p[0] =  Node("tan",[p[3],p[3]],"tan")


def p_root_term(p):
    'expr : ROOT opening term closing'
    p[0] =  Node("root",[p[3],2],"root")

def p_root_term_term(p):
    'expr : ROOT opening term term closing'
    p[0]  = Node("root",[p[3],p[4]],"root")



def p_trig_term(p):
    '''expr : COS opening term closing plus term
            | SIN opening term closing plus term
            | TAN opening term closing plus term
            | COS opening term closing minus term
            | SIN opening term closing minus term
            | TAN opening term closing minus term
            | SIN opening term closing times term
            | COS opening term closing times term
            | TAN opening term closing times term
            | term minus COS opening term closing
            | term plus  COS opening term closing
            | term times COS opening term closing
            | term divide COS opening term closing
            | term minus SIN opening term closing
            | term plus SIN opening term closing
            | term times SIN opening term closing
            | term  divide SIN opening term closing
            | term plus TAN opening term closing 
            | term minus TAN opening term closing
            | term times TAN opening term closing
            | term divide TAN opening term closing
            
            '''
    if p[1] == "cos" and p[5] == "+":
            p[0]  = Node("cosplusterm",[p[3],p[6]],p[5])
    if p[1] == "sin" and p[5] == "+":
            p[0]  = Node("sinplusterm",[p[3],p[6]],p[5])
    if p[1]  == "tan" and p[5] == "+":
        p[0] =  Node("tanplusterm",[p[3],p[6]],p[5])
    if p[1]  == "cos"  and p[5] == '-':
	     p[0] = Node("cosminusterm",[p[3],p[6]],p[5])
    if p[1] == "cos" and p[5] == "*":
	      p[0] = Node("costimesterm",[p[3],p[6]],p[5])
    if p[1] == "cos" and p[5] == "/":
	     p[0] =  Node("cosdivideterm",[p[3],p[6]],p[5])
    if p[1] == "sin" and p[5] == "-":
	    p[0] =  Node("sinminusterm",[p[3],p[6]],p[5])
    if p[1] == "sin" and p[5] == "*":
	    p[0] =  Node("sintimesterm",[p[3],p[6]],p[5])
    if p[1] == "sin" and p[5] == "/":
       p[0] = Node("sindivideterm",[p[3],p[6]],p[5])
    if p[1] == "tan" and p[5] == "-":
       p[0] = Node("tanminusterm",[p[3],p[6]],p[5])
    if p[1] == "tan" and p[5] == "*":
	    p[0] = Node("tantimesterm",[p[3],p[6]],p[5])
    if p[1] == "tan" and p[5] == "/":
	    p[0] = Node("tandivideterm",[p[3],p[6]],p[5])
    if p[2] == "+" and p[3] == "cos":
        p[0] = Node("termpluscos",[p[1],p[5]],p[2])
    if p[2] == "-" and p[3] == "cos":
        p[0] = Node("termminuscos",[p[1],p[5]],p[2])
    if p[2] == "*" and p[3] == "cos":
        p[0] =  Node("termtimescos",[p[1],p[5]],p[2])

    if p[2] == "/" and p[3] == "cos":
        p[0] =  Node("termdividecos",[p[1],p[5]],p[2])
    if p[2] == "+" and p[3] == "sin":
        p[0] = Node("termplussin",[p[1],p[5]],p[2])
    if p[2] == "-" and p[3] == "sin":
        p[0] =  Node("termminussin",[p[1],p[5]],p[2])

    if p[2] == "*" and p[3] == "sin":
        p[0] = Node("termtimessin",[p[1],p[5]],p[2])
    if p[2] == "+" and p[3] == "tan":
        p[0] =  Node("termaddtan",[p[1],p[5]],p[2])
    if p[2]  == "-" and p[3] == "tan":
        p[0] =  Node("termminustan",[p[1],p[5]],p[2])
    if p[2] == "/" and p[3] == "tan":
        p[0] =  Node("termdividetan",[p[1],p[5]],p[2])
    if p[2] == "/" and p[3] == "sin":
        p[0] = Node("termdividesin",[p[1],p[5]],p[2])
    if p[2] == "*"  and p[3] == "tan":
        p[0] = Node("termtimestan",[p[1],p[5]],p[2])





def p_trig_add_trig(p):
    '''expr : COS opening term closing plus COS opening term closing
            | SIN opening term closing plus SIN opening term closing
            | TAN opening term closing plus TAN opening term closing
            | COS opening term closing plus SIN opening term closing
            | COS opening term closing plus TAN opening term closing
            | SIN opening term closing plus COS opening term closing
            | SIN opening term closing plus TAN opening term closing
            | TAN opening term closing plus SIN opening term closing
            | TAN opening term closing plus COS opening term closing
            '''
    if p[1] == "cos" and p[6] == "cos":
         p[0] = Node("cospluscos",[p[3],p[8]],p[5])
    if p[1] == "sin" and p[6] == "sin":
        p[0] = Node("sinplussin",[p[3],p[8]],p[5])
    if p[1] == "sin" and p[6] == "cos":
        p[0] = Node("sinpluscos",[p[3],p[8]],p[5])
    if p[1] == "sin" and p[6] == "tan":
        p[0] = Node("sinplustan",[p[3],p[8]],p[5])
    if p[1] == "cos" and p[6] == "tan":
        p[0] =  Node("cosplustan",[p[3],p[8]],p[5])
    if p[1] == "tan" and p[6] == "tan":
        p[0] =  Node("tanplustan",[p[3],p[8]],p[5])
    if p[1]  == "tan" and p[6] == "cos":
        p[0] = Node("tanpluscos",[p[3],p[8]],p[5])
    if p[1]  == "tan" and p[6] == "sin":
        p[0] =  Node("tanplussin",[p[3],p[8]],p[5])


def p_trig_minus_trig(p):
    '''expr : COS opening term closing minus COS opening term closing
            | SIN opening term closing minus SIN opening term closing
            | TAN opening term closing minus TAN opening term closing
            | COS opening term closing minus SIN opening term closing
            | COS opening term closing minus TAN opening term closing
            | SIN opening term closing minus COS opening term closing
            | SIN opening term closing minus TAN opening term closing
            | TAN opening term closing minus SIN opening term closing
            | TAN opening term closing minus COS opening term closing
            '''
    if p[1] == "cos" and p[6] == "cos":
         p[0] = Node("cosminuscos",[p[3],p[8]],p[5])
    if p[1] == "sin" and p[6] == "sin":
        p[0] = Node("sinminussin",[p[3],p[8]],p[5])
    if p[1] == "sin" and p[6] == "cos":
        p[0] = Node("sinminuscos",[p[3],p[8]],p[5])
    if p[1] == "sin" and p[6] == "tan":
        p[0] = Node("sinminustan",[p[3],p[8]],p[5])
    if p[1] == "cos" and p[6] == "tan":
        p[0] =  Node("cosminustan",[p[3],p[8]],p[5])
    if p[1] == "tan" and p[6] == "tan":
        p[0] =  Node("tanminustan",[p[3],p[8]],p[5])
    if p[1]  == "tan" and p[6] == "cos":
        p[0] = Node("taninuscos",[p[3],p[8]],p[5])
    if p[1]  == "tan" and p[6] == "sin":
        p[0] =  Node("tanminussin",[p[3],p[8]],p[5])


def p_trig_times_trig(p):
    '''expr : COS opening term closing times COS opening term closing
            | SIN opening term closing times SIN opening term closing
            | TAN opening term closing times TAN opening term closing
            | COS opening term closing times SIN opening term closing
            | COS opening term closing times TAN opening term closing
            | SIN opening term closing times COS opening term closing
            | SIN opening term closing times TAN opening term closing
            | TAN opening term closing times SIN opening term closing
            | TAN opening term closing times COS opening term closing
            '''
    if p[1] == "cos" and p[6] == "cos":
         p[0] = Node("costimescos",[p[3],p[8]],p[5])
    if p[1] == "sin" and p[6] == "sin":
        p[0] = Node("sintimessin",[p[3],p[8]],p[5])
    if p[1] == "sin" and p[6] == "cos":
        p[0] = Node("sintimescos",[p[3],p[8]],p[5])
    if p[1] == "sin" and p[6] == "tan":
        p[0] = Node("sintimesan",[p[3],p[8]],p[5])
    if p[1] == "cos" and p[6] == "tan":
        p[0] =  Node("costimestan",[p[3],p[8]],p[5])
    if p[1] == "tan" and p[6] == "tan":
        p[0] =  Node("tantimestan",[p[3],p[8]],p[5])
    if p[1]  == "tan" and p[6] == "cos":
        p[0] = Node("tantimescos",[p[3],p[8]],p[5])
    if p[1]  == "tan" and p[6] == "sin":
        p[0] =  Node("tantimessin",[p[3],p[8]],p[5])



def p_trig_divide_trig(p):
    '''expr : COS opening term closing divide COS opening term closing
            | SIN opening term closing divide SIN opening term closing
            | TAN opening term closing divide TAN opening term closing
            | COS opening term closing divide SIN opening term closing
            | COS opening term closing divide TAN opening term closing
            | SIN opening term closing divide COS opening term closing
            | SIN opening term closing divide TAN opening term closing
            | TAN opening term closing divide SIN opening term closing
            | TAN opening term closing divide COS opening term closing
            '''
    if p[1] == "cos" and p[5] == "/" and p[6] == "cos":
         p[0] = Node("cosdividecos",[p[3],p[8]],p[5])
    if p[1] == "sin" and p[6] == "sin" and p[5] == '/':
        p[0] = Node("sindividesin",[p[3],p[8]],p[5])
    if p[1] == "sin" and p[6] == "cos" and p[5] == '/':
        p[0] = Node("sindividecos",[p[3],p[8]],p[5])
    if p[1] == "sin" and p[6] == "tan" and p[5] =='/':
        p[0] = Node("sindividetan",[p[3],p[8]],p[5])
    if p[1] == "cos" and p[6] == "tan" and p[5] == '/':
        p[0] =  Node("cosdividetan",[p[3],p[8]],p[5])
    if p[1] == "tan" and p[6] == "tan" and p[5] == '/':
        p[0] =  Node("tandividetan",[p[3],p[8]],p[5])
    if p[1]  == "tan" and p[6] == "cos" and p[5] == '/':
        p[0] = Node("tandividecos",[p[3],p[8]],p[5])
    if p[1]  == "tan" and p[6] == "sin" and p[5] == '/':
        p[0] =  Node("tandividesin",[p[3],p[8]],p[5])



def p_e_power(p):
    'expr : E pow term'
    p[0] = Node("pow",["e",p[3]],p[2])


def p_mod_term(p):
    'expr : term mod term'
    p[0] = Node("mod",[p[1],p[3]],p[2])


def p_sum_to_term(p):
    'expr  : term sumto term'
    p[0] =  Node("sumto",[p[1],p[3]],p[2])


def p_log_term_term(p):
    'expr : LOG opening term term closing'
    p[0] = Node("log",[p[3],p[4]],"log")

def p_log_term(p):
    'expr : LOG opening term closing'
    p[0] = Node("log",[p[3],str(10)],p[1])

def p_term_minus(p):
    'expr : term minus term'
    p[0]  = Node("minus",[p[1],p[3]],p[2])

def p_term_less_term(p):
    'expr : term lessthan  term'
    p[0] = Node("lessthan",[p[1],p[3]],p[2])


def p_term_greater_term(p):
    'expr : term greaterthan term'
    p[0] =  Node("greaterthan",[p[1],p[3]],p[2])

def p_term_power_term(p):
    'expr : term pow term'
    p[0] = Node("pow",[p[1],p[3]],p[2])

def p_term_equal_term(p):
    'expr : term equal term'
    p[0] =  Node("equal",[p[1],p[3]],p[2])

def p_term_greaterthanequal_term(p):
    'expr : term greaterthanequal term'
    p[0] = Node("greaterthanequal",[p[1],p[3]],p[2])

def p_term_lessthanequal_term(p):
    'expr : term lessthanequal term'
    p[0] =  Node("lessthanequal",[p[1],p[3]],p[2])
    

def p_term_times(p):
    'expr : term times term'
    p[0] = Node("times",[p[1],p[3]],p[2])


def p_term_div_term(p):
    'expr : term divide term'
    p[0] =  Node("divide",[p[1],p[3]],p[2])




def p_range(p):
    'expr : term range term'
    p[0] = Node("range",[p[1],p[3]],p[2])


def p_factorial(p):
    'expr : term factorial'
    p[0] = Node("factorial",[p[1],p[2]],p[2])



def p_term(p):
    'term : integer'
    p[0] = p[1]

def p_error(p):
    print("syntax error")
   
def p_opening(p):
    'opening : open'
    p[0] = p[1]



def p_closing(p):
    'closing : closed'
    p[0] = p[1]

parser = yacc.yacc()

