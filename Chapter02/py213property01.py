'''
* @Author: csy 
* @Date: 2019-05-16 10:06:57 
* @Last Modified by:   csy 
* @Last Modified time: 2019-05-16 10:06:57 
'''
# -*- coding: utf-8 -*-


class MyClass(object):
    def __init__(self):
        self._param = None

    def getParam(self):
        print("get param: %s" % self._param)
        return self._param

    def setParam(self, value):
        print("set param: %s" % self._param)
        self._param = value

    def delParam(self):
        print("del param: %s" % self._param)
        del self._param

    # 赋值时执行setParam，调用执行getParam，删除时执行delParam
    param = property(getParam, setParam, delParam)


if __name__ == "__main__":
    cls = MyClass()
    cls.param = 10  # 触发setParam
    print("current param : %s " % cls.param)  # 触发getParam
    del cls.param  # 触发delParam
