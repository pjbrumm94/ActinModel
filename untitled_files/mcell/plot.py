import pylab, os, glob

path = "./react_data/"
x = os.listdir(path)
print(x)
#s = [x for x in os.listdir(path) if x.endswith('.')]
#print(s)

#s = glob.glob("*.dat")
#print(s)
#for species in os.listdir('*.dat'):
#	print(species)

#datalist = [( pylab.loadtxt(filename), label ) for filename, label in s)
