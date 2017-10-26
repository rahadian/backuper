import time
import schedule
import sys,os
from distutils.dir_util import copy_tree
red = "\033[01;31m{0}\033[00m"
grn = "\033[01;36m{0}\033[00m"
def open():
	print red.format("==============================================================")
	print grn.format("Hi,This is a program for backuping your data. Made by arytux")
	print red.format("==============================================================")
	print "Make directory location for your backuped data."
class Core():

	def dirz(self):
	 	self.dir = raw_input("Enter your backup directory destination :")
 		makedir = "mkdir {}".format(self.dir)
 		os.system(makedir)
 		print "Done"
 		self.copyz = raw_input("Enter your directory(s) or file(s) for backup :" )
	def backup(self):
		#self.copycuz = shutil.copytree(self.copyz,self.dir)	
		self.copycuz = copy_tree(self.copyz,self.dir)	
def sche():
		schedule.every().day.at("13:07").do(corez.backup)
		while 1:
			schedule.run_pending()
			time.sleep(1)
			print "......waiting schedule......"

open()


corez = Core()
corez.dirz()

sche()


