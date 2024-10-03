import cv2
import pytesseract
import numpy as np
import pyttsx3

engine=pyttsx3.init()

# Set up Tesseract
pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'

# Set up camera
cap = cv2.VideoCapture(0)


while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Perform thresholding to obtain binary image
    ret, binary = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

    # Find contours in binary image
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    # Loop through contours
    for cnt in contours:
        # Check contour area and discard small contours
        area = cv2.contourArea(cnt)
        if area < 500:
            continue

        # Find bounding box for contour
        x, y, w, h = cv2.boundingRect(cnt)

        # Extract text using Tesseract
        text = pytesseract.image_to_string(gray[y:y+h, x:x+w], lang='eng')
        print(text)
        engine.say(text)
        engine.runAndWait()  

        # Draw bounding box and text on frame
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, text, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        

    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):

        break
  
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
