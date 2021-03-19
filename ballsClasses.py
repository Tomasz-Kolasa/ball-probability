import random, copy

class Ball:
    def __init__(self, color):
        self.color = color

class Bag:
    def __init__(self):
        self.balls = []
        self.ballsColors = ['red','green','blue','yellow','white']

    def addBall(self, ball:Ball):
        self.balls.append(ball)

    def fillWithRandomSetOfBalls(self, qty, ballsDesiredColors='any'):
        for i in range(qty):
            randomColorListNumber = random.randint(0,len(self.ballsColors)-1)
            randomColor = self.ballsColors[randomColorListNumber]
            self.addBall(Ball(randomColor))
        if ballsDesiredColors == 'useAllPossibleColors':
            qtyOfBallsInBag = len(self.balls)
            qtyOfPossibleColors = len(self.ballsColors)
            if qtyOfBallsInBag < qtyOfPossibleColors:
                raise Exception("Not possible to fill the bag with all possibile balls colors. Not enough balls")
            while not self.areAllBallsColorsInBag():
                self.emptyBag()
                self.fillWithRandomSetOfBalls(qty)

    def emptyBag(self):
        self.balls = []

    def areAllBallsColorsInBag(self)->bool:
        colorsNeededToMatch = self.ballsColors.copy()
        for ball in self.balls:
            if ball.color in colorsNeededToMatch:
                colorsNeededToMatch.remove(ball.color)
        if len(colorsNeededToMatch) == 0:
            return True
        else:
            return False

    def printBagInfo(self):
        print("Balls qty: {}".format(len(self.balls)))
        for ball in self.balls:
            print(ball.color)

class BagOperator:
    def __init__(self, bag:Bag):
        self.bag = bag
        self.ballsQtyGroupedByColor = self.groupBallsByColor()

    def getBallsQty(self):
        return len(self.bag.balls)

    def printBallsQtyByColor(self):
        print(self.ballsQtyGroupedByColor)

    def groupBallsByColor(self):
        groupedColors = {}
        for ball in self.bag.balls:
            if ball.color in groupedColors:
                qty = groupedColors[ball.color]
                groupedColors[ball.color] = qty+1
            else:
                groupedColors[ball.color] = 1
        return groupedColors

    def getPullOutProbabilityDictionaryForAllBalls(self):
        ballsProbability = {}
        ballsQty = len(self.bag.balls)
        for ballColor in self.ballsQtyGroupedByColor:
            ballsProbability[ballColor] = self.ballsQtyGroupedByColor[ballColor] / ballsQty * 100
        return ballsProbability

    def checkSpecifiedColorProbability(self, color):
        if not color in self.ballsQtyGroupedByColor:
            return 0
        probabilityDictionary = self.getPullOutProbabilityDictionaryForAllBalls()
        return probabilityDictionary[color]

    def checkTheMostProbableBallColour(self):
        probabilityDictionary = self.getPullOutProbabilityDictionaryForAllBalls()
        theMostProbableColors = []
        theBiggestProbability = 0
        for ballColor in probabilityDictionary:
            if probabilityDictionary[ballColor] > theBiggestProbability:
                theBiggestProbability = probabilityDictionary[ballColor]
                theMostProbableColors = [ballColor]
            elif probabilityDictionary[ballColor] == theBiggestProbability:
                theBiggestProbability = probabilityDictionary[ballColor]
                theMostProbableColors.append(ballColor)
        return theMostProbableColors

    def pullOutRandomBall(self):
        ballsInBagQty = len(self.bag.balls)
        if ballsInBagQty == 0:
            raise Exception("Bag empty")
        
        ballRandomIndex = random.randint(0,ballsInBagQty-1)
        ball = copy.deepcopy( self.bag.balls[ballRandomIndex] )
        self.bag.balls.remove(self.bag.balls[ballRandomIndex])
        self.groupBallsByColor()
        return ball