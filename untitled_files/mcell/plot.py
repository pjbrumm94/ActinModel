# PURPOSE: This code is used for plotting the number of molecules over the 
#entire simulation time. Data held in ".dat" files in the react_data folder
# AUTHOR: Peter J Brumm
# DATE: 11/30/2018

import pylab, os

# Create path to .dat files and retainer list
path	= "./react_data/"
flist	= []

# Show list of .dat files with labels in retainer
for f in os.listdir(path):
	if f.endswith('.dat'):
		flist.append((f, f.split(".")[0]))

# Import timecourse data and associate with label
datalist = [( label, pylab.loadtxt(path+filename))
		for filename, label in flist]

# For each data file, plot timecourse data with label
for label, data in datalist:
	pylab.plot(data[:,0], data[:,1], label=label)

# PyLab Plotting Area
pylab.legend()
pylab.xlabel('Timestep')
pylab.ylabel('Molecule Count')
pylab.show()
