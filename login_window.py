from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.uic import loadUi
import os

class LoginWindow(QMainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        ui_path = os.path.join(os.path.dirname(__file__), "login_window.ui")
        loadUi(ui_path, self)

        # connect login button
        self.login_button.clicked.connect(self.go_to_settings)

    def go_to_settings(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if username == "admin" and password == "admin":  # simple demo check
            from settings_window import SettingsWindow
            self.settings_window = SettingsWindow()
            self.settings_window.show()
            self.close()
        else:
            QMessageBox.warning(self, "Error", "Invalid username or password")
