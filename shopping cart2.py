import random


stored=['Name','Phone Num','Permanent Address','Delivery Address']

dict1={"best123":{"Name":"Balaji"},"best124":{"Name":"Siva"}}

class Users:
  
  def __init__(self,userid,name,phonenum,acc):
      self.userid=userid
      self.name=name
      self.phonenum=phonenum
      self.acc=acc

  def Verification(self):
    self.total=0
    self.t1=0
    total3=0

    while True:
        print("Select the given location\nadyar/besant nagar/indira nagar/t nagar")
      
        self.location1=input("Enter the location for delivery:").lower()
        location2=["adyar","besant nagar","indira nagar","t nagar"]

        if self.location1 not in location2:
            print("Sorry we are not available on your location")

        else:
            print("****************************************** WELCOME TO BEST SUPERMARKET ******************************************")
            print()
            break

  def New_cust(self):
      market="Best"
      self.location3=self.location1[:2]
      name=input("Enter your name:")

      if not name.isalpha():
          print('Enter alphabet only')
          name=input("Enter your name:")
    
      
      phone=input("Enter your phone number:")

      if not phone.isdigit():
          print('Enter numbers only')
          order_num=input("Enter your phone number:")
          
      address=input("Enter your address:")
      
      del_address=input("Enter the address for deliver your product:").lower()
      total=[name,phone,address,del_address]
      add=dict(zip(stored,total))
      acc_num=random.randint(1000,9999)
      acc_str=str(acc_num)
      self.acc=market+acc_str+self.location3
      dict1[self.acc]=add
      print("Your account number is:",self.acc)
      print("Your account was created sucessfully")
      print()

  def Shopping(self):
      choice1=[]
      choice2=[]

      while True:
        choice3=[1,2]
        user_inp=int(input("Enter 1 for purchase,2 for payment:"))

        if user_inp not in choice3:
            print("Please press one and 2 only")

        if user_inp==1:
          product1={"biscuits":20,"choclates":30,"lays":40,"cake":50}
          print("Select the product in the given list:",product1)
          toselect=input("Enter the items for purchase:").lower()
          choice4=["biscuits","choclates","lays","cake"]

          if toselect in product1.keys():
            quantity=int(input("Enter how many product you want:"))

            if quantity>=1:
              ov=quantity*product1[toselect]
              choice1.append(toselect)
              print("Your selected products is:",choice1)
              choice2.append(ov)
              print()
              print("Total cost is:",choice2)

            else:
              print("Quantity should not less than 1")

          else:
            print("Item does not exist.Please select from the given list")

        if user_inp==2:
          payment=list(zip(choice1,choice2))
          self.total=sum(choice2)
          print("Total cost of your purchase is:",self.total)
          print()
          break

