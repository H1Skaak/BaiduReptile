import time
import requests
import sys

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


page_num = 9999999	# 默认爬取页数


def get_baidu(key):
	process_start_time = time.time()
	# 不打开浏览器
	option = webdriver.ChromeOptions()
	option.add_argument("headless")
	browser = webdriver.Chrome(chrome_options=option)
	browser.get('https://www.baidu.com')
	browser.find_element_by_name('wd').send_keys(key,Keys.ENTER)
	i = 1
	global page_num
	try:
		while i <= int(page_num):
			print('正在爬取第 %d 页' % i ,"\n")
			print("-" * 100)
			i += 1
			time.sleep(6)
			# 获取下一页按钮
			page = browser.find_elements_by_class_name('n')[-1]
			results = browser.find_elements_by_class_name('result')
			
			for result in results:
				# 获取百度跳转网址
				url = result.find_element_by_tag_name('a').get_attribute('href')
				# 获取网址title
				title = result.find_element_by_tag_name('a').text
				print(title)
				get_url(url)

			page.click()
	except Exception as e:
		print(e)

	process_stop_time = time.time()
	diff_time = process_stop_time - process_start_time
	# 将计算出来的时间戳转换为结构化时间
	struct_time = time.gmtime(diff_time)
	print("爬取百度链接完成 "+ "一共耗时{0}分{1}秒".format(struct_time.tm_min,struct_time.tm_sec))
	browser.close()



def get_url(url):
	headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, compress',
    'Accept-Language': 'en-us;q=0.5,en;q=0.3',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'
	}
	try:
		# 请求拒绝重定向
		req = requests.get(url, headers=headers, allow_redirects=False)
		req.encoding = 'utf-8'
		# 获取头部Location 中url地址
		print(req.headers['Location'])
		print("-" * 100)
	except Exception as e:
		pass


def main():
	if len(sys.argv) <= 1 :
		print("Usage :python ", sys.argv[0] , "keyword")
		print("Usage :python ", sys.argv[0] , "keyword", "page")
		print("Usage :python ", sys.argv[0] , "查询的关键字", "页数")
		print("Usage :page默认无限大")
		sys.exit(1)
	key = sys.argv[1]
	try:
		global page_num
		page_num = sys.argv[2]
	except:
		pass
	
	get_baidu(key)


if __name__ == '__main__':
	main()