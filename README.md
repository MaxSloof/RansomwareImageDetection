# This GitHub repo was initially set up for my master thesis. 

iden_ransomware_VT.py allows you to lookup the hash filename of an unclassified folder of ransomware samples within the VirusTotal database. It will change the filename to the ransomware family as labelled by Microsoft + a counter, to ensure that every image has executable has a unique filename.

The image_conversion folders convert the labelled files to grayscale images. The 1-step conversion does not save the full resolution images, whereas as the 2-step conversion does.

The CNN, DCGAN, DCGAN classification, DenseNet, and ResNet folder all include iterations of their respective Neural Network models. To improve the performance of the NN models, I tried different versions to see which would lead to the highest performance. For my thesis I aim to compare the CNN model to another model, where I used a GAN to generate fake images and then a CNN-based model to see whether I could improve performance that way. 

The outdated_* folders include my first attempts at a GAN and CNN, but should be ignored. 

The template_nn folder is used to add additional features, graphs, and other misc. things. I can subsequently use those in Kaggle and on my local machine. 

The Misc. folder includes scripts that allow me to retrieve the output files from any Kaggle run. 

