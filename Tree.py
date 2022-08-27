class Tree():
    def __init__(self,data) -> None:
        self.data = data
        self.parent = None
        self.children = []

    
    def add_child(self,child):
        child.parent = self
        self.children.append(child)

    def get_level(self,root):
        level = 0
        p = root.parent
        while p:
            level+=1
            p = p.parent
        return level

    def printTree(self):
        level = self.get_level(self)
        print("|-"*level,end="")
        print(self.data)
        for child in self.children:
            child.printTree()

    def delete_tree(self,data):
        for index,child in enumerate(self.children):
            if child.data == data:
                del self.children[index]
                break


if __name__=="__main__":
    fav_animes = Tree("Favoruite Anime")

    action = Tree("Action")
    fantasy = Tree("Fantasy")
    thriller = Tree("Thriller")

    fav_animes.add_child(action)
    fav_animes.add_child(fantasy)
    fav_animes.add_child(thriller)

    action.add_child(Tree("One piece"))
    action.add_child(Tree("Dragon Ball"))

    fantasy.add_child(Tree("Black clover"))
    fantasy.add_child(Tree("Iruma from Demon school"))

    thriller.add_child(Tree("Death Note"))
    thriller.add_child(Tree("Spy x family")) 
    fav_animes.printTree()

    print('*'*10)
    thriller.delete_tree("Spy x family")

    thriller.printTree()