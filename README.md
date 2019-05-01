# qwertee-scrapper
A simple qwertee  Scrapper to download the images from the qwertee website creating a wallpaper collage to your computer.

You can use crontab to schedule your new wallapaper with the new designs every day.

## Requirements

You have to install:
* Pillow
* BeautifulSoup

Use pip3 to do it:

```bash
pip3 install pillow beautifulsoup4
```

## Usage

Write python3 qwertee_scrapper.py --help to see all the options

```bash
usage: qwertee_scrapper.py [-h] [--pages PAGES] [--rows ROWS] [--cols COLS]

optional arguments:
  -h, --help     show this help message and exit
  --pages PAGES  Defines the number of pages to be downloaded. Each page means
                 20 images
  --rows ROWS    Defines the number of rows.
  --cols COLS    Defines the number of columns.
```

A good example: I want to download 10 pages and create a wallpaper with 10 rows and 20 columns:

```bash
python3 qwertee_scrapper.py --pages 10 --rows 10 --col 20
```



***

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Licencia Creative Commons" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">Qwertee scrapper collage</span> by <span xmlns:cc="http://creativecommons.org/ns#" property="cc:attributionName">Julián Caro Linares</span> licensed by <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.<br /><br />
