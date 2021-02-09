'''
* @Author: csy 
* @Date: 2019-05-09 15:59:06 
* @Last Modified by:   csy 
* @Last Modified time: 2019-05-09 15:59:06 
'''
# -*- coding: utf-8 -*-


class MyClass(object):
    def __init__(self):
        self._param = None

    @property  # 调用时执行
    def param(self):
        print("get param: %s" % self._param)
        return self._param

    @param.setter  # 赋值时执行
    def param(self, value):
        print("set param: %s" % self._param)
        self._param = value

    @param.deleter  # 删除时执行
    def param(self):
        print("del param: %s" % self._param)
        del self._param


if __name__ == "__main__":
    cls = MyClass()
    cls.param = 10  # 触发@param.setter
    print("current param : %s " % cls.param)  # 触发@property
    del cls.param  # 触发@param.deleter
