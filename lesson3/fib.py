import time
def fb(n):
    if n==1 or n==2:
        return 1
    return fb(n-1)+fb(n-2)
start = time.time()
for i in range(1, 51):
    time.sleep(2)
    print('fb(%d)=%d' % (i, fb(i)))
end = time.time()
print('总时间为: %fs' % (end - start))

