# 具体类别
labels = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
nums = len(labels)

# GUI界面标题
title = "基于CNN的手写数字识别"

# 激活函数的种类
output_activation = 'softmax'  # softmax or sigmoid

# 模型保存路径
model_path = "model/number.h5"
# 检测的数据路径
path = 'data'
# 定义图片的统一尺寸大小，需为(WHC)三维格式
size = (28, 28, 1)
# 设置阈值
max_prob = 0.8
# 默认局域网摄像头地址
CameraLink = "http://admin:admin@192.168.0.65:8081"
# 局域网摄像头超时时间（毫秒）
CameraTimeout = 3000