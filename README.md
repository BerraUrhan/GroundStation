# GroundStation
🛰️Ground Station Software working with real data created with PyQt6 framework for TEKNOFEST Model Satellite Contest.🛰️

The ground station that I have created utilizes Xbee communication to send and receive data with the model satellite, allowing for a stable and reliable connection. 

Real-time data from the model satellite's BMP sensor, including temperature and pressure, are displayed on charts for easy visualization. In addition to this, the ground station features a gyro chart in the bottom left corner that displays pitch, roll, and yaw data. 

While live camera and map features are currently under development, the ground station provides accurate and reliable data for monitoring the performance of the model satellite.

The ground station also supports FTP functionality, which allows for easy transfer of files and data between the ground station and the model satellite.

NOTE : host, username and password should be changed based on your data in the FTPhandler.py class. Here is the code snippet that should be changed: 

    def uploadFile(self):
        uploadClient = FTPhandler('host', 'username', 'password')
        uploadClient.upload(str(self.uploadFileDir))

    def downloadFile(self):
        downloadClient = FTPhandler('host', 'username', 'password')
        downloadClient.retrieve()
        


<img width="1460" alt="Screenshot 2023-04-10 at 14 49 30" src="https://user-images.githubusercontent.com/102544533/230896281-642d6f66-a4ba-4c05-9a32-88c44b33bf6e.png">
