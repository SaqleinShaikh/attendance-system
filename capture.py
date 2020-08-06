import cv2 
import time

def PHOTO_T():

   key = cv2. waitKey(1)
   webcam = cv2.VideoCapture(0)
   while True:
       try:
           check, frame = webcam.read()
           cv2.imshow("Please press S for captured the photo", frame)
           key = cv2.waitKey(1)
           if key == ord('s'): 
               cv2.imwrite(filename='saved_img.jpg', img=frame)
               img_new = cv2.imread('saved_img.jpg', cv2.IMREAD_COLOR)
               #p.destroyAllWindows()
               img_new = cv2.imshow("Your entry is succesfully registerd enter any key to exit", img_new)
               cv2.waitKey(1650)
               time.sleep(1)
               cv2.destroyAllWindows()
               break
       except(KeyboardInterrupt):
           print("Turning off camera.")
           webcam.release()
           print("Camera off.")
           print("Program ended.")
           cv2.destroyAllWindows()
           break
    
