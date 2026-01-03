# 🎭 Emotion Detection AI (Local Setup)

A **Facial Emotion Detection** system built using **Deep Learning (CNN)** and trained on the **FER-2013 dataset**.  
This project is designed to run **locally** due to dataset size and hardware requirements.

⚠️ **Note:**  
The FER-2013 dataset is **not included in this repository** because it is large.  
You must download it manually using **Kaggle** and run the project locally.

---

## 🔥 Features

- Detects **7 human emotions**:
  - Angry
  - Disgust
  - Fear
  - Happy
  - Sad
  - Surprise
  - Neutral
- Real-time emotion prediction using webcam
- Confidence percentage for predictions
- Start / Stop detection control
- Emotion history visualization
- Glassmorphic, mobile-responsive UI
- Built with Flask + TensorFlow

---

## 🧠 Model Details

- **Model Type:** Convolutional Neural Network (CNN)
- **Dataset:** FER-2013 (Kaggle)
- **Input Shape:** 48×48 grayscale images
- **Batch Size:** 64
- **Epochs:** 10
- **Framework:** TensorFlow / Keras

---

## ⚠️ Why Dataset Is Not Included

The **FER-2013 dataset is large**, and GitHub has file size limits.  
To keep the repository clean and lightweight, the dataset is **excluded**.

✔ This is **standard practice** in machine learning projects.

---

## 📥 Dataset Download (FER-2013)

### Option 1: Using Kaggle CLI (Recommended)

#### 1️⃣ Install Kaggle
```bash
pip install kaggle
```
#### 2️⃣ **Create Kaggle API Token**
     -> Go to: https://www.kaggle.com/account
     -> Generate API Token
     -> Create kaggle.json manually:
           ```bash
           {
               "username": "your_kaggle_username",
               "key": "your_api_key"
           }
           ```
# SAVE IT AS
```bash
C:\Users\YOUR_NAME\.kaggle\kaggle.json
```
#### 3️⃣ Download Dataset
```bash
kaggle datasets download -d msambare/fer2013
```
#### 4️⃣ Extract & Move
Extract and place folders like this:
     ```bash
     emotion-detection/
         └── fer2013/
            ├── train/
            └── test/
    ```





