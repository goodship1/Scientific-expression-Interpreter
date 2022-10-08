from Parser import parser
from Lexer import scanner
from AST import Node
import sys
import math
from Typechecker import Typechecker

class Interperter(object):
   
    def __init__(self):
        self.program = {}
        self.number_of_lines = 0
        self.typechecker =  Typechecker()

    def read_file(self):
        s = sys.argv
        open_file = s[1]
        with open(open_file) as reader:
            for line_num,line in enumerate(reader):
                if line!="\n":
                    parse = parser.parse(line.strip())
                    self.program[line_num] = (parse,line_num)
                    line_num+1
                    self.number_number_lines = line_num
    
    def ast_visitor_add(self,add):
        return int(add[0]) + int(add[1])

    def ast_visitor_minus(self,minus):
        return int(minus[0]) - int(minus[1])

    def ast_visitor_times(self,times):
        return int(times[0]) * int(times[1])

    def ast_visitor_power(self,power):
        base = int(power[0])
        raise_to = int(power[1])
        result = None
        if raise_to == 0:
            return 1
        count = 0
        while True:
                result = base_power * base_power
                count+=1
                if count == raise_to:
                    break
        return result

        
    def ast_visitor_lessthanequal(self,lessthanequal):
        return int(lessthanequal[0]) <= int(lessthanequal[1])

    def ast_visitor_greaterthanequal(self,greaterthanequal):
        return int(greaterthanequal[0]) >= int(greaterthanequal[1])


    def ast_visitor_range(self,range_to):
        start = int(range_to[0])
        end = int(range_to[1])
        store = []
        for add_to in range(start,end+1):
            store.append(add_to)
        return store

    
    
    def ast_visitor_divide(self,divide):
        return int(divide[0]) / int(divide[1])


    def ast_visitor_sumto(self,sumto):
        start = int(sumto[0])
        end = int(sumto[1])
        store = 0
        for increment in range(start,end+1):
            store+=increment
        return store

    def ast_visitor_factorial(self,factorial):
        factor = int(factorial[0])
        result = 1
        if factor > 1:
            for calculate in range(1,factor+1):
                result = result * calculate
            return result
 

    def ast_visitor_power(self,power):
        if power[0] != "e": 
            base = int(power[0])
            raiseto =  int(power[1])
            return pow(base,raiseto)
        elif power[0] == "e":
            e = math.e
            return pow(e,int(power[1]))


    def ast_visitor_sin(self,trig):
       compute = int(trig[0])
       return math.sin(compute)

    
    def ast_visitor_root(self,root):
         if int(root[1]) == 2:
               convert =  int(root[0])
               return math.sqrt(convert)
         if int(root[1]) > 2:
                 return math.exp(math.log(int(root[0]))/int(root[1]))

    def ast_visitor_log(self,log):
        base = int(log[1])
        argument =  int(log[0])

        return math.log(argument,base)
    
    def ast_visitor_trig_minus_term(self,op,trig):
        term =  int(trig[0])
        arg  = int(trig[1])
        
        if op == "cosminusterm":
            return math.cos(arg) - term
        if op ==  "sinminusterm":
            return math.sin(arg) - term
        if op == "tanminusterm":
            return math.tan(arg) - term
        
    def ast_visitor_trig_add_trig(self,op,trig):
        arg_one =  int(trig[0])
        arg_two =  int(trig[1])
        if op == "cospluscos":
            return math.cos(arg_one) + math.cos(arg_two)
        if op == "sinplussin":
            return math.sin(arg_one) + math.sin(arg_two)
        if op == "sinpluscos" or op == "cosplussin":
            return math.sin(arg_one) + math.cos(arg_two)
        if op == "tanplussin" or op == "sinplustan":
            return math.tan(arg_one) + math.sin(arg_two)
        if op == "cosplustan" or op == "tanpluscos":
            return math.cos(arg_one) + math.tan(arg_two)
        if op == "tanplustan":
            return math.tan(arg_one) + math.tan(arg_two)


            

    def ast_visitor_trig_minus_trig(self,op,trig):
        arg_one =  int(arg_one)
        arg_two = int(arg_two)
        if op == "cosminuscos":
            return math.cos(arg_one) - math.cos(arg_two)
        if op == "sinminusin":
            return math.sin(arg_one) - math.sin(arg_two)
        if op == "tanminustan":
            return math.tan(arg_one) - math.tan(arg_two)
        if op == "cosminussin":
            return math.cos(arg_one) - math,sin(arg_two)
        if op == "sinminuscos":
            return math.sin(arg_one) - math.sin(arg_two)
        if op == "tanminustan":
            return math.tan(arg_one) - math.tan(arg_two)
        if op == "tanminussin":
            return math.tan(arg_one) - math.tan(arg_two)
        if op == "tanminuscos":
            return math.tan(arg_one) - math.cos(arg_two)


    def ast_visitor_trig_times_trig(self,op,trig):
        
        arg_one = int(trig[0])
        arg_two =  int(trig[1])
        
        if op == "costimescos":
            return math.cos(arg_one) * math.cos(arg_two)
        if op == "sintimessin":
            return math.sin(arg_one) * math.sin(arg_two)
        if op == "costimessin" or op == "sintimescos":
            return math.cos(arg_one) * math.sin(arg_two)
        if op == "tantimescos" or op == "costimestan":
            return math.cos(arg_one) * math.sin(arg_two)
        if op == "sintimescos" or op == "costimesin":
            return math.sin(arg_one) * math.cos(arg_two)
        if op =="tantimestan":
            return math.tan(arg_one) * math.tan(arg_one)




    def ast_visitor_term_divide_trig(self,op,trig):
        term = int(trig[0])
        arg = int(trig[1])
        if op == "termdividecos":
            return term /  math.cos(arg)
        if op == "termdividesin":
            return term / math.sin(arg)
        if op == "termdividetan":
            return term / math.tan(arg)
   


            

    def ast_visitor_trig_term(self,op,trig):
        term = int(trig[0])
        arg =  int(trig[1])
        if op == "termpluscos" or op == "cosplusterm":
            return term + math.cos(arg)
        if op == "termplussin" or op == "sinplusterm":
            return term +  math.sin(arg)
        if op == "termplustan" or op == "tanplusterm":
            return term + math.tan(arg)
        if op == "termminuscos":
            return term -  math.cos(arg)
        if op == "termminussin":
            return term - math.sin(arg)
        if op == "termminustan":
            return term -  math.tan(arg)
        if op == "termtimescos" or op == "costimesterm":
            return term * math.cos(arg)
        if op == "termtimessin" or op == "sinttimessin":
            return term * math.sin(arg)
        if op == "termtimestan" or op == "tantimesterm":
            return term * math.tan(arg)
        if op == "termaddtan" or op == "tanplusterm":
            return term + math.tan(arg)
        if op  == "termminustan":
            return term - math.tan(arg)
       




    def ast_visitor_cos(self,trig):
       compute = int(trig[0])
       return math.cos(compute)
       

    def ast_visitor_tan(self,trig):
       compute =  int(trig[0])
       return math.tan(compute)


    def ast_visitor_mod(self,mod):
        return int(mod[0]) % int(mod[1])
    
    def ast_visitor_greaterthan(self,greaterthan):
        return int(greaterthan[0]) > int(greaterthan[1])

    def ast_visitor_lessthan(self,lessthan):
        return int(lessthan[0]) < int(lessthan[1])

    def ast_visitor_equal(self,equal):
        return int(equal[0]) == int(equal[1])
    
    
    def vistingastnodes(self):
        program = []
        check = self.error_checking()
        if check == True:
            for values in self.program.values():
                if values[0].op == "add":
                    add = self.ast_visitor_add(values[0].child)
                    program.append(add)
                 
                
                if values[0].op == "termpluscos" or values[0].op == "cosplusterm":
                    termpluscos = self.ast_visitor_trig_term(values[0].op,values[0].child)
                    program.append(termpluscos)
                if values[0].op == "termminuscos":
                    termminuscos = self.ast_visitor_trig_term(values[0].op,values[0].child)
                    program.append(termminuscos)
                if values[0].op == "termtimescos" or values[0].op == "costimesterm":
                    termtimescos  = self.ast_visitor_trig_term(values[0].op,values[0].child)
                    program.append(termtimescos)
                if values[0].op == "termplussin" or values[0].op == "sinplusterm":
                    termplussin  = self.ast_visitor_trig_term(values[0].op,values[0].child)
                    program.append(termplussin)
                if values[0].op == "termminussin":
                    termminussin =  self.ast_visitor_trig_term(values[0].op,values[0].child)
                    program.append(termminussin)

                if values[0].op == "termtimessin" or values[0].op == "sintimesterm":
                    termtimessin = self.ast_visitor_trig_term(values[0].op,values[0].child)
                    program.append(termtimessin)
                

                if values[0].op == "cospluscos":
                    cospluscos  = self.ast_visitor_trig_add_trig(values[0].op,values[0].child)
                    program.append(cospluscos)

                if values[0].op == "sinplussin":
                    sinplussin = self.ast_visitor_trig_add_trig(values[0].op,values[0].child)
                    program.append(sinplussin)
                
                if values[0].op == "sinpluscos" or values[0].op == "cosplussin":
                    sinpluscos  = self.ast_visitor_trig_add_trig(values[0].op,values[0].child)
                    program.append(sinpluscos)
                
                if values[0].op == "tanplussin" or values[0].op == "sinplustan":
                    tanplussin =  self.ast_visitor_trig_add_trig(values[0].op,values[0].child)
                    program.append(tanplussin)

                if values[0].op == "tanplustan":
                    sinplussin = self.ast_visitor_trig_add_trig(values[0].op,values[0].child)
                    program.append(sinplussin)
                
                if values[0] == "cosminusterm":
                    cosminusterm =  self.ast_visitor_trig_minus_term(values[0].op,values[0].child)
                    program.append(cosminusterm)

                if values[0] == "sinminusterm":
                    sinminusterm =  self.ast_visitor_trig_minus_term(values[0].op,values[0].child)
                    program.append(sinminusterm)

                if values[0] == "tanminusterm":
                    termminustan = self.ast_visitor_trig_minus_term(values[0].op,values[0].child)
                    program.append(termminustan)
                
                if values[0].op == "cospluscos":
                    cospluscos  = self.ast_visitor_trig_add_trig(values[0].op,values[0].child)
                    program.append(cospluscos)
                if values[0].op == "sinplussin":
                    sinplussin = self.ast_visitor_trig_add_trig(values[0].op,values[0].child)
                    program.append(sinplussin)

                if values[0].op == "tanplustan":
                    tanplustan =  self.ast_visitor_trig_add_trig(values[0].op,values[0].child)
                    program.append(tanplustan)
                
                if values[0].op == "sinplustan" or values[0].op == "tanplussin":
                    sinplustan = self.ast_visitor_trig_add_trig(values[0].op,values[0].child)
                    program.append(sinplustan)

                if values[0].op == "cosplussin" or values[0].op == "sinpluscos":
                    cosplussin  = self.ast_visitor_trig_add_trig(values[0].op,values[0].child)
                    program.append(cosplussin)

                if values[0].op == "cosminuscos":
                    cosminuscos  = self.ast_visitor_trig_minus_trig(values[0].op,values[0].child)
                    program.append(cosminuscos)
                
                if values[0].op == "sinminussin":
                    sinminussin = self.ast_visitor_trig_minus_trig(values[0].op,values[0].child)
                    program.append(sinminussin)

                                
                if values[0].op == "termaddtan" or values[0].op == "tanplusterm":
                    termplustan = self.ast_visitor_trig_term(values[0].op,values[0].child)
                    program.append(termplustan)
                if values[0].op == "termminustan":
                    termminustan = self.ast_visitor_trig_term(values[0].op,values[0].child)
                    program.append(termminustan)
                if values[0].op == "termtimestan" or values[0].op == "tantimesterm":
                    termtimestan = self.ast_visitor_trig_term(values[0].op,values[0].child)
                    program.append(termtimestan)

                if values[0].op  == "sintimessin":
                    sintimessin  = self.ast_visitor_trig_times_trig(values[0].op,values[0].child)
                    program.append(sintimessin)
                
                if values[0].op == "sintimecos" or values[0].op == "costimessin":
                    sintimescos  = self.ast_visitor_trig_times_trig(values[0].op,values[0].child)
                    program.append(sintimescos)
                
            

                if values[0].op == "costimescos":
                    costimescos  = self.ast_visitor_trig_times_trig(values[0].op,values[0].child)
                    program.append(costimescos)


                if values[0].op == "cosminusterm":
                    cosminusterm  = self.ast_visitor_trig_minus_term(values[0].op,values[0].child)
                    program.append(cosminusterm)
                if values[0].op == "sinminusterm":
                    sinminusterm = self.ast_visitor_trig_minus_term(values[0].op,values[0].child)
                    program.append(sinminusterm)

                if values[0].op == "tanminusterm":
                    tanminusterm =  self.ast_visitor_trig_minus_term(values[0].op,values[0].child)
                    program.append(tanminusterm)

                if values[0].op == "termdividecos":
                    termdividecos  = self.ast_visitor_term_divide_trig(values[0].op,values[0].child)
                    program.append(termdividecos)
                
                if values[0].op == "termdividesin":
                    check_zero  = self.typechecker.operation(values[0].op,values[0].child)
                    if check_zero == True:
                        termdividesin =  self.ast_visitor_term_divide_trig(values[0].op,values[0].child)
                        program.append(termdividesin)
                if values[0].op == "termdividetan":
                    termdividetan =  self.ast_visitor_term_divide_trig(values[0].op,values[0].child)
                    program.append(termdividetan)


                if values[0].op == "minus":
                     minus = self.ast_visitor_minus(values[0].child)
                     program.append(minus)

                if values[0].op == "times":
                     times = self.ast_visitor_times(values[0].child)
                     program.append(times)

                if values[0].op == "mod":
                    mod_check = self.typechecker.operation(values[0].op,values[0].child)
                    if mod_check == True:
                        mod = self.ast_visitor_mod(values[0].child)
                        program.append(mod)
                
                if values[0].op == "sumto":
                    sumto =  self.ast_visitor_sumto(values[0].child)
                    program.append(sumto)

                if values[0].op == "range":
                    range_to =  self.ast_visitor_range(values[0].child)
                    program.append(range_to)

                if values[0].op == "factorial":
                    factorial = self.ast_visitor_factorial(values[0].child)
                    program.append(factorial)
                
                if values[0].op  == "equal":
                    equal = self.ast_visitor_equal(values[0].child)
                    program.append(equal)
                if values[0].op == "pow":
                    power = self.ast_visitor_power(values[0].child)
                    program.append(power)

                if values[0].op == "cos":
                    cos =  self.ast_visitor_cos(values[0].child)
                    program.append(cos)

                if values[0].op == "sin":
                    cos = self.ast_visitor_sin(values[0].child)
                    program.append(cos)

                if values[0].op == "tan":
                    tan = self.ast_visitor_tan(values[0].child)
                    program.append(tan)
                
                if values[0].op == "greaterthanequal":
                    greaterthanequal = self.ast_visitor_greaterthanequal(values[0].child)
                    program.append(greaterthanequal)


                if values[0].op == "greaterthan":
                    greaterthan =  self.ast_visitor_greaterthan(values[0].child)
                    program.append(greaterthan)

                if values[0].op == "lessthanequal":
                    lessthanequal = self.ast_visitor_lessthanequal(values[0].child)
                    program.append(lessthanequal)

                if values[0].op == "lessthan":
                    lessthan = self.ast_visitor_lessthan(values[0].child)
                    program.append(lessthan)

                
                if values[0].op == "log":
                    greaterthanzero =  self.typechecker.operation(values[0].op,values[0].child)
                    log = self.ast_visitor_log(values[0].child)
                    if greaterthanzero == False:
                        print("negative arguement or base < 2")
                        break
                    program.append(log)
                
                if values[0].op == "divide":
                    zero_check  = self.typechecker.operation(values[0].op,values[0].child)
                    if zero_check == False:
                        print("can not divide by zero")
                        break
                    if zero_check == True:
                        divide =  self.ast_visitor_divide(values[0].child)
                        program.append(divide)
 

                if values[0].op == "root":
                    root_check =  self.typechecker.operation(values[0].op,values[0].child)
                    root = self.ast_visitor_root(values[0].child)
                    if root_check == False:
                        print("root can not be negative")
                        break

                    program.append(root)



            self.runprogram(program)
                




    def runprogram(self,program):
        for run in program:
            print(run)


    
        

    
    def error_checking(self):
        flag = True
        for check in self.program.values():
            if check[0] == None:
                flag = False
        return flag
        

start  = Interperter()
start.read_file()
start.vistingastnodes()
