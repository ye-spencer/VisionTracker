import cv2

class camera_operator:
    def __init__(self):
        self.video = cv2.VideoCapture(0) #USB2.0 HD UVC WebCam


    def startscreen(self):
        while (True):
            # ret, frame = self.video.read()
            # cv2.imshow("frame", frame)
            #
            # if cv2.waitKey(1) & 0xFF == ord('q'):
            #     break
            ret, frame = self.video.read()

            cv2.imshow("kaleb is gay", frame)

            cv2.waitKey(0)

        self.video.release()

        cv2.destroyAllWindows()

