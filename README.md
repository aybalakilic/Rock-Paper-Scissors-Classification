# Rock-Paper-Scissors Classification with YOLOv11

This project implements a custom YOLOv11 model to classify hand gestures for Rock-Paper-Scissors. The model is trained on labeled images and deployed for both real-time camera-based predictions and static image classification.

## Features
- **Custom YOLOv11 Model**: Fine-tuned for Rock, Paper, and Scissors gestures.
- **Real-Time Detection**: Uses a webcam to classify hand gestures live.
- **Image Classification**: Processes static images for classification.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/username/rock-paper-scissors-yolov11.git
   cd rock-paper-scissors-yolov11
   ```

2. Ensure the YOLOv11 environment is set up correctly and the model file (`model_best.pt`) is placed in the project directory.

## Usage

### Real-Time Detection
Run the following command to use the webcam for live detection:
```bash
python predict_camera.py
```

### Static Image Classification
Use this command to classify a specific image:
```bash
python predict_images.py --source path/to/your/image.jpg
```

Replace `path/to/your/image.jpg` with the path of your image file.

### Output Example
The results will include:
- **Class Prediction**: Rock, Paper, or Scissors.
- **Confidence Score**: The confidence of the prediction.

## Training
For custom training, use:
```bash
python train.py --data data.yaml --weights yolov11.pt
```
Ensure the `data.yaml` file is configured correctly for your dataset.

## Model Information
- **Model**: YOLOv11
- **Classes**: Rock, Paper, Scissors

---

# Taş-Kağıt-Makas Sınıflandırması YOLOv11 ile

Bu proje, Taş, Kağıt, Makas el hareketlerini sınıflandırmak için özel bir YOLOv11 modeli uygular. Model, etiketlenmiş görüntüler üzerinde eğitilmiştir ve hem kamera hem de statik görüntüler için kullanılmıştır.

## Özellikler
- **Özel YOLOv11 Modeli**: Taş, Kağıt, Makas hareketleri için özelleştirilmiştir.
- **Gerçek Zamanlı Tespit**: Kamera kullanarak el hareketlerini anında sınıflandırır.
- **Görüntü Sınıflandırma**: Statik görüntüler üzerinde sınıflandırma yapar.

## Kurulum

1. Depoyu klonlayın:
   ```bash
   git clone https://github.com/username/rock-paper-scissors-yolov11.git
   cd rock-paper-scissors-yolov11
   ```

2. YOLOv11 kurulumunun doğru olduğundan ve model dosyasının (`model_best.pt`) proje dizininde bulunduğundan emin olun.

## Kullanım

### Gerçek Zamanlı Tespit
Canlı kamera tespiti için:
```bash
python predict_camera.py
```

### Statik Görüntü Sınıflandırma
Belirli bir görüntü için:
```bash
python predict_images.py --source path/to/your/image.jpg
```

`path/to/your/image.jpg` kısmını kendi görüntü yolunuzla değiştirin.

### Çıktı Örneği
Sonuçlar şunları içerir:
- **Sınıf Tahmini**: Taş, Kağıt veya Makas.
- **Güven Skoru**: Tahminin güvenilirliği.

## Eğitim
Kendi eğitiminizi yapmak için:
```bash
python train.py --data data.yaml --weights yolov11.pt
```
`data.yaml` dosyasının veri setinize uygun şekilde ayarlandığından emin olun.

## Model Bilgileri
- **Model**: YOLOv11
- **Sınıflar**: Taş, Kağıt, Makas

