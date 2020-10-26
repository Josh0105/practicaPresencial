import math

class calculadora:
    def __init__(self):
        self.historial = []
    
    def suma(self,a,b):
        self.historial.append(str(a)+" + "+str(b)+" = "+str(a+b))
        return a+b
    
    def resta(self,a,b):
        self.historial.append(str(a)+" - "+str(b)+" = "+str(a-b))
        return a-b
    
    def multiplicar(self,a,b):
        self.historial.append(str(a)+" * "+str(b)+" = "+str(a*b))
        return a*b
    
    def dividir(self,a,b):
        try:
            self.historial.append(str(a)+" / "+str(b)+" = "+str(a/b))
            return a/b
        except:
            self.historial.append("Division no definida")
            return False
    
    def potencia(self,a,b):
        try:
            self.historial.append(str(a)+" ^ "+str(b)+" = "+str(pow(a,b)))
            return pow(a,b)
        except:
            self.historial.append("Potencia no definida")
            False

    def raiz(self,a,b):
        try:
            self.historial.append(str(b)+" ^ ( 1 / "+str(a)+" ) = "+str(pow(b,(1/a))))
            return pow(b,(1/a))
        except:
            self.historial.append("Raiz no definida")
            return False