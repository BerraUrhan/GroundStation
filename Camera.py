import os
import sys
from PySide6.QtCore import QDate, QDir, QStandardPaths, Qt, QUrl, Slot
from PySide6.QtGui import QAction, QGuiApplication, QDesktopServices, QIcon
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QTabWidget, QToolBar, QVBoxLayout, QWidget)
from PySide6.QtMultimedia import (QCamera, QImageCapture,
                                  QCameraDevice, QMediaCaptureSession,
                                  QMediaDevices)
from PySide6.QtMultimediaWidgets import QVideoWidget


class ImageView(QWidget):
    def __init__(self, previewImage, fileName):
        super().__init__()

        #self._file_name = fileName

        #main_layout = QVBoxLayout(self)
        #self._image_label = QLabel()
        #self._image_label.setPixmap(QPixmap.fromImage(previewImage))
        #main_layout.addWidget(self._image_label)

        top_layout = QHBoxLayout()
        #self._file_name_label = QLabel(QDir.toNativeSeparators(fileName))
        #self._file_name_label.setTextInteractionFlags(Qt.TextBrowserInteraction)

        #top_layout.addWidget(self._file_name_label)
        top_layout.addStretch()
        copy_button = QPushButton("Copy")
        copy_button.setToolTip("Copy file name to clipboard")
        top_layout.addWidget(copy_button)
        copy_button.clicked.connect(self.copy)
        launch_button = QPushButton("Launch")
        launch_button.setToolTip("Launch image viewer")
        top_layout.addWidget(launch_button)
        launch_button.clicked.connect(self.launch)
        #main_layout.addLayout(top_layout)



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self._capture_session = None
        self._camera = None
        self._camera_info = None
        self._image_capture = None

        available_cameras = QMediaDevices.videoInputs()
        if available_cameras:
            # TODO:
            self._camera_info = available_cameras[0]
            self._camera = QCamera(self._camera_info)
            self._camera.errorOccurred.connect(self._camera_error)
            self._image_capture = QImageCapture(self._camera)
            """self._image_capture.imageCaptured.connect(self.image_captured)
            self._image_capture.imageSaved.connect(self.image_saved)
            self._image_capture.errorOccurred.connect(self._capture_error)"""
            self._capture_session = QMediaCaptureSession()
            self._capture_session.setCamera(self._camera)
            self._capture_session.setImageCapture(self._image_capture)

        self._current_preview = QImage()

        tool_bar = QToolBar()
        #self.addToolBar(tool_bar)

        #file_menu = self.menuBar().addMenu("&File")


        exit_action = QAction(QIcon.fromTheme("application-exit"), "E&xit",
                              self, shortcut="Ctrl+Q", triggered=self.close)
        #file_menu.addAction(exit_action)

        #about_menu = self.menuBar().addMenu("&About")
        about_qt_action = QAction("About &Qt", self)
        #about_menu.addAction(about_qt_action)

        self._tab_widget = QTabWidget()
        self.setCentralWidget(self._tab_widget)

        self._camera_viewfinder = QVideoWidget()
        self._tab_widget.addTab(self._camera_viewfinder, "Viewfinder")

        if self._camera and self._camera.error() == QCamera.NoError:
            name = self._camera_info.description()
            self.setWindowTitle(f"PySide6 Camera Example ({name})")
            self.show_status_message(f"Starting: '{name}'")
            self._capture_session.setVideoOutput(self._camera_viewfinder)
            #self._take_picture_action.setEnabled(self._image_capture.isReadyForCapture())
#            self._image_capture.readyForCaptureChanged.connect(self._take_picture_action.setEnabled)
            self._camera.start()
        else:
            self.setWindowTitle("PySide6 Camera Example")
            #self._take_picture_action.setEnabled(False)
            self.show_status_message("Camera unavailable")

    def show_status_message(self, message):
        self.statusBar().showMessage(message, 5000)

    def closeEvent(self, event):
        if self._camera and self._camera.isActive():
            self._camera.stop()
        event.accept()

    @Slot(int, QImageCapture.Error, str)
    def _capture_error(self, id, error, error_string):
        print(error_string, file=sys.stderr)
        self.show_status_message(error_string)

    @Slot(QCamera.Error, str)
    def _camera_error(self, error, error_string):
        print(error_string, file=sys.stderr)
        self.show_status_message(error_string)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    available_geometry = main_win.screen().availableGeometry()
    main_win.resize(available_geometry.width() / 3, available_geometry.height() / 2)
    main_win.show()
    sys.exit(app.exec())