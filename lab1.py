#################################################
# Lab1
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

#################################################
# Lab1 problems
#################################################

def nearestOdd(n):
    if(n%2 == 0):
        return n-1
    if(n > 0):
        if(int(n)%2 == 1):
            return int(n)
        else:
            return(int(n)+1)
    else:
        if(int(n)%2 == 1):
            return int(n)
        else:
            return(int(n)-1)


def rectanglesOverlap(x1, y1, w1, h1, x2, y2, w2, h2):
    if((y1 + h1 < y2) or (x1 + w1) < x2):
        return False
    if((y2 + h2 < y1) or (x2 + w2) < x1):
        return False
    else:
        return True

def isPerfectSquare(n):
    if(isinstance(n,int) == False or n < 0):
        return False
    else:
        return n**0.5 == int(n**0.5)

def getKthDigit(n, k):
    if(k < 0):
        return None
    else:
        return (abs(n)//10**k)%10


def setKthDigit(n, k, d):
    if(k < 0):
        return None
    else:
        if(n >= 0):
            return n - getKthDigit(n,k)*10**k + d*(10**k)
        else:
            return n + getKthDigit(n,k)*10**k - d*(10**k)

def riverCruiseUpstreamTime(totalTime, totalDistance, riverCurrent):
    if(totalTime < 0 or totalDistance < 0 or riverCurrent < 0):
        return None
    else:
        a = totalTime
        b = -totalDistance
        c = -totalTime*riverCurrent**2
        x1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
        x2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)
        v_ship = max(x1,x2)
        return totalDistance/2/(v_ship - riverCurrent)


#################################################
# Lab1 Test Functions
################################################

def testNearestOdd():
    print('Testing nearestOdd()... ', end='')
    assertEqual(nearestOdd(13), 13)
    assertEqual(nearestOdd(12.001), 13)
    assertEqual(nearestOdd(12), 11)
    assertEqual(nearestOdd(11.999), 11)
    assertEqual(nearestOdd(-13), -13)
    assertEqual(nearestOdd(-12.001), -13)
    assertEqual(nearestOdd(-12), -13)
    assertEqual(nearestOdd(-11.999), -11)
    print('Passed.')

def testRectanglesOverlap():
    print('Testing rectanglesOverlap()...', end='')
    assertEqual(rectanglesOverlap(1, 1, 2, 2, 2, 2, 2, 2), True)
    assertEqual(rectanglesOverlap(1, 1, 2, 2, -2, -2, 6, 6), True)
    assertEqual(rectanglesOverlap(1, 1, 2, 2, 3, 3, 1, 1), True)
    assertEqual(rectanglesOverlap(1, 1, 2, 2, 3.1, 3, 1, 1), False)
    assertEqual(rectanglesOverlap(1, 1, 1, 1, 1.9, -1, 0.2, 1.9), False)
    assertEqual(rectanglesOverlap(1, 1, 1, 1, 1.9, -1, 0.2, 2), True)
    assertEqual(rectanglesOverlap(1, 1, 2, 2, 2, 2, 2, 6), True)
    assertEqual(rectanglesOverlap(1, 1, 2, 2, 3,4,5,6), False)
    print('Passed.')

def testIsPerfectSquare():
    print('Testing isPerfectSquare()... ', end='')
    assertEqual(isPerfectSquare(0), True)
    assertEqual(isPerfectSquare(1), True)
    assertEqual(isPerfectSquare(16), True)
    assertEqual(isPerfectSquare(1234**2), True)
    assertEqual(isPerfectSquare(15), False)
    assertEqual(isPerfectSquare(17), False)
    assertEqual(isPerfectSquare(-16), False)
    assertEqual(isPerfectSquare(1234**2+1), False)
    assertEqual(isPerfectSquare(1234**2-1), False)
    assertEqual(isPerfectSquare(4.0000001), False)
    assertEqual(isPerfectSquare('Do not crash here!'), False)
    print('Passed.')

def testGetKthDigit():
    print('Testing getKthDigit()... ', end='')
    assertEqual(getKthDigit(809, 0), 9)
    assertEqual(getKthDigit(809, 1), 0)
    assertEqual(getKthDigit(809, 2), 8)
    assertEqual(getKthDigit(809, 3), 0)
    assertEqual(getKthDigit(0, 100), 0)
    assertEqual(getKthDigit(-809, 0), 9)

    print('Passed.')

def testSetKthDigit():
    print('Testing setKthDigit()... ', end='')
    assertEqual(setKthDigit(809, 0, 7), 807)
    assertEqual(setKthDigit(809, 1, 7), 879)
    assertEqual(setKthDigit(809, 2, 7), 709)
    assertEqual(setKthDigit(809, 3, 7), 7809)
    assertEqual(setKthDigit(0, 4, 7), 70000)
    assertEqual(setKthDigit(-809, 0, 7), -807)
    print('Passed.')

def testRiverCruiseUpstreamTime():
    print('Testing riverCruiseUpstreamTime()... ', end='')
    # example from the source notes:
    totalTime = 3 # hours
    totalDistance = 30 # 15km up, 15km back down
    riverCurrent = 2 # km/hour
    assertAlmostEqual(riverCruiseUpstreamTime(totalTime,
                                              totalDistance,
                                              riverCurrent),
                       1.7888736053508778) # 1.79 in notes
    # another simple example
    totalTime = 3 # hours
    totalDistance = 30 # 15km up, 15km back down
    riverCurrent = 0 # km/hour
    assertAlmostEqual(riverCruiseUpstreamTime(totalTime,
                                              totalDistance,
                                              riverCurrent),
                       1.5)
    assertAlmostEqual(riverCruiseUpstreamTime(4,56,2),2.2801098892805185)
    print('Passed.')

#################################################
# Lab1 Main
################################################

def main():
    lintAll() # check style rules
    testAll(
        testNearestOdd,
        testRectanglesOverlap,
        testIsPerfectSquare,
        testGetKthDigit,
        testSetKthDigit,
        testRiverCruiseUpstreamTime
    )

if __name__ == '__main__':
    main()
