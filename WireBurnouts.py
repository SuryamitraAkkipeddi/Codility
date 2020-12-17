class WeightedQuickUnion(object):
    ID = None       # ID[i] = component identifier of i
    weight = None   # weight[i] = number of nodes in the subtree(component)
                    # with i being the root
    def __init__(self, size):
        assert size > 0
        # Each individual cell is a component
        self.ID = [i for i in xrange(size)]
        # Each component has only one item initially
        self.weight = [1 for i in xrange(size)]
        return
    def findRoot(self, cell):
        ''' Return the root of tree, to which cell belongs.
            That is, the component identifier of cell.
        '''
        assert 0 <= cell < len(self.ID)
        while cell != self.ID[cell]:    cell = self.ID[cell]
        return cell
    def isConnected(self, p, q):
        ''' Check whether p and q belong to same component/tree.
        '''
        assert 0 <= p < len(self.ID) and 0 <= q < len(self.ID)
        return self.findRoot(p) == self.findRoot(q)
    def union(self, p, q):
        ''' Merge the components (trees), to which p and q belong
        '''
        assert 0 <= p < len(self.ID) and 0 <= q < len(self.ID)
        rootP = self.findRoot(p)
        rootQ = self.findRoot(q)
        # Already the same component
        if rootP == rootQ:              return
        if self.weight[rootP] >= self.weight[rootQ]:
            self.ID[rootQ] = rootP
            self.weight[rootP] += self.weight[rootQ]
        else:
            self.ID[rootP] = rootQ
            self.weight[rootQ] += self.weight[rootP]
        return
class Grid(object):
    ''' A wrapper class of WeightedQuickUnion for the current grid
    '''
    grid = None
    size = -1
    def __init__(self, size):
        self.grid = WeightedQuickUnion(size*size)
        # This is a size * size grid
        self.size = size
        return
    def isConnected(self, x1, y1, x2, y2):
        ''' Check whether the nodes (x1, y1) and (x2, y2) in the grid
            is connected or not.
        '''
        p = x1 * self.size + y1
        q = x2 * self.size + y2
        return self.grid.isConnected(p, q)
    def union(self, x1, y1, x2, y2):
        ''' Connect two nodes (x1, y1) and (x2, y2) in the grid
        '''
        p = x1 * self.size + y1
        q = x2 * self.size + y2
        self.grid.union(p, q)
        return
def solution(N, A, B, C):
    # Not enough burn out wires to stop the current from flowing
    if len(A) < N + N - 2:      return -1
    grid = Grid(N)
    # Get all the wires, which will burn out.
    removed = {}
    for index in xrange(len(A)):
        if C[index] == 0:   removed[(A[index], B[index], A[index], B[index]+1)] = True
        else:               removed[(A[index], B[index], A[index]+1, B[index])] = True
    # Add all the never-burn wires to the grid
    for x in xrange(N):
        for y in xrange(N):
            if y + 1 < N and not (x, y, x, y+1) in removed:
                grid.union(x, y, x, y+1)
            if x + 1 < N and not (x, y, x+1, y) in removed:
                grid.union(x, y, x+1, y)
    # Even if all the wires in A, B, and C burn out, the current is still flowing
    if grid.isConnected(0, 0, N-1, N-1):        return -1
    for index in xrange(len(A)-1, -1, -1):
        # Recovery one burn-out wire
        if C[index] == 0:
            grid.union(A[index], B[index], A[index], B[index]+1)
        else:
            grid.union(A[index], B[index], A[index]+1, B[index])
        # After recovery, the current could flow.
        if grid.isConnected(0, 0, N-1, N-1):    return index + 1
    # Would never be here.
    return -1