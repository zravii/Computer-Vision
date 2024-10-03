import cv2
import pytesseract
from googletrans import Translator
from gtts import gTTS
import os
import time

# Start the webcam stream
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Convert the image to grayscale for faster processing
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply adaptive thresholding to enhance text regions
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 2)

    # Find contours in the thresholded image
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Loop over the contours and filter out non-text regions
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        area = cv2.contourArea(contour)
        if area > 100 and 0.2 < w / h < 5:
            # Extract the text region and perform OCR
            roi = gray[y:y + h, x:x + w]
            text = pytesseract.image_to_string(roi)

            # Draw a rectangle around the text region and display the text
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            print(text)

            s1 = " "
            s2 = " "
            s1 = text.lstrip()
            s2 += s1
            print(s2) 
            translator = Translator()
            translation = translator.translate( s2 , dest='mr')   
            fin_trans = translation.text 
            print(fin_trans)

            import subprocess

            

            #while(fin_trans != " "):
                #tts = gTTS(fin_trans,lang='mr')
                #tts.save("trans_audio.mp3")
                #subprocess.call(['open', 'trans_audio.mp3'])  


        
       

    # Display the resulting frame
    cv2.imshow("Text Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    k = cv2.waitKey(30) & 0xff

    if k == 27: # press ‘ESC’ to quit

       break

# When everything is done, release the capture and close all windows
cap.release()
cv2.destroyAllWindows()

        
              
