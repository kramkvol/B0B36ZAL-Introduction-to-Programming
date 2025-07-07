class Node:
    def __init__(self, nextNode, prevNode, data):
        self.nextNode = None
        self.prevNode = None
        self.data = data 
 
class LinkedList:
    def __init__(self, head):
        self.head = None
 
class Car:
    def __init__(self, identification, name, brand, price, active):
        self.identification = identification
        self.name = name
        self.brand = brand
        self.price = price
        self.active = active
 
db = LinkedList(None)
 
def init(cars):
    for car in cars:
        add(car)  
 
def add(car):
    new_node = Node(None, None, car) 
    if db.head is None:  
        db.head = new_node 
    else:
        if car.price < db.head.data.price:    
           new_node.nextNode = db.head  
           db.head = new_node
        else:        
            current_node = db.head      
            while current_node.nextNode and current_node.nextNode.data.price <= new_node.data.price:
                current_node = current_node.nextNode
            new_node.nextNode=current_node.nextNode
            current_node.nextNode = new_node
 
 
 
def updateName(identification, name):
    current_node = db.head     
    while current_node:
        if current_node.data.identification == identification:
            current_node.data.name = name
            return
        current_node = current_node.nextNode
    return None    
 
def updateBrand(identification, brand):
    current_node = db.head      
    while current_node:
        if current_node.data.identification == identification:
            current_node.data.brand = brand
            return
        current_node = current_node.nextNode
    return None
 
def activateCar(identification):
    current_node = db.head      # current_node (как i в цикле for)
    while current_node:
        if current_node.data.identification == identification:
            current_node.data.active = True
            return
        current_node = current_node.nextNode
    return None
 
 
 
def deactivateCar(identification):
    current_node = db.head      # current_node (как i в цикле for)
    while current_node:
        if current_node.data.identification == identification:
            current_node.data.active = False
            return
        current_node = current_node.nextNode
    return None
 
def getDatabaseHead():
    return db.head
 
 
def getDatabase():
    return db
 
def calculateCarPrice():
    current_node = db.head    
    result = 0
    while current_node:
        if  current_node.data.active == True:
            result += current_node.data.price
        current_node = current_node.nextNode
    return result
 
 
def clean():
    current_node = db.head    
    while current_node:
        current_node.nextNode = None
        current_node = current_node.nextNode
    db.head = None