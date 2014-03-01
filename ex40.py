# -*- coding: utf-8 -*-
class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

happy_bady = Song(["Happy birthday to you",
	"I don't want to get sued",
	"So I'll stop right there"])

excuse = Song(["翻着我们的照片","想念若隐若现"])

happy_bady.sing_me_a_song()

excuse.sing_me_a_song()