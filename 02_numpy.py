import numpy as np



ndarr= np.arange(2,200,2)

lnarr= np.linspace(2,200,100)

print(ndarr)    

print("== "* 5)

print(lnarr)

zarr= np.zeros(10)
oarr= np.ones(9)

print(zarr)
print(oarr)

t = oarr.reshape(3,3)

print(t)
np.savetxt("t.txt",t,fmt="%d")

print(t.shape)
print(t.size)
print(t.dtype)


print(lnarr[0:10:2])

cp_arr= lnarr.copy()
vw_arr= lnarr.view()

print("--- "*5)
cp_arr[1]= 42
print(cp_arr[1])
print(lnarr[1])
print(vw_arr[1])

print("--- "*5)
vw_arr[4]=42
print(cp_arr[4])
print(lnarr[4])
print(vw_arr[4])
print("--- "*5)

print(cp_arr.base)
print(vw_arr.base)

test= np.random.normal(loc=100,scale=15,size=(10,10))
print(test)


choices = np.random.choice(['a','b','c','d'],p=[0.35,0.15,0.35,0.15],size=(10,10))
print(choices)

tmp =np.array([2,4,5,6,4,7,6,8])
tmp1=np.array([3,5,6,7,5,7,7,8])
print(tmp)
print(np.unique(tmp))

somma= np.add(tmp,tmp1)
print(somma)

mol = np.multiply(tmp,tmp1)
print(mol)

# trans= np.transpose(tmp)

sub = np.subtract(tmp,tmp1)
print(sub)

t1= tmp.reshape(2,4)
t2= tmp1.reshape(2,4)



sub1 = np.add(t1,t2)
print(sub1)

print("== == "*5)
print(t1)
print(t1.transpose())


print("== == "*5)
z= np.arange(24).reshape(2,3,4)
print(z)
print("** ** "*5)
print(np.transpose(z,axes=(1,0,2)) )

print("== == "*5)
a1= np.arange(1,24)
a2= np.arange(25,50)

a3= np.concatenate((a1,a2))
print(a3)

a4= np.split(a3,3)
print(a4)

print("== == "*5)
print(np.where(a3%2==00))
print(np.where(a3>10))
print(np.where(a3>10))

print(np.where(a3%2==0,"pari","dispari"))
print(np.where(a3> 3,10,5)) 

#print(np.where(a4%2==0)) 
arr= np.array([[1,2,3],[4,5,6],[7,8,9]])
print("*0* "*5)
print(np.where(arr%2==0,arr*2,0))


print("*-* "*5)
ciccio= np.random.randint(1,100,10)
print(ciccio)
print(np.sort(ciccio) )

# np.random.seed(seed=42)

print(np.random.shuffle(ciccio))
print(ciccio)

print(arr)
for x in np.nditer(arr,op_flags=['readwrite']):
    print(x)
    x=x*x

print(arr)

x1= np.array([1,2,3,4,5])
x2= np.array([6,7,8,9,10])  

print(np.lcm(7,3) )
print(np.lcm.reduce([x1,x2]) ) 

print(np.gcd(7,21) )
print(np.gcd.reduce([x1,x2]) ) 


print("---- ---- "  *3)
data= np.random.randint(1,100,size=(12,3))
wdat= np.linspace(0,1,36).reshape(12,3)
print(data)
print(wdat)

print(np.mean(data))
print(np.mean(data,axis=0))
print(np.mean(data,axis=1))

print(np.median(data))
print(np.median(data,axis=0))
print(np.median(data,axis=1))

print(np.std(data))
print(np.std(data,axis=0))
print(np.std(data,axis=1))

print(np.min(data))
print(np.min(data,axis=0))  
print(np.min(data,axis=1))

print(np.percentile(data,25)) #1° quartile
print(np.percentile(data,25,axis=0))# 25% of the data
print(np.percentile(data,25,axis=1))    

pond = np.average(data,weights=wdat)
print(pond)
print(np.average(data,axis=0,weights=wdat))
print(np.average(data,axis=1,weights=wdat))

print("*-*" * 5)
print(np.corrcoef(data))


print("---*--- "*4)
# print(np.histogram(data,bins=5))
data= np.array([12,5,56,78,34,98])
# print(np.histogram(data) )#,bins=50,range=(0,100)))

print( np.histogram(data , bins=100 ) )# , bins=[0,1,2,3]) )

# import matplotlib.pyplot as plt
# plt.hist(data, bins=100)
# plt.show()

arr1 = np.array([1,2,3,4,5])
arr2 = np.array([6,7,8,9,10])

print(np.vstack((arr1,arr2)))
print(np.hstack((arr1,arr2)))

#Serialization
np.savetxt("arr1.txt",arr1)
np.loadtxt("arr1.txt")