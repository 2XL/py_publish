
class clouddrive():

    def __init__(self):
        self.whoami = type(self).__name__
        print self.whoami

    def hello(self):
        print "{} say hello".format(self.whoami)
