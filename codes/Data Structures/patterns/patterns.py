# Prefix sim
def patterns():
    def create_prefix_sum(arr):
        for i in range(1, len(arr)):
            arr[i] += arr[i - 1]

##### 2 pointers
def is_palindrome(string):
    start = 0
    end = len(string) - 1

    while start < end:
        if string[start] != string[end]:
            return False
        start += 1
        end -= 1
    
    return True


##### brute force O(N * K)
def max_subarray_sum(arr, k):
    n = len(arr)

    max_sum = float('-inf')

    for i in range(n - k + 1):
        current_sum = 0

        for j in range(k):
            current_sum += arr[i + j]
        
        if current_sum > max_sum:
            max_sum = current_sum
            max_start_index = i
    
    return arr[max_start_index: max_start_index + k], max_sum

#### optimized sliding windows O(N)
def max_subarray_sum_sliding_window(arr, k):
    n = len(arr)

    window_sum = sum(arr[:k])

    max_sum = window_sum
    max_start_index = 0

    for i in range(n - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        if window_sum > max_sum:
            max_sum = window_sum
            max_start_index = i + 1
    
    return arr[max_start_index: max_start_index + k], max_sum

#### reverse linked list
def reverse_linked_list(head):
    prev = None
    current = head

    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next

    return prev


#### Monotonic stack
def next_greater_element(arr):
    n = len(arr)
    stack = []
    result = [-1] * n

    for i in range(n):
        while stack and arr[i] > arr[stack[-1]]:
            result[stack.pop()] = arr[i]

        stack.append(i)
    return result


#### def search rotated array
def search_rotated_array(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right)// 2

        if nums[mid] == target:
            return mid
        
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid -1
            else:
                left = mid + 1
        
        else: 
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid -1
    
    return -1 

##### Binary tree transversal
# preOrder: root -> left -> right
# InOrder: left -> root -> right
# PostOrder: left -> right -> root

def preorder_transversal(self, node):
    if node: 
        print(node.val, end=' ')
        self.preorder_transversal(node.left)
        self.preorder_transversal(node.right)

def inorder_transversal(self, node):
    if node:
        self.inorder_transversal(node.left)
        print(node.val, end = ' ')
        self.inorder_transversal(node.right)

def postorder_transversal(self, node):
    if node:
        self.postorder_traversal(node.left)
        self.postorder_traversal(node.right)
        print(node.val, end  = ' ')


# level by level a binary tree
# level-order traversal (breadth-first traversal) on a binary tree
from collections import deque

def levelOrder(root):
    if not root:
        return []

    result = []
    queue = deque([root]) # double ended queue fro m the collections module

    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(current_level)

    return result
