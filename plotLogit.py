import matplotlib.pyplot as plt
import numpy as np
xData = np.linspace(-8,8, 1000, endpoint = True)

def fnRetSigmoid(data):
	exponent = np.e ** (-1 * data)
	denominator = 1 + exponent
	return (1 / denominator)

yData = np.apply_along_axis(fnRetSigmoid, 0, xData)

# create basic plot
plt.plot(xData, yData, linewidth=1.5, color = 'r')

#get axes object
axes = plt.gca()

#make the top and bottom axes invisible
axes.spines['right'].set_color('none')
axes.spines['top'].set_color('none')

# moves the axes so that they are in the middle
axes.spines['bottom'].set_position(('data', 0.5))
axes.spines['left'].set_position(('data', 0))

#set tick position
axes.xaxis.set_ticks_position('bottom')
axes.yaxis.set_ticks_position('left')

#set the range of x & y
plt.xlim(-7,7)
plt.ylim(-.1, 1.1)


#set tick values 
xtickValue = [-6, -4, -2, 2, 4, 6]
xtickDisplay = ['-6', '-4', '-2',  '2', '4', '6' ]
plt.xticks(xtickValue, xtickDisplay)

ytickValue = [0, 0.25, 0.75, 1]
ytickDisplay = ['0.00', '0.25', '0.75', '1.00']
plt.yticks(ytickValue, ytickDisplay)

# the following returns: array([-6, -4, -2,  2,  4,  6])
# axes.get_xticks()

# the following returns: (-0.10000000000000001, 1.1000000000000001)
# axes.get_ylim()


xLower = np.round(axes.get_xlim(),4)[0]
xUpper = np.round(axes.get_xlim(),4)[1]

# lower = -7; upper = 7. 14+1 increments. 43 = (14 * 3) +1
xGrid = np.linspace(xLower, xUpper, 43, endpoint=True)
for xPos in xGrid:
	plt.axvline(xPos, linestyle='-', color = '#0000CC', alpha = 0.4, linewidth = 0.2)



yLower = np.round(axes.get_ylim(),4)[0]
yUpper = np.round(axes.get_ylim(),4)[1]

yGrid = np.linspace(yLower, yUpper, 25, endpoint=True)
 
for yPos in yGrid:
	plt.axhline(yPos, linestyle='-', color = '#0000CC', alpha = 0.4, linewidth = 0.2)


plt.show()


#now to save the plot as a pdf
from matplotlib.backends.backend_pdf import PdfPages
pp = PdfPages('logitPDF.pdf')
pp.savefig()
#you NEED to close the file
pp.close()













