# Rock-Paper-Scissors Classification with YOLOv11

This project demonstrates how to classify gestures for the game "Rock-Paper-Scissors" using a YOLOv11 model. The model is trained on labeled images of the three gestures and applied to real-time video streams to perform gesture classification.

## Features
- **Model Training**: Train a YOLOv11 model for Rock-Paper-Scissors classification.
- **Real-Time Detection**: Use a webcam to classify gestures in real-time.
- **Visualization**: Display the detected gestures with bounding boxes and class labels.

---

# Taş-Kağıt-Makas Sınıflandırması (YOLOv11 ile)

Bu proje, "Taş-Kağıt-Makas" oyunundaki el hareketlerini sınıflandırmak için YOLOv11 modeli kullanır. Model, üç hareketin etiketlenmiş görüntüleri üzerinde eğitilir ve gerçek zamanlı video akışlarında sınıflandırma işlemi gerçekleştirir.

## Özellikler
- **Model Eğitimi**: YOLOv11 modeli ile Taş-Kağıt-Makas sınıflandırması yapılabilir.
- **Gerçek Zamanlı Tespit**: Web kamerası kullanılarak hareketlerin gerçek zamanlı olarak sınıflandırılması.
- **Görselleştirme**: Sınıflandırılan hareketlerin sınıf etiketleri ve sınır kutuları ile görüntülenmesi.

---

## Installation / Kurulum

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/rock-paper-scissors-classification.git
   cd rock-paper-scissors-classification
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

1. Bu projeyi klonlayın:
   ```bash
   git clone https://github.com/yourusername/rock-paper-scissors-classification.git
   cd rock-paper-scissors-classification
   ```

2. Gerekli bağımlılıkları yükleyin:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage / Kullanım

### Model Training / Model Eğitimi
1. Place your dataset in the `data` folder and ensure `data.yaml` is configured correctly.
2. Train the model:
   ```bash
   from ultralytics import YOLO
   model = YOLO("yolov11s.pt")
   model.train(data="data.yaml", epochs=10, imgsz=640)
   ```

### Real-Time Classification / Gerçek Zamanlı Sınıflandırma
1. Run the following script for real-time classification:
   ```python
   from ultralytics import YOLO
   import cv2

   model = YOLO("best.pt")
   camera = cv2.VideoCapture(0)

   while True:
       ret, frame = camera.read()
       results = model.predict(frame)
       
       for result in results:
           boxes = result.boxes
           for box in boxes:
               x1, y1, x2, y2 = map(int, box.xyxy[0])
               cls = int(box.cls[0])
               label = f"{model.names[cls]}"
               cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
               cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

       cv2.imshow("Rock-Paper-Scissors", frame)
       if cv2.waitKey(1) & 0xFF == ord('q'):
           break

   camera.release()
   cv2.destroyAllWindows()
   ```

---

### **Sonuçlar** / **Results**

- **Trained Model**: The model achieves high accuracy in recognizing gestures from both images and real-time streams.
- **Visualization**: Bounding boxes and labels are overlaid on the video feed to indicate detected gestures.

- **Eğitilmiş Model**: Model, hem görüntülerde hem de gerçek zamanlı akışlarda hareketleri yüksek doğrulukla tanır.
- **Görselleştirme**: Tespit edilen hareketleri göstermek için sınır kutuları ve etiketler video akışına eklenir.

---

## Contributing / Katkıda Bulunma
Contributions are welcome! Please open an issue or submit a pull request if you'd like to improve this project.

Katkılarınızı memnuniyetle karşılıyoruz! Lütfen projeyi geliştirmek için bir sorun bildirin veya bir pull request gönderin.

---

## License / Lisans
This project is licensed under the MIT License. See the LICENSE file for details.

Bu proje MIT Lisansı altında lisanslanmıştır. Detaylar için LICENSE dosyasına bakınız.
