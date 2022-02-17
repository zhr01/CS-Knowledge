## CS knowledge

This project records all the CS knowledge I have learned.

### Contents

* [Computer System](#computer-system)
* [Programming Method](#programming-methods)
* Programming Languages
  * [Python3](#python)
  * [C/C++](#c/c++)
* [Data Structure &  Algorithms](#data-structure/algorithms)
* [Embedded Development](#embedded-development)
* [Machine Learning/Data Mining](#machine-learning)
* [Deep Learning Framework](#Deep-Learning-Framework)
* [Excellent Projects](#Excellent-Projects)
* [Deep Learning](#deep-learning)
* [Deep Reinforcement Learning](#deep-reinforcement-learning)
* [Computer Vision](#computer-vision)
* [Model Compression](#Model-Compression)
* [Tools](#tools)



### Computer System

* [字符编码](computer_system/encoding.md)
* 网络基础
  * [网络整体概述](computer_system/网络整体概述.md)
  * [链路层](computer_system/链路层.md)
  * [网络层](computer_system/网络层.md)
  * 传输层
  * HTTP
  * 
* 数据库
  * [数据库系统概述](computer_system/数据库系统概述.md)
  * [关系数据库设计](computer_system/关系数据库设计.md)
  * 
* 操作系统
  * [开机启动脚本的一些问题](computer_system/开机启动脚本的一些问题.md)
  * 
* 加密和安全
* 编译和体系结构
* 



### Programming Methods

* [Python编程风格规范](https://github.com/zh-google-styleguide/zh-google-styleguide/blob/master/google-python-styleguide/python_style_rules.rst)
* 



### Programming Languages

#### Python

* [参数包裹传递](python/参数包裹传递.md)
* [函数对象-错误处理-动态类型](python/函数对象-错误处理-动态类型.md)
* [内置函数](python/内置函数.md)
* [正则表达式](python/正则表达式.md)
* [进程与线程](python/进程与线程.md)
* [Python性能分析](python/Python性能分析.md)
* [yield的用法](python/yield的用法.md)
* 协程
* [sort()函数多属性排序](algorithm/sort()函数多属性排序.md)
* [变量对象的操作](python/变量对象的操作.md)
* [类 vs. 模块 vs. 包](python/类VS.模块VS.包.md)
* [各种输入方式的区别](python/各种输入方式的区别.md)
* 常用文件数据集类型的读取方法


#### C/C++

- [C指针主要用法](c/C指针主要用法.md)
- [C语言内存管理](c/C语言内存管理.md)
- [C链接器](c/C链接器.md)
- [修饰符](java/修饰符.md)
- [面向对象的三个基本特性（封装、继承、多态）](java/面向对象的三个基本特性（封装、继承、多态）.md)
- [构造函数与析构函数](java/构造函数与析构函数.md)
- 



### Data Structure/Algorithms

* algorithms

  * [排序](algorithm/algorithm-sorting.md)
  * [递归](algorithm/algorithm-recursion.md)
  * [回溯](algorithm/algorithm-backtracking.md)
  * [二分](algorithm/algorithm-Binary-Search.md)
  * [分治](algorithm/algorithm-divide-and-conquer.md)
  * [动归](algorithm/algorithm-dynamic-programming.md)
  * [贪心](algorithm/algorithm-greedy.md)
  * [滑窗](algorithm/algorithm-slide-window.md)

* datastructure

  * [链表](algorithm/datastructure-Linked-List.md)
  * [队列/堆/栈/字典](algorithm/datastructure-queue-heap-stack-map.md)
  * [图](algorithm/datastructure-graph.md)
  * [树](algorithm/datastructure-tree.md)
  * [字符串](algorithm/datastructure-String.md)

  



### Embedded Development

- Raspberry Pi
- Arduino
- MCU
- Jetson




### Machine Learning

- [pipeline](machine_learning/机器学习pipeline.md)
- [稀疏表示](machine_learning/稀疏表示.md)
- 

#### Probability & Statistics

* [统计概率思维导图](machine_learning/probability-statistics/统计概率思维导图.md)
* [描述性统计](machine_learning/probability-statistics/描述性统计.md)
* [★概率](machine_learning/probability-statistics/概率.md)
* [概率分布](machine_learning/probability-statistics/概率分布.md)
* [抽样分布](machine_learning/probability-statistics/抽样分布.md)
* [点估计](machine_learning/probability-statistics/概率论与数理统计--点估计.pdf)
* [区间估计](machine_learning/probability-statistics/概率论与数理统计--区间估计.pdf)
* [假设检验](machine_learning/probability-statistics/概率论与数理统计--假设检验的概念.pdf)
* 

#### Linear Algebra（线性代数）

- [整体概述](machine_learning/linear-algebra/整体概述.md)
- [行列式](machine_learning/linear-algebra/行列式.md)
- [矩阵](machine_learning/linear-algebra/矩阵.md)
- 

#### Data Pre-processing

- [数据预处理](machine_learning/数据预处理.md)
- [特征选择](machine_learning/特征选择.md)

  



#### Regression & Classification & Clustering（回归/分类/聚类）

- [线性模型](machine_learning/%E7%BA%BF%E6%80%A7%E6%A8%A1%E5%9E%8B.md)
- [视觉词袋模型](machine_learning/视觉词袋模型.md)
- [随机采样一致](machine_learning/随机采样一致.md)
- 典型算法
  - [回归](machine_learning/回归.md)
  - 决策树和随机森林
  - [支持向量机](machine_learning/支持向量机.md)
  - [聚类](machine_learning/聚类.md)
  - EM算法
  - 主题模型LDA
  - 隐马尔科夫模型
- 

#### Effectiveness Evaluation（评估标准）

- [评估方法与性能度量](machine_learning/评估标准.md)

#### PGM(Probabilistic Graphical Models概率图模型)



#### Dimensionality Reduction(降维)

- LDA
- [PCA](machien_learning/PCA.md)
- ICA
- [SVD](machine_learning/SVD.md)
- FA

#### Similarity Measure&Distance Measure(相似性与距离度量)

- [距离与相似性度量方法](machine_learning/距离与相似性度量方法.md)

#### Optimization

- [梯度下降法](machine_learning\梯度下降法.md)
- 常用优化器的比较
- 


#### python常用扩展包

- numpy(数组支持)
- scipy(矩阵支持)
- matplotlib/seaborn(画图)
  - [常用图形](machine_learning/常用图形.md)
  - [seaborn  tutorial](machine_learning/seaborn.ipynb)
- pandas(数据分析探索)
  - [pandas tutorial](machine_learning/pandas.md)
- scikit-learn(机器学习库)
  - 



### Deep Learning Framework

- PyTorch
- TensorRT
- onnx
- openVINO



### Excellent Projects

- mmcv
- mmdetection
- nni
- transformers




### Deep Learning

- [Neural networks and deep learning学习笔记](deep-learning/Neural networks and deep learning学习笔记.md)
- [Activation(激活函数)](deep-learning/激活函数.md)
- [Optimizers(优化器)](#optimization)
- Normlize
  - BatchNorm/LayerNorm/InstanceNorm/GroupNorm
  - 
- CNN
- RNN
- Model Compression
  - Pruning
  - Quantization
  - Distillation
  - NAS


- Analysis Pipeline
  - [data preprocess](#data-pre-processing)
  - learning architecture design 
  - [objective function select or design](deep-learning/目标函数.md)
  - train/optimize
    - [权值初始化](deep-learning/权值初始化.md)
    - [超参数调优](deep-learning/超参数调优.md)
    - ★如何防止过拟合
      - [data augmentation（数据增强）](deep-learning/data-augmentation.md)
      - [dropout](deep-learning/Dropout.md)
      - [weight decay（L1&L2）](deep-learning/权重衰减.md)
      - ...
    - [如何解决梯度消失/梯度爆炸](deep-learning/如何防止梯度消失和梯度爆炸.md)
    - [训练过程的可视化](deep-learning/CNN可视化.md)
    - fine-tune/bottleneck
    - 
  
- [克服过拟合和提高泛化能力的20条技巧和诀窍](deep-learning/深度学习性能提升的方法.md)

  

### Deep Reinforcement Learning

- Markov Decision Process
- Dynamic Programming
- Model-Free Prediction
- Model-Free Control
- Value Function Approximation
- Policy gradient
- Intergrating Learning and Planning
- Exploration and Exploitation
- 



### Computer Vision

* [整体概述](computer_vision/overview.md)

* [目标检测专题](computer_vision/object_detection.md)

* [目标跟踪专题](computer_vision/object_track.md)

* Classic Model
  * resnet
  * mobilenet
  * shufflenet
  * SSD
  * Yolo
  * CenterNet
  * FasterRcnn
  * MaskRcnn
  * BERT
  * Tranasformer

* Train/Inference Tricks
  
* OCR

* VIE

  




### Tools

* [Git](tools/git.md)
* [markdown](tools/markdowm.md)
* docker