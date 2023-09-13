<font size=20><b>Tensorflow模型GUI界面</b></font>

说明：本项目使用与使用`Tensorflow+Keras`训练的深度学习图像识别任务。

# 目录结构

- `data`：用于存放预测图片，后续通过`GUI`界面选择预测图片时默认打开的是该文件夹。
- `model`：用于存放`Tensorflow.Keras`训练出来的`.h5`模型。
- `lib`：工具代码文件夹。
- `UI`：`UI`界面文件夹。
- `run.py`：启动文件
- `setting.py`：配置文件

# 环境配置
本项目基于`Python 3.8` 和 `Tensorflow 2.9.1`

建议大家首先参照[该教程](http://minglog.hzbmmc.com/2023/02/24/Tensorflow2%20GPU%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%E7%8E%AF%E5%A2%83%E5%AE%89%E8%A3%85/)将`Tensorflow2.9.1`深度学习环境安装完成后，再去下载依赖库。

更多其他依赖库，可以使用以下命令下载：

```sh
pip install -r requirements.txt
```


# 快速开始

你可以通过修改`setting.py`配置文件来快速将你的模型部署到`GUI`界面。

具体要修改的内容如下所示：

1. `labels`：修改为你的任务构成的类别列表。

2. `title`：修改`GUI`界面中显示的标题。

3. `output_activation`：输出层激活函数的种类。应该为`sigmoid`和`softmax`中的一种。

4. `model_path`：模型的存储路径。

5. `path`：检测的数据路径。

6. `size`：图片的统一尺寸大小。

   > 需要注意的是，该值需为WHC三维格式。

7. `max_prob`：最大置信度。

8. `CameraLink`：默认局域网摄像头地址。

9. `CameraTimeout`：局域网摄像头连接超时时间。

上述配置文件内容配置完成后，可以通过以下代码直接开启`GUI`界面。

```sh
python run.py
```

![image-20230913195945581](https://ming-log.oss-cn-hangzhou.aliyuncs.com/img/image-20230913195945581.png)

支持选择图片进行检测、选择本机摄像头和局域网摄像头进行检测。

检测结果将展示在右侧。

![image-20230913200037709](https://ming-log.oss-cn-hangzhou.aliyuncs.com/img/image-20230913200037709.png)