from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
from PyQt5.QtGui import QImage, QPixmap
from detection import Detection


class DetectionWindow(QMainWindow):
    def __init__(self):
        super(DetectionWindow, self).__init__()
        loadUi("detection_window.ui", self)

        # Start detection thread
        self.thread = Detection()
        self.thread.changePixmap.connect(self.setImage)
        self.thread.start()

        # Connect stop button
        self.stop_button.clicked.connect(self.stopMonitoring)

    def setImage(self, image: QImage):
        """Display camera feed in QLabel"""
        self.camera_label.setPixmap(QPixmap.fromImage(image))

    def stopMonitoring(self):
        """Stop camera and close window"""
        if self.thread.isRunning():
            self.thread.stop()       # custom stop method in Detection
            self.thread.wait()       # wait for thread to finish
        self.close()

    def closeEvent(self, event):
        """Ensure camera thread is stopped if window is closed directly"""
        self.stopMonitoring()
        event.accept()
