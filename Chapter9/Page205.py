

class Resturants:
    def __init__(self, name, cusine):
        self.name = name
        self.cusine = cusine
        self.serving = 0
        
    def description(self):
        print(f'Resturant name:{self.name}')
        print(f"Cuisine type: {self.cusine}")
        
    def open_resturant(self):
        print(f'{self.name.title()} is OPEN!!!!!!!!!!')
        
    def who_is_served(self):
        print(f'{self.serving} customers tended to')
        
    def add_serving(self,order):
        self.serving += int(order)
        
resturant = Resturants('El Commadore', 'Mexican Cuisine')

resturant2 = Resturants('Fishaways', 'Seafood')

resturant3 = Resturants('KFC','Fast food')

print(resturant.name)
print(resturant.cusine)
print('\\\\\\\\\\\\\\\\\\\\\\')
resturant.add_serving(6)
resturant.open_resturant()
resturant.description()
resturant.who_is_served()
print()   
resturant2.add_serving(12) 
resturant2.open_resturant()
resturant2.description()
resturant2.who_is_served()
print()
resturant3.add_serving(22)
resturant3.open_resturant()
resturant3.description()
resturant3.who_is_served()

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
print('\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\')

class User:
    def __init__(self,f_name,l_name,number,address):
        self.f_name=f_name
        self.l_name = l_name
        self.number = number
        self.address = address
        self.log_attempts = 0
        
    def user_info(self):
        print(f'The user first name is: {self.f_name}') 
        print(f'The user last name is: {self.l_name}') 
        print(f'The user phone number is: {self.number}') 
        print(f'The user address is: {self.address}') 
        
    def greetings(self):
        print(f'Well...hello there {self.f_name}')
        
    def increment_atempt(self):
        self.log_attempts += 1
        print(f'login attempts: {self.log_attempts}')
        
    def log_res(self):
        self.log_attempts = 0
        print(f'Attempts reset: {self.log_attempts}')


person1 = User('Evangelis','Pitts',20,'116 Sierra')
person2 = User('Tracey', "Gooch", 39, "1012 LakeShore")
person3 = User("Max", 'Storey', 21, '10625 Cochron')

person1.greetings()
person1.user_info()
person1.log_attempts
for i in range(1,4):
    person1.increment_atempt()
person1.log_res()
print()
person2.greetings()
person2.user_info()
for i in range(1,4):
    person2.increment_atempt()
person2.log_res()
print()
for i in range(1,4):
    person3.increment_atempt()
person3.log_res()
person3.greetings()
person3.user_info()