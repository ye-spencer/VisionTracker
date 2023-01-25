import cv2

FRAMES_PER_SECOND = 30
CASC_PATH = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'

class camera_operator:
    def __init__(self):
        self.video = cv2.VideoCapture(0) #USB2.0 HD UVC WebCam
        self.facial_cascade = cv2.CascadeClassifier(CASC_PATH)


    def startscreen(self):
        while (True):
            ret, frame = self.video.read()

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = self.facial_cascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                flags=cv2.CASCADE_SCALE_IMAGE
            )



            cv2.imshow("{0} Face(s) Detected".format(len(faces)), frame)
            cv2.waitKey(int(1000 / FRAMES_PER_SECOND))


        self.video.release()

        cv2.destroyAllWindows()

