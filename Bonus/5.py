# Write your solution for algorithm 5 below

'''
Write an algorithm that takes in an unsorted integer array 
and finds a pair with a given sum.

For example, for input: [5, 10, 4, 7, 6, 2] and target = 9, 
the output would be 7, 2.
If there are no pairs with sum equal to the target number, 
then the output should be 'no pairs sum to the target'.
'''

def find_sum(lst, target):
    # puts list in ascending order
    sorted_list = sorted(lst)
    # index for first element of list
    left = 0
    # index for last element of list
    right = len(sorted_list) - 1

    # runs following code when left is less than right
    while left < right:
        # checks if left and right are equal to target
        # MUST be list[left] or whatever equivalenet
        if sorted_list[left] + sorted_list[right] == target:
            # if correct pairs found, then return and stop loop
            return(sorted_list[left], sorted_list[right])

        # if left and right are less than target, move left 1 to keep searching
        if sorted_list[left] + sorted_list[right] < target:
            left = left + 1
        # if left and right are above target, move right 1 to keep searching
        else:
            right = right - 1
    
    # if no pairs are found
    return("no pairs sum to target")
    



random = [5, 10, 4, 7, 6, 2]
print(find_sum(random, 9))