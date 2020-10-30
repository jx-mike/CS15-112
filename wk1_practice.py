#################################################
# Week1 Practice
#################################################

from cs112_f16_wk1 import assertEqual, assertAlmostEqual, lintAll, testAll
import math

#################################################
# Helper functions
#################################################

def almostEqual(d1, d2, epsilon=10**-7):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

import decimal
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

def distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

#################################################
# Wed Recitation
#################################################

def isFactor(f,n):
    if(n == 0):
        return True
    if (f == 0):
        return False
    if(n%f == 0):
        return True
    else:
        return False

def isMultiple(m, n):
    if(isFactor(n,m) == True):
        return True
    if(m == 0 and n!=0):
        return True
    else:
        return False

def isLegalTriangle(s1,s2,s3):
    if(s1+s2>s3 and s1+s3>s2 and s2+s3>s1):
        return True
    if(s1<0 or s2<0 or s3<0):
        return False
    else:
        return False

def triangleArea(s1, s2, s3):
    if(isLegalTriangle(s1,s2,s3) == True):
        s = (s1+s2+s3)/2
        return (s*(s-s1)*(s-s2)*(s-s3))**0.5
    else:
        return 0

def triangleAreaByCoordinates(x1, y1, x2, y2, x3, y3):
    s1 = distance(x1,y1,x2,y2)
    s2 = distance(x1,y1,x3,y3)
    s3 = distance(x2,y2,x3,y3)
    return triangleArea(s1,s2,s3)

#################################################
# Thu Lecture
#################################################

def nthFibonacciNumber(n):
    if(n < 0):
        return None
    else:
        m = n+1
        d = ((1+math.sqrt(5))**m-(1-math.sqrt(5))**m)/(2**m*math.sqrt(5))
        Fn = roundHalfUp(d)
        return Fn

def isEvenPositiveInt(x):
    if(isinstance(x,int) and x>0 and x%2 == 0):
        return True
    else:
        return False

def nearestBusStop(street):
    if(street < 0):
        return None
    if(street < 4 or street == 4):
        return 0
    if(street > 4 and street%8 <= 4):
        return int(street/8)*8
    if(street > 4 and street%8 > 4):
        return int(roundHalfUp(street/8)*8)



def lineIntersection(m1, b1, m2, b2):
    if(m1 == m2):
        return None
    else:
        x = (b2-b1)/(m1-m2)
        return x

def threeLinesArea(m1, b1, m2, b2, m3, b3):
    x1 = lineIntersection(m1,b1,m2,b2)
    x2 = lineIntersection(m2,b2,m3,b3)
    x3 = lineIntersection(m1,b1,m3,b3)
    y1 = m1 * x1 + b1
    y2 = m2 * x2 + b2
    y3 = m3 * x3 + b3
    if(m1 == m2 or m2 == m3 or m1 == m3):
        return 0
    else:
        return triangleAreaByCoordinates(x1,y1,x2,y2,x3,y3)



#################################################
# TA-led Small-Group Sessions
#################################################

def numberOfPoolBalls(rows):
    if(rows <= 0):
        return 0
    else:
        return int(rows * (rows + 1)/2)

def numberOfPoolBallRows(balls):
    if(balls <= 0):
        return 0
    else:
        return int(math.sqrt(2 * balls - 0.25) - 0.5) + 1

#################################################
# Test Functions
#################################################

def testIsFactor():
    print('Testing isFactor()... ', end='')
    assertEqual(isFactor(1,1), True)
    assertEqual(isFactor(2,10), True)
    assertEqual(isFactor(-5,25), True)
    assertEqual(isFactor(5,0), True)
    assertEqual(isFactor(0,0), True)
    assertEqual(isFactor(2,11), False)
    assertEqual(isFactor(10,2), False)
    assertEqual(isFactor(0,5), False)
    print('Passed.')

