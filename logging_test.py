#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/4/12 9:43
#@Author: liuweilong
#@File  : logging_test.py
import logging
#logging.basicConfig(level=logging.INFO)
logging.basicConfig(filename='run.log',level=logging.DEBUG,format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s')

logging.debug('debug info')
logging.info('hello world')
logging.warning('warming info')
logging.error('error info')
logging.critical('critical info')


#Handler 处理器  将日志记录发送至合适的路径 Handler处理器类型有很多种常用有三种
#StreamHandler  将日志记录输入发送到任何文件流的对象
#FileHandler  将日志记录输出发送到磁盘文件  它继承了StreamHandler输出功能
#logging.basicConfig(filename='run.log',level=logging.DEBUG)
#NullHandler 不做任何格式化或输出  它本质上是一个开发人员使用的无操作处理程序


#Filter 过滤器
#Handlers和loggers可以使用Filter来完成级别更复杂的过滤
#


#Formatter   使用Formatter对象设置日志信息最后的规则 结构和内容 默认的时间格式为%Y-%m-%d %H:%M:%S
#%(levelno)s  打印日志级别的数值
#%(levelname)s 打印日志级别名称
#%(pathname)s 打印当前执行程序的路径
#%(filename)s 打印当前执行程序名称
#%(funcName)s 打印日志当前函数
#%(lineno)d 打印日志的当前行号
#%(asctime)s 打印日志的时间
#%(thread)d 打印线程id
#%(threadName)s 打印线程名称
#%(process)d 打印进程id
#%(message)s 打印日志信息
#




