# coding: utf-8
import scrapy

class price(scrapy.Spider):
  name = "pSpider"
  start_urls = ['http://sh.58.com/zufang/?PGTID=0d3090a7-0000-2457-2150-b45c171059fd&ClickID=2']

  def parse(self, response):
    fileName = 'text.txt'
    items = response.css('.listUl li')
    num = 1
    for item in items:
      num = num + 1
      name = item.css('.room::text').extract_first() or '暂无'
      money = item.css('.money b::text').extract_first() or '暂无'
      with open(fileName, "a+", encoding='UTF-8') as f:
        f.write('户型' + name)
        f.write('' + '租金' + money)
        f.write('\n')
        f.close()
    next_page = response.css('.next::attr(href)').extract_first()
    print (next_page)
    print ('下一页')
    if next_page is not None:
      next_page = response.urljoin(next_page)
      yield scrapy.Request(next_page, callback=self.parse)
    self.log('保存文件成功')
