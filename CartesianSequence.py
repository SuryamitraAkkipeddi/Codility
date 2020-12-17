class Cartesian_Tree():
    ''' The class to construct the Cartesian Tree
    '''
    class node(object):
        # __slots__ keyword is used to improve the performance
        __slots__ = ('key', 'value', 'right', 'left', 'parent', 'height')
        def __init__(self, key, value):
            self.key = key          # Node's key
            self.value = value      # Node's value
            self.right = None       # Right Child
            self.left = None        # Left Child
            self.parent = None      # Parent Node
            self.height = 0         # The height of current sub-tree
            return
    def __init__(self, content):
        # Construction method:
        # http://en.wikipedia.org/wiki/Cartesian_tree#Efficient_construction
        self.nodes=[self.node(i, content[i]) for i in xrange(len(content))]
        self.root = self.nodes[0]
        for index in xrange(1, len(content)):
            prior = self.nodes[index-1]
            current = self.nodes[index]
            while prior.value <= current.value:
                # Finding a node with value greater than current node
                # Update the height information of nodes on the finding path
                # These nodes will NEVER be accessed again!
                # AND their height information is final.
                if prior.left != None:
                    prior.height = max(prior.left.height+1, prior.height)
                if prior.right != None:
                    prior.height = max(prior.right.height+1, prior.height)
                if prior.parent == None:
                    # Cannot find the node with greater value
                    # Current node will be the new root node
                    current.left = prior
                    current.height = prior.height + 1
                    prior.parent = current
                    self.root = current
                    break
                prior = prior.parent
            else:
                # Find the node, to say x, with greater value
                # x.right will be current node's left son
                # And current node will be the x's new right son
                current.left = prior.right
                current.parent = prior
                if current.left != None:
                    current.left.parent = current
                    current.height = current.left.height + 1
                prior.right = current
        # Some nodes, on the path from last processed node to root,
        # might have out-of-date height information. Update them.
        prior = self.nodes[-1]
        while prior.parent != None:
            if prior.parent.height <= prior.height:
                prior.parent.height = prior.height + 1
            prior = prior.parent
        return
    def get_height(self):
        return self.root.height
    heigth = property(get_height)
def solution(A):
    tree = Cartesian_Tree(A)
    return tree.heigth+1