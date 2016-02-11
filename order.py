# -*- coding: utf-8 -*-

class order:

    def __init__(self, orderID, location, quantity, productID):

        # productID is a list of product types

        self.orderID = orderID
        self.location = location
        self.quantity = quantity
        self.productIDsRequired = productID
        self.mywarehouse = None