# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque


class Codec:

    def __init__(self):
        self.end = "$"
        self.index = 0
        self.negative = "^"

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        queue = deque()
        result = deque()

        if root:
            queue.append(root)

        while queue != deque([]):
            current = queue.popleft()

            result.append(current)

            if current:
                queue.append(current.left)
                queue.append(current.right)

        data = ""

        for ele in result:
            if not ele:
                data += self.end
            else:
                if ele.val < 0:
                    data += str(ele.val) + self.negative
                else:
                    data += str(ele.val)

        return data

    def deserialize_helper(self, data, root):

        if not root:
            return

        if self.index < len(data):
            root.left = TreeNode(data[self.index]) if data[self.index] != self.end else None

        self.index += 1

        if self.index < len(data):
            root.right = TreeNode(data[self.index]) if data[self.index] != self.end else None

        self.index += 1

        self.deserialize_helper(data, root.left)
        self.deserialize_helper(data, root.right)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data:
            li = -1

            res = []

            i = 0

            while i < len(data):
                if data[i] == '-':
                    temp = ''
                    while data[i] != self.negative:
                        temp += data[i]
                        i += 1
                    i += 1
                    res.append(temp)
                else:
                    res.append(data[i])
                    i += 1

            while True:
                if res[-1] == self.end:
                    res.pop()
                else:
                    break

            root = TreeNode(res[self.index])
            self.index += 1
            self.deserialize_helper(res, root)
            return root

# Your Codec object will be instantiated and called as such:

root = TreeNode(4)
root.left = TreeNode(-7)
root.right = TreeNode(-3)
root.right.right = TreeNode(-3)
root.right.right.left = TreeNode(-4)
root.right.left = TreeNode(-9)
root.right.left.left = TreeNode(9)
root.right.left.right = TreeNode(-7)
root.right.left.left.left = TreeNode(6)
root.right.left.left.left.left = TreeNode(0)
root.right.left.left.left.right = TreeNode(6)
root.right.left.left.left.left.right = TreeNode(-1)
root.right.left.left.left.right.left = TreeNode(-4)
root.right.left.right.left = TreeNode(-6)
root.right.left.right.left.left = TreeNode(5)
root.right.left.right.right = TreeNode(-6)
root.right.left.right.right.left = TreeNode(9)
root.right.left.right.right.left.left = TreeNode(-2)

ser = Codec()
deser = Codec()
ans = deser.deserialize(ser.serialize(root))