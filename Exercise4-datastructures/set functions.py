#in main
import set_module
s1=set(map(int,input("Elements:").split()))
s2=set(map(int,input("Elements:").split()))
print("union\n",set_module.sunion(s1,s2))
print("intersection\n",set_module.sinter(s1,s2))
print("difference\n",set_module.sdifference(s1,s2))
print("symmetric\n",set_module.ssymmetric(s1,s2))
 #in set_module
def sunion(a,b):
    return a|b
def sinter(a,b):
    return a&b
def sdifference(a,b):
    return a-b
def ssymmetric(a,b):
    return a^b
