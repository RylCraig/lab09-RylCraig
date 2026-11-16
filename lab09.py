# Problem-solving practice (LeetCode / ICPC style).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def two_sum(nums, target):
    # Outline (write your plan here first):
    # To find where element 1 + element 2 = target number
    # Loop in loop to compare what the numbers add up to
    # Second loop does not need to check behind the first for 2 reasons:
    # avoid checking the same number
    # numbers behind have already been checked by first loop, assuming 1 answer
    #   ...

    # TODO: return the indices [i, j] (i < j) of the two numbers in `nums` that add up
    #   to `target`. Assume there is exactly one answer.
    for i in range(len(nums) -1): #-1 to avoid checking last number with out of bounds
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
            
    
    # pass


def max_profit(prices):
    # Outline:
    # Using same double loop structure:
    # Find situation where the profit (sale - purchase, right - left) is the greatest
    #   ...

    # TODO: `prices[i]` is a stock price on day i. Return the most profit obtainable by
    #   buying on one day and selling on a LATER day. If no profit is possible, return 0.
    size = len(prices)

    if size <= 1: #handle empty or single value list to prevent oob
        return 0

    profit = 0

    for i in range(size-1):
        for j in range(i+1, size):
            net = prices[j] - prices[i]
            if net > profit:
                profit = net

    return profit
    
    # pass


def max_subarray(nums):
    # Outline:
    # Compare sum of array sections with each other to see which one is the largest
    # Start with array length 1, increment by 1 after every check
    # find where array from left to right marker has the greatest sum
    #   ...

    # TODO: return the largest sum of any contiguous (in-a-row) block of numbers in
    #   `nums`. The list has at least one number.
    size = len(nums)
    maxsum = nums[0] # prevent no value assigned

    for segment in range(1, size+1): 
        left = 0 #always start comparisons from the left
        right = segment #start at index 1, steps up for each segment size, for initial sum

        for i in range(size - segment + 1): #index i will increment 1, 2, 3.. until max size, used to count how many times to step
            total = sum(nums[left:right]) # slicing array from left(inclusive) to right(exclusive)

            if total > maxsum:
                maxsum = total
            left += 1
            right += 1

    return maxsum
    # pass


def is_balanced(s):   # Part 4 - stretch (optional)
    # Outline:
    # closing brackets should always have the matching opening brackets before it to close properly
    # stack of brackets where only the end is compared against the next element
    # any opening brackets, add to list. Use closing brackets to determine when to remove the opening brackets.
    # only return true if all the comparisons went through without errors
    # example: {()} ok, ({)} x

    #   ...
    # TODO: return True if every bracket in `s` is closed correctly and in the right
    #   order. The brackets are ( ) [ ] { }. (Hint: a list used as a stack works well.)

    stack = []
    for symbol in s:
        if symbol in "({[":
            stack.append(symbol) # if it is an opening bracket, add to stack

        elif symbol in ")}]":
            # edge case: handle closing bracket without opening brackets, avoid stack[-1] out of range
            if not stack: # if stack is empty return false
                return False

            # if it is a closing bracket:
            match stack[-1]:
                case "(":
                    if symbol == ")":
                        stack.pop() # if symbol matches, remove open bracket
                    else:
                        return False # else it does not match and returns false

                case "{":
                    if symbol == "}":
                        stack.pop() # if symbol matches, remove open bracket
                    else:
                        return False # else it does not match and returns false

                case "[":
                    if symbol == "]":
                        stack.pop() # if symbol matches, remove open bracket
                    else:
                        return False # else it does not match and returns false

    # if all cases match, stack should be empty
    # if not, there is a missing close bracket
    if stack:
        return False

    # outside ifelse to handle empty s
    return True
    # pass


def main():
    # Optional scratch space - try your functions here, then run: python lab09.py
    # print(two_sum([2, 7, 11, 15], 9))   # [0, 1]
    pass


if __name__ == "__main__":
    main()
