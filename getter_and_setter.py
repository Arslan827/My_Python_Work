# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 11:42:23 2024

@author: saifi
"""

class myclass:
    def __init__(self,value):
        self.value=value
        
    @property 
    def value(self):
        return self._value
    @value.setter
    def value(self,new_value):
        self._value=new_value
        
obj=myclass(10)
obj.value=20
print(obj.value)

