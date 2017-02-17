from modules.GUIMain import GUIMain
from modules.Mediator import Mediator


class MWPlayerSync(object):
    def __init__(self):
        self.mediator = Mediator(self)
        self.GUI = GUIMain(self)

if __name__ == '__main__':
    MWPlayerSync()
