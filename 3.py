# Write your solution for algorithm 3 below

'''
 Write an algorithm that takes in an unsorted numerical list as an argument 
 and creates a new sorted list in descending order (use the sorted() function).

The sorted() function sorts in ascending order, 
but it can sort in descending order by adding a reverse parameter with 
a boolean value of True.
'''

unsorted_list = [2, 1, 9, 8, 10]
# reverse=True sorts list in descending order
sorted_list = sorted(unsorted_list, reverse=True)
print(sorted_list)