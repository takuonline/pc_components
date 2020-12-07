import scrapy
from scrapy.crawler import CrawlerProcess
from hifi_project.spiders.takealot import TakealotSpider
from hifi_project.spiders.computermania import ComputermaniaSpider
from hifi_project.spiders.hifi import HifiSpider

 

process = CrawlerProcess(
    settings={
    # "FEED_URI": "file:///users/taku/downloads/video/combined.csv",  # feeds uri is deeprecated and should use feeds
    
})

process.crawl(HifiSpider)

process.crawl(ComputermaniaSpider)

process.crawl(TakealotSpider)

process.start()
