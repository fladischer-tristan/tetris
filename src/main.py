"""
Entry point for game
"""

#import Tetris as t # Whole game as a package

#t.run()



class Car:
    def __init__(self):
        self.position = 0

    def fahren(self, distance: int):
        self.position = self.position + distance

myAuto = Car()
print(f"Auto1 pos: {myAuto.position}") # 0
myAuto.fahren(130)
print(f"Auto1 pos: {myAuto.position}") # 130

myAuto2 = Car()
print(f"Auto2 pos: {myAuto2.position}") # 0
for i in range(10):
    myAuto2.fahren(1)
print(f"Auto2 pos: {myAuto2.position}") # 10
