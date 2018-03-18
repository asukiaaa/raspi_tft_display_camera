# raspi_tft_display_camera

# Components
- Raspberry pi (Tested with using zero WH)
- Raspberry pi camera (Tested with using that for zero)
- [0.96" 160x80 Color TFT Display](https://www.adafruit.com/product/3533)

# Wiring

Raspberry pi | LCD
--- | ---
5V  | VCC
GND | GND
GPIO3 | TFTCS
GPIO27 | DC
GPIO22 | RST
GPIO10 (SPI0 MOSI) | MOSI
GPIO9  (SPI0 MISO) | MISO
GPIO11 (SPI0 SCLK) | SCLK

# Setup
## Activate SPI and Camera
```
sudo raspi-config
```

1. Activate `Interfaces` -> `SPI`
2. Activate 'Interfaces' -> `Camera`
3. reboot

## Install dependencies
```
sudo apt install python3-pygame python3-picamera
```

# Usage
## Start TFT display
```
sudo modprobe fbtft_device name=adafruit18 gpios=reset:22,dc:27,cs:3 rotate=90
```

Stop fbtft_device
(But sometime it is not enough. I suggest rebooting to reset fbtft.)
```
sudo modprobe -r fbtft_device
```

## Show hello world
```
sudo python3 hello.py
```

## Show polygon and lines
```
sudo python3 drawing.py
```

## Show camera image
```
sudo python3 show_camera_image.py
```

# License
MIT

# References
- [Raspberry Pi 2でカラーグラフィック液晶の制御](https://sakura87.net/archives/2232)
- [サインスマート 1.8″ TFT カラー LCD用のグラフィックライブラリの作成](https://qiita.com/TomoSoft/items/15430603cc8294130d8d)
- [adafruit/Adafruit-ST7735-Library](https://github.com/adafruit/Adafruit-ST7735-Library)
- [Wiring & Test | Adafruit Mini TFT - 0.96" 160x80](https://learn.adafruit.com/adafruit-mini-tft-0-dot-96-inch-180x60-breakout/wiring-test)
- [ILI9341ベースのQVGA/SPI TFT液晶モジュールを試してみる](https://qiita.com/toyoshim/items/84c026e97f6be200cb19)
- [Sensor Modes | Picamera Hardware](https://picamera.readthedocs.io/en/release-1.13/fov.html#sensor-modes)