def testIsMultiple():
    print('Testing isMultiple()... ', end='')
    assertEqual(isMultiple(1,1), True)
    assertEqual(isMultiple(2,10), False)
    assertEqual(isMultiple(-5,25), False)
    assertEqual(isMultiple(5,0), False)
    assertEqual(isMultiple(0,0), True)
    assertEqual(isMultiple(2,11), False)
    assertEqual(isMultiple(10,2), True)
    assertEqual(isMultiple(0,5), True)
    assertEqual(isMultiple(25,-5), True)
    print('Passed.')

def testIsLegalTriangle():
    print('Testing isLegalTriangle()... ', end='')
    assertEqual(isLegalTriangle(3, 4, 5), True)
    assertEqual(isLegalTriangle(5, 4, 3), True)
    assertEqual(isLegalTriangle(3, 5, 4), True)
    assertEqual(isLegalTriangle(0.3, 0.4, 0.5), True)
    assertEqual(isLegalTriangle(3, 4, 7), False)
    assertEqual(isLegalTriangle(7, 4, 3), False)
    assertEqual(isLegalTriangle(3, 7, 4), False)
    assertEqual(isLegalTriangle(5, -3, 1), False)
    assertEqual(isLegalTriangle(-3, -4, -5), False)
    print('Passed.')

def testTriangleArea():
    print('Testing triangleArea()... ', end='')
    assertAlmostEqual(triangleArea(3,4,5), 6)
    assertAlmostEqual(triangleArea(3,4,0), 0)
    assertAlmostEqual(triangleArea(3,4,7), 0)
    assertAlmostEqual(triangleArea(-3,-4,-5), 0)
    assertAlmostEqual(triangleArea(1,2,2.8), (2.9 * 1.9 * 0.9 * 0.1)**0.5)
    assertAlmostEqual(triangleArea(12,72**0.5,72**0.5),36)
    print('Passed.')

def testTriangleAreaByCoordinates():
    print('Testing triangleAreaByCoordinates()... ', end='')
    assertAlmostEqual(triangleAreaByCoordinates(1,1,9,1,5,5),16)
    assertAlmostEqual(triangleAreaByCoordinates(0,0,10,0,0,50),250)
    assertAlmostEqual(triangleAreaByCoordinates(1,3,5,3,3,(3+2*3**.5)),4*3**.5)
    assertAlmostEqual(triangleAreaByCoordinates(-6,7,-3,20,0,7),39)
    assertAlmostEqual(triangleAreaByCoordinates(-2,2,2,-2,5,5),20)
    assertAlmostEqual(triangleAreaByCoordinates(-2,2,-2,2,5,5),0)
    assertAlmostEqual(triangleAreaByCoordinates(7,7,-5,7,1,1),36)
    print('Passed.')


def testNthFibonacciNumber():
    print('Testing nthFibonacciNumber()... ', end='')
    assertEqual(nthFibonacciNumber(0), 1)
    assertEqual(nthFibonacciNumber(1), 1)
    assertEqual(nthFibonacciNumber(2), 2)
    assertEqual(nthFibonacciNumber(3), 3)
    assertEqual(nthFibonacciNumber(4), 5)
    assertEqual(nthFibonacciNumber(5), 8)
    assertEqual(nthFibonacciNumber(6), 13)
    print('Passed.')

def testIsEvenPositiveInt():
    print('Testing isEvenPositiveInt()... ', end='')
    assertEqual(isEvenPositiveInt(809), False)
    assertEqual(isEvenPositiveInt(810), True)
    assertEqual(isEvenPositiveInt(2389238001), False)
    assertEqual(isEvenPositiveInt(2389238000), True)
    assertEqual(isEvenPositiveInt(-2389238000), False)
    assertEqual(isEvenPositiveInt(0), False)
    assertEqual(isEvenPositiveInt('do not crash here!'), False)
    print('Passed.')

