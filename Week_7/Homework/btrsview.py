class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        next_level = deque(
            [root,]) #creating a dq first and then init with root
        rhs = []

        while next_level:
            curr_level = next_level
            next_level = deque()#resetting level wise

            while curr_level:
                node = curr_level.popleft()
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            rhs.append(node.val)

        return rhs