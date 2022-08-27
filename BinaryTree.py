from typing import List
from collections import deque


class Node():
    def __init__(self,data) -> None:
        self.data = data
        self.left = self.right = None


class BinaryTree():
    def __init__(self) -> None:
        self.root = None

    # def insert(self,root:Node,data:int):
    #     if data < root.data:
    #         if root.left is None:
    #             root.left = Node(data)
    #         else:
    #             self.insert(root.left, data)
        
    #     if data >= root.data:
    #         if root.right is None:
    #             root.right = Node(data)
    #         else:
    #             self.insert(root.right, data)
    def insert(self, root:Node, data:int):
        if root is None:
            return Node(data)
        if root.data > data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)
        return root

    def find(self,data)->bool:
        return self.__find_helper(self.root,data)

    def __find_helper(self, root:Node,data:int):
        if root is None:
            return False
        
        if root.data == data:
            return True
        
        if data<root.data:
            return self.__find_helper(root.left, data)
        else:
            return self.__find_helper(root.right, data)

    def buildTree(self,elements:List[int]):
        self.root = Node(elements[0])
        index = 0
        try:
            for i in range(1,len(elements)):
                index = i
                self.insert(self.root,elements[i])
        except Exception as e:
            print(e,index)
        return self.root


    def printTree(self,type='inorder'):
        if type == 'inorder':
            self.__inorder(self.root)
        if type == 'preorder':
            self.__preorder(self.root)
        if type == 'postorder':
            self.__postorder(self.root)
        if type == 'preorder_iterative':
            self.__preorder_iterative(self.root)
        if type == 'inorder_iterative':
            self.__inorder_iterative(self.root)
        if type == 'postorder_iterative':
            self.__postorder_iterative(self.root)
        

    def __inorder(self, root):
        if root:
            self.__inorder(root.left)
            print(root.data,end='->')
            self.__inorder(root.right)

    def __preorder(self,root):
        if root:
            print(root.data,end='->')
            self.__preorder(root.left)
            self.__preorder(root.right)

    def __postorder(self, root):
        if root:
            self.__postorder(root.left)
            self.__postorder(root.right)
            print(root.data,end='->')

    def __preorder_iterative(self, root):
        stack = []
        stack.append(root)

        while stack:
            node = stack.pop()
            print(node.data, end='->')
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
    
    def __inorder_iterative(self, root):
        stack = []
        while True:
            if root is not None:
                stack.append(root)
                root = root.left
            else:
                if not stack:
                    break
                root = stack.pop()
                print(root.data,end='->')
                root = root.right

    def __postorder_iterative(self,root):
        stack = []
        stack2 = []
        stack.append(root)
        while stack:
            root = stack.pop()
            stack2.append(root)
            if root.left is not None:
                stack.append(root.left)
            if root.right is not None:
                stack.append(root.right)

        while stack2:
            print(stack2.pop().data,end='->')     

             
            
            
            

if __name__=="__main__":
    bt = BinaryTree()
    elements = [15,12,27,7,14,20,88,23]
    bt.buildTree(elements)
    # print()
    # print('***Inorder***')
    # bt.printTree(type='inorder')
    # print()
    # print('***Preorder***')
    # bt.printTree(type='preorder')
    # print()
    # print('***Postorder***')
    # bt.printTree(type='preorder')
    # print()
    # bt.printTree(type='preorder_iterative')
    # bt.printTree(type='inorder')
    # print()
    # bt.printTree(type='inorder_iterative')
    bt.printTree(type='postorder')
    print()
    bt.printTree(type='postorder_iterative')
        



