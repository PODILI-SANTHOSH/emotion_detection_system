# 🎭 Emotion Detection System

An **Emotion Detection System** that identifies human emotions from facial expressions using deep learning.  
The project includes **model training** and a **local web application** to test emotion detection in real time.

This system is suitable for learning, research, and demo purposes.

---

## 🚀 Features

- Detects human emotions from facial images
- Trained using a Convolutional Neural Network (CNN)
- Supports real-time emotion prediction via a local web server
- Easy to train and run locally
- Clean separation between training and application logic

---

## 🧠 Emotions Detected

- Angry  
- Disgust  
- Fear  
- Happy  
- Sad  
- Surprise  
- Neutral  

---
## 🛠 Requirements

- Python 3.8 or above
- Webcam (for live detection)
- Virtual environment (recommended)

---

## 📦 Install Dependencies

```bash
pip install -r requirements.txt
```
#### 🧪 Train the Model
Run the training script to train the emotion detection model:
```bash
python train.py
```
After training completes, a model file (e.g., model.h5) will be saved automatically

#### 🌐 Run on Local Server
Start the local web application:
```bash
python app.py
```
Then open your browser and go to:
```bash
http://127.0.0.1:5000
```

#### 🖥 How It Works
     The model is trained on facial expression images.
     The trained model is loaded in the web application.
     Webcam input or uploaded images are processed.
     The system predicts the emotion and displays it in real time.

#### 🎯 Use Cases
     Emotion-aware applications
     Human-computer interaction
     Academic projects
     AI & ML learning demos
     Behavioral analysis experiments

#### ⚠ Notes
     Ensure proper lighting for accurate detection.
     Training time depends on dataset size and system performance.
     Best results are achieved with balanced datasets.