def testNearestBusStop():
    print('Testing nearestBusStop()... ', end='')
    assertEqual(nearestBusStop(0), 0)
    assertEqual(nearestBusStop(4), 0)
    assertEqual(nearestBusStop(5), 8)
    assertEqual(nearestBusStop(12), 8)
    assertEqual(nearestBusStop(13), 16)
    assertEqual(nearestBusStop(20), 16)
    assertEqual(nearestBusStop(21), 24)
    print('Passed.')

def testLineIntersection():
    print('Testing lineIntersection()... ', end='')
    assertEqual(lineIntersection(2.5, 3, 2.5, 11), None)
    assertEqual(lineIntersection(25, 3, 25, 11), None)
    # y=3x-5 and y=x+5 intersect at (5,10)
    assertAlmostEqual(lineIntersection(3,-5,1,5), 5)
    # y=10x and y=-4x+35 intersect at (2.5,25)
    assertAlmostEqual(lineIntersection(10,0,-4,35), 2.5)
    assertAlmostEqual(lineIntersection(10,0,-4,15), 1.0714285714285714)
    assertAlmostEqual(lineIntersection(0,7,1,0),7)
    assertAlmostEqual(lineIntersection(0,7,-1,2),-5)
    assertAlmostEqual(lineIntersection(1,0,-1,2),1)
    print('Passed.')

def testThreeLinesArea():
    print('Testing threeLinesArea()... ', end='')
    assertAlmostEqual(threeLinesArea(1, 2, 3, 4, 5, 6), 0)
    assertAlmostEqual(threeLinesArea(0, 7, 1, 0, -1, 2), 36)
    assertAlmostEqual(threeLinesArea(0, 3, -.5, -5, 1, 3), 42.66666666666666)
    assertAlmostEqual(threeLinesArea(1, -5, 0, -2, 2, 2), 25)
    assertAlmostEqual(threeLinesArea(0, -9.75, -6, 2.25, 1, -4.75), 21)
    assertAlmostEqual(threeLinesArea(1, -5, 0, -2, 2, 25), 272.25)
    print('Passed.')

def testNumberOfPoolBalls():
    print('Testing numberOfPoolBalls()... ', end='')
    assertEqual(numberOfPoolBalls(0), 0)
    assertEqual(numberOfPoolBalls(1), 1)
    assertEqual(numberOfPoolBalls(2), 3)   # 1+2 == 3
    assertEqual(numberOfPoolBalls(3), 6)   # 1+2+3 == 6
    assertEqual(numberOfPoolBalls(10), 55) # 1+2+...+10 == 55
    print('Passed.')

def testNumberOfPoolBallRows():
    print('Testing numberOfPoolBallRows()... ', end='')
    assertEqual(numberOfPoolBallRows(0), 0)
    assertEqual(numberOfPoolBallRows(1), 1)
    assertEqual(numberOfPoolBallRows(2), 2)
    assertEqual(numberOfPoolBallRows(3), 2)
    assertEqual(numberOfPoolBallRows(4), 3)
    assertEqual(numberOfPoolBallRows(6), 3)
    assertEqual(numberOfPoolBallRows(7), 4)
    assertEqual(numberOfPoolBallRows(10), 4)
    assertEqual(numberOfPoolBallRows(11), 5)
    assertEqual(numberOfPoolBallRows(55), 10)
    assertEqual(numberOfPoolBallRows(56), 11)
    print('Passed.')

#################################################
# Main
#################################################

def main():
    lintAll() # check style rules
    testAll(
        testIsFactor,
        testIsMultiple,
        testIsLegalTriangle,
        testTriangleArea,
        testTriangleAreaByCoordinates,
        testNthFibonacciNumber,
        testIsEvenPositiveInt,
        testNearestBusStop,
        testLineIntersection,
        testThreeLinesArea,
        testNumberOfPoolBalls,
        testNumberOfPoolBallRows
    )

if __name__ == '__main__':
    main()
