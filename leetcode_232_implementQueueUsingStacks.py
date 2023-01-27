'''
https://leetcode.com/problems/implement-queue-using-stacks/
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.
Notes:

You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.
 
Example 1:
Input
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 1, 1, false]

Explanation
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false
 

Constraints:
1 <= x <= 9
At most 100 calls will be made to push, pop, peek, and empty.
All the calls to pop and peek are valid.
 
Follow-up: Can you implement the queue such that each operation is amortized O(1) time complexity? In other words, performing n operations will take overall O(n) time even if one of those operations may take longer.
'''

class MyQueue:
    def __init__(self):
        self.stackA = []
        self.stackB = []
        self.first = None

    def push(self, val):
        if not self.stackA:
            self.first = val
        self.stackA.append(val)
    
    def pop(self) -> int:
        if self.empty():
            return None

        if not self.stackB:
            while self.stackA:
                self.stackB.append(self.stackA.pop())

        return self.stackB.pop()
    
    def peek(self) -> int:
        if self.stackB:
            return self.stackB[-1]
        return self.first
    
    def empty(self) -> bool:
        return not (self.stackA or self.stackB)

class Helper:
    def run_methods(self, method_names: list[str], params: list[any]) -> list[any]:
        q = MyQueue()
        output = [None]
        for i in range(1, len(method_names)):
            method = getattr(q, method_names[i])
            output.append(method(*params[i]))
        return output

import unittest
class Test(unittest.TestCase):
    def setUp(self):
        self.helper = Helper()
    
    def test_example_1(self):
        method_names = ["MyQueue", "push", "push", "peek", "pop", "empty"]
        params = [[], [1], [2], [], [], []]
        expected_output = [None, None, None, 1, 1, False]
        actual_output = self.helper.run_methods(method_names, params)
        self.assertEqual(actual_output, expected_output)

    def test_multiple_pushes(self):
        method_names = ["MyQueue", "push", "push", "push", "pop", "pop", "pop", "empty"]
        params = [[], [1], [2], [3], [], [], [], []]
        expected_output = [None, None, None, None, 1, 2, 3, True]
        actual_output = self.helper.run_methods(method_names, params)
        self.assertEqual(actual_output, expected_output)
    
    def test_empty_queue(self):
        method_names = ["MyQueue", "pop", "empty"]
        params = [[], [], []]
        expected_output = [None, None, True]
        actual_output = self.helper.run_methods(method_names, params)
        self.assertEqual(actual_output, expected_output)

    def test_multiple_pops(self):
        method_names = ["MyQueue", "push", "push", "pop", "pop", "pop", "empty"]
        params = [[], [1], [2], [], [], [], []]
        expected_output = [None, None, None, 1, 2, None, True]
        actual_output = self.helper.run_methods(method_names, params)
        self.assertEqual(actual_output, expected_output)
    
    def test_peek_without_pushes(self):
        method_names = ["MyQueue", "peek", "empty"]
        params = [[], [], []]
        expected_output = [None, None, True]
        actual_output = self.helper.run_methods(method_names, params)
        self.assertEqual(actual_output, expected_output)
    
    def test_peeks(self):
        method_names = ["MyQueue", "push", "push", "peek", "pop", "peek", "empty"]
        params = [[], [1], [2], [], [], [], []]
        expected_output =[None, None, None, 1, 1, 2, False]
        actual_output = self.helper.run_methods(method_names, params)
        self.assertEqual(actual_output, expected_output)
        
#######################################
if __name__ == '__main__':
    unittest.main()





