from collections import namedtuple
def solution(A):
    if len(A) < 3:
        return 0
    # The blocks in the stack is in strictly height descending order.
    # For the first block in the stack, its max_depth is maximum water
    # depth of its (exclusive) left area.
    # The other blocks' max_depth is the maximum water depth between its
    # previous block in the stack and itself, both exclusive.
    Block = namedtuple("Block", ["height", "max_depth"])
    stack = [Block(A[0],0)]
    for height in A[1:]:
        if height == stack[-1].height:
            # These two adjacent blocks have the same height. They act
            # totally the same in building any water container.
            continue
        elif height < stack[-1].height:
            stack.append(Block(height, 0))
        else:
            max_depth = 0
            # Let the current iterating block be C, the previous two
            # blocks in the stack be A and B. And their positions are
            # demoed as:
            #             C
            # A           C
            # A ... B ... C
            # while the blocks between A and B are omitted. So do the
            # blocks between B and C.
            #
            # The additional_depth consider the blocks A, B, and C only,
            # and igonres all the omitted blocks, such as:
            #       C
            # A     C
            # A  B  C   (no block is between A and B, or B and C)
            #
            # HOWEVER, the additional_depth is not always the maximum
            # water depth between A and C, because there may be some
            # water between A and B, or B and C, as exists in the omitted
            # blocks. We need to adjust the additional_depth to get the
            # maximum water depth between A and C, both exclusive.
            while len(stack) > 1 and height > stack[-1].height:
                additional_depth = min(stack[-2].height, height) - \
                                   stack[-1].height
                max_depth = max(max_depth, stack[-1].max_depth) + \
                            additional_depth
                stack.pop()
            # Combine leftward same-or-less-height blocks. These dropped
            # blocks are never going to be part of the remaining water
            # container.
            while len(stack) > 0 and height >= stack[-1].height:
                max_depth = max(max_depth, stack[-1].max_depth)
                stack.pop()
            stack.append(Block(height, max_depth))
    overall_max_depth = 0
    for block in stack:
        if block.max_depth > overall_max_depth:
            overall_max_depth = block.max_depth
    return overall_max_depth