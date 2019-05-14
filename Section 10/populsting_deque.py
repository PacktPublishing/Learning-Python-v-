import collections
d1 = collections.deque("Google")
print d1
d1.extend('raj')
print "after extend :n", d1
d1.append('hi')
print "After append :n",d1

d1.extendleft("de")
print "after extend leftn ", d1

d1.appendleft("le")
print "after append leftn ", d1