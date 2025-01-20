from ultralytics import YOLO
import matplotlib.pyplot as plt
import os
import matplotlib.image as mpimg
import numpy as np

model=YOLO("best.pt")
model.predict(source="images",save=True,save_dir="/predict") 

imagePath="runs\detect\predict"

imagePathsList=[]
for file in os.listdir(imagePath):
    if file.lower().endswith(('png', 'jpg', 'jpeg')):
        imagePathsList.append(os.path.join(imagePath, file))


plt.figure(figsize=(15, 15))  
for idx, img_path in enumerate(imagePathsList[:16]):  
    plt.subplot(4, 4, idx + 1)  
    image = mpimg.imread(img_path)
    plt.imshow(image)
    plt.axis("off")  # Eksenleri gizle


plt.tight_layout()
plt.show()