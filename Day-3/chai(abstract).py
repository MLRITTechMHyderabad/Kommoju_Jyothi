from abc import ABC, abstractmethod
class Chai:
    def __init__(self,name,base_price,quantity_in_stock):
        self.name=name
        self.base_price=base_price
        self.quantity_in_stock=quantity_in_stock
    def calculate_price(self):
        pass
    def display_info(self):
        pass
class MasalaChai(Chai):
    def calculate_price(self):
         return self.base_price+10
    def display_info(self):
        print(f"name:{self.name} | Price per cup: {self.calculate_price()} |Stock: {self.quantity_in_stock}")
        
class GingerChai(Chai):
    def calculate_price(self):
         return self.base_price+8
    def display_info(self):
        print(f"name:{self.name} | Price per cup: {self.calculate_price()} |Stock: {self.quantity_in_stock}")
class ElaichiChai(Chai):
    def calculate_price(self):
         return self.base_price+12
    def display_info(self):
        print(f"name:{self.name} | Price per cup: {self.calculate_price()} |Stock: {self.quantity_in_stock}")
class ChaiInventory:
    def __init__(self):
        self.chai_list=[]
    def add_chai(self,chai_obj):
        self.chai_list.append(chai_obj)

    def show_inventory():
        for i in self.chai_list:
            i.display_info()
    def get_total_inventory_value():
        total_value=sum(chai.calculate_price()* chai.quantity_in_stock for chai in self.chai_list)
        return total_value



inventory = ChaiInventory()

chai1 = MasalaChai("MasalaChai", 20, 50)
chai2 = GingerChai("GingerChai", 18, 40)
chai3 = ElaichiChai("ElaichiChai", 25, 30)

inventory.add_chai(chai1)
inventory.add_chai(chai2)
inventory.add_chai(chai3)

inventory.show_inventory()

print("Total Inventory Value: ₹", inventory.get_total_inventory_value())
    
    
