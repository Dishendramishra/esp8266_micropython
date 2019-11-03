How to install micropython on nodemcu

```shell
esptool erase_flash 

esptool --baud 460800 write_flash -fm dio -fs 16MB 0 ./bin/esp8266-20190529-v1.11.bin 0xffc000 ./bin/esp_init_data_default.bin
```



Micropython nodemcu examples

