class carshowroom:
    def __init__(self,cgst,sgst,insurance):
        self.cgst=cgst
        self.sgst=sgst
        self.ins=insurance
        #print("showroom taxes")
    def company(self):
        while True:
            print("select a car from tata,mercedez,mahindra")
            self.n=input("select a car")
            if self.n=="tata":
                print("welcome to tata")
                self.model()
                break
            elif self.n=="mercedez":
                print("welcome to mercedez")
                self.model()
                break
            elif self.n=="mahindra":
                print("welcome to mahindra")
                self.model()
                break
            else:
                print("enter valid company")
                break
    def model(self):
      if self.n=="tata":
        while True:
            print("the models are harriar and nexon")
            self.m=input("enter car")
            if self.m=="harriar":
                self.price(self.m)
                break
            elif self.m=="nexon":
                self.price(self.m)
                break
            else:
                print("enter valid model")
                break
      if self.n=="mercedez":
          while True:
              print("the model are amg and gwagon")
              self.m=input("enter car")
              if self.m=="amg":
                  self.price(self.m)
                  break
              elif self.m=="gwagon":
                  self.price(self.m)
                  break
              else:
                  print("enter valid model")

      if self.n=="mahindra":
          while True:
              print("the model are xuv and thar")
              self.m=input("enter car")
              if self.m=="xuv":
                  self.price(self.m)
                  break
              elif self.m=="thar":
                  self.price(self.m)
                  break
              else:
                  print("enter valid")
    def price(self,m):
        if m=="harriar":
            self.price=12500252
        elif m=="nexon":
            self.price=15869525
        elif m=="amg":
            self.price=1598955585
        elif m=="gwagon":
            self.price=545532255
        elif m=="xuv":
            self.price=125855525
        elif m=="thar":
            self.price=956526232
        total=self.price+self.cgst+self.sgst+self.ins
        print(total)

ob=carshowroom(0.18,0.18,100000)
ob.company()

