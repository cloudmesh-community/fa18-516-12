#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 15:54:06 2018

@author: yuluo
"""

from run import Run




class Advanced(object):
    
    def __init__(self, debug=False):
        self.debug = debug
        self.run = Run(debug=debug)
        self.result_dir = {}
        self.final_result = ''
        
    
    def a(self):
        return '#!/bin/bash\n echo "a-Monday$(date)"'
    
    def b(self):
        return '#!/bin/bash\n echo "b-Tuesday($USER)"'
    
    def c(self):
        return '#!/bin/bash\n echo "c-Wednesday($PWD)"'
    
    def d(self):
        return '#!/bin/bash\n echo "d-Thursday(Yu)"'
    
    def function_identifier(self, name):
        if name == 'a':
            return self.a()
        elif name == 'b':
            return self.b()
        elif name == 'c':
            return self.c()
        else:
            return self.d()
    
    
    def parall(self, par):
        
        scripts = ''   
        for i in par:
            scripts+=self.function_identifier(i)+','
        
        sub_result = self.run.run_local_or_remote(scripts[:-1], True)

        for i in range(len(par)):
            temp = sub_result[i].split(':')[2]
            index = temp.index('-')
            self.result_dir.update({temp[index-1]:temp})
        
        
        
    def sequential(self, work):
        for i in work:
            if '|' in i:
                par = i.split('|')
                self.parall(par)
            elif '+' in i:
                add = i.split('+')
                self.add(add)
            else:
                self.item(i)
                    
            
    def add(self, add_list):
        for i in add_list:
            
            self.final_result+=self.result_dir[i]
        
    def item(self, job):
        script=self.function_identifier(job)
        sub_result = self.run.run_local_or_remote(script, True)
        temp = sub_result[0].split(':')[2]
        index = temp.index('-')
        self.result_dir.update({temp[index-1]:temp})
        

    
    def formula(self, string):
        
        work = string.split(';')
        self.sequential(work)
        print('Running formula: '+string+', and the result is:')
        print(self.final_result)
            
        
        
        
            
            
        
            
        
        