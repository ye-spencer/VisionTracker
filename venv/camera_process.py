import cv2

FRAMES_PER_SECOND = 30

class camera_operator:
    def __init__(self):
        self.video = cv2.VideoCapture(0) #USB2.0 HD UVC WebCam


    def startscreen(self):
        while (True):
            ret, frame = self.video.read()
            cv2.imshow("Frame", frame)

            cv2.waitKey(int(1000 / FRAMES_PER_SECOND))


        self.video.release()

        cv2.destroyAllWindows()

