# -*- coding: utf-8 -*-
import Warehouse
import order

def readFile(fileName):
    f = ""

    with open(fileName) as file:
        f = file.read()

    f = f.split("\n")

    firstLine = f[0]
    firstLine = firstLine.split(" ")

    gridx = int(firstLine[0])
    gridy = int(firstLine[1])
    droneCount = int(firstLine[2])
    maxCommands = int(firstLine[3])
    maxPayload = int(firstLine[4])

    secLine = f[1]

    productCount = int(secLine)

    thLine = f[2]
    thLine = thLine.split(" ")

    for i in thLine:
        i = int(i)

    productWeights = thLine

    warehouseCount = int(f[3])
    
    newF = f[4:]

    listofwarehouseobjects = []

    for i in xrange(0, warehouseCount):
        print "loading warehouse: " + str(i)
        flin = newF[0]
        flin = flin.split(" ")

        location = [int(flin[0]), int(flin[1])]

        flin2 = newF[1]
        flin2 = flin2.split(" ")

        wobj = Warehouse.warehouse(location, flin2)

        listofwarehouseobjects.append(wobj)

        newF = newF[2:]

    """print productWeights

    print "Gridx " + str(gridx)
    print "Gridy " + str(gridy)
    print "dronecount " + str(droneCount)
    print "maxcommands " + str(maxCommands)
    print "maxpayload " + str(maxPayload)
    print "product count " + str(productCount)
    print "warehouseCount " + str(warehouseCount)"""

    nOrders = newF[0]
    newF = newF[1:]

    orderList = []

    for i in xrange(0, len(nOrders)):
        line = newF[0]
        line = line.split(" ")
        line[0] = int(line[0])
        line[1] = int(line[1])
        olocation = line
        oquan = int(newF[1])
        line = newF[2]
        line = line.split(" ")
        for j in xrange(0, len(line)):
            line[j] = int(line[j])
        oids = line
        obj = order.order(i, olocation, oquan, oids)

        newF = newF[3:]

    return gridx, gridy, listofwarehouseobjects, droneCount, maxCommands, maxPayload, orderList, productWeights