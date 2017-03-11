# OpenContainingFolder4CR.py
# A plugin script for ComicRack
# (c) 2017 Bryn Mosher (BadMonkey0001)
# GPL v3 License
################################################################################

import clr
#from ocf4cr import ocf4cr

########################################
# Hooks
########################################

#@Name Open Containing Folder for ComicRack
#@Hook Books
#@Description Open Containing Folder for ComicRack: Open a file browser for selected book(s).
#@Key open-containing-folder-button
#@Image ocf4cr.png
def ocf4crButton(books):
	#from cYo.Projects.ComicRack import Engine
	#print "\n".join(dir(Engine))
	ocf4cr.dbg("Calling ocf4cr.handleOcf4crButtonClicked(books)")
	ocf4cr.handleOcf4crButtonClicked(books)

#@Key open-containing-folder-button
#@Hook ConfigScript
def ocf4crSettingsMenu():
	ocf4cr.dbg("Calling ocf4cr.handleOcf4crSettingsMenuClicked()")
	ocf4cr.handleOcf4crSettingsMenuClicked()
	#ocf4crSettings()






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
#from MultipleDirsForm import MultipleDirsForm
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
		result = theForm.ShowDialog()
		theForm.Dispose()
		if result != DialogResult.Cancel:
			self.settings.loadSettingsFromFile()
			return True
		return False

	def warn(self, msg):
		print "[WARNING "+self.logPrefix+" "+datetime.now().strftime(self.logDateFormat)+"] "+msg

ocf4cr = OCF4CR()




















# MultipleDirsForm.py
# A plugin script for ComicRack
# (c) 2017 Bryn Mosher (BadMonkey0001)
# GPL v3 License
################################################################################

import clr
import sys
import System

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

from Ocf4crLang import lang

