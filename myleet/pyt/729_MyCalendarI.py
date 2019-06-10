class MyCalendar:

    def __init__(self):
        self.booklist=[0]
        
    def book(self, start: int, end: int) -> bool:
        # 填充数组
        alen=len(self.booklist)
        if end > alen:
            for i in range(end-alen,end-1):
                self.booklist[i]=[0]
        
        
        asum=0
        for i in range(start-1,end-1):
            asum+=self.booklist[i]
        
        # 判断是否冲突
        if asum==0:
            for i in range(start-1,end-1):
                self.booklist[i]=1
            return true
        else:
            return false



# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
# 每次执行book，先查占用的区间，如果不冲突，会占用一段数字范围，返回true；冲突则返回false
# Calendar会记录每段离散的区间
# 数据结构选数组，范围用下标代替，占用的下标数字为1，未占用为0