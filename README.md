# Rpi-status
用于监控树莓派状态的简单脚本<br>
<br>
安装方法<br>
<br>
pi用户登录，直接克隆仓库git clone https://github.com/We-Fly/Rpi-status.git <br>
打开文件夹，cd Rpi-status  <br>
如果有install.sh安装文件，也可以在联网状态下直接运行install.sh，无需手动克隆仓库  <br>
赋予安装脚本可执行权限chmod 755 install.sh  <br>
以普通用户权限执行安装脚本，不要用sudo，不要用root账户，否则python3-pip程序会有问题， ./install.sh  <br>
安装脚本会自动安装依赖环境和程序脚本，并赋予程序可执行权限。安装完成后会自动删除Rpi-status文件夹。  <br>
