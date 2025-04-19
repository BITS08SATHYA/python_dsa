class Stack:
    def __init__(self):
        self.list = []

    # def __str__(self):
    #     values = self.list.reverse()
    #     values = [str(x) for x in self.list]
    #     return '\n'.join(values)

    def __str__(self):
        values = [str(x) for x in reversed(self.list)]
        return '\n'.join(values)

