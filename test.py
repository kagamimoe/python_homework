# -*- coding: utf-8 -*-

from sys import exit
from random import randint


class Room(object):

    def enter(self):
    	print '这个房间还没建好呢骚年，请按回车退出房间'
    	exit(1)

class Death(Room):

	def enter(self):
		print '你死亡了，游戏结束了骚年，欢迎下次再来'
		exit(1)


class GoldRoom(Room):

	def enter(self):
		print '你来到了黄金之室。'
		print '这里看起来似乎是一千五百年前用来储藏宝藏的地方。'
		print '你看到了几个沉甸甸的大宝箱'
		print '你准备怎么做呢'
		print '1.打开箱子，取出宝藏'
		print '2.先观望下再说'
		
		action = raw_input(">")
		if action == ('1'):
			print '你打开了箱子，里面全是黄金，你欣喜若狂。'
			print '螳螂捕蝉黄雀在后，你被尾随在你后面的赏金猎人黑吃黑。卒。'
			return 'death'

		elif action == ('2'):
			print '你躲了起来，坐观其变，果然后面有人跟着你。'
			print '一群装备精良的赏金猎人进了房间，他们开始掠夺财宝。'
			print '好运没有持续太久，突然房间一阵摇晃，一条红龙冲了出来，把你们烧成了灰'
			return 'death'

		else:
			print ''
			return 'death'


class DarkRoom(Room):

	def enter(self):
		print '你来到了一间黑屋子，这里看起来相当的诡异。'
		print '屋子后面十分的黑暗，忽然飞出了一群蝙蝠'
		print '你准备怎么做呢'
		print '1.趴下'
		print '2.拿出宝剑，砍杀蝙蝠'
		
		action = raw_input(">")
		if action == ('1'):
			print '你趴下了，但似乎这群吸血蝙蝠并不打算放过你，你被蝙蝠吃了'
			return 'death'

		elif action == ('2'):
			print '你拿起宝剑，奋起杀怪，但似乎和你平时打网游里的剧情不同，你一只蝙蝠都没砍到。'
			print '蝙蝠在嘲笑你。'
			return 'death'

		else:
			print '你犹豫了半天，晚了，蝙蝠合体了，变成了大蝙蝠，一口气吞了你。'
			return 'death'

class MonsterRoom(Room):

	def enter(self):
		print '你来到了一个看起来不太友好的地方。'
		print '突然身后传来了响声，一只身长3米的巨魔走了出来。'
		print '你愣住了，准备采取以下动作'
		print '1.拔剑，击杀巨魔 2.施法，击杀巨魔'
		
		action = raw_input(">")
		if action == ('1'):
			print '你怒拔剑，准备和巨魔战斗。巨魔随便挥舞了一下巨棒，把你脑袋打开了花。'
			return 'death'

		elif action == ('2'):
			print '骚年你的魔法技能觉醒，一个大火球杀死了巨魔。'
			return 'GoldRoom'

		else:
			print '犹豫之间，巨魔饿了，把你吃了。'
			return 'death'

class StrangeRoom(Room):

	def enter(self): 
		print '你来到了一个奇怪的房间。'
		print '房间后有两个出口，你准备左转还是右转呢？'
		print '1.左转 2.右转'
		
		action = raw_input(">")
		if action == ('1'):
			print '你左转后，进去了一间黑暗的小屋。'
			return 'DarkRoom'

		elif action == ('2'):
			print '你右转后，进去了一间发臭的小屋。'
			return 'MonsterRoom'

		else:
			print '你犹豫不觉，头部莫名挨了一棍子，卒。'
			return 'death'

 class Map(object):
 	pass
	# def __init__(self, start_scene):
		# self.start_scene = start_scene
		# print "start_scene in __init__", self.start_scene

	# def next_scene(self, scene_name):
	# 	print "start_scene in next_scene"
	# 	val = Map.scenes.get(scene_name)
	# 	print "next_scene returns", val

	# def opening_scene(self):
	# 	return self.next_scene(self.start_scene)

# a_map = Map('StrangeRoom')
