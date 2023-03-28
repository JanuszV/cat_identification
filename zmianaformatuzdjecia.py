from PIL import Image
import glob
import os
import matplotlib.pyplot as plt


source="C:/Users/barto/Desktop/elo"
data_path=os.path.join(source,'*g')
files=glob.glob(data_path)
i=1
for file in files:
	image=Image.open(file)
	#plt.figure()
	#plt.imshow(image)
	image.save("C:/Users/barto/Desktop/eloelo/1({}).jpeg".format(i))
	i = i + 1