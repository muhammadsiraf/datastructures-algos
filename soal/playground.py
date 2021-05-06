class snake():
    body = []
    
    def __init__(self):
        self.body = []
    
    def eat(self, food):
        self.body.append(food)
        
    def sort_body(self):
        check = None
        
                
        self.body.sort()
    
    def display(self):
        self.sort_body()
        for each in self.body:
            print(each)
            

ular = snake()
ular.eat(1)
ular.eat(2)
ular.eat(5)
ular.eat(4)
ular.eat(3)
ular.eat(6)
ular.eat(9)
ular.display()
