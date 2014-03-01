# -*- coding: utf-8 -*-

formatter = "%s %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, True, False, True)
print formatter % (
	"请你吃香",
	"That you could type up right.",
	"But it did't sing.",
	"So I said goodnight."
	)