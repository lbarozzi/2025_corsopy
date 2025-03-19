import numpy as np
import matplotlib.pyplot as plt

#python3 -m pip install matplotlib
#python -m pip install matplotlib

x_pt= np.array([1,2,3,4,5])
y_pt= np.array([0.6,0.8,0.2,0.7,0.1])
y_pt1= np.array([0.8,0.4,0.7,0.2,0.9 ])

'''
plt.plot(x_pt,y_pt,'v-.r',label='Data Points')
plt.xlabel('Iteration')
plt.ylabel('Success Rate')
plt.grid()
plt.legend()
plt.show()  
'''

'''#subplot
plt.subplot(2,2,1)
plt.xlabel('Iteration')
plt.ylabel('Success Rate')
plt.grid()
plt.plot(x_pt,y_pt,'v-.r',label='Data Points')

plt.subplot(2,2,4)
plt.xlabel('Iteration')
plt.ylabel('Success Rate')
plt.grid()  
plt.plot(x_pt,y_pt,'v-b',label='Data Points')

plt.show()

'''
''' Scatter
x_pt=np.random.randint(1,100,10)
y_pt=np.random.randint(1,100,10)
colrs= np.array(['red','blue','green','yellow','purple','orange','black','pink','brown','grey'])
plt.scatter(x_pt,y_pt,color=colrs, marker="*")

x_pt=np.random.randint(1,100,10)
y_pt=np.random.randint(1,100,10)
plt.scatter(x_pt,y_pt, color='lime', marker="^")

plt.show()
#'''

''' Bar
x_pt=np.array(['A','B','C','D','E'])
y_pt=np.random.randint(1,100,5)
plt.bar(x_pt,y_pt,color='red')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Graph')
plt.grid()
plt.show()

#'''

''' Histogram
x= np.random.normal(loc=100,scale=15,size=100)
plt.hist(x,bins=100,color='lime')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.grid()
plt.show()
#'''

#''' Pie
sizes = np.random.randint(1,100,5)  
labels = ['A', 'B', 'C', 'D', 'E']
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue','red']
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')
plt.title('Pie Chart')
plt.show()
#'''