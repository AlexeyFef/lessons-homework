# создаем класс User, объявляем конструктор, создаем три класса 

class User:
    
    def __init__(self, _first_name, _last_name):
        self.first_name = _first_name
        self.last_name = _last_name        
    
    def say_first_name(self):
        print(self.first_name)

    def say_last_name(self):
        print(self.last_name)

    def say_first_name_last_name(self):
        print(self.first_name, self.last_name)    
