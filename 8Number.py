#Spencer Brinkman
#CSC 380 - Foundations of Artificial Intelligence
#January 26th, 2020


def NumberProblem():
    #Below is just basic User input code to determine which Algorithm and Difficulty to run based on user preference
    x = 1
    while(x == 1):
        print("Welcome to my code for solving the 8 Number Problem! Please select which Algorithm you would like to play!")
        print("1: Breadth First, 2: Depth First, 3: Uniform Cost, 4:Best First, 5: A*1, 6: A*2")
        algchoice = input("Enter algorithm number:")
        if(algchoice == "1"):
            print("You have chosen Breadth First Algorithm")
        if(algchoice == "2"):
            print("You have chosen Depth First Algorithm")
        if(algchoice == "3"):
            print("You have chosen Uniform Cost Algorithm")
        if(algchoice == "4"):
            print("You have chosen Best First Algorithm")
        if(algchoice == "5"):
            print("You have chosen A*1 Algorithm")
        if(algchoice == "6"):
            print("You have chosen A*2 Algorithm")
        print("Is this correct?")
        changechoice = input("Y/N: ")
        if (changechoice == "Y" or changechoice == "y"):
            x = 2
       
   
    y = 1
    while(y == 1):
        print("Now please choose the difficulty. 1: Easy, 2: Medium, 3: Hard")
        diffchoice = input("Enter difficulty number: ")
        if(diffchoice == "1"):
            print("You have selected Easy difficulty")
        if (diffchoice == "2"):
            print("You have selected Medium difficulty")
        if (diffchoice == "3"):
            print("You have selected Hard Difficulty! This is very hard and you may very well make this AI mad and create a Terminator-like situation... Are you sure you'd like to continue?")
            secondprompt = input("Y/N? :")
            if(secondprompt == "Y"):
                print("Okay you've asked for it!")
        print("Are these settings correct?")
        changechoice = input("Y/N: ")
        if (changechoice == "Y" or changechoice == "y"):
              y = 2

    if(algchoice == "1"):
        #Run Breadth First 
        BreadthF(diffchoice)
    if(algchoice == "2"):
        #Run Depth-First
        DF(diffchoice)
    if(algchoice == "3"):
        #Run Uniform-Cost
        UC(diffchoice)
    if(algchoice == "4"):
        #Run Best-First
        BestF(diffchoice)
    if(algchoice == "5"):
        #Run A*1
        A1(diffchoice)
    if(algchoice == "6"):
        #run A*2
        A2(diffchoice)


def NewNode(CurrentPuzzle, cost, parent, depth, moved, HVal, GVal, FVal):
    #code to create and return a new Node object
    return Node(CurrentPuzzle, cost, parent,depth,moved, 0, 0, 0)

class Node:
    #Node clas with values, CurrentPuzzle(current state of the node as a list),cost(value of tile moved), ParentNode, depth from root node, which direction the 0 was moved, Heuristic Value, GValue(cost from root node),
    #and F which is H+G
    def __init__(self, CurrentPuzzle, cost, parent, depth, moved, HVal, GVal, FVal):
        self.CurrentPuzzle = CurrentPuzzle
        self.cost = cost
        self.parent = parent
        self.depth = depth
        self.moved = moved
        self.HVal = HVal
        self.GVal = GVal
        self.FVal = FVal





def up(CurrentPuzzle, CurrentCost, CurrentNode, uniquenodes):
    #Moves the 0 in the up direction
    #Creates a new list called newpuzzle
    newpuzzle = CurrentPuzzle[:]
    #finds the location of the 0 tile
    location = newpuzzle.index(0)
    
   
    if(location == 0 or location == 1 or location == 2):
        #if 0 is in the top row it can't move up so return None
        return None
    else:
        #else swap values
        num = newpuzzle[location - 3]
       
        newpuzzle[location - 3] = 0
        newpuzzle[location] = num
        if(newpuzzle in uniquenodes):
            #check if already expanded 
            return None
        else:
            #returns a new node where the 0 was moved up
            return NewNode(newpuzzle, num, CurrentNode, depth(CurrentNode), "Moved UP", 0, 0, 0)
     

def down(CurrentPuzzle, CurrentCost, CurrentNode, uniquenodes):
    #moves 0 down
    newpuzzle = CurrentPuzzle[:]
    location = newpuzzle.index(0)
    if(location == 6 or location == 7 or location == 8):
        #if 0 in bottom row return None
        return None
   
    else:
        num = newpuzzle[location + 3]
     
        newpuzzle[location + 3] = 0
        newpuzzle[location] = num
        if(newpuzzle in uniquenodes):
            return None
        else:
            return NewNode(newpuzzle, num, CurrentNode, depth(CurrentNode), "Moved DOWN", 0, 0, 0)
   
