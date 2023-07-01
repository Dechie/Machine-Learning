class HashTable:
    def insert(self, key, value):
        """insert a new key-value pair"""
        pass
    
    def find(self, key);
        """find the value associated with a key"""
        pass

    def update(self, key, value):
        """change the value associated with a key"""
        pass

    def list_all(self):
        """list all keys"""
        pass
    

MAX_HASH_TABLE_SIZE = 4096

data_list = [None] * MAX_HASH_TABLE_SIZE 

ord('a')
ord('b')
ord('c')

def get_index(data_list, astring):
    """a variable to store the result
    (updated after after each iteration"""
    result = 0

    for achar in astring:
        """convert the character to a number using ord"""
        anum = ord(achar)

        """update result by adding number"""
        result += anum
        
    """take reminder of result with size of data_list"""
    
    return result % len(data_list)







































