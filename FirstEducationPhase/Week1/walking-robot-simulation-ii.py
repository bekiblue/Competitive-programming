class Robot:
    def __init__(self, width: int, height: int):
        self.width=width
        self.height=height
        self.dir="East"
        self.pos=[0,0]
        self.cur=0
        self.moved=False
    def step(self, num: int) -> None:
        if self.cur+num > 2*self.height+2*self.width-5:
            self.moved=True
        self.cur=(self.cur+num)%(2*self.height+2*self.width-4)
        if self.moved and self.cur==0:
            self.dir="South" 
            self.pos=0,0
        elif 0 <= self.cur <= self.width-1:
            self.dir="East"
            self.pos=self.cur,0
        elif self.width <= self.cur <= self.width+self.height-2:
            self.dir="North" 
            self.pos=self.width-1,self.cur-self.width+1 
        elif self.width+self.height-1 <= self.cur <= 2*self.width+self.height-3:
            self.dir="West"
            self.pos=2*self.width+self.height-self.cur-3,self.height-1
        elif 2*self.width+self.height-2<= self.cur <= 2*self.width+2*self.height-5:
            self.dir="South" 
            self.pos=0,2*self.width+2*self.height-self.cur-4
    def getPos(self) -> List[int]:
       return  self.pos
    def getDir(self) -> str:
        return self.dir

# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()