"""
    Implement a function with signature transfer(S, T) that transfers all elements
    from stack S onto stack T, so that the element that starts at the top
    of S is the first to be inserted onto T, and the element at the bottom of S
    ends up at the top of T.
"""


from ArrayStack import *


def transfer(S: ArrayStack, T: ArrayStack) -> ArrayStack:
    """
        Transfer all elements from stack S onto stack T.
        @param: S, T
        @precondition: S is not empty stack, T be empty stack
        @return: T stack (not empty)
    """
    try:
        if S.is_empty():
            raise Empty('Stack is empty')
        elif not S.is_empty() and T.is_empty():
            for i in range(len(S)):
                T.push(S.pop())
        return T
    except BaseException('A bug!') as E:
        raise E


def removed_by_recursion(stack: ArrayStack, n_elements: int) -> ArrayStack:

    """
        Method for removing all the elements from a stack, using recursion technique.
        @param: stack, stack's length
        @precondition: param is type object ArrayStack
        @return: stack is returned without elements within
    """
    if n_elements != 0:
        stack.pop()
        removed_by_recursion(stack, n_elements - 1)     # recursive way
    return stack


stack_ = ArrayStack()

for j in range(1, 11, 1):
    stack_.push(j)

print(f'Before removed_by_recursion call: {stack_}')
removed_by_recursion(stack_, len(stack_))
print(f'After call the function: {stack_}')
