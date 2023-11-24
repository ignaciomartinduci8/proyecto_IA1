
class Audio:

    def __init__(self, tag, mfcc):
        self.tag = tag
        self.mfcc = mfcc

    def getData(self):
        return [self.tag, self.mfcc]