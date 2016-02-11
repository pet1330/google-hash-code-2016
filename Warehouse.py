# -*- coding: utf-8 -*-


class warehouse:

    def __init__(self, location, product):
        self.location = location
        self.deliveryPoints = list()

        self.allProducts = product
        self.wishlist = list()
        self.excessInventory = []

        self.allProducts = self.convertInv(self.allProducts)

    def take(self,item):

        for i in xrange(0, len(self.excessInventory)):
            if item == self.excessInventory[i]:
                self.excessInventory.pop(i)
                self.allProducts.pop(i)
                return true

        return false

    def inventoryCheck(self):

        self.excessInventory = self.allProducts

        for i in self.deliveryPoints:
            for j in i.productIDsRequired:

                found = False

                for k in xrange(0, len(self.excessInventory)):
                    if k == j:
                        del excessInventory[k]
                        found = True
                        break

                if found != True:

                    self.wishlist.append(j)

    def convertInv(self,before):
        before = map(int, before)
        after = []
        for i in xrange(0, len(before)):
            for j in xrange(0, before[i]):
                after.append(i)

        return after