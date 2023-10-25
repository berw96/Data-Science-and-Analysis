from ctypes import *

mydll = cdll.LoadLibrary("clibs/libraries/TestCPPLibrary.dll")

result = mydll.MultiplyNumbers(4,7)

print(result)
