import os
import tensorflow as tf
import numpy as np
import cv2

path_root = "C:/Users/Max/Documents/thesis_data"

def get_data():
  img_list = []
  for root, dirs, files in os.walk(path_root):
    for f in files:
      file_path = f"{root}/{f}"
      img_list.append(file_path)

  # Read images
  img_size = 64 # Image size of GAN is 64x64
  data = np.empty((len(img_list), img_size, img_size, 3), dtype=np.float32)

  ## Read and convert to images
  for i, img_path in enumerate(img_list):
    # read image
    img = cv2.imread(img_path)

    # resize image
    img = cv2.resize(img, (img_size, img_size), 
                    interpolation = cv2.INTER_CUBIC)
    # save to array
    data[i] = img

  # Normalize the input data.
  def scale(image):
    image = tf.cast(image, tf.float32)
    image /= 255.0
    return image

  data = tf.data.Dataset.from_tensor_slices(data)
  dataset = data.map(scale)
  
  return dataset

data = get_data()

dataset = next(data)
print(dataset.shape)

