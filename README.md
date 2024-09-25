# proxy-switch
switch proxy mode(Manual/Disabled) for linux(Ubuntu 22.04)

## 应用说明
为了方便切换网络代理模式，用chatgpt辅助写了一个python脚本，再编写一个desktop文件将其变为应用程序，就可以单击应用图标启动，也可以利用tweaks开机自启动。

运行后在顶部状态栏生成一个图标，表示当前状态，on/绿色表示manual，off/红色表示none。

单击该图标后出现状态栏，点击Toggle proxy，即可切换代理状态。（只支持Manual和Disabled互换，目前也没有其他需求～）

## 应用演示
应用图标

![image](https://github.com/user-attachments/assets/5daf62f8-d35d-48bb-bb70-24606d355e41)

顶部状态栏图标

![image](https://github.com/user-attachments/assets/8835f7a6-afb3-4a36-82f0-f42c6d9fd6d1)

单击后菜单栏

![image](https://github.com/user-attachments/assets/49b067de-5fdf-4374-a98a-fd54b2f38cfc)



## 应用构建
```
mkdir /opt/proxy-GUI/
cd ~/Downloads/proxy-switch/  # 请自行切换到代码所在位置
sudo cp proxy.py button.png proxy-on.png proxy-off.png /opt/proxy-GUI/ 
cp proxy.desktop ~/.local/share/applications/
cd ~/.local/share/applications/
chmod a+x proxy.desktop
```




