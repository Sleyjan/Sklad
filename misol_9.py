class Base:

    def __init__(self,x):

        self.x=x

    def show(self):

        print('Base ', self.x)


class Delivative(Base):
        
    def __init__(self):
    
        Base.__init__(self,20)

        self.name = ''

a = Base(10)

b = Delivative()

a.show()

b.show()


