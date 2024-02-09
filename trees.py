import random
class Node:
    def __init__(self,d):
        self.left = None
        self.right = None 
        self.data = d 
    def insert(self,d):
        if self.data:
            if d<self.data:
                if self.left is None:
                    self.left = Node(d)
                else:
                    self.left.insert(d)
            elif d>self.data:
                if self.right is None:
                    self.right = Node(d)
                else:
                    self.right.insert(d)
        else:
            self.data=d
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()
    def inorder(self,root):
        res = []
        if root:
            res = root.inorder(root.left)
            res.append(root.data)
            res += root.inorder(root.right)
        return res
    def preorder(self,root):
        res = []
        if root:
            res.append(root.data)
            res += root.inorder(root.left)
            res += root.inorder(root.right)
        return res
    def postorder(self,root):
        res = []
        if root:
            res = root.inorder(root.left)
            res += root.inorder(root.right)
            res.append(root.data)
        return res
        

r_val = int(input("Enter root: "))
root = Node(r_val)

for i in range(10):
    root.insert(random.randint(0,100))

print("Inorder: ",root.inorder(root))
print("Preorder: ",root.preorder(root))
print("Postorder: ",root.postorder(root))