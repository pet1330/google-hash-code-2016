# -*- coding: utf-8 -*-

import math
import filereader
import drone
import Warehouse

class world:

    drones = list()

    def __init__(self):
        self.datasetfromfile = filereader.readFile("data_set/busy_day.in")
        self.gridx = self.datasetfromfile[0]
        self.gridy = self.datasetfromfile[1]
        self.warehouseObjects = self.datasetfromfile[2]
        self.droneCount = self.datasetfromfile[3]
        self.maxCommands = self.datasetfromfile[4]
        self.maxPayload = self.datasetfromfile[5]
        self.orderObjects = self.datasetfromfile[6]
        self.productWeights = self.datasetfromfile[7]

        # Create the drones
        for i in xrange(self.droneCount):
            self.drones.append(drone.drone(self.warehouseObjects[0].location, self.maxPayload))

        # Calculate the nearest wearhouse to each order and vise-versa
        type(self.orderObjects)
        for order in self.orderObjects:
            calculatedDistances = []
            for wh in self.warehouseObjects:
                calculatedDistances.append(travelTime(order.location,wh.location))
            order.mywarehouse = self.warehouseObjects[calculatedDistances.index(min(calculatedDistances))]
            wh.deliveryPoints.append(order)


        # for wh1 in self.warehouseObjects:
        #     calculatedDistances = []
        #     for wh2 in self.warehouseObjects:
        #         calculatedDistances.append(travelTime(order.location,wh.location)
        #     order.mywarehouse = self.warehouseObjects[calculatedDistances.index(min(calculatedDistances))]


            # wh.excessInventory
            # wh.wishlist
            # for wh1 in self.self.warehouseObjects:
            #     for wh2 in self.self.warehouseObjects:

        self.commandList = list()
        for wh1 in self.warehouseObjects:
            for wh2 in self.warehouseObjects:
                if wh1 == wh2:
                    continue
                for wl in wh1.wishlist:
                    for el in wh2.excessInventory:
                        if wl in el:
                            self.commandList.append((wh1,wh2,wh1.wishlist.index(wl)))
                            wh2.excessInventory.remove(wl)
                            wh2.allProducts.remove(wl)
                            wh1.wishlist.remove(wl)
                            wh1.allProducts.append(wl)
        print self.commandList




        # list of orders

        # How many can we currently delvier to from our inventory





        
    def simulate(self):
        print "CALLED"
        # Loop through time starting zero
        for t in xrange(self.maxCommands):
            for d in self.drones: d.step()
            for i in self.commandList:
                print i
                continue
                for d in self.drones:
                    if not d.checkBusy:
                        print "%i L %i %i %i " % (d.idx,wh1.idx,p,1)

    def travelTime(self, From, To):
        return math.ceil(math.sqrt(pow((From[0] - To[0]),2) + pow((From[1] - To[1]),2)))