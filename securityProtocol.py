import hashlib
import sys

print "hi"

m = hashlib.md5()
y = hashlib.md5()
input = 'a'
username = "kevster555999"
password = "myPassword12345"
counter = 0
m.update(password)
y.update(password)
print m.hexdigest()
print y.hexdigest()
myHash = m.hexdigest()

#FIX
def dynamic_programming(list, sum):
    min = [ sys.maxint for i in range(0,sum)]
    for i in range(0,sum):
        for j in range(0,len(list)):
            if(min[i] < min[i-list[j]]):
                min[i] = min[i-list[j]]+1
        
    print min[sum-1]
    return min[sum-1]


if __name__ == "__main__":
    dynamic_programming([1,2,3,4,5],4)