def left(CurrentPuzzle, CurrentCost, CurrentNode, uniquenodes):
    #moves 0 left
    newpuzzle = CurrentPuzzle[:]
    location = newpuzzle.index(0)
    if(location == 0 or location == 3 or location == 6):
        #if 0 in leftmost column, return None
        return None
    else:
        num = newpuzzle[location - 1]
       
        newpuzzle[location - 1] = 0
        newpuzzle[location] = num
        if(newpuzzle in uniquenodes):
            return None
        else:
            return NewNode(newpuzzle, num, CurrentNode,depth(CurrentNode), "Moved LEFT", 0, 0, 0)
       

def right(CurrentPuzzle, CurrentCost, CurrentNode, uniquenodes):
    newpuzzle = CurrentPuzzle[:]
    location = newpuzzle.index(0)
    if(location == 2 or location == 5 or location == 8):
        return None
    else:
        num = newpuzzle[location + 1]
        newpuzzle[location + 1] = 0
        newpuzzle[location] = num
        if(newpuzzle in uniquenodes):
            return None
        else:
            return NewNode(newpuzzle, num, CurrentNode, depth(CurrentNode), "Moved RIGHT",0, 0, 0)
       
def depth(CurrentNode):
    #returns depth of Node, e.g. depth of its parent + 1
    NodeDepth = CurrentNode.depth + 1

    return NodeDepth

       

def BreadthF(diffchoice):
    #Breadth first choice
    #sets goal puzzle to whichever difficulty was chosen
    if(diffchoice == "1"):
        puzzle = [1, 3, 4, 8, 6, 2, 7, 0, 5]
        print("Starting puzzle =", puzzle)
    elif(diffchoice == "2"):
        puzzle = [2, 8, 1, 0, 4, 3, 7, 6, 5]
    else:
        puzzle = [5, 6, 7, 4, 0, 8, 3, 2, 1]
    #setting variables to use later
    cost = 0
    #uniquenodes will store the history of nodes expanded so there are no repeats
    uniquenodes = []
    #queue to expand nodes through
    q = []
    #setting root node to the start node
    root = NewNode(puzzle, 0, 0, 0, "Starting node", 0, 0, 0)
    #Maximumspace will be compared later to find the Space(largest size of queue)
    MaximumSpace = 1
    #setting time to 0 to increment every expansion
    time = 0
    
    q.append(root)
    goalpuzzle = [1, 2, 3, 8, 0, 4, 7, 6, 5]
    while(q[0].CurrentPuzzle != goalpuzzle):
        CurrentNode = q[0]
        time+= 1
        uniquenodes.append(CurrentNode.CurrentPuzzle)
        print(CurrentNode.CurrentPuzzle)
        cost += CurrentNode.cost
        #Output that will be seen on interface
        print(CurrentNode.moved, " " , "cost = ", CurrentNode.cost, ", total cost = ", cost)
        #Now compute all up,down,left,right. These functions also take care of creating the node
        upnode = up(CurrentNode.CurrentPuzzle, 0, CurrentNode, uniquenodes)
        q.append(upnode)
        downnode = down(CurrentNode.CurrentPuzzle, 0, CurrentNode, uniquenodes)
        q.append(downnode)
        leftnode = left(CurrentNode.CurrentPuzzle, 0, CurrentNode, uniquenodes)
        q.append(leftnode)
        rightnode = right(CurrentNode.CurrentPuzzle, 0, CurrentNode, uniquenodes)
        q.append(rightnode)
        #set space =  0 to find MaximumSpace in for loop below
        space = 0
        for i in q:
            #remove any None value
            if(i == None):
                q.remove(i)
       
            else:
                #after the for loop this will tell us the size of the Queue
                space+= 1
        if(space > MaximumSpace):
            #will find Maximum queue size once the program is all done
            MaximumSpace = space
            
        #pop the queue to go on to next one    
        q.pop(0)
       
    #while loop done which means solution is found

    cost+= q[0].cost
    #add the final node cost to cost
    #same with space
    space+= 1
    print(q[0].CurrentPuzzle)
    
   
    print("Success!")
    print("Size of queue at largest(space): ", MaximumSpace, " , Nodes popped off queue: ", time, " Depth to solution: ",q[0].depth)
    print("Final cost: ", cost)
   