class MultipleDirsForm(Form):
	maxOpen = 0

	def __init__(self, ocf4cr, dirList):
		self._dirList = dirList
		self._checkList = []
		self._selectingAll = False
		self.ocf4cr = ocf4cr
		self.maxWindows = self.ocf4cr.settings.get("maxWindows")
		self.InitializeComponent(dirList)

	def directoryCheckboxesItemCheck(self, sender, e):
		checkedCount = len(self.directoryCheckboxes.CheckedItems)
		if self.maxWindows > 0:
			maxString = str(self.maxWindows);
		else:
			maxString = lang.enUs("unlimited");
			print "---- new val "+str(bool(e.NewValue.Checked))
			#print "---- str(e.NewValue) "+str(e.NewValue)+" - "+str(type(e.NewValue.Checked))+"\n"+"\n".join(dir(e.NewValue.Checked))
			# the checkbox is on its way to changing state, but hasn't yet
			if sender.GetItemCheckState(e.Index):
				self.selectAllCheckbox.Checked = checkedCount - 1 == len(self._dirList)
			else:
				self.selectAllCheckbox.Checked = checkedCount + 1 == len(self._dirList)
		if not sender.GetItemCheckState(e.Index):
			self.selectAllCheckbox.Text = lang.enUs("selectAll")+" "+lang.enUs("selectAllCount").replace('@count@', str(checkedCount+1)).replace('@max@', maxString)
			if not self._selectingAll and self.maxWindows > 0 and checkedCount >= self.maxWindows:
				self.ocf4cr.dbg("Preventing check beyond maxWindows ("+str(self.maxWindows)+") for index "+str(e.Index))
				e.NewValue = e.CurrentValue
				return
		else:
			self.selectAllCheckbox.Text = lang.enUs("selectAll")+" "+lang.enUs("selectAllCount").replace('@count@', str(checkedCount-1)).replace('@max@', maxString)
		#"selectAllCount": "(@count@ of max @max@ selected)",
		#	self.selectAllCheckbox.Text = lang.enUs("selectAll")+" "+lang.enUs("selectAll")
		#else:
		#	self.selectAllCheckbox.Text = lang.enUs("selectAll")
		#if len(self.directoryCheckboxes.CheckedItems) >= self.maxWindows:
		#	self.directoryCheckboxes.SetItemChecked(e.Index, False)

	def freshenmultipleLabelText(self):
		if self.maxWindows > 0:
			self.selectAllCheckbox.Text = lang.enUs("selectAll")+" "+lang.enUs("selectAllCount").replace('@count@', str(len(self.directoryCheckboxes.CheckedItems))).replace('@max@', str(self.maxWindows))
			self.labelMessage.Text = lang.enUs("multipleSelected").replace("@maxWindowsNotification@", lang.enUs("maxWindowsNotification").replace("@maxWindows@", str(self.maxWindows)))
		else:
			self.selectAllCheckbox.Text = lang.enUs("selectAll")+" "+lang.enUs("selectAllCount").replace('@count@', str(len(self.directoryCheckboxes.CheckedItems))).replace('@max@', lang.enUs("unlimited"))
			self.labelMessage.Text = lang.enUs("multipleSelected").replace("@maxWindowsNotification@", lang.enUs("maxWindowsUnlimitedNotification"))

	def clickCloseButton(self, sender, e):
		self.Close()

	def clickOpenButton(self, sender, e):
		self.ocf4cr.dbg("Opening directories:\n"+"\n".join(list(self.directoryCheckboxes.CheckedItems)))
		self.ocf4cr.openMultipleDirsWithCommand(list(self.directoryCheckboxes.CheckedItems))
		self.Close()

	def clickOpenSettingsButton(self, sender, e):
		self.ocf4cr.showSettingsForm()
		self.maxWindows = self.ocf4cr.settings.get("maxWindows")
		self.freshenmultipleLabelText()
		if not self.ocf4cr.settings.get("enableMultiWinForMultiSelected"):
			self.Close()

	def clickSelectAll(self, sender, e):
		doAll = self.selectAllCheckbox.Checked
		self.directoryCheckboxes.Refresh()

		idx = 0
		self._selectingAll = True
		while idx < len(self.directoryCheckboxes.Items):
			self.directoryCheckboxes.SetItemChecked(idx, doAll)
			self.ocf4cr.dbg("Selecting "+("all" if doAll else "none")+" checked "+self.directoryCheckboxes.GetItemText(idx))
			idx += 1
			if self.maxWindows > 0 and idx >= self.maxWindows:
				self.ocf4cr.dbg("Hit max number of items that can be selected.")
				break
		self._selectingAll = False

	def InitializeComponent(self, dirList):
		self.labelMessage = System.Windows.Forms.Label()
		self.labelMultipleWarning = System.Windows.Forms.Label()
		self.selectAllCheckbox = System.Windows.Forms.CheckBox()
		self.directoryCheckboxes = System.Windows.Forms.CheckedListBox()
		self.openButton = System.Windows.Forms.Button()
		self.openSettingsButton = System.Windows.Forms.Button()
		self.cancelButton = System.Windows.Forms.Button()
		for dirName in dirList:
			self._checkList.append(System.Windows.Forms.CheckBox())
		self.SuspendLayout()
		#
		# labelMessage
		#
		self.labelMessage.AutoSize = False
		self.labelMultipleWarning.Anchor = System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left | System.Windows.Forms.AnchorStyles.Right
		self.labelMessage.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point)
		self.labelMessage.Location = System.Drawing.Point(12, 9)
		self.labelMessage.Name = "labelMessage"
		self.labelMessage.Size = System.Drawing.Size(700, 32)
		self.freshenmultipleLabelText()
		self.labelMessage.TabStop = False
		#
		# selectAllCheckbox
		#
		self.selectAllCheckbox.AutoSize = True
		self.selectAllCheckbox.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point)
		self.selectAllCheckbox.Location = System.Drawing.Point(12, 44)
		self.selectAllCheckbox.Name = "selectAllCheckbox"
		self.selectAllCheckbox.Size = System.Drawing.Size(80, 17)
		self.selectAllCheckbox.TabIndex = 0
		self.selectAllCheckbox.Text = lang.enUs("selectAll")+" "+lang.enUs("selectAllCount").replace('@count@', "0").replace('@max@', str(self.maxWindows))
		self.selectAllCheckbox.UseVisualStyleBackColor = True
		self.selectAllCheckbox.Click += System.EventHandler(self.clickSelectAll)
		#
		# directoryCheckboxes
		#
		self.directoryCheckboxes.Anchor = System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left | System.Windows.Forms.AnchorStyles.Right
		self.directoryCheckboxes.FormattingEnabled = True
		self.directoryCheckboxes.CheckOnClick = True
		self.directoryCheckboxes.Location = System.Drawing.Point(12, 67)
		self.directoryCheckboxes.Name = "directoryCheckboxes"
		self.directoryCheckboxes.Size = System.Drawing.Size(703, 237)
		self.directoryCheckboxes.TabIndex = 1
		self.directoryCheckboxes.ItemCheck += System.Windows.Forms.ItemCheckEventHandler(self.directoryCheckboxesItemCheck)
		for dirName in self._dirList:
			self.directoryCheckboxes.Items.Add(dirName, False)
		#
		# labelMultipleWarning
		#
		self.labelMultipleWarning.AutoSize = False
		self.labelMultipleWarning.Anchor = System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left | System.Windows.Forms.AnchorStyles.Right
		self.labelMultipleWarning.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point)
		self.labelMultipleWarning.ForeColor = System.Drawing.Color.FromName("Red")
		self.labelMultipleWarning.Location = System.Drawing.Point(12, 305)
		self.labelMultipleWarning.Name = "labelMessage"
		self.labelMultipleWarning.Size = System.Drawing.Size(700, 32)
		self.labelMultipleWarning.Text = lang.enUs("multipleWarning")
		self.labelMultipleWarning.Padding = Padding(50, 0, 50, 0)
		self.labelMultipleWarning.TextAlign = System.Drawing.ContentAlignment.TopCenter
		self.labelMultipleWarning.TabStop = False
		#
		# openButton
		#
		self.openButton.Anchor = System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left | System.Windows.Forms.AnchorStyles.Right
		self.openButton.Location = System.Drawing.Point(12, 345)
		self.openButton.Name = "openButton"
		self.openButton.Size = System.Drawing.Size(703, 23)
		self.openButton.TabIndex = 2
		self.openButton.Text = lang.enUs("openSelected")
		self.openButton.UseVisualStyleBackColor = True
		self.openButton.Click += System.EventHandler(self.clickOpenButton)
		#
		# openSettingsButton
		#
		self.openSettingsButton.Anchor = System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left | System.Windows.Forms.AnchorStyles.Right
		self.openSettingsButton.Location = System.Drawing.Point(12, 373)
		self.openSettingsButton.Name = "openSettingsButton"
		self.openSettingsButton.Size = System.Drawing.Size(703, 23)
		self.openSettingsButton.TabIndex = 5
		self.openSettingsButton.Text = "Open Settings"
		self.openSettingsButton.UseVisualStyleBackColor = True
		self.openSettingsButton.Click += System.EventHandler(self.clickOpenSettingsButton)
		#
		# cancelButton
		#
		self.cancelButton.Anchor = System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left | System.Windows.Forms.AnchorStyles.Right
		self.cancelButton.Location = System.Drawing.Point(12, 401)
		self.cancelButton.Name = "cancelButton"
		self.cancelButton.Size = System.Drawing.Size(703, 23)
		self.cancelButton.TabIndex = 3
		self.cancelButton.Text = lang.enUs("cancel")
		self.cancelButton.UseVisualStyleBackColor = True
		self.cancelButton.Click += System.EventHandler(self.clickCloseButton)
		#
		# Form1
		#
		self.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
		self.ClientSize = System.Drawing.Size(730, 434)
		self.Controls.Add(self.labelMessage)
		self.Controls.Add(self.labelMultipleWarning)
		self.Controls.Add(self.directoryCheckboxes)
		self.Controls.Add(self.openSettingsButton)
		self.Controls.Add(self.openButton)
		self.Controls.Add(self.cancelButton)
		self.CancelButton = self.cancelButton
		self.Controls.Add(self.selectAllCheckbox)
		self.Name = "Form1"
		self.Text = lang.enUs("windowTitle")
		self.MaximizeBox = False
		self.MinimizeBox = False
		self.MinimumSize = System.Drawing.Size(730, 434)
		self.MaximumSize = System.Drawing.Size(2500, 2000)
		self.ControlBox = True
		self.Icon = self.ocf4cr.windowIconResource
		self.CenterToScreen()
		self.ResumeLayout(False)
		self.PerformLayout()
