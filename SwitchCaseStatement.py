from typing import *
import math

def areaSwitchCase(ch: int, a: List[float]):
    def circleArea():
        r=a[0]
        area=math.pi*r*r
        return "{0:.5f}".format(area)
    def rectangleArea():
        l=a[0]
        b=a[1]
        area=l*b
        return "{0:.5f}".format(area)
    switch={
        1:circleArea,
        2:rectangleArea
    }
    return switch.get(ch)()