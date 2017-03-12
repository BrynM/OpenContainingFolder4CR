# ocf4cr.py
# A plugin script for ComicRack
# (c) 2017 Bryn Mosher (BadMonkey0001)
# GPL v3 License
################################################################################

import clr
import sys
import System
import re
from datetime import datetime
from time import sleep

clr.AddReference("System")
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")
clr.AddReference("PresentationFramework")
clr.AddReference("PresentationCore")

from System.Diagnostics import Process
import System.Windows.Forms
from System.Windows.Forms import *
import System.Drawing
from System.Drawing import *
from System.Collections import *
from System.IO import *

from Ocf4crLang import lang
from Ocf4crSettings import Ocf4crSettings
from MultipleDirsForm import MultipleDirsForm
from SettingsForm import SettingsForm

class OCF4CR:
	version = "0.0.6"
	debug = True
	env = {
		'explorer': {
			"path": "C:\Windows\explorer.exe",
			"args": "/e @separate@ /root,\"@path@\"",
			"separateArg": "/separate",
		},
	}
	logDateFormat = '%Y-%m-%d %H:%M:%S'
	logPrefix = "OCF4CR"
	rgxAllWhitespaceOrEmpty = re.compile("^\s*$")
	rgxAllWhitespaceOrEmptyOrComment = re.compile("(^\s*$|^\#|^\s*\#)")
	rgxBooleanFalse = re.compile("^(\s*)?[Ff]alse(\s+.*)?")
	rgxTrimString = re.compile("(^[\s\"']+|[\s\"']+$)")
	rgxMatchASetting = re.compile("^(\s*)?([^=\s]+)(\s*)?=(\s*)?(.*)(\s*)?$")
	rootScriptDirectory = FileInfo(__file__).DirectoryName
	rootDirectory = FileInfo(FileInfo(FileInfo(__file__).Directory.ToString()).Directory.ToString()).Directory
	settings = None
	windowIconPath = None
	windowIconResource = None
	runCommandDelay = 0.3

	def __init__(self):
		self.logPrefix = "OCF4CR"+self.version+""
		self.log("Instantiated OCF4CR")
		self.windowIconPath = Path.Combine(self.rootScriptDirectory, "ocf4cr.ico")
		self.windowIconResource = Icon(self.windowIconPath)
		self.settings = Ocf4crSettings(self)

	def buildOpenerCommand(self):
		if self.settings.get("enableCustomCommand"):
			return self.settings.get("customExec")

		return self.env["explorer"]["path"];

	def buildSingleCommandArgs(self, path):
		separateString = "";
		args = ""

		if self.settings.get("enableCustomCommand"):
			args = self.settings.get("customArgs")
			if args.find("@path") < 0:
				# always at least provide the path
				args += " @path@"
		else:
			args = self.env['explorer']['args']
			if self.settings.get("explorerSeparateProcess"):
				separateString = self.env["explorer"]["separateArg"];

		return str(args).replace('@path@', path).replace('@separate@', separateString)

	def dbg(self, msg):
		if self.debug:
			print "[DEBUG "+self.logPrefix+" "+datetime.now().strftime(self.logDateFormat)+"] "+msg

	def getDirectoriesList(self, books):
		self.dirListAll = []

		if books.Count < 1:
			return self.dirListAll

		for book in books:
			if book.FileDirectory and not self.rgxAllWhitespaceOrEmpty.match(book.FileDirectory):
				self.dirListAll.append(book.FileDirectory)

		self.dirListAll.sort()
		return list(set(self.dirListAll))

	def handleOcf4crButtonClicked(self, books):
		self.log("Triggered main icon handler")
		if not books:
			MessageBox.Show(lang.enUs("nobooks"), lang.enUs("windowTitle"), MessageBoxButtons.OK, MessageBoxIcon.Information)
			return

		self.dirList = self.getDirectoriesList(books)

		if not self.dirList:
			MessageBox.Show(lang.enUs("nodirs"), lang.enUs("windowTitle"), MessageBoxButtons.OK, MessageBoxIcon.Information)
			return

		self.settings.loadSettingsFromFile()
		self.dirCount = len(self.dirList)

		if self.openCustomCommandWithList(self.dirList):
			return;

		if self.dirCount > 1 and not self.settings.get("onlyUseFirstDir"):
			if self.settings.get("ignoreMultiSelected"):
				self.dbg("Ignored multiple selection according to settings")
				return

			self.log("Showing multiple form")
			self.showMultipleForm(self.dirList)
			return

		self.log("Opening single directory \""+self.dirList[0]+"\"")
		self.openDirWithCommand(self.dirList[0], False)

	def handleOcf4crSettingsMenuClicked(self):
		self.log("Triggered ocf4crSettings")
		self.showSettingsForm()

	def log(self, msg):
		print "["+self.logPrefix+" "+datetime.now().strftime(self.logDateFormat)+"] "+msg

	def openDirWithCommand(self, dirPath, noWarnings):
		if self.openCustomCommandWithList(self.dirList):
			return;

		parsedCommand = self.buildOpenerCommand()
		parsedArgs = self.buildSingleCommandArgs(dirPath)
		try:
			self.dbg("Running \""+parsedCommand+"\" "+parsedArgs)
			Process.Start(parsedCommand, parsedArgs)
		except:
			errType, errValue, errTrace = sys.exc_info()
			MessageBox.Show(lang.enUs("failedCommand")+"\n\n"+parsedCommand+" "+parsedArgs+"\n\n"+str(errValue), lang.enUs("windowTitle"), MessageBoxButtons.OK, MessageBoxIcon.Warning)

	def openCustomCommandWithList(self, dirList):
		if not self.settings.get("enableCustomCommand") or self.settings.get("customArgs") == "":
			self.dbg("Custom commands are disabled or custom args are empty. Skipping trying to open with @list@. "+self.settings.get("customArgs"))
			return False

		if not System.IO.File.Exists(self.settings.get("customExec")):
			MessageBox.Show(lang.enUs("customCommandNotFound")+"\n\n\""+self.settings.get("customExec")+"\"", lang.enUs("windowTitle")+" "+lang.enUs("error"), MessageBoxButtons.OK, MessageBoxIcon.Error)
			# We want to halt, so we pretend we did something.
			return True

		if self.settings.get("customArgs").find("@list@") > -1:
			parsedCommand = self.buildOpenerCommand()
			listLen = len(dirList)
			maxWin = self.settings.get("maxWindows")

			if maxWin > 0 and listLen > maxWin:
				self.dbg("Using "+str(maxWin)+" of "+str(listLen)+" directories for a single command")
				dirPile = '"'+'" "'.join(dirList[0:maxWin])+'"'
			else:
				self.dbg("Using "+str(listLen)+" directories for a single command")
				dirPile = '"'+'" "'.join(dirList)+'"'

			parsedArgs = self.settings.get("customArgs").replace("@list@", dirPile)

			try:
				self.dbg("Running \""+parsedCommand+"\" "+parsedArgs)
				Process.Start(parsedCommand, parsedArgs)
			except:
				errType, errValue, errTrace = sys.exc_info()
				MessageBox.Show(lang.enUs("failedCommand")+"\n\n"+parsedCommand+" "+parsedArgs+"\n\n"+str(errValue), lang.enUs("windowTitle"), MessageBoxButtons.OK, MessageBoxIcon.Warning)
			return True

		return False

	def openMultipleDirsWithCommand(self, dirList):
		if not isinstance(dirList, list):
			MessageBox.Show(lang.enUs("invalidList")+str(type(dirList)), lang.enUs("windowTitle"), MessageBoxButtons.OK, MessageBoxIcon.Warning)
		else:
			opened = 0
			maxOpened = self.settings.get("maxWindows")
			for dirName in dirList:
				sleep(self.runCommandDelay)
				self.openDirWithCommand(dirName, True)
				opened += 1
				if maxOpened > 0 and opened >= maxOpened:
					self.dbg("Opened "+str(opened)+" windows of max "+str(maxOpened))
					return

	def showMultipleForm(self, dirList):
		theForm = MultipleDirsForm(self, dirList)
		result = theForm.ShowDialog()
		theForm.Dispose()
		if result != DialogResult.Cancel:
			return True
		return False

	def showSettingsForm(self):
		theForm = SettingsForm(self, self.settings)
		theForm.ShowDialog()
		self.settings.loadSettingsFromFile()
		theForm.Dispose()

	def warn(self, msg):
		print "[WARNING "+self.logPrefix+" "+datetime.now().strftime(self.logDateFormat)+"] "+msg

ocf4cr = OCF4CR()


