import os, sys

for i in range(1001, 1500):
    newpath = ((r'/Users/vsivajothy/Area51/APACHE/SynapseTestBed/VFS/Out/client_%s-test') % (i)) 
    if not os.path.exists(newpath): os.makedirs(newpath)
