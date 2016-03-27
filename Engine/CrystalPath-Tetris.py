from PPlay.window import Window

class CrystalPathTetris:
    def __init__(self):
        self._initComponents()
    def _initComponents(self):
        self._window = Window(640,480)
        self._execute = True

    def runGame(self):
        while self._execute:
            self._drawObject()

    def _drawObject(self):
        self._window.set_background_color((255,255,255))
        self._window.update()

if __name__ == '__main__':
    tetris = CrystalPathTetris()
    tetris.runGame()