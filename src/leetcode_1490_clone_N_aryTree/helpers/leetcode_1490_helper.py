class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


from collections import deque


class TreeHelpers:
    def dict_to_tree(self, root_val, tree_dict):
        if not root_val:
            return None

        root = Node(root_val)
        q = deque([root])

        while q:
            node = q.popleft()

            for child_val in tree_dict.get(node.val, []):
                child = Node(child_val)
                node.children.append(child)
                q.append(child)

        return root

    def tree_to_dict(self, root: Node):
        if not root:
            return {}

        tree_dict = {}
        q = deque([root])

        while q:
            node = q.popleft()
            tree_dict[node.val] = []

            for child in node.children:
                tree_dict[node.val].append(child.val)
                q.append(child)

            if not tree_dict[node.val]:
                del tree_dict[node.val]

        return tree_dict
