from ballsClasses import *

bag = Bag()
bag.fillWithRandomSetOfBalls(100, 'useAllPossibleColors')
bag.addBall( Ball('green') ) # balls can be added this way as well

bagOperator = BagOperator( bag )

print("There are {} balls in the bag.".format( bagOperator.getBallsQty() ))

print("Balls quantities in the bag by colors:")
bagOperator.printBallsQtyByColor()

ballColor = 'green'
probablityInPercent = bagOperator.checkSpecifiedColorProbability(ballColor)
print( "{} color ball pull out probability is: {:.2f}%".format(ballColor, probablityInPercent) )

colors = bagOperator.checkTheMostProbableBallColour()
print("The most probable ball colour/s to be pulled out of the bag: {}".format( ', '.join(colors) ))

ball = bagOperator.pullOutRandomBall()
print(f"You've pulled out a {ball.color} ball out of the bag.")
print("There are {} balls in the bag now.".format( bagOperator.getBallsQty() ))