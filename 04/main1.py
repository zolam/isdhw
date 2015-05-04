class Dimension:
	def_init_(self,x,y):
            self.x=x
            self.y=y
        def area(self):
            pass
class Ellipse(Dimension):
    def_init_(self,a,b):
        Dimension_init_(self,a,b):
    def area(self):
        return 3.14*self.x*self.y
class Square(Dimension):
    def_init_(self,c,0):
        Dimension_init_(self,c,0):
    def area(self):
        return self.x*self.x
class Rectangle(Dimension):
    def_init_(self,w,h):
        Dimension_init_(self,w,h):
    def area(self):
        return self.x*self.y
class Circle(Dimension):
    def_init_(self,r,0):
        Dimension_init_(self,r,0):
    def area(self):
        return self.x*self.x
d1=Ellipse(10,20)
d2=Square(15,0)
d3=Rectangle(20,15)
d4=Circle(5,0)
print(d1.area(),d2.area(),d3.area(),d4.area())
print(d1.area()+d2.area()+d3.area()+d4.area())
    

            
 
