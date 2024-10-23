class Car: 
    def __init__(self,model,color,volume) : 
        if isinstance(model,str):
            self.color=color 
        else: 
            raise ValueError('Color must be of type str') 
                
        if isinstance(model,str):
            self.model=model 
        else: 
            raise ValueError('model must be of type str')   
        
        if isinstance(volume,float):
            self.volume=volume
        else: 
            raise ValueError('Volume must be of type float')    
        
    def drive(self,speed):
            return f'this car drives {speed} km/h'

    def __str__(self) : 
        return(f'model -{self.model}\n'
               f'color -{self.color}\n'
               f'volume -{self.volume}\n')
    
print('Jusly cars') 
car_1 = Car(model='Lexus', color='white', volume=5.0) 
car_2 = Car('Porshe', 'red', 5.7) 
print(f'{car_1}\n'
      f'----------\n' 
      f'{car_2}')
print(car_1.drive(200)) 
print(car_2.drive(500)) 

class HybridCar(Car) : 
    def __init__(self, model, color, volume,battery, comfort):
        super().__init__(model, color, volume)
        if isinstance(comfort, bool) : 
            self.comfort = comfort 
        else: 
            raise ValueError('Comf must be typ bool') 
        
        if isinstance(battery, float) : 
            self.battery = comfort 
        else: 
            raise ValueError('Comf must be typ float') 
        
    def __str__(self):
        return super().__str__()+(f'\nBattery {self.battery}\n' 
                                  f'Comfort {self.comfort}\n') 
    
hybrud_1 = HybridCar(model='Toyota Land Cruiser' , color='Black' , volume = 5.7, battery=101.1, comfort=False) 
hybrud_2 = HybridCar('BMW' , 'Blue' , 4.3, 89.9,True) 
print(f'----------\n'
      f'{hybrud_1}\n' 
      f'{hybrud_2}')
        
