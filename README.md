# This GitHub repo contains all the code for my MSc Business Information Management final thesis

iden_ransomware_VT.py allows you to lookup the hash filename of an unclassified folder of ransomware samples within the VirusTotal database. It will change the filename to the ransomware family as labelled by Microsoft + a counter, to ensure that every image has executable has a unique filename.

The image_conversion folders convert the labelled files to grayscale images. The 1-step conversion does not save the full resolution images, whereas as the 2-step conversion does.

The folders starting with 'experiments_' are all the different versions that I have gone through to arrive at the final models. The final CGAN model can be found under 'final_model_Conditional_GAN'. The final classification models can be found under 'final_models_cross_validation'. 

The outdated_* folders include my first attempts at a GAN and CNN, but should be ignored. 

The template_nn folder is used to add additional features, graphs, and other misc. things. I can subsequently use those in Kaggle and on my local machine. 

The Misc. folder includes scripts that allow me to retrieve the output files from any Kaggle run. 
The misc_experiments folder include a learning curve where I try to see how large the training set needs to be to achieve good performance. 

