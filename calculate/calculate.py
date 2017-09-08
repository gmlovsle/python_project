#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
#__author__ = "Genming Zhang"
import re
def A_and_S(find_M_and_D):
    er = float(re.search("\-?\d+\.?\d*",find_M_and_D).group())
    ed = float(re.search("(\d+\.?\d*)$",find_M_and_D).group())
    operate = re.findall("(\+|\-)",find_M_and_D)
    operate = operate[len(operate)-1]
    if operate == "+":
        result = er + ed
    else:
        result = er - ed
    return str(result)

def M_and_D(find_M_and_D):
    er = float(re.search("\-?\d+\.?\d*",find_M_and_D).group())
    ed = float(re.search("(\d+\.?\d*)$",find_M_and_D).group())
    operate = re.search("\*|\/",find_M_and_D).group()
    if operate == "*":
        result = er * ed
    else:
        result = er / ed
    return str(result)

def calculate(expression):
    while True:
        find_M_and_D = re.search("\-?\d+\.?\d*(\*|\/)\d+\.?\d*",expression)
        if find_M_and_D == None:
            find_A_and_S = re.search("\-?\d+\.?\d*(\+|\-)\d+\.?\d*",expression)
            if find_A_and_S == None:
                find_number = re.search("\-?\d+\.?\d*",expression)
                expression = find_number.group()
                break
            else:
                findAS = find_A_and_S.group()
                result = A_and_S(findAS)
                expression = expression.replace(findAS,result,1)
        else:
            findMD = find_M_and_D.group()
            result = M_and_D(findMD)
            expression = expression.replace(findMD,result,1)
    return expression




