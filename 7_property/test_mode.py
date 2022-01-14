import sys
class cust_module(type(sys)):
    @property
    def remark(self):
        return self._remark
    @remark.setter
    def remark(self,value):
        self._remark = value
sys.modules[__name__].__class__ = cust_module