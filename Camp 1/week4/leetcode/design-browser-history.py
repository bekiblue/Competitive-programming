class ListNode:
    def __init__(self,url,next=None,prev=None):
        self.url=url
        self.next=next
        self.prev=prev
class BrowserHistory:
    def __init__(self, homepage: str):
        self.homepage=ListNode(homepage)
        self.dummyHead=ListNode("Head",self.homepage)
        self.dummyTail=ListNode("Tail",None,self.homepage)
        self.homepage.prev=self.dummyHead
        self.homepage.next=self.dummyTail
        self.cur=self.homepage
    def visit(self, url: str) -> None:
        self.cur.next=ListNode(url,self.dummyTail,self.cur)
        self.cur=self.cur.next
        self.dummyTail.prev=self.cur
    def back(self, steps: int) -> str:
        while self.cur != self.dummyHead:
            if steps==0:
                return self.cur.url
            self.cur=self.cur.prev
            steps-=1
        self.cur=self.homepage
        return self.cur.url
    

    def forward(self, steps: int) -> str:
        while self.cur != self.dummyTail:
            if steps==0:
                return self.cur.url
            self.cur=self.cur.next
            steps-=1
        self.cur=self.dummyTail.prev
        return self.cur.url

        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)