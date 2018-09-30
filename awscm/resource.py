#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 18:07:10 2018

@author: yuluo
"""
import yaml, sys

class Resource(object):
    
    def __init__(self, debug=False):
        self.yamlFile = "/Users/yuluo/Desktop/cloudmesh.yaml"
        self.debug = debug
        
    def readFile(self, yamlFile):
        cloudmesh = ""
        with open(yamlFile, "r") as stream:
            try:
                cloudmesh = yaml.load(stream)
            except yaml.YAMLError as exc:
                print(exc)    
        return cloudmesh  
    
    def updateFile(self, newContent):
        with open(self.yamlFile, "w") as output:
            yaml.dump(newContent,output)
          
    def add(self, content, filePath):
        newContent = self.readFile(filePath)
        for i in newContent:
            (((content["cloudmesh"])['cloud'])['test']).update({i:newContent[i]})
        self.updateFile(content)
        
    def remove(self, content, item):   
        for i in ((content['cloudmesh'])['cloud'])['test']:
            if ((((content['cloudmesh'])['cloud'])['test'])[i])['name'] == item or ((((content['cloudmesh'])['cloud'])['test'])[i])['label'] == item:
                del (((content['cloudmesh'])['cloud'])['test'])[i]
                break
        self.updateFile(content) 
        
    def review(self, item, cloud, cluster, default):
        result = {}
        for i in cloud:
            for j in cloud[i]:
                if ((cloud[i])[j])['name'] == item or ((cloud[i])[j])['label'] == item:
                    result = {j:(cloud[i])[j]}
        for i in cluster:
            if (cluster[i])['name'] == item or (cluster[i])['label'] == item:
                result = {i:cluster[i]}
                
        if result == {}:
            print('Cannot find the instance ' + item + ', please check the instance label or name')
            sys.exit()
        else:
            return result
