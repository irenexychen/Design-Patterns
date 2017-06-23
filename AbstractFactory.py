__author__ = 'Xiang-Yi'
# Different classes denoting different types of objects having a common characteristic: Knight, Rook & Bishop


class Knight:
    '''One of many classes having a common characteristic'''
    def directionOfMovement(self):
        return "Neither horizontally nor vertically."
    def stepsInMovement(self):
        return "2 and a half."
    def __str__(self):
        return "Knight"

class Rook:
    '''One of many classes having a common characteristic'''
    def directionOfMovement(self):
        return "Horizontally or vertically."
    def stepsInMovement(self):
        return "As many as 7."
    def __str__(self):
        return "Rook"

class Bishop:
    '''One of many classes having a common characteristic'''
    def directionOfMovement(self):
        return "Diagonally."
    def stepsInMovement(self):
        return "As many as 7."
    def __str__(self):
        return "Bishop"

# Concrete Factories having getter methods to return objects of above classes: KnightFactory, RookFactory & BishopFactory
class KnightFactory:
    '''Concrete Factory based on a class; returns an object of the corresponding class'''
    def getPiece(self):
        return Knight()

class RookFactory:
    '''Concrete Factory based on a class; returns an object of the corresponding class'''
    def getPiece(self):
        return Rook()

class BishopFactory:
    '''Concrete Factory based on a class; returns an object of the corresponding class'''
    def getPiece(self):
        return Bishop()

# Abstract Factory which takes a concrete factory object as input, obtains the object from the factory, and provides a method to expose details of the object: Piece Factory
class PieceFactory:
    '''An abstract factory which takes a concrete factory object as input, obtains the object from the factory, and provides a method to expose details of the object. '''
    def __init__(self, pieceFactory):
        self._pieceFactory = pieceFactory


    def changeFactory(self,pieceFactory):
        self._pieceFactory = pieceFactory


    def detailsOfChosenPiece(self):
        '''utility method to display details of object returned by the abstract factory'''
        chosenPiece = self._pieceFactory.getPiece()
        print("Chosen piece:", chosenPiece)
        print("Direction of chosen piece:", chosenPiece.directionOfMovement())
        print("Number of steps the chosen piece can move:", chosenPiece.stepsInMovement())

objectOfConcreteFactory = RookFactory()
objectOfAbstractFactory = PieceFactory(objectOfConcreteFactory)
objectOfAbstractFactory.detailsOfChosenPiece()


objectOfConcreteFactory = KnightFactory()
objectOfAbstractFactory.changeFactory(objectOfConcreteFactory)
objectOfAbstractFactory.detailsOfChosenPiece()

