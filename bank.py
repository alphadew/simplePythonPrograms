class Bank:
    ac_no=0
    balance=0
    deposit_amt=0
    ac_type=""
    name=""
    def get_data(self):
        self.ac_no=int(input("Enter Acc Number"))
        self.name=input("Enter Name")
        self.acc_type=input("Enter type")
        self.balance=int(input("Enter balance"))
        print(self.balance)
    def deposit(self):
        self.deposit_amt=int(input("Enter deposit amount"))
        self.balance+=self.deposit_amt
    def show(self):
        print("Custoemr Details\n",self.name,self.name,self.ac_type,self.balance)
    def withdraw(self):
        val=int(input("Enter withdraw amount"))
        if self.balance>=val:
            self.balance-=val
            print(self.balance)
        else:
            print("invalid amount")
ob=Bank()
while 1:

    print("1.Register\n2.Display Details\n3.Deposit\n4.Withdraw")
    x=int(input("Enter choice"))
    if x==1:
        ob.get_data()
    elif x==2:
        ob.show()
    elif x==3:
        ob.deposit()
    elif x==4:
        ob.withdraw()
    else:
        print("Invalid entry")
        
