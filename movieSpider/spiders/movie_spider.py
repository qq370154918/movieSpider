import scrapy
from movieSpider.items import MoviespiderItem

class MovieSpiderSpider(scrapy.Spider):
    name = 'movie_spider'
    allowed_domains = ['movie.douban.com']   #准许爬取的域名
    start_urls = ['http://movie.douban.com/top250']   #入口url

    def parse(self, response):
        #这里编写解析规则
        movie_item = response.xpath("//div[@class='article']/ol/li")
        for item in movie_item:
            # 创建存储对象
            movieItem = MoviespiderItem()
            # 爬取电影信息
            # 电影序号
            movieItem['serial_number'] = item.xpath(".//div/div/em/text()").extract_first()
            # 电影名称
            movieItem['film_name'] = item.xpath(".//div/div/div/a/span[@class='title']/text()").extract_first()
            # 电影的年份 制作人等信息
            info_item = item.xpath(".//div/div/div[@class='bd']/p[1]/text()").extract()
            # 电影制作人
            movieItem['film_maker'] = "".join(info_item[0].split())
            # 电影年份
            movieItem['film_time'] = (''.join(info_item[1].split())).split('/')[0]
            # 电影出品国家
            movieItem['film_country'] = (''.join(info_item[1].split())).split('/')[1]
            # 电影类型
            movieItem['film_type'] = (''.join(info_item[1].split())).split('/')[2]
            # 电影引用
            movieItem['film_quote'] = item.xpath(".//div/div/div[@class='bd']/p[2]/span/text()").extract_first()
            # 电影评分
            movieItem['film_score'] = item.xpath(
                ".//div/div/div[@class='bd']/div/span[@class='rating_num']/text()").extract_first()
            # 将数据传到pipeline
            yield movieItem
        # 解析下一页url
        next_page = response.xpath("//div[@class='paginator']/span[@class='next']/link/@href").extract()
        # 判断是否有下一页
        if next_page:
            next_page = next_page[0]
            url = self.start_urls[0] + next_page
            # 将下一页url传给调度器
            yield scrapy.Request(url, callback=self.parse)
