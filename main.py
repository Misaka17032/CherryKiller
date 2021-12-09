# coding=utf-8

import requests
import time
import json
import random
from tqdm import tqdm

aid = 209712177
listen_freq = 4
print_beat = 10

def get_data(aid):
	data = json.loads(requests.get("http://api.bilibili.com/archive_stat/stat?aid={}".format(aid)).text)
	if data["code"] != 0:
		return None
	data = data["data"]
	return [data["view"], data["danmaku"], data["reply"], data["favorite"], data["coin"], data["share"], data["like"]]

if __name__ == '__main__':
	f = open("config.txt", "r", encoding="utf-8")
	config = json.loads(f.read())
	aid = config["aid"]
	listen_freq = config["listen_freq"]
	print_beat = config["print_beat"]
	f = open("crnmsl.txt", "r", encoding="utf-8")
	www = f.read().split("\n")

	abs_data_delta = [0, 0, 0, 0, 0, 0, 0]
	print("开始监听。")
	temp = init_stat = get_data(aid)
	if init_stat == None:
		print("获取数据失败。叔叔可能盯上了这个ip，请稍后再试。")
		quit()
	init_time = time.localtime(time.time())
	print(time.strftime("于%Y-%m-%d-%H:%M:%S，aid为{}的视频数据为：".format(aid), init_time))
	print("播放：{}｜弹幕：{}｜回复：{}｜收藏：{}｜硬币：{}｜分享：{}｜点赞：{}".format(*init_stat))
	while True:
		for i in tqdm(range(print_beat)):
			time.sleep(listen_freq + random.random())
			stat = get_data(aid)
			while stat == None:
				time.sleep(listen_freq)
				stat = get_data(aid)
				print("获取数据失败。叔叔可能盯上了这个ip，请稍后再试。")
			abs_data_delta = [abs_data_delta[j] + max(0, stat[j] - temp[j]) for j in range(7)]
			temp = stat
		end_time = time.localtime(time.time())
		rlt_data_delta = [stat[i] - init_stat[i] for i in range(7)]
		text = time.strftime("从{}至%Y-%m-%d-%H:%M:%S，aid为{}的视频数据增长为：\n".format(time.strftime("%Y-%m-%d-%H:%M:%S", init_time), aid), end_time)
		text += "（相对）播放：{}｜弹幕：{}｜回复：{}｜收藏：{}｜硬币：{}｜分享：{}｜点赞：{}\n".format(*rlt_data_delta)
		text += "（绝对）播放：{}｜弹幕：{}｜回复：{}｜收藏：{}｜硬币：{}｜分享：{}｜点赞：{}\n".format(*abs_data_delta)
		print(text)

		text = "播放数据观测报告：\n" + text
		text += random.choice(www)
		f = open("report.txt", "w", encoding="utf-8")
		f.write(text)
	f.close()