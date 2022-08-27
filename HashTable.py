class HashTable():
    def __init__(self,size=100) -> None:
        self.size = size
        self.hash_table = [None for i in range(self.size)]

    def get_hash_key(self,key):
        h = 0
        for item in key:
            h+=ord(item)
        return h%self.size

    def __set_item__(self,key,val):
        hash = self.get_hash_key(key)
        if self.hash_table[hash] is None:
            self.hash_table[hash]  = [(key,val)]
        else:
            found = False
            for index , element in enumerate(self.hash_table[hash]):
                if element[0] == key:
                    self.hash_table[hash][index] = (key,val)
                    found = True
                    break
            if not found:
                self.hash_table[hash].append((key,val))

    def __get_item__(self, key):
        hash = self.get_hash_key(key)
        if self.hash_table[hash] is None:
            return
        for element in self.hash_table[hash]:
            if element[0] == key:
                return element[1]
    
    def __del_item__(self, key):
        hash = self.get_hash_key(key)
        if self.hash_table[hash] is None:
            return
        for index, element in enumerate(self.hash_table[hash]):
            if element[0] == key:
                del self.hash_table[hash][index]


if __name__=="__main__":
    ht = HashTable()
    ht.__set_item__("dhanu",25)
    ht.__set_item__("anudh",27)
    print(ht.__get_item__("anudh"))
    print(ht.hash_table)
    ht.__del_item__("anudh")
    print(ht.hash_table)
    print(ht.__get_item__("dhanu"))
            
