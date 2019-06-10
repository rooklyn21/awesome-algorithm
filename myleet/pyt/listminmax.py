# -*- coding: utf-8 -*-
def findMinAndMax(L):

    if len(L)==0:
        return (None,None)

    if len(L) == 1:
        return(L[0],L[0])

    if len(L)>1:
        minl=maxl=L[0]
        for i in L:
            if i < minl:
                minl = i
            if i > maxl:
                maxl = i

        return (minl, maxl)

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败1!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败2!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败3!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败4!')
else:
    print('测试成功5!')