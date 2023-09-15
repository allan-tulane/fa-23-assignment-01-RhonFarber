"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    if x <= 1:
        return x
    else:
        ra = foo(x-1)
        rb = foo(x-2)
    return ra + rb

def longest_run(myarray, key):
    longest_run = 0
    current_run = 0
    
    for num in myarray:
        if num == key:
            current_run += 1
            longest_run = max(longest_run, current_run)
        else:
            current_run = 0
    
    return longest_run

class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    
    
def longest_run_recursive(mylist, key):
    if len(mylist) == 0:
        return Result(0, 0, 0, False)
    
    if len(mylist) == 1:
        if mylist[0] == key:
            return Result(1, 1, 1, True)
        else:
            return Result(0, 0, 0, False)
    
    mid = len(mylist) // 2
    left_half = mylist[:mid]
    right_half = mylist[mid:]
    
    left_result = longest_run_recursive(left_half, key)
    right_result = longest_run_recursive(right_half, key)
    
    left_size = left_result.left_size
    right_size = right_result.right_size
    
    if left_result.is_entire_range and right_half[0] == key:
        left_size += right_result.left_size
    
    if right_result.is_entire_range and left_half[-1] == key:
        right_size += left_result.right_size
    
    longest_size = max(left_result.longest_size, right_result.longest_size, left_result.right_size + right_result.left_size)
    is_entire_range = left_result.is_entire_range and right_result.is_entire_range
    
    return Result(left_size, right_size, longest_size, is_entire_range)

## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3


