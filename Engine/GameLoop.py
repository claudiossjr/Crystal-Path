# Game: Crystal Path
# Criado por: Claudio, Gabriel, Phillipe
from PPlay.window import Window
from PPlay.gameimage import GameImage
from PPlay.sound import Sound
import random, time, pygame, sys
from pygame.locals import *
from PPlay.gameimage import*

class GameLoop:
    def __init__(self):
        self.__init_components__()
        self.FPS = 25
        self.WINDOWWIDTH = 640
        self.WINDOWHEIGHT = 480
        self.BOXSIZE = 15
        self.BOARDWIDTH = 10
        self.BOARDHEIGHT = 20
        self.BLANK = '.'

        self.MOVESIDEWAYSFREQ = 0.15
        self.MOVEDOWNFREQ = 0.1

        self.XMARGIN = int((self.WINDOWWIDTH - self.BOARDWIDTH * self.BOXSIZE) / 2)
        self.TOPMARGIN = self.WINDOWHEIGHT - (self.BOARDHEIGHT * self.BOXSIZE) - 5

        #               R    G    B
        self.WHITE       = (255, 255, 255)
        self.GRAY        = (185, 185, 185)
        self.BLACK       = (  0,   0,   0)
        self.RED         = (155,   0,   0)
        self.LIGHTRED    = (175,  20,  20)
        self.GREEN       = (  0, 155,   0)
        self.LIGHTGREEN  = ( 20, 175,  20)
        self.BLUE        = (  0,   0, 155)
        self.LIGHTBLUE   = ( 20,  20, 175)
        self.YELLOW      = (155, 155,   0)
        self.LIGHTYELLOW = (175, 175,  20)

        self.BORDERCOLOR = self.BLUE
        self.BGCOLOR = self.BLACK
        self.TEXTCOLOR = self.WHITE
        self.TEXTSHADOWCOLOR = self.GRAY
        self.COLORS = (self.BLUE,      self.GREEN,      self.RED,      self.YELLOW)
        self.LIGHTCOLORS = (self.LIGHTBLUE, self.LIGHTGREEN, self.LIGHTRED, self.LIGHTYELLOW)
        assert len(self.COLORS) == len(self.LIGHTCOLORS) # each color must have light color

        self.TEMPLATEWIDTH = 5
        self.TEMPLATEHEIGHT = 5

        self.A_SHAPE_TEMPLATE = [['.....',
                                  '.....',
                                  '..OO.',
                                  '.....',
                                  '.....'],
                                 ['.....',
                                  '..O..',
                                  '..O..',
                                  '.....',
                                  '.....']]

        self.B_SHAPE_TEMPLATE = [['.....',
                                  '.....',
                                  '..O..',
                                  '..O..',
                                  '.....'],
                                 ['.....',
                                  '.....',
                                  '.OO..',
                                  '.....',
                                  '.....']]

        self.PIECES = {'A': self.A_SHAPE_TEMPLATE,
                       'B': self.B_SHAPE_TEMPLATE,}

    #Initial Fucntions
    def __init_components__(self):
        #sessão de janela
        self._window = Window(640, 480)
        self._window.title = "Crystal Path -"

        self._fundo_sound = Sound("../Sounds/menuprincipal.ogg")
        self._fundo_sound.sound.set_volume(10/100)

        #janela Menu Principal
        self._window_background_menu_initial = GameImage("../MENU/Background.png")
        self._logo = GameImage("../MENU/LOGO.png")
        self._new_game_button = GameImage("../MENU/BOTAO - Iniciar.png")
        self._continue_game_button = GameImage("../MENU/BOTAO - Continuar.png")
        self._exit_game_button = GameImage("../MENU/BOTAO - Sair.png")

        #janela Seleção de personagens
        self._window_background_menu_char = GameImage("../CharMenu/Background.png")
        self._guerreiro_menu = GameImage("../CharMenu/Guerreiromenu.png")
        self._feiticeira_menu = GameImage("../CharMenu/Feiticeiramenu.png")
        self._arqueiro_menu = GameImage("../CharMenu/Arqueiromenu.png")

        #seleção de fase
        self._fase_1 = GameImage("../FaseMenu/fase1.png")
        self._fase_2 = GameImage("../FaseMenu/fase2.png")
        self._fase_3 = GameImage("../FaseMenu/fase3.png")
        self._mapa = GameImage("../FaseMenu/mapa.png")
        self._mapa_som = Sound("../Sounds/teriasong.ogg")
        self._mapa_som.sound.set_volume(15/100)

        #seleção do jogo

        #jogo

        #personagens
        self._guerreiro = GameImage("../CharMenu/Guerreiromenu.png")
        self._feiticeira = GameImage("../CharMenu/Feiticeiramenu.png")
        self._arqueiro = GameImage("../CharMenu/Arqueiromenu.png")


        #Controle
        self._execute = True
        self._window_to_display_ = 1
        self._mouse = Window.get_mouse()
        self._keyboard = Window.get_keyboard()

        #Não tem player selecionado. Será :
        # 1. Guerreiro
        # 2. Feiticeiro
        # 3. Arqueiro
        self._current_player_type_ = False
        self._current_game_option_ = False

    #Funções game loop
    def Run(self):
        while self._execute:
            self.__draw_window_components_()



    #Private Functions
    def __draw_window_components_(self):
        #Menu Principal
        if self._window_to_display_ == 1:
            self.__main_menu_listener()
            self.__main_menu_position()
            self.__draw_main_menu__()

        #Seleção de personagens
        elif self._window_to_display_ == 2:
            self.__char_menu_listener()
            self.__char_menu_position()
            self.__draw_char_menu__()

        #Seleção da fase
        elif self._window_to_display_ == 3:
            self.__game_option_listener_()
            self.__game_option_position__()
            self.__draw_game_option__()

        #Janela do jogo
        elif self._window_to_display_ == 4:
            self.__draw_game_view__()

        self._window.update()

    def __main_menu_listener(self):
        #PEGANDO POSIÇÂO DO MOUSE
        mx,my = self._mouse.get_position()
        if mx >= self._new_game_button.x and mx <= (self._new_game_button.x + self._new_game_button.width):
            if my >= self._new_game_button.y and my <= (self._new_game_button.y + self._new_game_button.height):
                if (self._mouse.is_button_pressed(1)):
                    self._window_to_display_ = 2
                    #LOAD GAME
        if mx >= self._continue_game_button.x and mx <= (self._continue_game_button.x + self._continue_game_button.width):
            if my >= self._continue_game_button.y and my <= (self._continue_game_button.y + self._continue_game_button.height):
                if (self._mouse.is_button_pressed(1)):
                    self._window_to_display_ = 6
        if mx >= self._exit_game_button.x and mx <= (self._exit_game_button.x + self._exit_game_button.width):
            if my >= self._exit_game_button.y and my <= (self._exit_game_button.y + self._exit_game_button.height):
                if (self._mouse.is_button_pressed(1)):
                    self._window.close()

    #Private Functions Menu Principal
    def __main_menu_position(self):
        self._new_game_button.x = self._window.width/2 - self._new_game_button.width/2
        self._new_game_button.y = (2*self._window.height)/3

        self._continue_game_button.x = self._window.width/2 - self._continue_game_button.width/2
        self._continue_game_button.y = (2*self._window.height)/3 + self._new_game_button.height + 20

        self._exit_game_button.x = self._window.width/2 - self._exit_game_button.width/2
        self._exit_game_button.y = (2*self._window.height)/3 + self._new_game_button.height + 20 + self._continue_game_button.height + 20

        self._logo.x = self._window.width/2 - self._logo.width/2
        self._logo.y = self._logo.height + 20

    def __draw_main_menu__(self):
        self._fundo_sound.play()
        self._window_background_menu_initial.draw()
        self._logo.draw()
        self._new_game_button.draw()
        self._continue_game_button.draw()
        self._exit_game_button.draw()

    #Private Functions Menu Personagens

    def __char_menu_listener(self):

        mx,my = self._mouse.get_position()
        if mx >= self._guerreiro_menu.x and mx <= self._guerreiro_menu.x + self._guerreiro_menu.width:
            if my >= self._guerreiro_menu.y and my <= self._guerreiro_menu.y + self._guerreiro_menu.height:
                if ( self._mouse.is_button_pressed(1)):
                    self._current_player_type_ = self._guerreiro

        elif mx >= self._feiticeira_menu.x and mx <= self._feiticeira_menu.x + self._feiticeira_menu.width:
            if my >= self._feiticeira_menu.y and my <= self._feiticeira_menu.y + self._feiticeira_menu.height:
                if ( self._mouse.is_button_pressed(1)):
                    self._current_player_type_ = self._feiticeira

        elif mx >=  self._arqueiro_menu.x and mx <= self._arqueiro_menu.x + self._arqueiro_menu.width:
            if my >= self._arqueiro_menu.y and my <= self._arqueiro_menu.y + self._arqueiro_menu.height:
                if ( self._mouse.is_button_pressed(1)):
                    self._current_player_type_ = self._arqueiro
        if self._current_player_type_:
            self._window_to_display_ = 3

    def __char_menu_position(self):
        self._guerreiro_menu.x = self._window.width/8
        self._guerreiro_menu.y = 0.18 * self._window.height

        self._feiticeira_menu.x = (self._window.width / 8) + self._guerreiro_menu.width
        self._feiticeira_menu.y = 0.18 * self._window.height

        self._arqueiro_menu.x = (self._window.width/8) + self._guerreiro_menu.width + self._feiticeira_menu.width
        self._arqueiro_menu.y = 0.18 * self._window.height

    def __draw_char_menu__(self):

        self._window_background_menu_char.draw()
        self._guerreiro_menu.draw()
        self._feiticeira_menu.draw()
        self._arqueiro_menu.draw()

    #Privae Functions Menu Escolha da Fase
    def __game_option_listener_(self):
        #PEGANDO POSIÇÂO DO MOUSE
        mx,my = self._mouse.get_position()
        if mx >= self._fase_1.x and mx <= (self._fase_1.x + self._fase_1.width):
            if my >= self._fase_1.y and my <= (self._fase_1.y + self._fase_1.height):
                if (self._mouse.is_button_pressed(1)):
                    self._current_game_option_ = 1
        if mx >= self._fase_2.x and mx <= (self._fase_2.x + self._fase_2.width):
            if my >= self._fase_2.y and my <= (self._fase_2.y + self._fase_2.height):
                if (self._mouse.is_button_pressed(1)):
                    self._current_game_option_ = 2
        if mx >= self._fase_3.x and mx <= (self._fase_3.x + self._fase_3.width):
            if my >= self._fase_3.y and my <= (self._fase_3.y + self._fase_3.height):
                if (self._mouse.is_button_pressed(1)):
                    self._current_game_option_ = 3

        if self._current_game_option_:
            self._window_to_display_ = 4

    def __game_option_position__(self):
        self._fase_1.x = self._window.width/3
        self._fase_1.y = self._window.height*2 / 3

        self._fase_2.x = self._window.width / 2
        self._fase_2.y = self._window.height / 2

        self._fase_3.x = self._window.width - self._fase_2.width - 50
        self._fase_3.y = self._window.height*2 / 3

    def __draw_game_option__(self):
        self._fundo_sound.sound.stop()
        self._mapa_som.play()
        self._mapa.draw()
        self._fase_1.draw()
        self._fase_2.draw()
        self._fase_3.draw()

    #Private Functions Janela do Tetris
    def __draw_game_view__(self):
        self._mapa_som.sound.stop()
        pygame.init()
        self.FPSCLOCK = pygame.time.Clock()
        self.DISPLAYSURF = pygame.display.set_mode((self.WINDOWWIDTH, self.WINDOWHEIGHT))
        self.BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
        self.BIGFONT = pygame.font.Font('freesansbold.ttf', 50)
        pygame.display.set_caption('Teste Laboratório')

        # self.showTextScreen('Testando Tetris')
        while True: # game loop
            self.runGame()
            self.showTextScreen('Game Over')

    def runGame(self):
        # setup variables for the start of the game
        board = self.getBlankBoard()
        lastMoveDownTime = time.time()
        lastMoveSidewaysTime = time.time()
        lastFallTime = time.time()
        movingDown = False # note: there is no movingUp variable
        movingLeft = False
        movingRight = False
        score = 0
        level, fallFreq = self.calculateLevelAndFallFreq(score)

        fallingPiece = self.getNewPiece()
        nextPiece = self.getNewPiece()

        while True: # game loop
            if fallingPiece == None:
                # No falling piece in play, so start a new piece at the top
                fallingPiece = nextPiece
                nextPiece = self.getNewPiece()
                lastFallTime = time.time() # reset lastFallTime

                if not self.isValidPosition(board, fallingPiece):
                    return # can't fit a new piece on the board, so game over

            self.checkForQuit()
            for event in pygame.event.get(): # event handling loop
                if event.type == KEYUP:
                    if (event.key == K_p):
                        # Pausing the game
                        self.DISPLAYSURF.fill(self.BGCOLOR)
                        pygame.mixer.music.stop()
                        self.showTextScreen('Paused') # pause until a key press
                        pygame.mixer.music.play(-1, 0.0)
                        lastFallTime = time.time()
                        lastMoveDownTime = time.time()
                        lastMoveSidewaysTime = time.time()
                    elif (event.key == K_LEFT or event.key == K_a):
                        movingLeft = False
                    elif (event.key == K_RIGHT or event.key == K_d):
                        movingRight = False
                    elif (event.key == K_DOWN or event.key == K_s):
                        movingDown = False

                elif event.type == KEYDOWN:
                    # moving the piece sideways
                    if (event.key == K_LEFT or event.key == K_a) and self.isValidPosition(board, fallingPiece, adjX=-1):
                        fallingPiece['x'] -= 1
                        movingLeft = True
                        movingRight = False
                        lastMoveSidewaysTime = time.time()

                    elif (event.key == K_RIGHT or event.key == K_d) and self.isValidPosition(board, fallingPiece, adjX=1):
                        fallingPiece['x'] += 1
                        movingRight = True
                        movingLeft = False
                        lastMoveSidewaysTime = time.time()

                    # rotating the piece (if there is room to rotate)
                    elif (event.key == K_UP or event.key == K_w):
                        fallingPiece['rotation'] = (fallingPiece['rotation'] + 1) % len(self.PIECES[fallingPiece['shape']])
                        if not self.isValidPosition(board, fallingPiece):
                            fallingPiece['rotation'] = (fallingPiece['rotation'] - 1) % len(self.PIECES[fallingPiece['shape']])
                    elif (event.key == K_q): # rotate the other direction
                        fallingPiece['rotation'] = (fallingPiece['rotation'] - 1) % len(self.PIECES[fallingPiece['shape']])
                        if not self.isValidPosition(board, fallingPiece):
                            fallingPiece['rotation'] = (fallingPiece['rotation'] + 1) % len(self.PIECES[fallingPiece['shape']])

                    # making the piece fall faster with the down key
                    elif (event.key == K_DOWN or event.key == K_s):
                        movingDown = True
                        if self.isValidPosition(board, fallingPiece, adjY=1):
                            fallingPiece['y'] += 1
                        lastMoveDownTime = time.time()

                    # move the current piece all the way down
                    elif event.key == K_SPACE:
                        movingDown = False
                        movingLeft = False
                        movingRight = False
                        for i in range(1, self.BOARDHEIGHT):
                            if not self.isValidPosition(board, fallingPiece, adjY=i):
                                break
                        fallingPiece['y'] += i - 1

            # handle moving the piece because of user input
            if (movingLeft or movingRight) and time.time() - lastMoveSidewaysTime > self.MOVESIDEWAYSFREQ:
                if movingLeft and self.isValidPosition(board, fallingPiece, adjX=-1):
                    fallingPiece['x'] -= 1
                elif movingRight and self.isValidPosition(board, fallingPiece, adjX=1):
                    fallingPiece['x'] += 1
                lastMoveSidewaysTime = time.time()

            if movingDown and time.time() - lastMoveDownTime > self.MOVEDOWNFREQ and self.isValidPosition(board, fallingPiece, adjY=1):
                fallingPiece['y'] += 1
                lastMoveDownTime = time.time()

            # let the piece fall if it is time to fall
            if time.time() - lastFallTime > fallFreq:
                # see if the piece has landed
                if not self.isValidPosition(board, fallingPiece, adjY=1):
                    # falling piece has landed, set it on the board
                    self.addToBoard(board, fallingPiece)
                    score += self.removeCompleteLines(board)
                    level, fallFreq = self.calculateLevelAndFallFreq(score)
                    fallingPiece = None
                else:
                    # piece did not land, just move the piece down
                    fallingPiece['y'] += 1
                    lastFallTime = time.time()

            # drawing everything on the screen
            self.DISPLAYSURF.fill(self.BGCOLOR)
            self.drawBoard(board)
            self.drawStatus(score, level)
            self.drawNextPiece(nextPiece)
            if fallingPiece != None:
                self.drawPiece(fallingPiece)

            pygame.display.update()
            self.FPSCLOCK.tick(self.FPS)


    def makeTextObjs(self,text, font, color):
        surf = font.render(text, True, color)
        return surf, surf.get_rect()


    def terminate(self):
        pygame.quit()
        sys.exit()


    def checkForKeyPress(self):
        # Go through event queue looking for a KEYUP event.
        # Grab KEYDOWN events to remove them from the event queue.
        self.checkForQuit()

        for event in pygame.event.get([KEYDOWN, KEYUP]):
            if event.type == KEYDOWN:
                continue
            return event.key
        return None


    def showTextScreen(self,text):
        # This function displays large text in the
        # center of the screen until a key is pressed.
        # Draw the text drop shadow
        titleSurf, titleRect = self.makeTextObjs(text, self.BIGFONT, self.TEXTSHADOWCOLOR)
        titleRect.center = (int(self.WINDOWWIDTH / 2), int(self.WINDOWHEIGHT / 2))
        self.DISPLAYSURF.blit(titleSurf, titleRect)

        # Draw the text
        titleSurf, titleRect = self.makeTextObjs(text, self.BIGFONT, self.TEXTCOLOR)
        titleRect.center = (int(self.WINDOWWIDTH / 2) - 3, int(self.WINDOWHEIGHT / 2) - 3)
        self.DISPLAYSURF.blit(titleSurf, titleRect)

        # Draw the additional "Press a key to play." text.
        pressKeySurf, pressKeyRect = self.makeTextObjs('Press a key to play.', self.BASICFONT, self.TEXTCOLOR)
        pressKeyRect.center = (int(self.WINDOWWIDTH / 2), int(self.WINDOWHEIGHT / 2) + 100)
        self.DISPLAYSURF.blit(pressKeySurf, pressKeyRect)

        while self.checkForKeyPress() == None:
            pygame.display.update()
            self.FPSCLOCK.tick()


    def checkForQuit(self):
        for event in pygame.event.get(QUIT): # get all the QUIT events
            self.terminate() # terminate if any QUIT events are present
        for event in pygame.event.get(KEYUP): # get all the KEYUP events
            if event.key == K_ESCAPE:
                self.terminate() # terminate if the KEYUP event was for the Esc key
            pygame.event.post(event) # put the other KEYUP event objects back


    def calculateLevelAndFallFreq(self,score):
        # Based on the score, return the level the player is on and
        # how many seconds pass until a falling piece falls one space.
        level = int(score / 10) + 1
        fallFreq = 0.27 - (level * 0.02)
        return level, fallFreq

    def getNewPiece(self):
        # return a random new piece in a random rotation and color
        shape = random.choice(list(self.PIECES.keys()))
        newPiece = {'shape': shape,
                    'rotation': random.randint(0, len(self.PIECES[shape]) - 1),
                    'x': int(self.BOARDWIDTH / 2) - int(self.TEMPLATEWIDTH / 2),
                    'y': -2, # start it above the board (i.e. less than 0)
                    'color': random.randint(0, len(self.COLORS)-1)}
        return newPiece


    def addToBoard(self,board, piece):
        # fill in the board based on piece's location, shape, and rotation
        for x in range(self.TEMPLATEWIDTH):
            for y in range(self.TEMPLATEHEIGHT):
                if self.PIECES[piece['shape']][piece['rotation']][y][x] != self.BLANK:
                    board[x + piece['x']][y + piece['y']] = piece['color']


    def getBlankBoard(self):
        # create and return a new blank board data structure
        board = []
        for i in range(self.BOARDWIDTH):
            board.append([self.BLANK] * self.BOARDHEIGHT)
        return board


    def isOnBoard(self,x, y):
        return x >= 0 and x < self.BOARDWIDTH and y < self.BOARDHEIGHT


    def isValidPosition(self,board, piece, adjX=0, adjY=0):
        # Return True if the piece is within the board and not colliding
        for x in range(self.TEMPLATEWIDTH):
            for y in range(self.TEMPLATEHEIGHT):
                isAboveBoard = y + piece['y'] + adjY < 0
                if isAboveBoard or self.PIECES[piece['shape']][piece['rotation']][y][x] == self.BLANK:
                    continue
                if not self.isOnBoard(x + piece['x'] + adjX, y + piece['y'] + adjY):
                    return False
                if board[x + piece['x'] + adjX][y + piece['y'] + adjY] != self.BLANK:
                    return False
        return True

    def isCompleteLine(self,board, y):
        # Return True if the line filled with boxes with no gaps.
        for x in range(self.BOARDWIDTH):
            if board[x][y] == self.BLANK:
                return False
        return True


    def removeCompleteLines(self,board):
        # Remove any completed lines on the board, move everything above them down, and return the number of complete lines.
        numLinesRemoved = 0
        y = self.BOARDHEIGHT - 1 # start y at the bottom of the board
        while y >= 0:
            if self.isCompleteLine(board, y):
                # Remove the line and pull boxes down by one line.
                for pullDownY in range(y, 0, -1):
                    for x in range(self.BOARDWIDTH):
                        board[x][pullDownY] = board[x][pullDownY-1]
                # Set very top line to blank.
                for x in range(self.BOARDWIDTH):
                    board[x][0] = self.BLANK
                numLinesRemoved += 1
                # Note on the next iteration of the loop, y is the same.
                # This is so that if the line that was pulled down is also
                # complete, it will be removed.
            else:
                y -= 1 # move on to check next row up
        return numLinesRemoved


    def convertToPixelCoords(self,boxx, boxy):
        # Convert the given xy coordinates of the board to xy
        # coordinates of the location on the screen.
        return (self.XMARGIN + (boxx * self.BOXSIZE)), (self.TOPMARGIN + (boxy * self.BOXSIZE))


    def drawBox(self,boxx, boxy, color, pixelx=None, pixely=None):
        if color == self.BLANK:
            return
        if pixelx == None and pixely == None:
            pixelx, pixely = self.convertToPixelCoords(boxx, boxy)
        pygame.draw.rect(self.DISPLAYSURF, self.COLORS[color], (pixelx + 1, pixely + 1, self.BOXSIZE - 1, self.BOXSIZE - 1))
        pygame.draw.rect(self.DISPLAYSURF, self.LIGHTCOLORS[color], (pixelx + 1, pixely + 1, self.BOXSIZE - 4, self.BOXSIZE - 4))


    def drawBoard(self,board):
        # draw the border around the board
        pygame.draw.rect(self.DISPLAYSURF, self.BORDERCOLOR, (self.XMARGIN - 3, self.TOPMARGIN - 7, (self.BOARDWIDTH * self.BOXSIZE) + 8, (self.BOARDHEIGHT * self.BOXSIZE) + 8), 5)

        # fill the background of the board
        pygame.draw.rect(self.DISPLAYSURF, self.BGCOLOR, (self.XMARGIN, self.TOPMARGIN, self.BOXSIZE * self.BOARDWIDTH, self.BOXSIZE * self.BOARDHEIGHT))
        # draw the individual boxes on the board
        for x in range(self.BOARDWIDTH):
            for y in range(self.BOARDHEIGHT):
                self.drawBox(x, y, board[x][y])


    def drawStatus(self,score, level):
        # draw the score text
        scoreSurf = self.BASICFONT.render('Score: %s' % score, True, self.TEXTCOLOR)
        scoreRect = scoreSurf.get_rect()
        scoreRect.topleft = (self.WINDOWWIDTH - 150, 20)
        self.DISPLAYSURF.blit(scoreSurf, scoreRect)

        # draw the level text
        levelSurf = self.BASICFONT.render('Level: %s' % level, True, self.TEXTCOLOR)
        levelRect = levelSurf.get_rect()
        levelRect.topleft = (self.WINDOWWIDTH - 150, 50)
        self.DISPLAYSURF.blit(levelSurf, levelRect)


    def drawPiece(self,piece, pixelx=None, pixely=None):
        shapeToDraw = self.PIECES[piece['shape']][piece['rotation']]
        if pixelx == None and pixely == None:
            # if pixelx & pixely hasn't been specified, use the location stored in the piece data structure
            pixelx, pixely = self.convertToPixelCoords(piece['x'], piece['y'])

        # draw each of the boxes that make up the piece
        for x in range(self.TEMPLATEWIDTH):
            for y in range(self.TEMPLATEHEIGHT):
                if shapeToDraw[y][x] != self.BLANK:
                    self.drawBox(None, None, piece['color'], pixelx + (x * self.BOXSIZE), pixely + (y * self.BOXSIZE))


    def drawNextPiece(self,piece):
        # draw the "next" text
        nextSurf = self.BASICFONT.render('Next:', True, self.TEXTCOLOR)
        nextRect = nextSurf.get_rect()
        nextRect.topleft = (self.WINDOWWIDTH - 120, 80)
        self.DISPLAYSURF.blit(nextSurf, nextRect)
        # draw the "next" piece
        self.drawPiece(piece, pixelx=self.WINDOWWIDTH-120, pixely=100)



if __name__ == '__main__':
    game_engine = GameLoop()
    game_engine.Run()