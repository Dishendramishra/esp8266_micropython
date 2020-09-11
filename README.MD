# Making Windows 10 Developer Friendly :blush:

**Installing scoop** 

```shell
Set-ExecutionPolicy RemoteSigned -scope CurrentUser
Invoke-Expression (New-Object System.Net.WebClient).DownloadString('https://get.scoop.sh')
```

  

**Pre-requisities**

```shell
scoop install sudo
pip install adafruit-ampy esptool
```

  

# How to install micropython on nodemcu

```shell
git clone https://github.com/Dishendramishra/esp8266_micropython
cd esp8266_micropython
sudo esptool.py erase_flash 
sudo esptool.py --baud 460800 write_flash -fm dio -fs 16MB 0 ./bin/esp8266-20190529-v1.11.bin 0xffc000 ./bin/esp_init_data_default.bin
```

  

# Micropython nodemcu examples

**SSD1306 OLED**

```shell
ampy --port COM3 --baud 115200 put oled-example/main.py
```