def DF(diffchoice):
    #Depth First search
    if(diffchoice == "1"):
        puzzle = [1, 3, 4, 8, 6, 2, 7, 0, 5]
    elif(diffchoice == "2"):
        puzzle = [2, 8, 1, 0, 4, 3, 7, 6, 5]
    else:
        puzzle = [5, 6, 7, 4, 0, 8, 3, 2, 1]
    cost = 0
    time = 0
    MaximumSpace = 1
    uniquenodes = []
    stack = []
    #Depth first will utilize a stack this time by performing Last-In First-Out
    root = NewNode(puzzle, 0, 0, 0, "Starting node", 0, 0, 0)
    stack.append(root)
    CurrentNode = root
    goalpuzzle = [1, 2, 3, 8, 0, 4, 7, 6, 5]
    while(CurrentNode.CurrentPuzzle != goalpuzzle):
        #pop the stack and have it equal to CurrentNode
        CurrentNode = stack.pop()
        space = 0
        time+= 1
        while(CurrentNode == None):
            #remove Nones from stack
            CurrentNode = stack.pop()
        for i in stack:
            #find length of stack
            space+= 1
        if(space > MaximumSpace):
            MaximumSpace = space
        uniquenodes.append(CurrentNode.CurrentPuzzle)
        print(CurrentNode.CurrentPuzzle)
        cost += CurrentNode.cost
        print(CurrentNode.moved, " " , "cost = ", CurrentNode.cost, ", total cost = ", cost)
        upnode = up(CurrentNode.CurrentPuzzle, 0, CurrentNode, uniquenodes)
        stack.append(upnode)
        downnode = down(CurrentNode.CurrentPuzzle, 0, CurrentNode, uniquenodes)
        stack.append(downnode)
        leftnode = left(CurrentNode.CurrentPuzzle, 0, CurrentNode, uniquenodes)
        stack.append(leftnode)
        rightnode = right(CurrentNode.CurrentPuzzle, 0, CurrentNode, uniquenodes)
        stack.append(rightnode)
    
    
    print("Success")
    print(CurrentNode.CurrentPuzzle)
    print("Size of queue at largest(space): ", MaximumSpace, " , Nodes popped off queue: ", time, "Depth to solution: ", CurrentNode.depth)
    print("Final Cost: ", cost)



def UC(diffchoice):
    #Uniform-Cost Search
    #works for easy. Doesn't work for Medium/Hard due to prioritizing everything over bigger numbers such as 6, 7, and 8.
    if(diffchoice == "1"):
        puzzle = [1, 3, 4, 8, 6, 2, 7, 0, 5]
        print("Starting puzzle =", puzzle)
    elif(diffchoice == "2"):
        puzzle = [2, 8, 1, 0, 4, 3, 7, 6, 5]
    else:
        puzzle = [5, 6, 7, 4, 0, 8, 3, 2, 1]
    cost = 0
    uniquenodes = []
    q = []
    root = NewNode(puzzle, 0, 0, 0, "Starting Node", 0, 0, 0)
    q.append(root)
    CurrentNode = root
    time = 0
    MaximumSpace = 1
    goalpuzzle = [1, 2, 3, 8, 0, 4, 7, 6, 5]
    while(q[0].CurrentPuzzle!= goalpuzzle):
        CurrentNode = q[0]
        q.pop(0)
        print(CurrentNode.CurrentPuzzle)
        print("Depth: ", CurrentNode.depth)
        uniquenodes.append(CurrentNode.CurrentPuzzle)
        time+= 1
        cost+= CurrentNode.cost
        print(CurrentNode.moved, ", Cost: ", CurrentNode.cost, " Total cost: ", cost)
        upnode = up(CurrentNode.CurrentPuzzle, 0, CurrentNode, uniquenodes)
        q.append(upnode)
       
        downnode = down(CurrentNode.CurrentPuzzle, 0, CurrentNode, uniquenodes)
        q.append(downnode)
        leftnode = left(CurrentNode.CurrentPuzzle, 0, CurrentNode, uniquenodes)
        q.append(leftnode)
        
        rightnode = right(CurrentNode.CurrentPuzzle, 0, CurrentNode, uniquenodes)
        q.append(rightnode)
        #set minimumValue to 9 to comapare cost of each Node to below.
        minimumvalue = 9
        
        space = 0
        for i in q:
            if(i == None):
                #remove Nones
                q.remove(i)
            elif(i.cost < minimumvalue):
                space+=1
                #set minimum value to i.cost, e.g. finds the smallest cost change in the for loop
                minimumvalue = i.cost
                #swaps values in the q, moves the lowest cost to q[0]
                pos = q.index(i)
                num = q[0]
                q[0] = i
                q[pos] = num
                #print(i.cost)
                #CurrentNode = i
                #print("Queue : ", i.CurrentPuzzle)
            else:
                space+=1
        if(space > MaximumSpace):
            MaximumSpace = space
        
               


    #Successful, add cost, and print details           
    cost+= CurrentNode.cost    
    #space+= 1
    print(q[0].CurrentPuzzle)
    print("Success!")
    print("Size of queue at largest(space): ", MaximumSpace, " , Nodes popped off queue: ", time, ", Depth to solution: ", q[0].depth)
    print("Final cost: ", cost)
    return




