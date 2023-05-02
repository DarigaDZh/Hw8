class Hello:
    def __init__(self, strr):
        self.strr = strr
class Hi(Hello):
    def __init__(self,strr):
        super().__init__(strr)