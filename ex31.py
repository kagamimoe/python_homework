# -*- coding: utf-8 -*-
print "你进去了一个漆黑的房间，里面有两扇门，你准备进入第一扇门还是第二扇门呢？"

door = raw_input("> ")

if door == "1":
    print "房间里面有个老虎在吃肉，你准备采取以下哪种动作呢？"
    print "1. 和它一起分享肉。"
    print "2. 对老虎大叫。"

    bear = raw_input("> ")

    if bear == "1":
        print "干的好,老虎把你一起吃了"
    elif bear == "2":
        print "干的好,老虎把你一起吃了"
    else:
        print "干的好,老虎被你 %s 吓跑了" % bear

elif door == "2":
    print "真倒霉，门后面藏了一个恶鬼，你被吃了。"

else:
    print "你站在门口犹豫了半天，被后面的僵尸吃了脑子。"