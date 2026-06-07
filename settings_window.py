from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.uic import loadUi
import os

class SettingsWindow(QMainWindow):
    def __init__(self):
        super(SettingsWindow, self).__init__()
        ui_path = os.path.join(os.path.dirname(__file__), "settings_window.ui")
        loadUi(ui_path, self)

        # connect start monitoring button
        self.start_button.clicked.connect(self.go_to_detection)

    def go_to_detection(self):
        location = self.location_input.text()
        send_to = self.sendto_input.text()

        if not location or not send_to:
            QMessageBox.warning(self, "Error", "Please fill all fields before continuing")
            return

        from detection_window import DetectionWindow
        self.detection_window = DetectionWindow()
        self.detection_window.show()
        self.close()