def BestF(diffchoice):
    #h value = number of tiles NOT in correct position
    if(diffchoice == "1"):
        puzzle = [1, 3, 4, 8, 6, 2, 7, 0, 5]
        print("Starting puzzle =", puzzle)
    elif(diffchoice == "2"):
        puzzle = [2, 8, 1, 0, 4, 3, 7, 6, 5]
        print("Starting puzzle =", puzzle)
    else:
        puzzle = [5, 6, 7, 4, 0, 8, 3, 2, 1]
        print("Starting puzzle =", puzzle)
    cost = 0
    uniquenodes = []
    q = []
    root = BestFNewNode(puzzle, 0, 0, 0, "Starting Node", 12, 0, 0)
    q.append(root)
    CurrentNode = root
    time = 0
    MaximumSpace = 1
    goalpuzzle = [1, 2, 3, 8, 0, 4, 7, 6, 5]
    while(q):

        uniquenodes.append(CurrentNode.CurrentPuzzle)
        time+= 1
        cost+= CurrentNode.cost
        print(CurrentNode.moved, ", Cost: ", CurrentNode.cost, " Total cost: ", cost)
        #Created new Up,down,left,right functions due to adding H Values
        upnode = BestFup(CurrentNode.CurrentPuzzle, 0, CurrentNode, uniquenodes, goalpuzzle)
        q.append(upnode)
        downnode = BestFdown(CurrentNode.CurrentPuzzle, 0, CurrentNode, uniquenodes, goalpuzzle)
        q.append(downnode)
        leftnode = BestFleft(CurrentNode.CurrentPuzzle, 0, CurrentNode, uniquenodes, goalpuzzle)
        q.append(leftnode)
        rightnode = BestFright(CurrentNode.CurrentPuzzle, 0, CurrentNode, uniquenodes, goalpuzzle)
        q.append(rightnode)
        #setting HVal to 10 to later compare to find node with smallest H Value
        minimumHVal = 10
        stack = []
        space = 0
        for i in q:
            if(i == None):
                #print("removed")
                q.remove(i)
            elif(i.HVal < minimumHVal):
               # print("Node: ", i.CurrentPuzzle)
                #print("Value: ", i.HVal)
                space+= 1
                minimumHVal = i.HVal
                #append lowest HValue to stack to easily obtain
                stack.append(i)
            else:
                space+=1
        if(space > MaximumSpace):
            MaximumSpace = space
        #remove from stack and save Node to num
        num = stack.pop()
        if(num.CurrentPuzzle == goalpuzzle):
            cost+= num.cost
            print("Success")
            print("Puzzle: ", num.CurrentPuzzle)
            print("Final cost: ", cost)
            print("Size of queue at largest(space): ", MaximumSpace, " , Nodes popped off queue: ", time, ", Depth to solution: ",num.depth) 
            return 
        print(num.CurrentPuzzle)
        #remove Num from Q if not equal to goalpuzzle
        q.remove(num)
        CurrentNode = num
       
       



def findHVal(CurrentPuzzle, goalpuzzle):
    #function to Find the HValue for BestFirst and A*1(not A*2)
    HValue = 0
    if(CurrentPuzzle == None):
        #return None if Node = None
        return None
    else:
        #creates a NewPuzzle
        NewPuzzle = CurrentPuzzle[:]
    for i in range(0,9):
        if(NewPuzzle[i] != goalpuzzle[i]):
            #if tile not in correct position, add 1 to HValue
            HValue+= 1
   
    return HValue



def BestFup(CurrentPuzzle, CurrentCost, CurrentNode, uniquenodes, goalpuzzle):
   
    #Up function for Best First. Same As above, except it runs findHVal to determine HValue of the node
    newpuzzle = CurrentPuzzle[:]
    location = newpuzzle.index(0)
   
    if(location == 0 or location == 1 or location == 2):
        return None
    else:
        num = newpuzzle[location - 3]
       
        newpuzzle[location - 3] = 0
        newpuzzle[location] = num
        if(newpuzzle in uniquenodes):
            return None
        #print("moved up")
        #print(newpuzzle)
        else:
            #print("UP node: ", newpuzzle)
            return BestFNewNode(newpuzzle, num, CurrentNode, depth(CurrentNode),"moved UP", findHVal(newpuzzle, goalpuzzle), 0, 0)
     

