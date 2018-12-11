import math


def sqInRect(lng, wdth):
    # your code
    #     print("lng:"+str(lng))
    #     print("wdth:"+str(wdth))

    if (lng == wdth):
        return None

    myList = []
    chkLng = lng
    chkWdth = wdth

    def processList():
        nonlocal chkLng
        nonlocal chkWdth
        if (chkLng < chkWdth):  ## width will be smaller and can be added to make square first
            holdWdth = chkWdth
            chkWdth = chkLng
            chkLng = holdWdth

        myList.append(chkWdth)
        chkLng = chkLng - chkWdth  ## after making square check remaining length and see if square exists
        ##print(chkLng)
        if (chkLng > 0):  # if space exists again check for square
            processList()

    processList()
    ##print(myList)
    return myList
