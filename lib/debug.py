#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Customer
from classes.many_to_many import Order
from classes.many_to_many import Coffee

if __name__ == '__main__':
    print("HELLO! :) let's debug")

    g1 = ("chess")
    g2 = Game("monopoly")
    p1 = Player("Melissa")
    p2 = Player("Tyler")
    p3 = Player("Katie")

    r1 = Result(p1,g1,1)
    r2 = Result(p2,g2,3)
    r3 = Result(p1,g2,6)
    r4 = Result(p2,g1,8)
    r5 = Result(p2,g1,10)
    r6= Result(p1,g2,15)


    ipdb.set_trace()
