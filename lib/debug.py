#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Customer
from classes.many_to_many import Order
from classes.many_to_many import Coffee

if __name__ == '__main__':
    print("HELLO! :) let's debug")

   
   
   
   
  


c1 = Coffee("Dunkin")
c2 = Coffee("Butello")
c3 = Coffee("SantoDomingo")

cb = Customer("Melisssa")
cc = Customer("Maria")
cd= Customer("Magdalena")

oa = Order(cb, c1, 5)
ob = Order(cc, c2, 7)
oc = Order(cd, c3, 9)
           


ipdb.set_trace()
