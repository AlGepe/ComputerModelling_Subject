import numpy as np
import utils as u
import matplotlib.pyplot as plt

N = 10
matrix = np.random.randint(2,size=(N, N))
mat = np.random.randint(2,size=(N, N))
m = np.random.randint(2,size=(N, N))

# matrix[0,0] = 99999
# matrix[1,0] = -99999
plt.imshow(matrix, interpolation='nearest', cmap='seismic')
print(matrix)
plt.show()
plt.imshow(matrix+mat, interpolation='nearest', cmap='seismic')
print(matrix+mat)
plt.show()
plt.imshow((matrix+mat+m)*1, interpolation='nearest', cmap='seismic')
print(matrix+mat+m)
plt.show()
plt.imshow((matrix+mat+m)*10, interpolation='nearest', cmap='RdBu')
print((matrix+mat+m)*10)
plt.show()
plt.imshow((matrix+mat+m)*10-(matrix+mat+m), interpolation='nearest', cmap='gist_stern')
print(((matrix+mat+m)*10)-(mat+m))
plt.show()

'''
print("original")
print(matrix)
print('\n')
print("Shifted by 0, 0")
print(u.shiftPB(matrix, [0, 0]))
print('\n')
print("Shifted by 1, 0")
print(u.shiftPB(matrix, [1, 0]))
print('\n')
print("Shifted by -1, 0")
print(u.shiftPB(matrix, [-1, 0]))
print('\n')
print("Shifted by 0, -1")
print(u.shiftPB(matrix, [0, -1]))
print('\n')
print("Shifted by 0, 1")
print(u.shiftPB(matrix, [0, 1]))
# +-1
print('\n')
print("Shifted by -1, 1")
print(u.shiftPB(matrix, [-1, 1]))
print('\n')
print("Shifted by 1, -1")
print(u.shiftPB(matrix, [1, -1]))
print('\n')
print("Shifted by -1, -1")
print(u.shiftPB(matrix, [-1, -1]))
print('\n')
print("Shifted by 1, 1")
print(u.shiftPB(matrix, [1, 1]))
print('\n')
'''