def BestFdown(CurrentPuzzle, CurrentCost, CurrentNode, uniquenodes, goalpuzzle):
    #down function for Best First. Same As above, except it runs findHVal to determine HValue of the node
    newpuzzle = CurrentPuzzle[:]
    location = newpuzzle.index(0)
    if(location == 6 or location == 7 or location == 8):
        return None
   
    else:
        num = newpuzzle[location + 3]
     
        newpuzzle[location + 3] = 0
        newpuzzle[location] = num
        if(newpuzzle in uniquenodes):
            return None
        else:
            return BestFNewNode(newpuzzle, num, CurrentNode, depth(CurrentNode), "moved DOWN", findHVal(newpuzzle, goalpuzzle), 0, 0)
   
def BestFleft(CurrentPuzzle, CurrentCost, CurrentNode, uniquenodes, goalpuzzle):
    #Left function for Best First. Same As above, except it runs findHVal to determine HValue of the node
    newpuzzle = CurrentPuzzle[:]
    location = newpuzzle.index(0)
    if(location == 0 or location == 3 or location == 6):
        return None
    else:
        num = newpuzzle[location - 1]
       
        newpuzzle[location - 1] = 0
        newpuzzle[location] = num
        if(newpuzzle in uniquenodes):
            return None
        else:
            return BestFNewNode(newpuzzle, num, CurrentNode, depth(CurrentNode), "Moved LEFT", findHVal(newpuzzle, goalpuzzle), 0, 0)
       

def BestFright(CurrentPuzzle, CurrentCost, CurrentNode, uniquenodes, goalpuzzle):
    #Right function for Best First. Same As above, except it runs findHVal to determine HValue of the node
    newpuzzle = CurrentPuzzle[:]
    location = newpuzzle.index(0)
    if(location == 2 or location == 5 or location == 8):
        return None
    else:
        num = newpuzzle[location + 1]
        newpuzzle[location + 1] = 0
        newpuzzle[location] = num
        if(newpuzzle in uniquenodes):
            return None
        else:
            return BestFNewNode(newpuzzle, num, CurrentNode, depth(CurrentNode), "Moved RIGHT", findHVal(newpuzzle, goalpuzzle), 0, 0)
       



def BestFNewNode(CurrentPuzzle, cost, parent, depth, moved, HValue, GValue, FValue):
    #NewNode function for Best First same as Above except it returns an HValue
    return Node(CurrentPuzzle, cost, parent, depth, moved, HValue, 0, 0)


def A1(diffchoice):
    #A*1 algorithm. F(n) = G(n) + H(n), where G(n) is total cost from root node and H(n) is # tiles not in correct
    #position
    if(diffchoice == "1"):
        puzzle = [1, 3, 4, 8, 6, 2, 7, 0, 5]
        print("Starting puzzle =", puzzle)
    elif(diffchoice == "2"):
        puzzle = [2, 8, 1, 0, 4, 3, 7, 6, 5]
        print("Starting puzzle =", puzzle)
    else:
        puzzle = [5, 6, 7, 4, 0, 8, 3, 2, 1]
        print("Starting puzzle =", puzzle)
    cost = 0
    uniquenodes = []
    q = []
    #create a new root node, sets HVal to 12 to not mess with below comparison and similar again with F Value
    root = A1NewNode(puzzle, 0, 0, 0, 0, 12, 0, 100000)
    q.append(root)
    CurrentNode = root
    time = 0
    MaximumSpace = 1
    goalpuzzle = [1, 2, 3, 8, 0, 4, 7, 6, 5]
    while(q):
        #CurrentNode = q[0]
        #q.pop(0)
        uniquenodes.append(CurrentNode.CurrentPuzzle)
        print("HVal: ", CurrentNode.HVal)
        print("GVal: ", CurrentNode.GVal)
        time+= 1
        cost+= CurrentNode.cost
        print(CurrentNode.moved, ", Cost: ", CurrentNode.cost, " Total cost: ", cost)
        #Up,left,right,down functions specifically for A1.
        upnode = A1up(CurrentNode.CurrentPuzzle, cost, CurrentNode, uniquenodes, goalpuzzle)
        q.append(upnode)
        downnode = A1down(CurrentNode.CurrentPuzzle, cost, CurrentNode, uniquenodes, goalpuzzle)
        q.append(downnode)
        leftnode = A1left(CurrentNode.CurrentPuzzle, cost, CurrentNode, uniquenodes, goalpuzzle)
        q.append(leftnode)
        rightnode = A1right(CurrentNode.CurrentPuzzle, cost, CurrentNode, uniquenodes, goalpuzzle)
        q.append(rightnode)
        #sets MinimumFVal for comparison below to find lowest F Value
        minimumFVal = 10000
        stack = []
        space = 0
        for i in q:
            if(i == None):
                q.remove(i)
            elif(i.FVal < minimumFVal):
                space+=1
                minimumFVal = i.FVal
                stack.append(i)
            else:
                space+=1
        if(space > MaximumSpace):
            MaximumSpace = space
        
        
        num = stack.pop()
        
        print(num.CurrentPuzzle)
        if(num.CurrentPuzzle == goalpuzzle):
            #print(num.HVal)
            cost+= num.cost
            print("Success!")
            print("Puzzle :" , num.CurrentPuzzle)
            print("Final cost: ", cost)
            print("Size of queue at max(space): ", space, ", Time: ", time, ", Depth to solution: ", num.depth)
            return
            
            
        q.remove(num)
        CurrentNode = num

