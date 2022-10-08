class Typechecker(object):



    
    def operation(self,op,expression):
        if op == "root":
            return self.root_type_check(expression)
        if op == "log":
            return self.log_check(expression)
        if op == "divide":
           return self.divide_by_zero_check(expression)
        if op == "mod":
           return self.mod_check(expression)
        if op == "termdividesin":
           return self.term_divide_trig_check(expression)
        if op == "sindividesin":
           return self.trig_divide_trig_check(expression)




    def trig_divide_trig(self,trig):
        pass

    
    def term_divide_trig_check(self,trig):
        
        if int(trig[1]) == 0:
            return False
        return True

            
        
    
    
    def root_type_check(self,root):
        #check if root is positive
        if int(root[0]) < 0 and int(root[1]) < 0:
            return False
        return True
      
    def mod_check(self,mod):
       if int(mod[1]) == 0:
           return False
       return True
        

    def log_check(self,log):
        #checks if log is greater then zero and base > 2 
        if int(log[1][0])<=0 and int(log[1][1]) < 2 :
            return False
        return True


    def divide_by_zero_check(self,divide):
        if int(divide[1]) == 0:
            return False
        return True

