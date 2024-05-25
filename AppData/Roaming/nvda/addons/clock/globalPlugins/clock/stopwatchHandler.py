# Clock Add-on for NVDA
# Author: Hrvoje Katich and contributors
# Copyright 2013-2021, released under GPL.

import time


class Stopwatch(object):
	startTime = None
	stopTime = None
	running = False

	def start(self) -> None:
		self.startTime = time.time()
		self.running = True

	def reset(self) -> None:
		self.startTime = None
		self.stopTime = None
		self.running = False

	def elapsedTime(self) -> float:
		if not self.startTime:
			return 0.0
		if self.stopTime:
			return self.stopTime - self.startTime
		return time.time() - self.startTime

	def stop(self) -> None:
		self.stopTime = time.time()
		self.running = False
