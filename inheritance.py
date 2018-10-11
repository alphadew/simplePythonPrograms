class person:
    name=""
    code=0
class A(person):
    pay=0
class B(person):
    exp=0
    def get(self,nam,code,exp):
        self.name=nam
        self.code=code
        self.exp=exp
    def show(self):
        print("from class B")
        print(self.name,self.exp,self.code)
        
obj=B()
obj.get("Amal",1,5)
obj.show()
