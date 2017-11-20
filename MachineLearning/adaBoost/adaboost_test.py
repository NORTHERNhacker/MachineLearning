# -*- coding: utf-8 -*-

from __future__ import division
import numpy as np
import scipy as sp

from MachineLearning.adaBoost.adaBoost import ADABC

'''
 Example 0:
 this example is from the <统计学习方法>
'''
'''


X = np.array([0,1,2,3,4,5,6,7,8,9]).reshape(1,-1)
y = np.array([1,1,1,-1,-1,-1,1,1,1,-1]).transpose()
a= ADABC(X,y)
a.train(5)

'''

'''
Example 1:
this is example for 2 dimension
'''
X=np.array([
[0.55,4.4],
[1.1,2.8],
[1.85,1.95],
[3.15,1.7],
[4,2.7],
[3.75,3.95],
[2.8,4.4],
[2.35,3.2],
[3.05,2.25],
[3.55,2.6],
[3.1,3],
[3,3.4],
[1,7.3],
[1.4,6.7],
[3.05,6.9],
[4.3,7.15],
[4.75,7],
[5.5,5.85],
[5.95,4.75],
[6.45,3.15],
[6.5,1.35],
[6.3,0.95],
[5.95,0.85],
[5.95,1.6],
[5.85,2.75],
[5.65,4],
[5.35,5.25],
[5,6.15],
[4.7,6.3],
[3.85,6.5],
[2.55,6.55],
[1.4,6.65],
[0.6,6.75],
[0.6,6.85],
[5.35,0.9]]).transpose()


y=np.array([
[-1],
[-1],
[-1],
[-1],
[-1],
[-1],
[-1],
[-1],
[-1],
[-1],
[-1],
[-1],
[1],
[1],
[1],
[1],
[1],
[1],
[1],
[1],
[1],
[1],
[1],
[1],
[1],
[1],
[1],
[1],
[1],
[1],
[1],
[1],
[1],
[1],
[1]]).transpose()
a= ADABC(X,y)
a.train(5)
print (a.pred([[0.55,1.1,5.35],
[4.4,2.8,0.9]]))