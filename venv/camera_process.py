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

            faces = self.facial_cascade.detectMultiScale(
                cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), #turn it grayscale for identification
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                flags=cv2.CASCADE_SCALE_IMAGE
            )

            for face in faces:
                cv2.rectangle(frame, (face[0], face[1]), (face[0] + face[2], face[1] + face[3]), (0, 128, 128), 2)

            cv2.imshow("Main Frame", frame)
            cv2.setWindowTitle("Main Frame", "{0} Face(s) Detected".format(len(faces)))
            if (cv2.waitKey(int(1000 / FRAMES_PER_SECOND)) & 0xFF == ord('p')):
                break

        self.video.release()

        cv2.destroyAllWindows()

