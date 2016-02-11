# -*- coding: utf-8 -*-

class drone:
    def __init__(self, location, maximum_load):
        self.location = location
        self.maximum_load = maximum_load
        productsOnBoard = list()
        self.state = 0


        self.alarm = 0
        self.isBusy = False

    def Load(self, warehouse, product):
        if warehouse.take(product):
            productsOnBoard.append(product)

    def Unload(self,product):
            if product in self.productsOnBoard:
                self.productsOnBoard.remove(product)
                return True
            return False

    def deliver(self,productLocation, ):
        pass

    def droneCurrentWeight(self):
        return sum([i.weight for i in self.productsOnBoard])

    def setAlarm(self, time):

        self.isBusy = True
        self.alarm = time

    def checkBusy(self):

        return self.isBusy

    def step(self):

        if self.alarm > 0:
            self.alarm -= 1

            if self.alarm == 0:
                self.isBusy = False
