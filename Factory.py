__author__ = 'Xiang-Yi'
class Rook:
    '''A simple Rook class'''
    def move(self):         # self is the instance/object
        return "I move any number of spaces but only horizontally or vertically."

class Knight:
    '''A simple Knight class'''
    def move(self):
        return "I move 2 and half spaces."

class Bishop:
    '''A simple Bishop class'''
    def move(self):
        return "I move any number of spaces diagonally."

# A Factory Method that returns the object based on an input.
def makeChessPiece(piece):
    '''Factory method that takes a string and returns an object based on it.'''
    pieces = {"knight": Knight(), "bishop": Bishop(), "rook": Rook()}
    return pieces[piece]

class ChessPieceFactory:
    def createChessPiece(self, inputString):  #note two parameters, but when using, self can be omitted
        createdPiece = makeChessPiece(inputString)
        return createdPiece

chessPieceFactory = ChessPieceFactory()  #creating NEW instance

pieceOne = chessPieceFactory.createChessPiece('knight')
print("Knight:", pieceOne.move())

pieceTwo = chessPieceFactory.createChessPiece('bishop')
print("Bishop:", pieceTwo.move())

pieceThree = chessPieceFactory.createChessPiece('rook')
print("Rook:", pieceThree.move())

pieceFour = chessPieceFactory.createChessPiece('knight')

