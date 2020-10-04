# Problem Domain
Given a binary tree, print it in reverse from leaf level to root level

# Input/Output
- Input: Binary tree
- Output: list

# Visuals

	    	    7
    	3		        9
    2	   10       1     -3
  4   N   N   1   N  N   N   6
			                N   3

[3, 4, 1, 6, 2, 10, 1, -3, 3, 9, 7]
Queue = []
output = [7, 3, 9, 2, 10, 1, -3, 4, 1, 6, 3]


# Algorithm:
- import Queue
- For BinrayTree class, add a method named reverse_traverse
- Create an instance of a queue (data)
- enqueue the root of the tree
- create a nested function in the method named "_traverse"
- Loop until queue is empty
	- dequeue x
	- push x to some list (output)
	- enqueue left then right of x if they are not None
- return output list
- call _traverse
- return reverse _traverse()

## First check
reverse =  [3, 6, 1, 4, -3, 1, 10, 2, 9, 3, 7]
expected = [3, 4, 1, 6, 2, 10, 1, -3, 3, 9, 7]
- So we need to modify the algorithm to enqueue right then left



# Code

```python
from queue_lib import Queue
class BianryTree:
	def reverse_traverse(self):
		queue = Queue() # 1
		queue.enqueue(self.root) # 1
		output = [] # 1
		def _traverse:
			while queue.peek(): # n
				x = dequeue() # 1
				output.push(x.value) # 1
				if x.right:
                    queue.enqueue(x.right) # 1
				if x.left:
                    queue.enqueue(x.left) # 1
			return output # 1
	    return _traverse()[::-1] # 2*n
```

# Tracing
```python
"""
	    	     7
    	3		         9
    2	   10        1      -3
  4   N   N   1     N  N   N   6
			                  N   3
"""

expected = [3, 4, 1, 6, 2, 10, 1, -3, 3, 9, 7]
actual   = [3, 4, 1, 6, 2, 10, 1, -3, 3, 9, 7]

queue = []
output = [7, 9, 3, -3, 1, 10, 2, 6, 1, 4, 3]

x = 3
```

# BigO
- Time: O(n)
- Space: O(n)
