import numbers

class Error(Exception):
    pass

class Opera():
    def soma(self, op1, op2):
        self.check_nat(op1)
        self.check_nat(op2)
        return op1+op2

    def sub(self, op1, op2):
        self.check_nat(op1)
        self.check_nat(op2)
        self.check_result_sub(op1, op2)
        return op1-op2

    def mult(self, op1, op2):
        self.check_nat(op1)
        self.check_nat(op2)
        return op1*op2

    def div(self, op1, op2):
        self.check_nat(op1)
        self.check_nat(op2)
        self.check_zero(op2)
        self.check_result(op1, op2)
        return op1/op2

    def check_nat(self, op):
        if not (isinstance(op, numbers.Integral) and op >= 0):
            raise Error(f"{op} nao e inteiro")

    def check_zero(self, op):
        if op == 0:
            raise Error("Nao e possivel fazer uma divisao por zero")

    def check_result(self,op1, op2):
        if not op1%op2==0:
            raise Error("Resultado nao pertence aos naturais")

    def check_result_sub(self, op1, op2):
        if op1-op2<0:
            raise Error("Resultado negativo")