def findFVal(CurrentPuzzle, HVal, GVal):
    #finds the F Value, e.g HVal + GVal. This function works for BOTH A*1 and A*2 as the HValue for A*2 is just replaced to be the Manhattan Distance instead of misplaced tiles
    FValue = 0
    if(CurrentPuzzle == None):
        return None
    else:
        #totalcost+= cost
        #HValue = CurrentPuzzle.HVal
        FValue = HVal + GVal
        return FValue




def A1up(CurrentPuzzle, CurrentCost, CurrentNode, uniquenodes, goalpuzzle):
    #Up function for A1

    newpuzzle = CurrentPuzzle[:]
    location = newpuzzle.index(0)
    HVal = 0
   
    if(location == 0 or location == 1 or location == 2):
        return None
    else:
        num = newpuzzle[location - 3]
       
        newpuzzle[location - 3] = 0
        newpuzzle[location] = num
        if(newpuzzle in uniquenodes):
            return None
        else:
            #compute both HValue and GValue and then call findFVal to find FValue
            HVal = findHVal(newpuzzle, goalpuzzle)
            GVal = findGVal(newpuzzle, CurrentNode, num)
            return A1NewNode(newpuzzle, num, CurrentNode, depth(CurrentNode), "Moved UP", HVal, GVal,findFVal(newpuzzle,HVal, GVal))
     

def A1down(CurrentPuzzle, CurrentCost, CurrentNode, uniquenodes, goalpuzzle):
    #down function for A1
    newpuzzle = CurrentPuzzle[:]
    location = newpuzzle.index(0)
    HVal = 0
    #print(location)
    if(location == 6 or location == 7 or location == 8):
        return None
   
    else:
        num = newpuzzle[location + 3]
     
        newpuzzle[location + 3] = 0
        newpuzzle[location] = num
        if(newpuzzle in uniquenodes):
            return None
        else:
            #compute both HValue and GValue and then call findFVal to find FValue
            HVal = findHVal(newpuzzle, goalpuzzle)
            GVal = findGVal(newpuzzle, CurrentNode, num)
            return A1NewNode(newpuzzle, num, CurrentNode, depth(CurrentNode), "Moved DOWN", HVal,GVal, findFVal(newpuzzle, HVal, GVal))
   
def A1left(CurrentPuzzle, CurrentCost, CurrentNode, uniquenodes, goalpuzzle):
    #left for A1
    newpuzzle = CurrentPuzzle[:]
    location = newpuzzle.index(0)
    HVal = 0
    if(location == 0 or location == 3 or location == 6):
        return None
    else:
        num = newpuzzle[location - 1]
       
        newpuzzle[location - 1] = 0
        newpuzzle[location] = num
        if(newpuzzle in uniquenodes):
            return None
        else:
        #compute both HValue and GValue and then call findFVal to find FValue#
            HVal = findHVal(newpuzzle, goalpuzzle)
            GVal = findGVal(newpuzzle, CurrentNode, num)
            return A1NewNode(newpuzzle, num, CurrentNode, depth(CurrentNode), "Moved LEFT", HVal, GVal, findFVal(newpuzzle, HVal, GVal))
       

