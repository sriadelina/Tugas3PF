import copy
from ctypes import _NamedFuncPointer


# Prototype Class
class Cookie:
    def _init_(self, name):
        self.name = name
 
    def clone(self):
        return copy.deepcopy(self)
 
# Concrete Prototypes to clone
class CoconutCookie(Cookie):
    def _init_(self):
        Cookie._init_(self, 'Coconut')
 
# Client Class
class CookieMachine:
    def _init_(self, cookie):
        self.cookie = cookie
 
    def make_cookie(self):
        return self.cookie.clone()
 
if _NamedFuncPointer == '_main_':
    prot = CoconutCookie()
    cm = CookieMachine(prot)
    for i in range(10):
        temp_cookie = cm.make_cookie()