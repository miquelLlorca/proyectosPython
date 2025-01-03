from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

im = Image.open('jorge.jpg')

img = np.asarray(im)

im.close()

print(np.shape(img))

res = []
for i in range(9):
    res.append(0)

for i in range(len(img)):
    for j in range(len(img[0])):
        for k in range(3):
            n = str(img[i][j][k])
            for l in range(len(n)):
                if(n[l] == '1'):
                    res[0] += 1
                elif(n[l] == '2'):
                    res[1] += 1
                elif(n[l] == '3'):
                    res[2] += 1
                elif(n[l] == '4'):
                    res[3] += 1
                elif(n[l] == '5'):
                    res[4] += 1
                elif(n[l] == '6'):
                    res[5] += 1
                elif(n[l] == '7'):
                    res[6] += 1
                elif(n[l] == '8'):
                    res[7] += 1
                elif(n[l] == '9'):
                    res[8] += 1

#--------------------------------------------------------------------------------------------

def autolabel(rects, xpos='center'): 
    xpos = xpos.lower()  # normalize the case of the parameter
    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0.5, 'right': 0.57, 'left': 0.43}  # x_txt = x + w*off

    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()*offset[xpos], 1.01*height,
                '{}'.format(height), ha=ha[xpos], va='bottom')



ind = np.arange(9)  #localizacion de barras
width = 0.3 # ancho de barras

fig, ax = plt.subplots()

rects1 = ax.bar(ind - width, res, width, color='r')


ax.set_title('Ley de benfort')
ax.set_xticks(ind)
ax.set_xticklabels(('1', '2', '3', '4', '5', '6', '7', '8', '9'))
ax.legend(loc='best')

plt.show()


