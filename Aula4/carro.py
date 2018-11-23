#coding: utf-8

class Carro:
    def __init__(self,autonomia):
        self.autonomia = autonomia
        self.combustivel = 0
        self.km = 0.0


    def abastecer(litros):
        self.combustivel=litros
        print('Quantidade Tanque' + self.combustivel)

        
    def rodar():
        if(self.combustivel>0 and self.autonomia<self.km):
            self.km+=1            
            print(str(self.km)+ ' KM Rodado')
            
        
        
    
car = Carro(100)
car.abastecer(50)





