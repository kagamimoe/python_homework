# -*- coding: utf-8 -*-
print "你现在碰到了一个鬼 你准备怎么办？"
print "1.转身逃跑 2.跟它搏斗 3.怒而飞"
number = raw_input('>')
print number
if number == '1':
	print "你没有逃脱鬼的掌心 你被鬼吃了 oh yeah"
elif number == '2':
	print "你跟鬼搏斗，结果被鬼一下打死"
elif number == '3':
	print "你怒而飞，飞上了天，鬼追不上你，你成功逃脱"
else:
	print "你犹豫不觉，被鬼吃掉"