from douban import DoubanWang

d = DoubanWang(
    'https://movie.douban.com/j/search_subjects?type=tv&tag=%E9%9F%A9%E5%89%A7&sort=recommend&page_limit=20&page_start=0',
    '韩剧')
d.run()
