class Stack:

    def __init__(self):

        self.stack = list()

    def push(self, item):

        self.stack.append(item)

    def pop(self):

        if len(self.stack) > 0:
            popped = self.stack.pop()
            return popped
        else:
            return None

    def peek(self):

        if len(self.stack) > 0:
            return self.stack[len(self.stack) - 1]
        else:
            return None

    def __str__(self):
        return str(self.stack)


if __name__ == '__main__':
    stack_ = Stack()

    for i in range(10):

        stack_.push(i)

    print(stack_)

    stack_.pop()
    stack_.pop()
    print(stack_.peek())
    print(str(stack_))
