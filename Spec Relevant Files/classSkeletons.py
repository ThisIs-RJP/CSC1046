from abc import ABC, abstractmethod
from typing import List, Dict

#######################################
########### CLASS SKELETONS ########### 
#######################################

class ChessPieceMovementLogic(ABC):
    @abstractmethod
    def move(self, position: 'Position'):
        pass

class ChessPiece(ChessPieceMovementLogic):
    def __init__(self, position: 'Position', is_white: bool):
        """
            Position is wrapped in quotation marks
            to inform the function of an incoming
            argument with type Position. This will be evident
            Throughout this file
        """
        self.position           = position
        self.isWhite            = is_white
        self.isFrozen           = False
        self.isCursed           = False
        self.isDoubleCapturable = False

    def getPosition(self):
        return self.position

    def updatePosition(self, position: 'Position'):
        self.position = position

    @abstractmethod
    def move(self, position: 'Position'):
        pass

# Validator class to validate moves and handle special cases
class Validator:
    def validateMove(self, chessPiece: ChessPiece, startPosition: 'Position', endPosition: 'Position'):
        ## Just general code to handle normal movement
        pass

    def specialCasesHandler(self, chessPiece: ChessPiece, startPosition: 'Position', endPosition: 'Position'):
        ## Some code to handle special cases such as castling and en passant
        pass

# Board class containing chess pieces, validator, and other properties
class Board:
    def __init__(self):
        self.squares = [[None for _ in range(8)] for _ in range(8)] 
        """
            Initialising each square as None, to allow them to be occupied with ChessPieces
        """
        self.roundCounter                                    = 0
        self.check                                           = False
        self.validator                                       = Validator()
        self.trapDoorPositions: Dict['Position', 'TrapDoor'] = {}

        """
            Infering that type that will be used for Keys and values for this dictionary
            In this case, the keys and values will hold the types Position and TrapDoor respectively
        """

    def movePiece(self, chessPiece: ChessPiece, startPosition: 'Position', endPosition: 'Position'):
        ## General piece movement logic, uses Validator class to validate the move
        pass

    def trapDoorGenerator(self):
        ## Code to generate trapdoors, initialising them with a random position on the board with an event
        pass

    def isCheckmate(self):
        ## Code to check if game has reached a checkmate state => Output the winner if condition is true
        pass

    def isOnTrapDoorHandler(self):
        ## Code to check if a piece is on a trapdoor and handle the event
        pass

    def isStalemate(self):
        ## Code to check if game has reached a stalemate state
        pass

# TrapDoor class containing position and associated event
class TrapDoor:
    def __init__(self, position: 'Position', event: str):
        self.position = position
        self.event    = event

# Position class defining coordinates on the chessboard
class Position:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

# Individual ChessPiece subclasses, each implementing its specific move logic
class King(ChessPiece):
    def __init__(self, position: 'Position', is_white: bool): 
        super().__init__(position, is_white)
        ## To initialise the already defined attributes of the ChessPiece class
        self.hasMoved = False
        ## This and the rook piece will have this
        ## It is to ensure that the piece has not moved and is able to castle

    def move(self, position: 'Position'):
        pass

class Queen(ChessPiece):
    def move(self, position: 'Position'):
        pass

class Rook(ChessPiece):
    def __init__(self, position: 'Position', is_white: bool):
        super().__init__(position, is_white)
        self.hasMoved = False

    def move(self, position: 'Position'):
        pass

class Bishop(ChessPiece):
    def move(self, position: 'Position'):
        pass

class Knight(ChessPiece):
    def move(self, position: 'Position'):
        pass

class Pawn(ChessPiece):
    def __init__(self, position: 'Position', is_white: bool):
        super().__init__(position, is_white)
        self.hasMoved = False
        self.isAtEnd  = False

    def randomPromotion(self):
        ## Code to randomly promote the pawn and delete the previous piece object and replace it with the chosen promotion piece
        pass

    def move(self, position: 'Position'):
        pass

class Player:
    def __init__(self, is_white: bool):
        self.moveHistory = []
        self.chatHistory = []
        self.isWhite     = is_white
