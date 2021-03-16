import WebPageIndex

"""
This file writes a heap-based implementation of a PriorityQueue named WebpagePriorityQueue.
Its functionalities are implemented according to assignment descriptions.

Student number: 20146359
Student name: Xinyu Chen
Date: Mar 5, 2021
"""

class WebpagePriorityQueue:
    def __init__(self, query=None, instances=[]):
        self.heap = [] 
        self.query = query
        
        for i in instances:
            self.heap.append(i)
            self._reheap(len(self.heap)-1)  
        
        self.size = len(self.heap) 
        
    # Return the max value from a heap without return 
    def peek(self):
        if self.heap[1] != None:
            return self.heap[1]
        return False
    
    # Return the max value from a heap and delete the value
    def poll(self):
        if len(self.heap) != 0:
            self._swap(self.heap, self.size-1, 0)
            max = self.heap.pop(1)
            self.size -= 1

            # Re-order the heap after polling
            for i in range(self.size):
                self._reheap(i)
            
            self._poll_check(1)
        
        else:
            raise IndexError("Underflow") 
        return max
       
    def _poll_check(self, i):
        left = 2*i + 1
        right = 2*i + 2
        max = i

        if (left <= len(self.heap)-1) and (self.heap[left][1] > self.heap[i][1]):
            max = left
            
        if (right <= len(self.heap)-1) and (self.heap[right][1] > self.heap[i][1]):
            max = right
            
        if (max != i):
            self._swap(self.heap, i, max)
            self._poll_check(max)

    def reheap(self, query):
        self.query = query
        self.heap = self._count(self.heap)
        self._reheap(len(self.heap)-1)
        self._prioritized(len(self.heap)-1)
    
    # Put the inserted node in the right place to meet max heap requirements
    def _reheap(self, index):
        # Find the parrent node's index of the current node
        parent = index // 2
        if parent < 0 :
            return 
        # If inserted node's value is greater than the parent node's value, swap
        if self.heap[parent] < self.heap[index]:
            self._swap(self.heap, parent, index)
            self._reheap(parent)


    # Prioritized queue for query based on the frequency of the searched query appears in the file
    def _prioritized(self, index):
        parent = index // 2
        if parent <= 0 :
            return 
        # If inserted node's value is greater than the parent node's value, swap
        if self.heap[parent][1] < self.heap[index][1]:
            self._swap(self.heap, parent, index)
        self._prioritized(parent)
    
    def _swap(self, heap, i, j):
        heap[i], heap[j] = heap[j], heap[i]
        
    # Count the frequency of the searched query appears in the file and return a new nested list like [['file path', int(frequency)], ['file path', int(frequency)]]
    # Example: ['./data/doc8-heap.txt', 5]
    def _count(self, instances):
        individual_query_list = self.query.lower().split()
        top_tree = []
        
        for instance in instances:
            count = 0
            for individuals in individual_query_list:
                file = WebPageIndex.WebPageIndex(instance)
                count += file.getCount(individuals)
                top_tree.append([instance, count])
        return top_tree


if __name__ == "__main__":

    instances = ['./data/doc7-redblacktree.txt', './data/doc1-arraylist.txt', './data/doc8-heap.txt', 
                 './data/doc5-queue.txt', './data/doc3-binarysearchtree.txt', './data/doc9-hashtable.txt', 
                 './data/doc4-stack.txt', './data/doc2-graph.txt', './data/doc6-AVLtree.txt']
    
        
    queue = WebpagePriorityQueue("AVL tree", instances)
    
    
    queue.reheap("tree") 
    print("peek:", queue.peek()) # ['./data/doc8-heap.txt', 5]
    
    print(queue.poll()) # ['./data/doc8-heap.txt', 5]
    print(queue.poll()) # ['./data/doc7-redblacktree.txt', 4]
    print(queue.poll()) # ['./data/doc6-AVLtree.txt', 3]
    

    
    