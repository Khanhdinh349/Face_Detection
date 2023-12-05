import cv2
import os

cap = cv2.VideoCapture(0)

eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

if not os.path.exists("first"):
    os.makedirs("first")

image_captured = False

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in eyes:
        eye_area = w * h
        eye_open_threshold = 2000

        if eye_area >= eye_open_threshold:
            eye_status = "Open"
            img_name = os.path.join("first", "first_image.jpg")
            cv2.imwrite(img_name, frame)
            print("Đã chụp và lưu hình.")
            image_captured = True

            if eye_status == "Open":
                cv2.destroyAllWindows()
                cap.release()
                exit()

        else:
            eye_status = "Closed"

        cv2.putText(frame, f"Eye Open: {eye_status}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    cv2.imshow("Eye Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
