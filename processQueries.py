import WebpagePriorityQueue
import os

"""
This file implements a simple web search engine based on assignment descriptions. 
The code is runable but it has some bugs from 2.3 that I could not figure out how to fix. 

Student number: 20146359
Student name: Xinyu Chen
Date: Mar 5, 2021
"""

# This function takes a folder path and returns a list of WebPageIndex instances, representing the txt files in the given input folder
# Reference to opening a folder: https://realpython.com/working-with-files-in-python/
def readFiles(folder):
    files_in_folder = os.listdir(folder)
    instances = []

    for entry in files_in_folder:

        # instances.append(WebPageIndex.WebPageIndex('./data/' + entry))
        instances.append('./data/' + entry)
    # print(type(instances[0]))
    return instances


def main(query_file, folder):
    instances = readFiles(folder)
    # print(instances) # ['./data/doc7-redblacktree.txt', './data/doc1-arraylist.txt', './data/doc8-heap.txt', './data/doc5-queue.txt', './data/doc3-binarysearchtree.txt', './data/doc9-hashtable.txt', './data/doc4-stack.txt', './data/doc2-graph.txt', './data/doc6-AVLtree.txt']

    # Read the query file
    query = open(query_file, 'r')
    queries = []
    line = query.readline().rstrip('\n')
    while line != "":
        queries.append(line)
        line = query.readline().rstrip('\n')
    query.close()

    # queries: ['tree', 'binary tree', 'queue', 'data', 'array']

    # Get the user specified limit
    specified_limit = int(
        input("Please enter the number of matched files you would like to return: "))
    
    count_down = specified_limit
    # Create a WebPagePriorityQueue instance
    priority_queue = WebpagePriorityQueue.WebpagePriorityQueue("", instances)
    

    for q in queries:
        priority_queue = WebpagePriorityQueue.WebpagePriorityQueue(
            q, instances)
        priority_queue.reheap(q)
        print(q)

        while count_down > 0:
            print(priority_queue.poll())
            count_down -= 1
            
        count_down = specified_limit
        


if __name__ == "__main__":
    readFiles('./data')
    main('./queries.txt', './data')
