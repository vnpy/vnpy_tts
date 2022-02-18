# vn.py框架的TTS底层接口

<p align="center">
  <img src ="https://vnpy.oss-cn-shanghai.aliyuncs.com/vnpy-logo.png"/>
</p>

<p align="center">
    <img src ="https://img.shields.io/badge/version-6.5.1.1-blueviolet.svg"/>
    <img src ="https://img.shields.io/badge/platform-windows|linux-yellow.svg"/>
    <img src ="https://img.shields.io/badge/python-3.7|3.8|3.9|3.10-blue.svg" />
    <img src ="https://img.shields.io/github/license/vnpy/vnpy.svg?color=orange"/>
</p>

## 说明

基于TTS的6.5.1接口封装开发，对接类CTP的仿真交易环境。

目前TTS支持的仿真交易包括：

- 期货
    - 中金所
    - 上期所
    - 大商所
    - 郑商所
    - 能交所
- 股票
    - 上交所
    - 深交所

## 安装

安装需要基于3.0.0版本以上的[VN Studio](https://www.vnpy.com)。

直接使用pip命令：

```
pip install vnpy_tts
```

或者下载解压后在cmd中运行：

```
pip install -e .
```

由于在安装的同时需要编译C++代码，因此在执行上述命令之前需要去微软[官网](https://my.visualstudio.com/Downloads?q=build%20tools)下载Visual Studio Build Tools。其中工作负荷选择Visual C++生成工具，同时推荐下载2017版。

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
