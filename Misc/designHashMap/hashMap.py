# Design HashMap

# Bucket approach
# .put(key, value)
# Time: O(n)  -> n = # of entries in/len of hashmap;
#                all entries could end up in one bucket and
#                if the desired entry is at the end of the 
#                list in that bucket, would have to traverse
#                length of list to find the entry to replace
# Space: O(1) -> don't create new space that grows with the input,
#                besides a new tuple 

# .get(key)
# Time: O(n)  -> n = # of entries in/len of hashmap;
#                all entries could end up in one bucket and
#                if the desired entry is at the end of the 
#                list in that bucket, would have to traverse
#                length of list to retrive and return the entry
# Space: O(1) -> no extra space needed to get a value

# .remove(key)
# Time: O(n)  -> n = # of entries in/len of hashmap;
#                all entries could end up in one bucket and
#                if the desired entry is at the end of the 
#                list in that bucket, would have to traverse
#                length of list to find and remove the entry
# Space: O(1) -> output/space needed does not grow with input

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.numBuckets = 1000
        self.buckets = [-1] * self.numBuckets

    def put(self, key: int, value: int):
        """
        value will always be non-negative.
        """
        index = key % self.numBuckets
        
        if self.buckets[index] == -1:
            self.buckets[index] = [(key, value)]
        else:
            for i, kv in enumerate(self.buckets[index]):
                if kv[0] == key:
                    self.buckets[index][i] = (key, value)
                    break
            else:
                self.buckets[index].append((key, value))

    def get(self, key: int):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        index = key % self.numBuckets
        
        if self.buckets[index] == -1:
            return -1
        else:
            for kv in self.buckets[index]:
                if kv[0] == key:
                    return kv[1]
            else:
                return -1
        
    def remove(self, key: int):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        index = key % self.numBuckets
        
        if self.buckets[index] == -1:
            return
        else:
            for i, kv in enumerate(self.buckets[index]):
                if kv[0] == key:
                    del self.buckets[index][i]
                    break


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)