# Tgdd Crawler

Crawler để cào thông tin sản phẩm từ website https://www.thegioididong.com/

Hiện tại chỉ cào được các category sau:

- may-tinh-bang
- dtdd
- lap-top
- dong-ho-thong-minh
- dong-ho-deo-tay
## Installation

 Install Scrapy

```bash
pip install Scrapy
```

## Usage
- Cào hết các category, hơi lâu tẹo :v
```bash
scrapy crawl tgdd
```
* Cào theo category
```bash
scrapy crawl tgdd -a category=may-tinh-bang
```