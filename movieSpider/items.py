# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
#Item.py文件是用来定义存储结构的地方
import scrapy


class MoviespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #声明数据结构
    film_name=scrapy.Field(serializer=str)
    #你可以指定数据的类型
    serial_number=scrapy.Field()
    #电影类型
    film_type=scrapy.Field()
    #出品时间
    film_time = scrapy.Field()
    # 国家
    film_country = scrapy.Field()
    # 评分
    film_score = scrapy.Field()
    #导演，演员
    film_maker = scrapy.Field()
    #电影引语
    film_quote = scrapy.Field()

