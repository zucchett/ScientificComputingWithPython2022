class Temperature():
    x = []
    def __init__(self,celsius):
        if celsius > -273.15:
            self.celsius = celsius
            
        else:
            raise ValueError('ERROR: Temperatures below -273.15C are not possible')
    def somma(self):
        return self.celsius +100


t = Temperature(float(input("")))
print(t.celsius)
print(t.somma())