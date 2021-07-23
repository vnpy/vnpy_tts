# vn.py框架的TTS底层接口

<p align="center">
  <img src ="https://vnpy.oss-cn-shanghai.aliyuncs.com/vnpy-logo.png"/>
</p>

<p align="center">
    <img src ="https://img.shields.io/badge/version-6.5.1.3-blueviolet.svg"/>
    <img src ="https://img.shields.io/badge/platform-windows|linux-yellow.svg"/>
    <img src ="https://img.shields.io/badge/python-3.7-blue.svg" />
    <img src ="https://img.shields.io/github/license/vnpy/vnpy.svg?color=orange"/>
</p>

## 说明

基于CTP期货版的6.5.1接口封装开发的模拟交易TTS（Tick Trading System）接口【7x24】。

## 安装

安装需要基于2.2.0版本以上的[VN Studio](https://www.vnpy.com)。

直接使用pip命令：

```
pip install vnpy_tts
```


或者下载解压后在cmd中运行：

```
python setup.py install
```

## 使用

以脚本方式启动（script/run.py）：

```
from vnpy.event import EventEngine
from vnpy.trader.engine import MainEngine
from vnpy.trader.ui import MainWindow, create_qapp

from vnpy_tts import TtsGateway


def main():
    """主入口函数"""
    qapp = create_qapp()

    event_engine = EventEngine()
    main_engine = MainEngine(event_engine)
    main_engine.add_gateway(TtsGateway)
    
    main_window = MainWindow(main_engine, event_engine)
    main_window.showMaximized()

    qapp.exec()


if __name__ == "__main__":
    main()
```

## 连接

模拟账号可通过https://github.com/krenx1983/tradenow 获取。

连接信息如下：

{
    "用户名": "xxxxxx",
    "密码": "xxxxxx",
    "经纪商代码": "",
    "交易服务器": "121.36.146.182:20002",
    "行情服务器": "121.36.146.182:20004",
    "产品名称": "",
    "授权编码": ""
}

经纪商代码、产品名称、授权编码三项可以不填。
