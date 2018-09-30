#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 17:02:23 2018

@author: yuluo
"""

import yaml

class Config(object):
    
    def __init__(self, name = "/Users/yuluo/Desktop/cloudmesh.yaml", debug=False):
        self.debug = debug
        self.yaml = name
        self._conf = {}
        
    def config(self):
        with open(self.yaml, "r") as stream:
            try:
                self._conf = yaml.load(stream)
            except yaml.YAMLError as exc:
                print(exc)    
        
    def get_default(self):
        default = self._conf.get('cloudmesh').get('default')
        return default
    
    def get_cloud(self):
        cloud = self._conf.get('cloudmesh').get('cloud')
        return cloud
    
    def get_cluster(self):
        cluster = self._conf.get('cloudmesh').get('cluster')
        return cluster
    
    def get_config(self):
        return self._conf
    
    