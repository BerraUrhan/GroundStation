from PyQt6.QtWidgets import QApplication, QFileDialog, QWidget, QGridLayout, QLineEdit, QPushButton, QLabel
from pathlib import Path
from ftplib import FTP
import sys
import os


class FTPhandler:
    def __init__(self, host, username, password) -> None:
        self.hostname = host
        self.username = username
        self.password = password

    def upload(self, dir):
        with FTP(self.hostname) as ftpClient:
            ftpClient.login(self.username, self.password)

            uploadFile = open(dir, 'rb')
            if not open(dir):
                print("could NOT open the video")
            uploadString = 'STOR ' + os.path.basename(dir)
            ftpClient.storbinary(uploadString, uploadFile)
            uploadFile.close()

            ftpClient.quit()

    def retrieve(self):
        with FTP(self.hostname) as ftpClient:
            ftpClient.login(self.username, self.password)

            fileDirectory = ftpClient.nlst()
            if len(fileDirectory) > 0:
                for file in fileDirectory:
                    filename = file.split()[-1]
                    with open(filename, 'wb') as downloadFile:
                        downloadString = 'RETR ' + filename
                        ftpClient.retrbinary(downloadString, downloadFile.write)

            ftpClient.quit()


class MainWindowFTP(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('FTP Demo')
        self.setGeometry(100, 100, 400, 100)

        layout = QGridLayout()
        self.setLayout(layout)

        file_browse = QPushButton('Browse')
        file_browse.clicked.connect(self.open_file_dialog)
        self.filename_edit = QLineEdit()

        uploadButton = QPushButton('Upload')
        uploadButton.clicked.connect(self.uploadFile)

        downloadButton = QPushButton('Download')
        downloadButton.clicked.connect(self.downloadFile)

        layout.addWidget(QLabel('File:'), 0, 0)
        layout.addWidget(self.filename_edit, 0, 1)
        layout.addWidget(file_browse, 0, 2)
        layout.addWidget(uploadButton, 1, 2)
        layout.addWidget(downloadButton, 2, 2)

        self.show()

    def open_file_dialog(self):
        filename, ok = QFileDialog.getOpenFileName(self, "Select a File")
        if filename:
            path = Path(filename)
            self.filename_edit.setText(str(path))
            self.uploadFileDir = str(path)

    def uploadFile(self):
        uploadClient = FTPhandler('host', 'username', 'password')
        uploadClient.upload(str(self.uploadFileDir))

    def downloadFile(self):
        downloadClient = FTPhandler('host', 'username', 'password')
        downloadClient.retrieve()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindowFTP()
    window.show()

    app.exec()