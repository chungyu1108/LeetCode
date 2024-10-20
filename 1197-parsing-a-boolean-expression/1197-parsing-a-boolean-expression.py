class Solution(object):  
    def parseBoolExpr(self, expression):  
        def evaluate(expr):  
            if expr == 't':  
                return True  
            elif expr == 'f':  
                return False  
            
            if expr[0] == '!':  
                return not evaluate(self.extract_inner(expr[2:-1]))  
            elif expr[0] == '&':  
                inner_exprs = self.extract_inner_expressions(expr[2:-1])  
                return all(evaluate(inner) for inner in inner_exprs)  
            elif expr[0] == '|':  
                inner_exprs = self.extract_inner_expressions(expr[2:-1])  
                return any(evaluate(inner) for inner in inner_exprs)  
        
        return evaluate(expression)  

    def extract_inner(self, expr):  
        return expr  

    def extract_inner_expressions(self, expr):  
        inner_expressions = []  
        balance = 0  
        current = []  
        
        for char in expr:  
            if char == ',' and balance == 0:  
                inner_expressions.append(''.join(current))  
                current = []  
            else:  
                if char == '(':  
                    balance += 1  
                elif char == ')':  
                    balance -= 1  
            
                current.append(char)  
        
        if current:  
            inner_expressions.append(''.join(current))  
        
        return inner_expressions  

