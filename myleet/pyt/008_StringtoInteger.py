# 题目要求，字符串转换为整数。
# 从开始起 忽略所有空格直到遇见第一个非空字符。
# 如果是数字或者-或+号 就往后找尽可能多的数字 直到遇见非数字字符结束。
# 如果非数字或者-+号，则返回0

# 算法设计
# 1.从起始位置按顺序查找字符，空则下一个。找到第一个非空字符，位置为n
# 2. 如果str[n] 不在 [-+0123456789]范围内，返回0
# 3. 如果在范围内，往下查找下一个非数字字符，位置为m
# 4. 得到子串str[n,m]，转为数字，如果> 2n31-1，返回2n31-1,小于-2n31，返回-2n31;否则返回本身。
import math
class Solution:
    def myAtoi(self, str: str) -> int:
        nums='0123456789'
        n=m=0
        asign=anum=''
        num1=max1=0

        # 处理空串
        if len(str) == 0:
            return 0

        # 1.从起始位置按顺序查找字符，空则下一个。找到第一个非空字符，位置为n，获得新串nstr
        for i in range(len(str)):
            if str[i] != ' ':
                n=i
                break
        nstr = str[n:]

        # 2. 如果nstr[0]是-，+，则获得符号asign，获得数字anum=nstr[1:]
        # 如果nstr[0]是纯数字，获得数字anum=nstr
        # 否则返回0
        if nstr[0] == '-' or nstr[0] == '+':
            asign=nstr[0]
            anum=nstr[1:]
        elif nums.find(nstr[0]) > -1 :
            anum=nstr
        else:
            return 0

        # 3. 在anum，往下查找到下一个非数字字符，直到最后一个连续的非数字字符，位置标记为m
        for j in range(1,len(anum)):
            if nums.find(anum[j]) > -1 :
                m += 1
            else:
                break


        # 4 转换为数字，并跟最大最小值比较
        try:
            num1 = int(asign+anum[:m+1])
        except  ValueError as e:
            print(e)
        max1 = pow(2,31)

        if num1 > max1-1:
            return max1-1
        elif num1 < -max1:
            return -max1
        else:
            return num1

    def test(self):
        test=["42","   -42","4193 with words","words and 987","-91283472332","3.14159"]
        for each in test:
            print(each,self.myAtoi(each))
    def testsingle(self):
        each="+3.1415926"
        print(each, self.myAtoi(each))

Solution().testsingle()
# Solution().test()
