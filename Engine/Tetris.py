# setup variables for the start of the game
        board = self.getBlankBoard()
        enemyBoard = self.getBlankBoard()
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
            # self.drawEnemyBoard(enemyBoard)
            # self.drawStatus(score, level)
            self.drawNextPiece(nextPiece)
            if fallingPiece != None:
                self.drawPiece(fallingPiece)

            pygame.display.update()
            self.FPSCLOCK.tick(self.FPS)
