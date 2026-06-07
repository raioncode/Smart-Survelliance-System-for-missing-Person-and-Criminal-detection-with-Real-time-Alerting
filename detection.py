from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QImage
import cv2


class Detection(QThread):
    changePixmap = pyqtSignal(QImage)

    def __init__(self):
        super(Detection, self).__init__()
        self.running = False   # start as False
        self.cap = None

    def run(self):
        print("[Detection] Thread started")
        self.running = True
        self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # CAP_DSHOW = more stable on Windows

        if not self.cap.isOpened():
            print("[Detection] ❌ Failed to open camera")
            return

        while self.running:
            ret, frame = self.cap.read()
            if not ret:
                continue  # skip bad frames, don’t exit

            rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb_image.shape
            bytes_per_line = ch * w
            qimg = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
            self.changePixmap.emit(qimg)

        # cleanup
        self.cap.release()
        print("[Detection] Thread stopped")

    def stop(self):
        """Stop the camera safely"""
        self.running = False
        self.wait()  # wait until run() exits
