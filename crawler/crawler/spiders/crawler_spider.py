import json
from scrapy import Spider
from scrapy.selector import Selector
from crawler.items import CrawlerItem

class CrawlerSpider(Spider):
    name = "crawler"
    allowed_domains = ["thegioididong.com"]
    start_urls = ["https://www.thegioididong.com/laptop/msi-creator-z17-hx-studio-a14vgt-i7-272vn",
                  "https://www.thegioididong.com/laptop/lenovo-legion-pro-7-16irx9h-i9-83de001mvn",
                  "https://www.thegioididong.com/laptop/apple-macbook-pro-14-inch-m3-max-2023-14-core",
                  "https://www.thegioididong.com/laptop/lenovo-thinkpad-x13-ultra-7-21lu004lvn",
                  "https://www.thegioididong.com/laptop/msi-prestige-14-ai-studio-c1udxg-ultra-7-058vn",
                  "https://www.thegioididong.com/laptop/asus-fa506nfr-r7-hn113w",
                  "https://www.thegioididong.com/laptop/dell-inspiron-15-3530-i5-p16wd2",
                  "https://www.thegioididong.com/laptop/asus-fa506ncr-r7-hn097w"]
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
        'ROBOTSTXT_OBEY': False,
        'DOWNLOAD_DELAY': 2,
        'RETRY_ENABLED': True,
        'RETRY_TIMES': 3,
    }

    def parse(self, response):
        # Extract the JSON-LD script and parse it
        json_ld = response.xpath('//script[@type="application/ld+json" and @id="productld"]/text()').get()
        if json_ld:
            product_data = json.loads(json_ld)

            # Initialize item
            item = CrawlerItem()

            # Extract product name
            item['prod_name'] = product_data.get("name", None)

            # Extract brand
            brand_data = product_data.get('brand', {})
            item['brand'] = brand_data.get('name', [None])[0]  # Extract first element of the 'name' array if exists

            # Extract other fields from 'additionalProperty'
            additional_properties = {prop['name']: prop['value'] for prop in product_data.get('additionalProperty', [])}
            item['cpu'] = additional_properties.get('Công nghệ CPU', None)
            item['gpu'] = additional_properties.get('Card màn hình', None)
            item['ram'] = additional_properties.get('RAM', None)
            item['screen_size'] = additional_properties.get('Màn hình', None)
            item['screen_fresh_rate'] = additional_properties.get('Tần số quét', None)
            item['screen_resolution'] = additional_properties.get('Độ phân giải', None)
            item['battery'] = additional_properties.get('Thông tin Pin', None)
            item['battery_capacity'] = additional_properties.get('Công suất bộ sạc', None)
            item['os'] = additional_properties.get('Hệ điều hành', None)
            item['weight'] = additional_properties.get('Khối lượng tịnh', None)
            item['cost'] = product_data.get("offers", {}).get("price", None)

            yield item