# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 15:42:00 2018

@author: Krishnamoorthy KBhat
"""

vegetable={'Tomato':20,'Potato':60,'Brinjal':30}
fruits={'Banana':30,'Grapes':40,'Apple':80}
milkprod={'Icecream':30,'cake':30}
def vegetable_func(item,number):
        if(item in vegetable.keys()):
            f=vegetable[item]
            return f*number 
        else:print("Vegetable not in the list")

def fruits_func(item,number):
    for i in fruits:
        if(item in fruits.keys()):
            f=fruits[item]
            return f*number        
        else:print("Fruit not in the list")

def milkprod_func(item,number):
    for i in milkprod:
        if(item in milkprod.keys()):
          f=milkprod[item]
          return f*number
        else:print("Milk Product not in the list")

print("------Select the item name from the menu------\n")
print("'vegetable' or 'fruits' or 'milkprod'")
item = input()
file=open('write.txt','a')
if(item=='vegetable'):
          print(vegetable)
          s=input("Enter the vegetable:\n")
          
          print("Enter the number of vegetable required:\n")
          req = input()
          file.writelines([s])
          file.writelines(['   ' '   ',req])
          x=str(vegetable_func(s,int(req)))
          file.writelines(['   ' '   ''    ',x])
          file.write("\n")
          file.close()
          print("Total no. of vegetable is:",x)
elif(item=='fruits'):
         print(fruits)
         s=input("Enter the fruit:\n")
         print("Enter the number of fruit items required:\n")
         req = input()
         file.writelines([s])
         file.writelines(['   ' '   ',req])
         x=str(fruits_func(s,int(req)))
         file.writelines(['   ' '   ''    ',x])
         file.write("\n")
         file.close()
         print("Total no. of fruits is:",x)
else:
         print(milkprod)
         s=input("Enter the Milk product:\n")
         print("Enter the number of Milk Product items required:\n")
         req = input()
         file.writelines([s])
         file.writelines(['   ' '   ',req])
         x=str(milkprod_func(s,int(req)))
         file.writelines(['   ' '   ''    ',x])
         file.write("\n")
         file.close()

         print("Total no. of Milk Products is:",x)


    
    