def A1right(CurrentPuzzle, CurrentCost, CurrentNode, uniquenodes, goalpuzzle):
    #Right for A1
    newpuzzle = CurrentPuzzle[:]
    location = newpuzzle.index(0)
    HVal = 0
    if(location == 2 or location == 5 or location == 8):
        return None
    else:
        num = newpuzzle[location + 1]
        newpuzzle[location + 1] = 0
        newpuzzle[location] = num
        if(newpuzzle in uniquenodes):
            return None
        else:
       #compute both HValue and GValue and then call findFVal to find FValue
            HVal = findHVal(newpuzzle, goalpuzzle)
            GVal = findGVal(newpuzzle, CurrentNode, num)
            return A1NewNode(newpuzzle, num, CurrentNode, depth(CurrentNode), "Moved RIGHT", HVal, GVal,findFVal(newpuzzle,HVal, GVal))

def findGVal(newpuzzle, parent, cost):
    #Computes the G Value, e.g. cost from root node to the current node, so just add Cost of current puzzle to parent node'sG Value
    if(newpuzzle == None):
        return None
    parentnode = parent
    GValue = cost + parentnode.GVal
    return GValue
    
       



def A1NewNode(CurrentPuzzle, cost, parent, depth, moved, HVal, GVal, FVal):
    #Creates a new node for A1, using HVal, GVal, and FVal
    return Node(CurrentPuzzle, cost, parent, depth, moved, HVal, GVal, FVal)



def A2(diffchoice):
    #A*2 algorithm, where g = total cost from root node, h = Manhattan distance
    if(diffchoice == "1"):
        puzzle = [1, 3, 4, 8, 6, 2, 7, 0, 5]
        print("Starting puzzle =", puzzle)
    elif(diffchoice == "2"):
        puzzle = [2, 8, 1, 0, 4, 3, 7, 6, 5]
        print("Starting puzzle =", puzzle)
    else:
        puzzle = [5, 6, 7, 4, 0, 8, 3, 2, 1]
        print("Starting puzzle =", puzzle)
    cost = 0
    uniquenodes = []
    q = []
    root = A1NewNode(puzzle, 0, 0, 0, 0, 12, 0, 100000)
    q.append(root)
    CurrentNode = root
    time = 0
    MaximumSpace = 1
    goalpuzzle = [1, 2, 3, 8, 0, 4, 7, 6, 5]
    while(q):
        uniquenodes.append(CurrentNode.CurrentPuzzle)
        time+= 1
        cost+= CurrentNode.cost
        print("Depth: ", CurrentNode.depth)
        print(CurrentNode.moved, ", Cost: ", CurrentNode.cost, " Total cost: ", cost)
        #A2 has its own up,down,left,right functions to deal with the Manhattan Distance
        upnode = A2up(CurrentNode.CurrentPuzzle, cost, CurrentNode, uniquenodes, goalpuzzle)
        q.append(upnode)
        downnode = A2down(CurrentNode.CurrentPuzzle, cost, CurrentNode, uniquenodes, goalpuzzle)
        q.append(downnode)
        leftnode = A2left(CurrentNode.CurrentPuzzle, cost, CurrentNode, uniquenodes, goalpuzzle)
        q.append(leftnode)
        rightnode = A2right(CurrentNode.CurrentPuzzle, cost, CurrentNode, uniquenodes, goalpuzzle)
        q.append(rightnode)
        minimumFVal = 10000
        stack = []
        space = 0
        for i in q:
            if(i == None):
                q.remove(i)
            elif(i.FVal < minimumFVal):
                #finds smallest F Value(H + G) and appends it to a stack for easy access
                minimumFVal = i.FVal
                stack.append(i)
                space+=1
            else:
                space+=1
        if(space > MaximumSpace):
            MaximumSpace = space
        
              
        num = stack.pop()
        print(num.CurrentPuzzle)
        if(num.CurrentPuzzle == goalpuzzle):
            #print(num.HVal)
            cost+= num.cost
            print("Success!")
            print("Puzzle :" , num.CurrentPuzzle)
            print("Final cost: ", cost)
            print("Size of queue at max(space): ", space, ", Time: ", time, ", Depth to solution: ", num.depth)
            return
            
            
        q.remove(num)
        #remove from the Queue
        CurrentNode = num
    



def findManhattanVal(CurrentPuzzle, goalpuzzle):
    #finds the Manhattan Distance for a puzzle
    #Idea behind this logic is seen below where the left 2d array is the starting easy puzzle and the right is the goal
    #Now I converted both in list format to a 2d array since it is easier to then compare Manhattan distance in a 2d array format
    #1 3 4      1 2 3
    #8 6 2      8 0 4
    #7 0 5      7 6 5

