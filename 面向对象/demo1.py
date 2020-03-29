class TextCss:
    def __init__(self):
        self.a = 0
        self.b = 10
    def info(self):
        print('a:',self.a,'b:',self.b)
    def xx(self):
        self.c = 'wow'
if __name__ == "__main__":
    tc = TextCss()
    tc.xx()
    # tc.info()
    # TextCss().info()
    print(tc.c)