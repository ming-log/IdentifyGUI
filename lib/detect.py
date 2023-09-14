import tensorflow as tf
import settings
import matplotlib.pyplot as plt
import cv2
import numpy as np
from CVUtils import CVUtils

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def detect_one_from_filepath(img_path, model=tf.keras.models.load_model(settings.model_path)):
    if settings.size[2] == 3:
        img = CVUtils.read_image(img_path)
        # 对单张图片进行检测
        img = img[:, :, ::-1]
        # resize
        img = cv2.resize(img, settings.size[:2])
        img = np.expand_dims(img, 0)
    else:
        img = cv2.imread(img_path, 0)
        # resize
        img = cv2.resize(img, settings.size[:2])
        img = np.expand_dims(img, 0)
        img = np.expand_dims(img, -1)
    predict_res = model.predict(img)
    if settings.output_activation == 'softmax':
        predict_label = settings.labels[predict_res.argmax()]
        max_prob = predict_res.max()
    else:
        predict_res = predict_res[0]
        predict_label = settings.labels[0 if predict_res < 0.5 else 1]
        max_prob = [1-predict_res if predict_res < 0.5 else predict_res][0][0]
    return predict_label, max_prob

def detect_one_from_array(img, model=tf.keras.models.load_model(settings.model_path)):
    if settings.size[2] == 3:
        # 对单张图片进行检测
        img = img[:, :, ::-1]
        # resize
        img = cv2.resize(img, settings.size[:2])
        img = np.expand_dims(img, 0)
    else:
        img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        # resize
        img = cv2.resize(img, settings.size[:2])
        img = np.expand_dims(img, 0)
        img = np.expand_dims(img, -1)
    predict_res = model.predict(img)
    if settings.output_activation == 'softmax':
        predict_label = settings.labels[predict_res.argmax()]
        max_prob = predict_res.max()
    else:
        predict_res = predict_res[0]
        predict_label = settings.labels[0 if predict_res < 0.5 else 1]
        max_prob = [1-predict_res if predict_res < 0.5 else predict_res][0][0]
    return predict_label, max_prob

def initModel(model=tf.keras.models.load_model(settings.model_path)):
    img = np.random.random(settings.size)
    img = np.expand_dims(img, 0)
    predict_res = model.predict(img)
    if settings.output_activation == 'softmax':
        predict_label = settings.labels[predict_res.argmax()]
        max_prob = predict_res.max()
    else:
        predict_res = predict_res[0]
        predict_label = settings.labels[0 if predict_res < 0.5 else 1]
        max_prob = [1-predict_res if predict_res < 0.5 else predict_res][0][0]
    return predict_label, max_prob

if __name__ == "__main__":
    initModel()
