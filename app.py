from flask import Flask, render_template, Response, jsonify
import cv2, numpy as np
from tensorflow.keras.models import load_model

app = Flask(__name__)

model = load_model("model.h5")
emotions = ['Angry','Disgust','Fear','Happy','Sad','Surprise','Neutral']

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

camera = None
detecting = False
last_result = {"emotion": "None", "confidence": 0}

def open_camera():
    global camera
    if camera is None or not camera.isOpened():
        camera = cv2.VideoCapture(0)

def close_camera():
    global camera
    if camera and camera.isOpened():
        camera.release()
        camera = None

def generate_frames():
    global last_result
    while True:
        if not detecting or camera is None:
            continue

        success, frame = camera.read()
        if not success:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x,y,w,h) in faces:
            roi = gray[y:y+h, x:x+w]
            roi = cv2.resize(roi, (48,48))
            roi = roi.reshape(1,48,48,1) / 255.0

            preds = model.predict(roi, verbose=0)[0]
            idx = np.argmax(preds)

            label = emotions[idx]
            confidence = round(float(preds[idx]) * 100, 2)

            last_result = {"emotion": label, "confidence": confidence}

            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
            cv2.putText(frame, f"{label} {confidence}%",
                        (x,y-10),
                        cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,255,255),2)

        _, buffer = cv2.imencode(".jpg", frame)
        frame = buffer.tobytes()

        yield (b"--frame\r\n"
               b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/video")
def video():
    return Response(generate_frames(),
                    mimetype="multipart/x-mixed-replace; boundary=frame")

@app.route("/toggle")
def toggle():
    global detecting
    detecting = not detecting

    if detecting:
        open_camera()
    else:
        close_camera()

    return jsonify({"detecting": detecting})

@app.route("/status")
def status():
    return jsonify(last_result)

if __name__ == "__main__":
    app.run(debug=True)