class Discount(Users):
  def __init__(self,userid,name,phonenum,acc):
    Users.__init__(self,userid,name,phonenum,acc)
    self.total1=0
    self.total2=0

  def discount2(self):
      product2={"sugar":50,"rice":40,"atta":55}
      add1=[]
      add2=[]
      add3=[]

      while True:
        choice5=[1,2,3]
        user_inp2=int(input("Enter 1 for sale, 2 for Discount Sale and 3 for Delivery:"))

        if user_inp2 not in choice5:
            print("Please press 1,2 and 3 only")


        if user_inp2==1:
          print("Enter the products to be purchased:",product2)
          select=input("Select the product:").lower()
          check=["sugar","rice","atta"]

          if not name.isalpha():
              print("Enter sugar,rice and atta only")
              select=input("Select the product:")


          if select in product2.keys():
            quantity2=int(input("Enter the quantity to be purchased:"))


            if quantity2>=1:
              mult_prod=quantity1*procuct2[select]
              add1.append(select)
              print("Your selected Item is:",add1)
              cart2.append(mult_prod)
              print("Total cost of cost is:",add2)
              payment2=list(zip(add1,add2))
              total3=sum(add2)
              print("Total cost of your purchase is:",total3)

            else:
              print("Quantity should not be less than 1")

          else:
            print("Item does not exist.Please select from the list given")
                        
                        
        if user_inp2==2:
          print("Get 5% discount on 1Kg of Sugar and 10% discount on 5Kg of Sugar")
          print("Get 4% discount on 10Kg of Rice and 8% discount on 25Kg of Rice")
          print("Get 6% discount on 5Kg of Atta and 12% discount on 10Kg of Atta")
        
          select2=input("Press Sugar to get discount on sugar\n Press rice to get discount on rice\n Press atta to get discount on atta\n Please press Sugar,Rice or Atta:").lower()
          validentry=["sugar","rice","atta"]

          if select2 in product2.keys():

            if select2=="sugar":
              sugar=int(input("Enter the quantity you want 1kg or 5kg:"))

              if sugar==1:
                mult=sugar*product2[select2]
                add1.append(select2)
                print("Your selected item is:",add1)
                add2.append(mult)
                sum_add2=sum(add2)
                print("Total cost of cost is:",sum_add2)
                total4=sum_add2*5/100
                self.t1=sum_add2-total4
                add3.append(self.t1)
                payment3=list(zip(add1,add3))
                print()
                print("Total cost of your purchase after discount is:",self.t1)

              elif sugar==5:
                mult=sugar*product2[select2]
                add1.append(select2)
                print("Your selected item is:",add1)
                add2.append(mult)
                sum_add2=sum(add2)
                print("Total cost of cost is:",sum_add2)
                total4=sum_add2*10/100
                self.t1=sum_add2-total4
                add3.append(self.t1)
                payment3=list(zip(add1,add3))
                print("Total cost of your purchase after discount is:",self.t1)

            if select2=="rice":
              rice=int(input("Enter the quantity you want 10kg or 25kg:"))

              if rice==10:
                mult=rice*product2[select2]
                add1.append(select2)
                print("Your selected item is:",add1)
                add2.append(mult)
                sum_add2=sum(add2)
                print("Total cost of cost is:",sum_add2)
                total4=sum_add2*4/100
                self.t1=sum_add2-total4
                add3.append(self.t1)
                payment3=list(zip(add1,add3))
                print("Total cost of your purchase after discount is:",self.t1)

              elif rice==25:
                mult=rice*product2[select2]
                add1.append(select2)
                print("Your selected item is:",add1)
                add2.append(mult)
                sum_add2=sum(add2)
                print("Total cost of cost is:",sum_add2)
                total4=sum_add2*8/100
                self.t1=sum_add2-total4
                add3.append(self.t1)
                payment3=list(zip(add1,add3))
                print("Total cost of your purchase after discount is:",self.t1)

            if select2=="atta":
              atta=int(input("Enter the quantity you want 10kg or 25kg:"))

              if atta==5:
                mult=atta*product2[select2]
                add1.append(select2)
                print("Your selected item is:",add1)
                add2.append(mult)
                sum_add2=sum(add2)
                print("Total cost of cost is:",sum_add2)
                total4=sum_add2*6/100
                self.t1=sum_add2-total4
                add3.append(self.t1)
                payment3=list(zip(add1,add3))
                print("Total cost of your purchase after discount is:",self.t1)

              elif atta==10:
                mult=atta*product2[select2]
                add1.append(select2)
                print("Your selected item is:",add1)
                add2.append(mult)
                sum_add2=sum(add2)
                print("Total cost of far is:",sum_add2)
                total4=sum_add2*12/100
                self.t1=sum_add2-total4
                add3.append(self.t1)
                payment3=list(zip(add1,add3))
                print("Total cost of your purchase after discount is:",self.t1)

                

        if user_inp2==3:
            break

    
  def Deliver(self):
    print("Do you wish to have a delivery or pick up from the store")
    delivery1=input("Press (yes) to delivery your product or (no) to pick up from the store:").lower()
    
    if delivery1=="yes":

      print("Select your location within the areas given.\n t Nagar - 50\n Adyar - 70\n Besant Nagar - 20\n Indira Nagar - 40")

      while True:
        del_location=input("Enter your location for delivery:").lower()
        location4=["adyar","besant Nagar","indira Nagar","t Nagar"]


        if del_location not in location4:
            print("Enter valid location")

        if del_location in location4:

          if del_location=="adyar":
            print("The total cost of your order with delivery charge for",del_location,"is:",self.total+self.t1+70)

          elif del_location=="besant Nagar":
            print("The total cost of your order with delivery charge for",del_location,"is:",self.total+self.t1+20)

          elif del_location=="indira Nagar":
            print("The total cost of your order with delivery charge for",del_location,"is:",self.total+self.t1+40)

          elif del_location=="t-Nagar":
            print("The total cost of your order with delivery charge for",del_location,"is:",self.total+self.t1+40)
            break
        else:
          print("Delivery not available in the selected location.Please pick it from the store after Payment. Your Total Cost is:",self.total+self.t1,"Thank You !")
        break  
          
    elif del_location=="no":
      print("You can pick your order after 30 mins of Payment from the store.Your Total Cost is:",self.total+self.t1+total3,"Thank You!")

