# Задание 1 
class Animals:
    def __init__(self,name,age,weight,habitat,diet) :
        if isinstance(name,str):
            self.name=name
        else:
            raise ValueError ('Name must be of type str') 
        if isinstance(age,int):
            self.age=age
        else:
             raise ValueError ('Age must be of type int') 
        if isinstance(weight, (int, float)): 
            self.weight = weight
        else:
            raise ValueError('Weight must be of type int or float')
        if isinstance(habitat,str):
            self.habitat = habitat 
        else:
            raise ValueError ('Name must be of type str') 
        if isinstance(diet,str):
            self.diet=diet
        else:
            raise ValueError ('Name must be of type str')   
        
    def eat(self):
        return f'{self.name} ест {self.diet}.'

    def sleep(self):
        return f'{self.name} спит.'

    def make_sound(self):
        return f'{self.name} издает звук.'

    def move(self):
        return f'{self.name} передвигается.'

    def __str__(self):
        return (f'Name-{self.name}\n'
                f'Age-{self.age}\n'
                f'Gender-{self.weight}\n'
                f'Height-{self.habitat}\n'
                f'Hobby-{self.diet}')  
    
class Reptiles (Animals): 
    def __init__(self, name, age, weight, habitat, diet,special_attr):
        super().__init__(name, age, weight, habitat, diet) 
    def crawl(self):
        return f'{self.name} ползет.'

    def shed_skin(self):
        return f'{self.name} сбрасывает кожу.'

    def bask_in_sun(self):
        return f'{self.name} греется на солнце.'

    def lay_eggs(self):
        return f'{self.name} откладывает яйца.'     
    
snake = Reptiles(name='Змея', age=5, weight=12, habitat='Лес', diet='Мыши', special_attr='Ядовитая')
lizard = Reptiles(name='Ящерица', age=3, weight=0.5, habitat='Пустыня', diet='Насекомые', special_attr='Хвост длиной 10 см')
turtle = Reptiles(name='Черепаха', age=50, weight=100, habitat='Океан', diet='Водоросли', special_attr='Панцирь 60 см')


class Mammals(Animals):
    def __init__(self, name, age, weight, habitat, diet, special_attr):
        super().__init__(name, age, weight, habitat, diet)
        self.special_attr = special_attr

    def run(self):
        return f'{self.name} бежит.'

    def hunt(self):
        return f'{self.name} охотится.'

    def nurture_young(self):
        return f'{self.name} заботится о потомстве.'

    def communicate(self):
        return f'{self.name} общается с другими животными.'
lion = Mammals(name='Лев', age=8, weight=190, habitat='Саванна', diet='Мясо', special_attr='Грива длиной 30 см')
elephant = Mammals(name='Слон', age=25, weight=6000, habitat='Саванна', diet='Трава', special_attr='Бивни 1.5 м')
kangaroo = Mammals(name='Кенгуру', age=6, weight=90, habitat='Австралия', diet='Трава', special_attr='Высота прыжка 3 м')
class ZooShow:
    def __init__(self, show_name, ticket_price, animal_performer):
        self.show_name = show_name
        self.ticket_price = ticket_price
        self.animal_performer = animal_performer
        self.tickets_sold = 0

    def perform_show(self):
        return f'{self.animal_performer.name} выполняет трюки на шоу "{self.show_name}".'

    def display_info(self):
        return (f'Название шоу: {self.show_name}\n'
                f'Участвует животное: {self.animal_performer.name}\n'
                f'Возраст: {self.animal_performer.age} лет\n'
                f'Среда обитания: {self.animal_performer.habitat}\n'
                f'Диета: {self.animal_performer.diet}')

    def sell_ticket(self, num_tickets):
        self.tickets_sold += num_tickets
        return f'Продано {num_tickets} билетов.'

    def calculate_revenue(self):
        return f'Выручка: {self.tickets_sold * self.ticket_price} $.'
lion_show = ZooShow(show_name='Царский охотник', ticket_price=20, animal_performer=lion)

# Выполнение методов шоу
print(lion_show.perform_show())
print(lion_show.display_info())
print(lion_show.sell_ticket(100))
print(lion_show.calculate_revenue())



