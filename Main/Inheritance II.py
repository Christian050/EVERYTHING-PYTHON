class Snake:
    def __init__(self, name):
        self.name = name

class SnakeType:
    def __init__(self, name, threat):
        Snake.__init__(self, name)
        self.threat = threat

    def danger(self):
        return'%s can %s' % (self.name, self.threat)


if __name__ == '__main__':
    x = SnakeType('Python', 'Swallow you')
    print(x.danger())
