class Point:
      x=0
      y=0
      def MovePoint(self,newx,newy):
            self.x=newx
            self.y=newy
      def PrintPoint(self):
            print("x="+ str(self.x))
            print("y="+ str(self.y))
origin=Point()
myPoint=Point()
myPoint.MovePoint(10,6)
myPoint.PrintPoint() 
origin.PrintPoint()                 