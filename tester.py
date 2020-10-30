import math

def distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

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


def lineIntersection(m1, b1, m2, b2):
    if(m1 == m2):
        print("None")
    else:
        x = (b2-b1)/(m1-m2)
        return x

def threeLinesArea(m1, b1, m2, b2, m3, b3):
    x1 = lineIntersection(m1,b1,m2,b2)
    x2 = lineIntersection(m1,b1,m3,b3)
    x3 = lineIntersection(m2,b2,m3,b3)
    y1 = m1 * x1 + b1
    y2 = m2 * x2 + b2
    y3 = m3 * x3 + b3
    s1 = distance(x1,y1,x2,y2)
    s2 = distance(x1,y1,x3,y3)
    s3 = distance(x2,y2,x3,y3)
    if(m1 == m2):
        return 0
    if(m1 == m3):
        return 0
    if(m2 == m3):
        return 0
    else:
        return triangleArea(s1,s2,s3)

        


def main():
    m1 = 0
    b1 = 7
    m2 = 1
    b2 = 0
    m3 = -1
    b3 = 2
    x1 = lineIntersection(m1,b1,m2,b2)
    x2 = lineIntersection(m2,b2,m3,b3)
    x3 = lineIntersection(m1,b1,m3,b3)
    y1 = m1 * x1 + b1
    y2 = m2 * x2 + b2
    y3 = m3 * x3 + b3
    s1 = distance(x1,y1,x2,y2)
    s2 = distance(x1,y1,x3,y3)
    s3 = distance(x2,y2,x3,y3)
    print(x1,y1,x2,y2,x3,y3,s1,s2,s3)
    print(isLegalTriangle(s1,s2,s3))
    print(triangleArea(s1,s2,s3))
    print(triangleAreaByCoordinates(x1,y1,x2,y2,x3,y3))


if __name__ == "__main__":
    main()
