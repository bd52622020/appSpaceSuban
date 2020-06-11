#Write a Python program to display some information about the OS where the script is running

import platform as pl

os_profile = [
        'architecture',
        'linux_distribution',
        'mac_ver',
        'machine',
        'node',
        'platform',
        'processor',
        'python_build',
        'python_compiler',
        'python_version',
        'release',
        'system',
        'uname',
        'version',
    ]
for key in os_profile:
  if hasattr(pl, key):
    print(key +  ": " + str(getattr(pl, key)()))
    
    #Write a Python program to check whether three given lengths (integers) of three sides form
    # a right triangle. Print "Yes" if the given sides form a right triangle otherwise print "No".
    
    
    
    print("Input three integers(sides of a triangle)")
int_num = list(map(int,input().split()))
x,y,z = sorted(int_num)
if x**2+y**2==z**2:
    print('Yes')
else:
    print('No')
    
    
#Write a Python script to concatenate following dictionaries to create a new one.

#a={1:10, 2:20} 
#b={3:30, 4:40} 
#c={5:50,6:60}

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4 = {}
for d in (dic1, dic2, dic3): dic4.update(d)
print(dic4)


#4) Write a Python script to check whether a given key already exists in a dictionary.

#d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 6


d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def is_key_present(x):
  if x in d:
      print('Key is present in the dictionary')
  else:
      print('Key is not present in the dictionary')
is_key_present(5)
is_key_present(9)

