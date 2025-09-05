# Scrapy settings for job project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "job"

SPIDER_MODULES = ["job.spiders"]
NEWSPIDER_MODULE = "job.spiders"

ADDONS = {}


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "job (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Concurrency and throttling settings
#CONCURRENT_REQUESTS = 16
CONCURRENT_REQUESTS_PER_DOMAIN = 1
DOWNLOAD_DELAY = 1

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,en-IN;q=0.8',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Not;A=Brand";v="99", "Microsoft Edge";v="139", "Chromium";v="139"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0',
    # 'cookie': 'vstr=cb564106-6958-4514-9242-e7e2ccac5203; ref=3; COOKIE_CONSENT={"key":"eyJuZWNlc3NhcnkiOnRydWUsImFuYWx5dGljcyI6dHJ1ZSwiYWR2ZXJ0aXNpbmciOnRydWUsInBlcnNvbmFsaXphdGlvbiI6dHJ1ZX0=","consent":{"necessary":true,"analytics":true,"advertising":true,"personalization":true},"accepted":true}; vstrType=1; _ga=GA1.1.1470885182.1756628003; ajs_anonymous_id=e38c47ee-c0ff-4800-9161-861bd1ead3c0; bm_lso=F423E523F2B1D0FB02EFBDB98AC3A0DC43B1C223F1CD8F634BF821EDCF8B880C~YAAQUJUjF+yFfOOYAQAA5VOA/wQKXyL3gZYuQsKtBPSf1056DT7x/QErRPzWlJ7FIgqtjql3i3G8yBzmt6CjURuXxrxw8hF/o+6npo5/DA+zomWvBZdobMzi18tkONQihnI/g9XzF2LLwO+g9IjkfII3LVuUnV0vZ2xGveSAwh++cq59+NI25LaBQ23EddM/lF5mZUNJMLObwUallJiFe6LEO+j7Fj1KJ+yIZnoNlSKd2ifkJHIa6hozog58W82FpUxp+aEHZwJPAlus/lH4MfuE6Ek2EQ+f88Vrl+ixq4TqIWdvcPFV49+jjouw65fIJTvlfFdW4dcxoxqxX4yG97lgjns3qFyTwKW6wlKmIXh5QSMz5uagjMWZWijVy8ripN2Txwv2UTkbV8iihZevGUB4zu4NeRUb4hX/qCzewM4alYb5pTa3BFSG7vfUXCf/nvKMPl38Y43vZpQEhGE=^1756633266660; bm_s=YAAQUZUjF7moE+yYAQAAk8CA/wOM6Gspod4CBMW0iZHDAkFF3Czauw0aMBlY0rz2RD2cayEudNjcos4y5qfOK+3G0E3Ocej/L+0DyOCBcnmOQ1h+Cu0MauNXTcw6DuwLw/8cOBvtbhPMn8cubbXzxcChup/fRnhvWxgoE6g4HZSGZZOAYQOALuqB8ZKLmr2XJGyV8fIMOm6f3Wlne8nm5z4ihXR8GgS0QaJjUWDn3WBcDnoCwJhVvGd1wweLJnzQEBMjPGFs8WCSPq8yLJt/Ihli4I9Bg7hsGuD9UYXPKBL/+mnH4ByuZzigj39m70v+ef8lqdxA5yiPNYJ4u1E6skwOltV7JnvgGYjFJg7OsPqV1Ql3yI0u5M4SdRE64t5ywEghrSfwI8u7Q7GpRFKslSzvC0OTjmziEWInblqPS6k/Rf8i0iKcuOud11cqsew8dp2JX6LbJj/0mHh65rZnHh/OD0vqot+fZfi/dQ9LvBImntJFRqXBiK05TFcSXizjTSrosvH3VPGmvnZ05HAhkZmi2Yag1vtlNa01DaNjteYAyZyCFzhwKyTEmYQWTQjJB77f6ZFCd32EhxfdayU=; visitor_layeruid=c9467602-014c-46eb-b884-1e71a2ee1b17_1_rmc_GENRIC; vsutms=d489051c-fb70-42b9-b24a-78d4d30b8958#cb564106-6958-4514-9242-e7e2ccac5203#0bc13202-484b-4f4f-a530-b62277a40304#1756896917##||||; ew_exp=eed16e85-6b2a-419d-8c13-474003f67c36_3_1_0_rmc_030925,534d35f2-24d2-4baa-a4ff-14c2fdc3ea3c_4_1_0_rmc_030925; x-georegion=104,IN,KA,BANGALORE,,,,,,12.98,77.58,GMT+5.50,,AS,,mobile,45609,vhigh,5000; ak_bmsc=8806E2A80204A0DDA1BE005EC4DEA58C~000000000000000000000000000000~YAAQUJUjF7v9zuOYAQAAfdhXFB3AbyzY3WG1awhzSi2ZwKFEgZlIDfO8LXIZtDGilU8U+AECfNLXygm869uGM7lxU0k0/1v1zLZDghPT70J65esacgXHLZttie/7IbQVhQT9tpiUgPlv2LAeRy7ER07NHgxzZxk/n0nsqoI/At9TKgXLtp52RnU0Gx8YIxRuI5fXi6YMBt7tzGlGeqMUqzYkbe0awb0PGqykr3/lDIny8JLISFsGt9jgqWtU7yGtbEXT4uRYhc0n+p6ephWjgxBj4t8EF24+f+nxWZzUi6q3ALGg9dD6PahB0IIQTwgTSwZbYsaSDZEheT9AL0I2Vi6s79zNQKjnBHnZl5wgYNm+QPnrCzU1VcxwWM9rhzphFlV8qAty+kLHWqcloJrL+ukZxpY0GxrxdGd3JnOpOXWhYHgzoZgIdDvxNeEgVp0ynm0Q6iOiFI3k; bm_mi=77B09C993863011B93E20CF6A15DEAC7~YAAQUJUjF7z9zuOYAQAAfdhXFB1HssgCASymiOm9TjlSD1d0Ek8TOvIUDvvDT3UfPQWTGKyILN43NjGsFFkKAN2G7LnGpk7KUhPZ6yI3EdakKC7hAltiMBK0nLB2F1ovd70i5WqoFSQtiFbO6MjjXNeca8tyrDcIGJPyw99ME8Fgb92dKSG/YmOh4GWYOZZIvjvmN1Dx5OSX7b6A2Vc0zFdQ98lzLYADcaYUSXpHG2msUp2uYQ/JhBwzz/tbIdStHyWPuCa6tILd+grmEL1o6wVL/oJZTAiFLhjSZL+GXgQAex+LoRDFCiEy8u9CQoK3Jq3d2FznN3gzNG4/RqEhatSJ~1; vssessionuid=3052be9f-bb3f-4860-aea9-69ce171d7c6d; fs_user=0; _ga_DJ23BNLRSH=GS2.1.s1756982957$o7$g0$t1756982957$j60$l0$h0; bm_sv=F6609EBFDB80EBF038A4AE8AD14D6CBE~YAAQUZUjF6kbi+yYAQAAPqFYFB26B1Ach+C/BWi/58GAkN3Xlremc6t21QOGZ62IdE5cqyGHurFb7o7g0uVu/hgbT/D+tcbqnp7QidqUB5xtdO5v60pBih1AR5H3ZXPyeMVVfepwohlOXs1tWR//YO9YRQrct2xiLLGE2qX6qyeLeoUWSQ2tkrrVLGxskTWptoHpZd+BPQB3WtMOBGvKmzJQfcH1Y5i9cs+67Iisk5MOO2lXC2J1xC3ryDEuSm4=~1',


}


# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "job.middlewares.JobSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "job.middlewares.JobDownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    "job.pipelines.JobPipeline": 300,
#}
ITEM_PIPELINES = {
    "job.pipelines.QuotesElementsDatabase4Pipeline": 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
FEED_EXPORT_ENCODING = "utf-8"
