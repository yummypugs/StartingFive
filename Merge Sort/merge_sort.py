def mergesort(alist):
    """
    This is an implementation of the merge sort function.
    :param alist: An unsorted list that is being passed through the function
    :return: Returns nothing, as the original list is being modified. No return needed and you can print out the same
            list you entered into the function!
    """
    if len(alist) > 1:  # checks if the list is already at a length of one -- meaning the recursion has reached the
        # end, and will therefor end the recursion going down.
        left = alist[:len(alist) // 2]  # splits the list into a left and right half, using the len // 2 function so
        # that a "rounded down" integer is being used to slice the list
        right = alist[len(alist) // 2:]

        # recursion
        mergesort(left)  # initialize recursion on the left side of the list
        mergesort(right)  # initialize recursion on the right side of the list

        # merge

        left_index = 0  # initial left list index, will change over time!
        right_index = 0  # initial right list index, will change over time!
        sorted_index = 0  # merged list index, will change over time!

        while left_index < len(left) and right_index < len(right):  # this is where the merging begins, indexes are
            # being checked if they are in the list indexes, if they are not, this means that one list was longer as
            # the other one and then this while gets skipped during the last iteration
            if left[left_index] < right[right_index]:  # checks whether the first number in the left list is smaller
                # than the first number in the right list.
                alist[sorted_index] = left[left_index]  # original list is being updated with the new smallest value
                # from leftmost position of the left list
                left_index += 1  # left index is increased and sorted_index is also increased following the completion
                # of this if-else block. The while loop will continue as long as both left_index < len(left) and
                # right_index < len(right) are true!
            else:
                alist[sorted_index] = right[right_index]
                right_index += 1
            sorted_index += 1

        while left_index < len(left):  # this and the following while block will only execute when either the left or
            # right list is longer than the other. In this case, the last number in that list will automatically be
            # added to the end of the original list as it will be the largest number from this list set.
            alist[sorted_index] = left[left_index]
            left_index += 1
            sorted_index += 1

        while right_index < len(right):
            alist[sorted_index] = right[right_index]
            right_index += 1
            sorted_index += 1


#list_ = [6, 5, 12, 10, 9, 1]
#mergesort(list_)
#print(list_)
