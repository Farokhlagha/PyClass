
class person:
    def __init__(self,n,a,h,c,e):

        # properties
        self.name = n
        self.age = a
        self.height = h
        self.city = c
        self.country = 'Iran' # no need parameter
        self.eye_color = e
        self.spouse = ''


    # methods
    def  sleep(self):
        ...
    def walk(self):
       ...

    def marry(self, name, name2):
        self.spouse = name
        self.child = name2
                
    def eat(self):
     ...

# object
my_friend = person('amir', 30, 190, 'london', 'green')
my_sister = person('sara', 10, 112, 'newyork', 'blue')

print(my_friend.name)
print(my_sister.age)
print(my_friend.spouse)
my_friend.marry('mamad', 'jafar')
print(my_friend.spouse)
print(my_friend.child)
