class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None
        
class SLinkedList:
    def __init__(self):
        self.headval = None
        
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval
            
    def is_loop(self):
        first_head = self.headval
        printval = self.headval
        while printval is not None:
            if printval == first_head:
                return True
                break
            
    def InsBegin(self, newdata):
        new_node = Node(newdata)
        new_node.nextval = self.headval
        self.headval = new_node
        
    def InsLast(self, newdata):
        new_node = Node(newdata)
        if self.headval == None:
            self.headval = new_node
            return
        if not is_loop(self):
            lastp = self.headval
            while lastp.nextval:
                lastp = lastp.nextval
            lastp.nextval = new_node
            
    def InBetween(self, middle_node, newdata):
        if middle_node is None:
            print("the mentioned node is absent")
            return
            
list1 = SLinkedList()
list1.headval = Node("Mon")
e2 = Node("tues")
e3 = Node("wed")
e4 = Node("thus")
e5 = Node("fry")
e6 = Node("sat")
e7 = Node("sun")


e2.nextval = e3
e3.nextval = e4
e4.nextval = e5
e5.nextval = e6
e6.nextval = e7
e7.nextval = list1.headval
list1.headval.nextval=e2

if list1.is_loop:
    print("this is loop")
    # list1.listprint()