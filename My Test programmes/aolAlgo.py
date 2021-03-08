# Driver code 
# fuel = [{ "a":20, "b":40, "c":30 }] 
# excavation = [{ "a":20, "b":30, "c":30 }] 

fuel = [['a',20], ['b',40], ['c',30]] 
excavation = [['a',20], ['b',30], ['c',50]]
vol = 300
noOfMachines = len(excavation) 
mostEffecient = []
for i in range(noOfMachines):
    temp = excavation[i][1]/fuel[i][1]
    mostEffecient.insert(i,temp)
    # mostEffecient.insert(i,fuel[i][0])

mostEffecient.sort()
print("mostEffecient",mostEffecient)
	
def noClosestToOne(listOfNum):
    value_chosen = 1
    for val in range(len(listOfNum)):
        if abs(listOfNum[val] - value_chosen) < minimum:
            final_value = listOfNum[val]
            index = val
            minimum = abs(listOfNum[val] - value_chosen)
    return final_value,index

def printknapSack(vol, excavation, fuel, noOfMachines): 
    mostEffecient = []
    rankedMachine = []
    bestsuit = []
    onehrResult = 0 
    countHrs = 0
    totalexcavation = 0
    addextraMachine = []
    # sum of excavation of machines for 1hr
    for i in range(noOfMachines):        
        onehrResult += excavation[i][1]

    if(onehrResult < vol):

        #sum of Excavation of machines until it exceeds give "vol"
        while (vol> totalexcavation):
            totalexcavation += onehrResult
            countHrs += 1

        if(totalexcavation > vol):
            remainingExcavation = vol - (totalexcavation -onehrResult )
            countHrs -= 1        # we substracted onehrResult from the totalexcavation so countHrs decreased by 1

            # which machine has the closest excavation rate and most efficient
            for i in range(noOfMachines):
                temp2 = remainingExcavation / excavation[i][1]
                bestsuit.insert(i, temp2 )
                print(excavation[i][0])
        
            for i in range(len(bestsuit)):
                if(bestsuit[i] > 1.5):
                    addextraMachine.append(bestsuit[i])
                    print(bestsuit[i])
            
            # thisforcount = 0
            # for i in range(len(bestsuit)):
            #     if(bestsuit[i] > 1.5):
            #         addextraMachine[i].append(bestsuit[i])
            #         thisforcount+=1
            #         print(bestsuit[i])
                
                # if(len(addextraMachine) > 1):
                #     print("asdfsaf")
                # for i in range(len(addextraMachine)):

            print("extra machines to be added", addextraMachine)
            print("bestsuit",bestsuit)

            machineName = noClosestToOne(bestsuit)
            print("Extra machine", machineName)

        
            print("remaining Excavation", remainingExcavation)
            print("1hrResult", onehrResult)
            print("total excavation", totalexcavation)
            print("total no of hrs required where all machines run", countHrs)
            mahineindex = machineName[1]
            print( excavation[mahineindex][0] ,", this machine needs to work", countHrs+1)
            print("Extra machine", machineName)
        else:
            print("each machine need to do",countHrs ," hrs of work")
    else:
        print("excessive machines are being ordered")

    
    

printknapSack(vol, excavation, fuel, noOfMachines) 




