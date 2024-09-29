#Code by GVV Sharma
#September 12, 2023
#Revised July 21, 2024
#released under GNU GPL
#Rank

import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Define the coordinates of points A, B, and C
a, b, c = 1, 2, 3  # You can change these values as needed

#Given points
A = np.array(([a, b + c])).reshape(-1,1) 
B = np.array(([b, c + a])).reshape(-1,1)  
C = np.array(([c, a + b])).reshape(-1,1)  

#Print rank 
print(LA.matrix_rank(np.block([B-A,C-A])))

#Generate line points
def line_gen(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

#Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')

#Labeling the coordinates
tri_coords = np.block([[A,B,C]])
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A','B','C']
for i, txt in enumerate(vert_labels):
    #plt.annotate(txt, # this is the text
    plt.annotate(f'{txt}\n({tri_coords[0,i]:.0f}, {tri_coords[1,i]:.0f})',
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

# Set labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Collinear Points A, B, C')
plt.grid(True)
plt.legend()
plt.savefig('Figure_1.jpg')
plt.show()
