import cv2
import time

# Set up camera
cap = cv2.VideoCapture(0)  # 0 = default camera

time.sleep(5)
# Capture image
ret, frame = cap.read()

# Save image
filename = "demo_text.jpg"
cv2.imwrite(filename, frame)

# Release camera
cap.release()
cv2.destroyAllWindows()

print(f"Image saved as {filename}")

# text recognition
import pytesseract

# read image
img = cv2.imread("/Users/ravime/Desktop/Project/Object_Detection+count -Using_YOLOv3-master/demo_text.jpg")

# configurations


# pytessercat
pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'


text = pytesseract.image_to_string(img)

# print text
text = text.split('\n')
print(text)