#created a dictionary where the index of the list format is the key to the value of which it represents in a 2d array. So [0] in list would equal [0,0](top left) in a 2d array and so on
    newdict = {
	0: [0,0],
	1: [0,1],
	2: [0,2],
	3: [1,0],
	4: [1,1],
	5: [1,2],
	6: [2,0],
	7: [2,1],
	8: [2,2]
}
    ManhattanVal = 0
    if(CurrentPuzzle == None):
        #return None if None
        return None
    else:
        NewPuzzle = CurrentPuzzle[:]
        for i in range(0, 9):
            #for loop through 0,9(lengths of both puzzle and goalpuzzle)
            if(NewPuzzle[i] != goalpuzzle[i]):
                
		#finds tiles not in right position
                #sets the index to num
                num = i
                #finds where the same number in NewPuzzle is location in the GoalPuzzle
                goalnum = goalpuzzle.index(NewPuzzle[i])
                for x, y in newdict.items():
                    #for loop through the keys(x) and values(y) in newdict
                    if(x == num):
                        #finds the 2d array indices associated with the index of the list
                        newpuzzleindices = y
                    elif(x == goalnum):
                        #same but does it for GoalPuzzle
                        goalpuzzleindices = y
                #now do the math for the manhattan distance which is abs(row-row) + abs(column-column) and sum all of them
                ManhattanVal+= abs(newpuzzleindices[0] - goalpuzzleindices[0]) + abs(newpuzzleindices[1] - goalpuzzleindices[1])

    return ManhattanVal


            
            
            
def A2up(CurrentPuzzle, CurrentCost, CurrentNode, uniquenodes, goalpuzzle):
   
    #Up for A2
    newpuzzle = CurrentPuzzle[:]
    location = newpuzzle.index(0)
    HVal = 0
   
    if(location == 0 or location == 1 or location == 2):
        return None
    else:
        num = newpuzzle[location - 3]
       
        newpuzzle[location - 3] = 0
        newpuzzle[location] = num
        if(newpuzzle in uniquenodes):
            return None
        else:
            HVal = findManhattanVal(newpuzzle, goalpuzzle)
            GVal = findGVal(newpuzzle, CurrentNode, num)
            return A1NewNode(newpuzzle, num, CurrentNode, depth(CurrentNode), "Moved UP", HVal, GVal,findFVal(newpuzzle,HVal, GVal))
     

def A2down(CurrentPuzzle, CurrentCost, CurrentNode, uniquenodes, goalpuzzle):
    #Down for A2
    newpuzzle = CurrentPuzzle[:]
    location = newpuzzle.index(0)
    HVal = 0
    #print(location)
    if(location == 6 or location == 7 or location == 8):
        return None
   
    else:
        num = newpuzzle[location + 3]
     
        newpuzzle[location + 3] = 0
        newpuzzle[location] = num
        if(newpuzzle in uniquenodes):
            return None
        else:
            HVal = findManhattanVal(newpuzzle, goalpuzzle)
            GVal = findGVal(newpuzzle, CurrentNode, num)
            return A1NewNode(newpuzzle, num, CurrentNode, depth(CurrentNode), "Moved DOWN", HVal,GVal, findFVal(newpuzzle, HVal, GVal))
   
def A2left(CurrentPuzzle, CurrentCost, CurrentNode, uniquenodes, goalpuzzle):
    #Left for A2
    newpuzzle = CurrentPuzzle[:]
    location = newpuzzle.index(0)
    HVal = 0
    if(location == 0 or location == 3 or location == 6):
        return None
    else:
        num = newpuzzle[location - 1]
       
        newpuzzle[location - 1] = 0
        newpuzzle[location] = num
        if(newpuzzle in uniquenodes):
            return None
        else:
        #print("moved left")
        #print(newpuzzle)
            HVal = findManhattanVal(newpuzzle, goalpuzzle)
            GVal = findGVal(newpuzzle, CurrentNode, num)
            return A1NewNode(newpuzzle, num, CurrentNode, depth(CurrentNode), "Moved LEFT", HVal, GVal, findFVal(newpuzzle, HVal, GVal))
       

def A2right(CurrentPuzzle, CurrentCost, CurrentNode, uniquenodes, goalpuzzle):
    #right for A2
    newpuzzle = CurrentPuzzle[:]
    location = newpuzzle.index(0)
    HVal = 0
    if(location == 2 or location == 5 or location == 8):
        return None
    else:
        num = newpuzzle[location + 1]
        newpuzzle[location + 1] = 0
        newpuzzle[location] = num
        if(newpuzzle in uniquenodes):
            return None
        else:
            HVal = findManhattanVal(newpuzzle, goalpuzzle)
            GVal = findGVal(newpuzzle, CurrentNode, num)
            return A1NewNode(newpuzzle, num, CurrentNode, depth(CurrentNode), "Moved RIGHT", HVal, GVal,findFVal(newpuzzle,HVal, GVal))    
    



    
