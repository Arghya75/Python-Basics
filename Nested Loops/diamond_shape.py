n = 5
for i in range(n-1):
    print(' '*((n-i)-1)+'* '*(i+1))
for j in range(n):
    print(' '*j+'* '*(n-j))



'''
output:
    *
   * *
  * * *
 * * * *
* * * * *
 * * * *
  * * *
   * *
    *
'''