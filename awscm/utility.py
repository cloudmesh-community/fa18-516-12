#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 19:15:04 2018

@author: yuluo
"""
import subprocess


class Utility(object):
    
    def __init__(self, debug=False):
        self.debug = debug
        self.default_path_aws = '/home/ubuntu/'
        
    
    def get_instance(self, instance):
       
        title = list(instance.keys())[0]
        instance = instance.get(title)
        return instance

            
            
            
    def copy_file(self, instance, file, where):
        #runable for aws
        
        instance = self.get_instance(instance)
        try:
            if instance.get('address'):
                username = instance.get('address') + "@" + instance.get('credentials').get('username')
                key = instance.get('credentials').get('publickey')
                subprocess.check_output(["scp", key, file, username+":"+self.default_path_aws+where])
            else:
                username = 'ubuntu@'+instance.get('credentials').get('EC2_ACCESS_ID')
                key = instance.get('credentials').get('EC2_SECRET_KEY')
                subprocess.check_output(["scp", "-i", key, file, username+":"+self.default_path_aws+where])         
            return "Success to copy the file " + file + " to " + self.default_path_aws+where
        except:
            return "Faile to access the instance"
        
        
    def copy_folder(self, instance, folder, where):
        #runable for aws
        
        instance = self.get_instance(instance)
        try:
            if instance.get('address'):
                username = instance.get('address') + "@" + instance.get('credentials').get('username')
                key = instance.get('credentials').get('publickey')
                subprocess.check_output(["scp", key, "-r", folder, username+":"+self.default_path_aws+where])
            else:
                username = 'ubuntu@'+instance.get('credentials').get('EC2_ACCESS_ID')
                key = instance.get('credentials').get('EC2_SECRET_KEY')
                subprocess.check_output(["scp", "-i", key, "-r",  folder, username+":"+self.default_path_aws+where])         
            return "Success to copy the folder " + folder + " to " + self.default_path_aws+where
        except:
            return "Faile to access the instance"
        
        
    def dir_list(self, instance, where):
        instance = self.get_instance(instance)
        output = ''
        
        try:
            if instance.get('address'):
                username = instance.get('address') + "@" + instance.get('credentials').get('username')
                key = instance.get('credentials').get('publickey')
                output = subprocess.check_output(["ssh", key, username, 'ls', self.default_path_aws+where]).decode("utf-8")
            else:
                username = 'ubuntu@'+instance.get('credentials').get('EC2_ACCESS_ID')
                key = instance.get('credentials').get('EC2_SECRET_KEY')
                #output = os.popen("ls"+ " | " + "ssh"+ " -i "+ key +" "+ username).read()
                output = subprocess.check_output(["ssh", "-i", key, username, 'ls', self.default_path_aws+where]).decode("utf-8")         
            return output
        except:
            return "Faile to access the instance" 
        
        
    def delete_file(self, instance, file, where):
        instance = self.get_instance(instance)
        try:
            if instance.get('address'):
                username = instance.get('address') + "@" + instance.get('credentials').get('username')
                key = instance.get('credentials').get('publickey')
                subprocess.check_output(["ssh", key, username, 'rm', self.default_path_aws+where+file])
            else:
                username = 'ubuntu@'+instance.get('credentials').get('EC2_ACCESS_ID')
                key = instance.get('credentials').get('EC2_SECRET_KEY')
                #output = os.popen("ls"+ " | " + "ssh"+ " -i "+ key +" "+ username).read()
                subprocess.check_output(["ssh", "-i", key, username, 'rm', self.default_path_aws+where+file])       
            return "Success to delete the file " + file + " from " + self.default_path_aws+where
        except:
            return "Faile to access the instance" 
        
    def delete_folder(self, instance, folder, where):
        instance = self.get_instance(instance)
        try:
            if instance.get('address'):
                username = instance.get('address') + "@" + instance.get('credentials').get('username')
                key = instance.get('credentials').get('publickey')
                subprocess.check_output(["ssh", key, username, 'rm', '-r', self.default_path_aws+where+folder])
            else:
                username = 'ubuntu@'+instance.get('credentials').get('EC2_ACCESS_ID')
                key = instance.get('credentials').get('EC2_SECRET_KEY')
                #output = os.popen("ls"+ " | " + "ssh"+ " -i "+ key +" "+ username).read()
                subprocess.check_output(["ssh", "-i", key, username, 'rm', '-r', self.default_path_aws+where+folder])       
            return "Success to delete the folder " + folder + " from " + self.default_path_aws+where
        except:
            return "Faile to access the instance" 
        
    def create_folder(self, instance, folder, where):
        instance = self.get_instance(instance)
        try:
            if instance.get('address'):
                username = instance.get('address') + "@" + instance.get('credentials').get('username')
                key = instance.get('credentials').get('publickey')
                subprocess.check_output(["ssh", key, username, 'mkdir', self.default_path_aws+where+folder])
            else:
                username = 'ubuntu@'+instance.get('credentials').get('EC2_ACCESS_ID')
                key = instance.get('credentials').get('EC2_SECRET_KEY')
                #output = os.popen("ls"+ " | " + "ssh"+ " -i "+ key +" "+ username).read()
                subprocess.check_output(["ssh", "-i", key, username, 'mkdir', self.default_path_aws+where+folder])       
            return "Success to create the folder " + folder + " in " + self.default_path_aws+where
        except:
            return "Faile to access the instance"
        
        
    def read_file(self, instance, file, where):
        instance = self.get_instance(instance)
        output = ""
        try:
            if instance.get('address'):
                username = instance.get('address') + "@" + instance.get('credentials').get('username')
                key = instance.get('credentials').get('publickey')
                output = subprocess.check_output(["ssh", key, username, 'cat', self.default_path_aws+where+file]).decode("utf-8")
            else:
                username = 'ubuntu@'+instance.get('credentials').get('EC2_ACCESS_ID')
                key = instance.get('credentials').get('EC2_SECRET_KEY')
                #output = os.popen("ls"+ " | " + "ssh"+ " -i "+ key +" "+ username).read()
                output = subprocess.check_output(["ssh", "-i", key, username, 'cat', self.default_path_aws+where+file]).decode("utf-8")   
            return output
        except:
            return "Faile to access the instance"
        
        
    def download_file(self, instance, file, where, local):
        instance = self.get_instance(instance)
        
        try:
            if instance.get('address'):
                username = instance.get('address') + "@" + instance.get('credentials').get('username')
                key = instance.get('credentials').get('publickey')
                subprocess.check_output(["scp", key, username+":"+self.default_path_aws+where+file, local])
            else:
                username = 'ubuntu@'+instance.get('credentials').get('EC2_ACCESS_ID')
                key = instance.get('credentials').get('EC2_SECRET_KEY')
                #output = os.popen("ls"+ " | " + "ssh"+ " -i "+ key +" "+ username).read()
                subprocess.check_output(["scp", "-i", key, username+':'+self.default_path_aws+where+file, local])  
            return "Success to download file " + self.default_path_aws+where+file + " to " + local
        except:
            return "Faile to access the instance"
        
        
        
    def download_folder(self, instance, folder, where, local):
        instance = self.get_instance(instance)
        
        try:
            if instance.get('address'):
                username = instance.get('address') + "@" + instance.get('credentials').get('username')
                key = instance.get('credentials').get('publickey')
                subprocess.check_output(["scp", key, '-r', username+":"+self.default_path_aws+where+folder, local])
            else:
                username = 'ubuntu@'+instance.get('credentials').get('EC2_ACCESS_ID')
                key = instance.get('credentials').get('EC2_SECRET_KEY')
                #output = os.popen("ls"+ " | " + "ssh"+ " -i "+ key +" "+ username).read()
                subprocess.check_output(["scp", "-i", key, '-r', username+':'+self.default_path_aws+where+folder, local])  
            return "Success to download folder " + self.default_path_aws+where+folder + " to " + local
        except:
            return "Faile to access the instance"
        
        
    def check_process(self, instance, process):
        instance = self.get_instance(instance)
        output = ""
        try:
            if instance.get('address'):
                username = instance.get('address') + "@" + instance.get('credentials').get('username')
                key = instance.get('credentials').get('publickey')
                output = subprocess.check_output(["ssh", key, username, 'ps', 'aux', '|', 'grep', process]).decode("utf-8")
            else:
                username = 'ubuntu@'+instance.get('credentials').get('EC2_ACCESS_ID')
                key = instance.get('credentials').get('EC2_SECRET_KEY')
                #output = os.popen("ls"+ " | " + "ssh"+ " -i "+ key +" "+ username).read()
                output = subprocess.check_output(["ssh", '-i', key, username, 'ps', 'aux', '|', 'grep', process]).decode("utf-8")  
            return output
        except:
            return "Faile to access the instance"