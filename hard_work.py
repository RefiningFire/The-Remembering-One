class Display:
    def __init__(self):
        self.open = 'Hello, '
        self.mid = 'my name is '
        self.name = 'Kevin.'

    def greeting(self):
        self.all = (self.open + self.mid + self.name)
        self.phrase = [i for i in self.all]

        for char in self.phrase:
            print(char, end='')
        print()
