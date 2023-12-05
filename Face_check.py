import cv2
import os

processed_faces_directory = 'second'  

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        face_region = gray[y:y+h, x:x+w]

        for filename in os.listdir(processed_faces_directory):
            if filename.endswith(".jpg") or filename.endswith(".png"):
                processed_face = cv2.imread(os.path.join(processed_faces_directory, filename), 0)

                similarity = cv2.matchTemplate(face_region, processed_face, cv2.TM_CCOEFF_NORMED)

                threshold = 0.8
                if similarity.max() >= threshold:  # So sánh giá trị lớn nhất trong mảng similarity
                    print("Yes")
                    break
        else:
            print("No")

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
