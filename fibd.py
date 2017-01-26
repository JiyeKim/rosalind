import sys

# ages
print('input n month remain')
n = int(sys.stdin.readline())
# alive
print('input m month alive')
m= int(sys.stdin.readline())
print('remain n month = ', n)
print('alive m month =', m)
ages = [1] + [0]*(m-1)
#print (1, 'month later', ages)
for i in range(n-1):
  ages = [sum(ages[1:])] + ages[:-1]
  #print(i+2, 'month later', ages)

print('\n','FIBD solution') 
print(n, 'month later', ages)
print('total number of rabbits =', sum(ages))


