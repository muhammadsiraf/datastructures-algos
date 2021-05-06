import collections

Node = collections.namedtuple('Node', ['left', 'right', 'value'])

def contains(root, value):
    print("this value", root.value)
    if root.value == value:
        print("found")
        return True
    
    if root.right!=None:
        return contains(root.right, value)
    elif root.left!=None:
        return contains(root.left, value)
            
n20 = Node(value=232, left=None, right=None)
n3 = Node(value=3, left=n6, right=n7)
n2 = Node(value=4, left=n1, right=n3)
n4 = Node(value=5, left=n8, right=n9)
n5 = Node(value=6, left=n10, right=n11)
n6 = Node(value=62, left=n12, right=n13)
n7 = Node(value=7, left=n14, right=n15)
n8 = Node(value=10, left=n16, right=n17)
n9 = Node(value=22, left=n18, right=n19)
n10 = Node(value=32, left=n20, right=None)
n11 = Node(value=42, left=None, right=None)
n12 = Node(value=62, left=None, right=None)
n13 = Node(value=32, left=None, right=None)
n14 = Node(value=32, left=None, right=None)
n15 = Node(value=452, left=None, right=None)
n16 = Node(value=62, left=None, right=None)
n17 = Node(value=62, left=None, right=None)
n18 = Node(value=232, left=None, right=None)
n19 = Node(value=342, left=None, right=None)
n1 = Node(value=1, left=n4, right=n5)

        
print(contains(n2, 3))