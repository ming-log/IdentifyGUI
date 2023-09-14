from PySide6.QtCore import QCoreApplication, Qt, QTimer
from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog, QWidget, QMessageBox
from PySide6.QtGui import QPixmap, QImage
from UI.MainIdentify_ui import Ui_MainWindow
from UI.ChildrenDetect_ui import Ui_Dialog
import cv2
import sys
import os
import time
# 添加软件包检索目录
sys.path.append('.')
import tensorflow as tf
import settings
from lib.detect import detect_one_from_filepath, detect_one_from_array, initModel

# 设置当连接局域网摄像头超过5秒时，退出连接
os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = f"timeout;{settings.CameraTimeout}"

def convert2QImage(img):
    height, width, channel = img.shape
    return QImage(img, width, height, width * channel, QImage.Format_RGB888)

class MainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainForm, self).__init__(parent)
        self.setupUi(self)
        self.title.setText(settings.title)
        # 定义槽函数
        self.detect_image.clicked.connect(self.open_image)
        self.detect_camera.clicked.connect(self.open_camera)
        self.detect_camera_2.clicked.connect(self.open_camera2)
        # 导入模型
        self.model = tf.keras.models.load_model(settings.model_path)
        # 初始化模型
        initModel(self.model)
        # 定义检测摄像头timer
        self.timer1 = QTimer()
        self.timer1.timeout.connect(self.detectCamera)  # 设置检测函数
        self.timer1.setInterval(1)
        # 定义检测摄像头timer
        self.timer2 = QTimer()
        self.timer2.timeout.connect(self.detectCamera)  # 设置检测函数
        self.timer2.setInterval(1)
        # 定义视频帧
        self.videoFrame = None
        # 定义摄像头设备句柄
        self.cap = None
        # 定义局域网摄像头地址
        self.cameraLink = 0

        # 定义计算FPS属性
        self.prev_frame_time = 0
        self.new_frame_time = 0
        self.fps = 0

        # 定义子页面
        self.child = ChildrenForm()
        # 定义子页面槽函数
        self.child.timer = self.timer2

    def open_image(self):
        self.stopAllTimer()
        file_path, _ = QFileDialog.getOpenFileName(self, '选择图片', settings.path, "Image files (*.jpg *.jpeg, *.png)")
        # 当不为空时，显示图片
        if file_path:
            self.input.setPixmap(QPixmap(file_path))
            pred_label, max_prob = detect_one_from_filepath(file_path, self.model)
            if max_prob >= settings.max_prob:
                self.result.setStyleSheet("QLabel{color:green;}")
                self.result.setText(f"{pred_label}\n{max_prob*100:.2f}%")
            else:
                self.result.setStyleSheet("QLabel{color:red;}")
                self.result.setText("不存在目标")

    def open_camera(self):
        if (self.detect_camera.text() != "停止检测"):
            self.stopAllTimer()
            self.cap = cv2.VideoCapture(0)
            self.child.cap = None
            self.timer1.start()
            self.detect_camera.setStyleSheet("QPushButton{color:white;}\
                                              QPushButton{background-color:green;}")
            self.detect_camera.setText('停止检测')
        else:
            self.timer1.stop()
            self.cap.release()
            self.detect_camera.setStyleSheet("QPushButton{color:black;}\
                                             QPushButton{background-color:white;}")
            self.detect_camera.setText('本机摄像头检测')

    def open_camera2(self):
        if (self.detect_camera_2.text() != "停止检测"):
            self.stopAllTimer()
            self.child.show()  # 展示子窗口
            self.detect_camera_2.setStyleSheet("QPushButton{color:white;}\
                                                QPushButton{background-color:green;}")
            self.detect_camera_2.setText('停止检测')
        else:
            self.timer2.stop()
            if self.child.cap:
                self.child.cap.release()
            self.detect_camera_2.setStyleSheet("QPushButton{color:black;}\
                                             QPushButton{background-color:white;}")
            self.detect_camera_2.setText('局域网摄像头检测')

    def detectCamera(self):
        # 获取当前视频帧
        if self.child.cap:
            ret, frame = self.child.cap.read()
        else:
            ret, frame = self.cap.read()
        # 添加fps
        self.new_frame_time = time.time()
        self.fps = "FPS:" + str(int(1/(self.new_frame_time - self.prev_frame_time)))
        self.prev_frame_time = self.new_frame_time
        cv2.putText(frame, self.fps, (7, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (100, 255, 0), 3, cv2.LINE_AA)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.input.setPixmap(QPixmap.fromImage(convert2QImage(frame)))
        pred_label, max_prob = detect_one_from_array(frame, self.model)
        if max_prob >= settings.max_prob:
            self.result.setStyleSheet("QLabel{color:green;}")
            self.result.setText(f"{pred_label}\n{max_prob*100:.2f}%")
        else:
            self.result.setStyleSheet("QLabel{color:red;}")
            self.result.setText("不存在目标")
    
    def stopAllTimer(self):
        self.timer1.stop()
        self.timer2.stop()
    

class ChildrenForm(QWidget, Ui_Dialog):
    def __init__(self):
        super(ChildrenForm, self).__init__()
        self.setupUi(self)
        self.textEdit.setPlainText(settings.CameraLink)  # 设置默认地址
        # 设置槽连接
        self.submit.clicked.connect(self.getCameraLink)
        self.cancle.clicked.connect(self.close)
        self.timer = None
        self.cap = None

    def getCameraLink(self):
        CameraLink = self.textEdit.toPlainText()
        self.cap = cv2.VideoCapture(CameraLink, cv2.CAP_FFMPEG)
        if (self.cap is not None) and (self.cap.isOpened()):
            self.timer.stop()
            self.timer.start()
            self.close()
        else:
            QMessageBox.warning(self, "摄像头连接异常", "摄像头连接异常。\n请检查局域网摄像头是否处于开启状态，并填写正确的连接地址。", QMessageBox.Yes )

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ui = MainForm()
    ui.show()
    sys.exit(app.exec())
