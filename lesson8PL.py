class Resonn:
    def __init__(self, name , age, gender,height,hobby): 
        if isinstance(name,str):
            self.name = name 
        else: 
            raise ValueError("Name must be of type str") 
        
        if isinstance(age,int): 
            self.age = age 
        else:
            raise ValueError("Age must be of type int")  
        
        if isinstance(gender,str): 
            self.gender = gender 
        else:
            raise ValueError("Gender must be of type str")   
        
        if isinstance(height,int): 
            self.height = height 
        else:
            raise ValueError("height must be of type int")  
         
        if isinstance(hobby,int): 
            self.hobby = hobby 
        else:
            raise ValueError("hobby must be of type int")  
         