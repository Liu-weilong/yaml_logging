#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/3/18 10:15
#@Author: liuweilong
#@File  : capalibity.py
from appium import webdriver
import yaml
import logging
import logging2
import logging3

file = open('family.yaml','r')
data = yaml.load(file)
logging.basicConfig(level = logging.INFO,filename = 'runlog.log',format=('%(asctime)s %(filename)s[line:%(lineno)d]%(levelname)s%(message)'))

desired_caps = {}
desired_caps['platformName'] = data['platformName']
desired_caps['platforVersion'] = data['platforVersion']
desired_caps['deviceName'] = data['deviceName']
desired_caps['app'] = data['app']
desired_caps['appPackage'] = data['appPackage']
desired_caps['appActivity'] = data['appActivity']
dirver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port']) + '/wd/hub',desired_caps)







