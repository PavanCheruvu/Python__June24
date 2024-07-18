T=(['file1',1001,'10KB'],['file2',1002,'15KB'],['file3',1003,'20KB'])

#print(T[0][-1],T[0][0],T[0][1])
print('FileSize  Filename FileIndex')
for v in T:
    print("{}\t {}\t {}".format(v[-1],v[0],v[1]))
