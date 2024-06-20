class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self, level):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.get_level() < level:
            for child in self.children:
                child.print_tree(level)

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def location_tree():
    # CTO Hierarchy
    california = TreeNode('California')
    california.add_child(TreeNode('San Francisco'))
    california.add_child(TreeNode('Mountain View'))
    california.add_child(TreeNode('Palo Alto'))

    newj = TreeNode('New Jersey')
    newj.add_child(TreeNode('Princeton'))
    newj.add_child(TreeNode('Trenton'))

    usa = TreeNode("USA")
    usa.add_child(newj)
    usa.add_child(california)

    Karnataka = TreeNode('Karnataka')
    Karnataka.add_child(TreeNode('Bangalore'))
    Karnataka.add_child(TreeNode('Mysore'))

    Gujarat = TreeNode('Gujarat')
    Gujarat.add_child(TreeNode('Ahmedabad'))
    Gujarat.add_child(TreeNode('Baroda'))

    India = TreeNode("India")
    India.add_child(Gujarat)
    India.add_child(Karnataka)

    glob = TreeNode("Global")
    glob.add_child(India)
    glob.add_child(usa)

    return glob


if __name__ == '__main__':
    root_node = location_tree()
    root_node.print_tree(1)
    root_node.print_tree(2)
    root_node.print_tree(3)