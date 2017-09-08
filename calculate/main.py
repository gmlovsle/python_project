#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
#__author__ = "Genming Zhang"
import calculate
import re
a= "1 - 2 * ( (60-30 +(9-2*5/3 + 7/3*99/4*2998 +10 * 568/14 )*(-40/5) ) - (-4*3)/ (16-3*2) )"
b = re.sub(" ","",a)
'''
1-2*((60-30+(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))=2776672.6952380957
'''
print(b)
count = 0
while True:
    b = b.replace("+-","-")
    b = b.replace("-+","-")
    b = b.replace("--","+")
    b = b.replace("++","+")
    repeat_M = re.search("(\+|\-)\d+\.?\d*(\*|\/)\-",b)
    if repeat_M !=None:
        repeat = repeat_M.group()
        if repeat[0] == "+":
            repeat_new = re.search("\d+\.?\d*(\*|\/)?",repeat).group()
            b = b.replace(repeat,"-%s" %repeat_new)
        else:
            repeat_new = re.search("\d+\.?\d*(\*|\/)?",repeat).group()
            b = b.replace(repeat,"+%s" %repeat_new)
    re.sub("\-\-","\+",b)
    find_First = re.search("\(\-{0,1}\d+\.?\d*((\+|\-|\*|\/)\d+\.?\d*){0,}\)",b)
    if find_First == None:
        result = calculate.calculate(b)
        b = b.replace(b,result,1)
        break
    else:
        expression = find_First.group()
        result = calculate.calculate(expression)
        b = b.replace(expression,result,1)
print("=%s"%b)