class Lucky_spin(Discount):
  __custname="balaji"

  def __init__(self,userid,name,phonenum,acc):
    Discount.__init__(self,userid,name,phonenum,acc)

  def spin_wheel(self):
    
    print(("*")*40,"WELCOME TO LUCKY SPIN DRAW",("*")*40)
    spin=int(input("Press 1 for lucky Draw and 2 for exit"))

    if spin==1:

      cust_id=input("Enter your customer id:")
      if not cust_id.isdigit() and cust_id.isalpha():
          print('Enter numbers only')
          cust_id=input("Enter your customer id:")
          
      name=input("Enter your name:")
      if not name.isalpha():
          print('Enter alphabets only')
          name=input("Enter your name:")


      location=input("Enter your location:")
      if not location.isalpha():
          print('Enter alphabets only')
          location=input("Enter your location:")
      
      print("Thank you for register")
      spin1=int(input("Press 1 to Spin:"))
      gift="Better Luck Next Time"
      print("Sorry.Better Luck Next Time.You have 2 more Chances")
      spin2=int(input("Press 1 to Spin:"))
      gift=("1000rs coupon","2000rs coupon","3000rs coupon","Smart watch","Bluetooth speaker","Better Luck Next Time")
      gift2=random.choice(gift)
      

      if gift2=="Better Luck Next Time":
        print("Sorry! Spin Again")
        spin3=int(input("Press 1 to Spin:"))
        gift=("1000rs coupon","2000rs coupon","3000rs coupon","Smart watch","Bluetooth speaker","Better Luck Next Time")
        gift2=random.choice(gift)

        if gift2=="Better Luck Next Time":
          print("Sorry ! You Lost all your Spins")

        else:
          print("Congratulations you won:",gift2)
          print("Please collect it from the store by providing your customer Id.")

      else:
        print("Congratulations you won:",gift2)
        print("Please collect it from the store by providing your customer Id.")  
    else:
      pass    


  def final(self):
    choice6=[1,2,3]

    while True:
      print("Press 1,if you are a new customer")
      print("Press 2,if you are an existing customer")
      print("Press 3,to Exit")

      user_inp3=int(input("Enter 1,2 or 3:")) 

      while user_inp3 not in choice6:
        print("Please enter only 1,2 or 3:")
        user_inp3=int(input("Enter 1,2 or 3:"))     
 
      if user_inp3==1:
        obj.New_cust()

      if user_inp3==2:
        Id=(input("Enter your Customer Id:"))

        

        if Id in dict1:
          print("Welcome back",dict1[Id]["Name"])
          obj.Shopping()
          obj.discount2()
          obj.Deliver()  

        else:
          print("Customer Id does not exist.If you are a new user,Please register to continue shopping!")
          obj.final()
        print("Thank you for shopping with us!Visit Again!")
        break

      if user_inp3==3:
        print("Thank you for shopping with us!Visit Again!")
        break


obj=Lucky_spin("best123","Balaji",9597978256,3556)
obj.Verification()
obj.final()
obj.spin_wheel()


      
        
                        
                    
                
            
    

                
        
        


        
        

       

                                      
