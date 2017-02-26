# OpenContainingFolder4CR.py
# A plugin script for ComicRack
# (c) 2017 Bryn Mosher (BadMonkey0001)
# GPL v3 License
################################################################################

import clr
import sys
import System
import re

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

from System.Windows.Interop import WindowInteropHelper

from System.Collections import *

from System.IO import Path, FileInfo

#import multipleDirsForm
#from multipleDirsForm import MultipleDirsForm

rootScriptDirectory = FileInfo(__file__).DirectoryName

debugPrefix = "[OCF4CR Debug] "
logPrefix = "[OCF4CR] "
rgxAllWhitespaceOrEmpty = re.compile("^\s*$")
settingsPath = Path.Combine(rootScriptDirectory, "OCF4C_settings.dat")
windowIconPath = Path.Combine(rootScriptDirectory, "Bad_Monkey_Logo_just_monkey_icon.ico")
windowIconResource = Icon(windowIconPath)
windowTitle = "Open Containing Folder for ComicRack"

ocf4crVersion = "0.0.5"

ocf4crDefaultSettings = {
	"ignoreMultiple": False,
	"maxMultiple": 0,
	"openMultiple": True,
	"onlyOpenFirst": False,
	"separateExplorer": True,
}

ocf4crOpeners = {
	'explorer': {
		"path": "C:\Windows\explorer.exe",
		"args": "/e @separateExplorer@ /root,\"@path@\"",
		"separateExplorer": "/separate"
	},
}

ocf4crStrings = {
	"cancel": "Cancel",
	"failedCommand": "Could not run explore.exe command!!!",
	"invalidList": "Not a valid list.\n",
	"multipleSelected": "Multiple directories found. Please select the ones you which to open.",
	"multipleWarning": "Warning! This could open many windows at once and may be slow for large numbers of directories. Open multiple at your own risk!",
	"nobooks": "You don't have any books selected.\n\nPlease select at least one book.",
	"nodirs": "Couldn't find any directories.\n\nPlease select at least one book with a file.",
	"openSelected": "Open selected directories",
	"selectAll": "Select All",
}

########################################
# Hooks
########################################

#@Name Open Containing Folder for ComicRack
#@Hook Books
#@Description Open Containing Folder for ComicRack: Open a file browser for a selected book.
#@Key open-containing-folder-button
#@Image OCF4CR.png
def ocf4crButton(books):
	log("Triggered ocf4crButton")

	if not books:
		MessageBox.Show(ocf4crStrings['nobooks'], windowTitle, MessageBoxButtons.OK, MessageBoxIcon.Information)
		return

	dirList = getDirectoriesList(books)

	if not dirList:
		MessageBox.Show(ocf4crStrings['nodirs'], windowTitle, MessageBoxButtons.OK, MessageBoxIcon.Information)
		return

	dirCount = len(dirList)

	if dirCount > 1:
		showMultipleForm(dirList)
		return

	openDirInExplorer(dirList[0])

#@Name Open Containing Folder for ComicRack Settings
#@Hook Library
#@Image OCF4CR.png
#@Key open-containing-folder-button
def ocf4crSettings():
	log("Triggered ocf4crSettings")
	MessageBox.Show("Set this!", windowTitle, MessageBoxButtons.OK, MessageBoxIcon.Information)

#@Key open-containing-folder-button
#@Hook ConfigScript
def ocf4crSettingsMenu():
	ocf4crSettings()

########################################
# Funcs
########################################

def dbg(msg):
	print debugPrefix+msg

def getDirectoriesList(books):
	dirListAll = []

	if books.Count < 1:
		return dirListAll

	for book in books:
		if book.FileDirectory and not rgxAllWhitespaceOrEmpty.match(book.FileDirectory):
			dirListAll.append(book.FileDirectory)

	dirListAll.sort()
	return list(set(dirListAll))

def log(msg):
	print logPrefix+msg

def openDirInExplorer(dirPath):
	parsedArgs = str(ocf4crOpeners['explorer']['args']).replace('@path@', dirPath)
	try:
		Process.Start(ocf4crOpeners['explorer']['path'], parsedArgs)
	except:
		errType, errValue, errTrace = sys.exc_info()
		MessageBox.Show(ocf4crStrings['failedCommand']+"\n\n"+ocf4crOpeners['explorer']['path']+" "+parsedArgs+"\n\n"+str(errValue), windowTitle, MessageBoxButtons.OK, MessageBoxIcon.Warning)

def openMultipleDirsInExplorer(dirList):
	if not isinstance(dirList, list):
		MessageBox.Show(ocf4crStrings["invalidList"]+str(type(dirList)), windowTitle, MessageBoxButtons.OK, MessageBoxIcon.Warning)
	else:
		for dirName in dirList:
			openDirInExplorer(dirName)

def showMultipleForm(dirList):
	theForm = MultipleDirsForm(dirList)
	result = theForm.ShowDialog()
	theForm.Dispose()
	if result != DialogResult.Cancel:
		return True
	return False

########################################
# Forms
########################################

class MultipleDirsForm(Form):
	def __init__(self, dirList):
		self._dirList = dirList
		self.InitializeComponent(dirList)

	def InitializeComponent(self, dirList):
		self.labelMessage = System.Windows.Forms.Label()
		self.labelMultipleWarning = System.Windows.Forms.Label()
		self.selectAllCheckbox = System.Windows.Forms.CheckBox()
		self.directoryCheckboxes = System.Windows.Forms.CheckedListBox()
		self.openButton = System.Windows.Forms.Button()
		self.cancelButton = System.Windows.Forms.Button()
		self.SuspendLayout()
		#
		# labelMessage
		#
		self.labelMessage.AutoSize = False
		self.labelMessage.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point)
		self.labelMessage.Location = System.Drawing.Point(12, 9)
		self.labelMessage.Name = "labelMessage"
		self.labelMessage.Size = System.Drawing.Size(567, 20)
		self.labelMessage.Text = ocf4crStrings['multipleSelected']
		self.labelMessage.TabStop = False
		#
		# labelMultipleWarning
		#
		self.labelMultipleWarning.AutoSize = False
		self.labelMultipleWarning.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point)
		self.labelMultipleWarning.ForeColor = System.Drawing.Color.FromName("Red")
		dbg("--- dir foo\n"+"\n".join(dir(System.Drawing.Color)))
		#this.explorerSeparateCheckbox.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(192)))), ((int)(((byte)(0)))), ((int)(((byte)(0)))));
		#this.explorerSeparateCheckbox.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(192)))), ((int)(((byte)(0)))), ((int)(((byte)(0)))));
		self.labelMultipleWarning.Location = System.Drawing.Point(12, 32)
		self.labelMultipleWarning.Name = "labelMessage"
		self.labelMultipleWarning.Size = System.Drawing.Size(700, 32)
		self.labelMultipleWarning.Text = ocf4crStrings['multipleWarning']
		self.labelMultipleWarning.TabStop = False
		#
		# selectAllCheckbox
		#
		self.selectAllCheckbox.AutoSize = True
		self.selectAllCheckbox.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point)
		self.selectAllCheckbox.Location = System.Drawing.Point(12, 67)
		self.selectAllCheckbox.Name = "selectAllCheckbox"
		self.selectAllCheckbox.Size = System.Drawing.Size(80, 17)
		self.selectAllCheckbox.TabIndex = 0
		self.selectAllCheckbox.Text = ocf4crStrings['selectAll']
		self.selectAllCheckbox.UseVisualStyleBackColor = True
		#
		# directoryCheckboxes
		#
		self.directoryCheckboxes.Anchor = System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left | System.Windows.Forms.AnchorStyles.Right
		self.directoryCheckboxes.FormattingEnabled = True
		self.directoryCheckboxes.CheckOnClick = True
		self.directoryCheckboxes.Location = System.Drawing.Point(12, 90)
		self.directoryCheckboxes.Name = "directoryCheckboxes"
		self.directoryCheckboxes.Size = System.Drawing.Size(703, 264)
		self.directoryCheckboxes.TabIndex = 1
		for dirName in dirList:
			foo = self.directoryCheckboxes.Items.Add(dirName)
			#dbg("--- dir foo\n"+"\n".join(dir(foo)))
		#
		# openButton
		#
		self.openButton.Anchor = System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left | System.Windows.Forms.AnchorStyles.Right
		self.openButton.Location = System.Drawing.Point(15, 364)
		self.openButton.Name = "openButton"
		self.openButton.Size = System.Drawing.Size(703, 23)
		self.openButton.TabIndex = 2
		self.openButton.Text = ocf4crStrings['openSelected']
		self.openButton.UseVisualStyleBackColor = True
		self.openButton.Click += System.EventHandler(self.clickOpenButton)
		#
		# cancelButton
		#
		self.cancelButton.Anchor = System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left | System.Windows.Forms.AnchorStyles.Right
		self.cancelButton.Location = System.Drawing.Point(15, 393)
		self.cancelButton.Name = "cancelButton"
		self.cancelButton.Size = System.Drawing.Size(703, 23)
		self.cancelButton.TabIndex = 3
		self.cancelButton.Text = ocf4crStrings['cancel']
		self.cancelButton.UseVisualStyleBackColor = True
		self.cancelButton.Click += System.EventHandler(self.clickCloseButton)
		#
		# Form1
		#
		#self.AutoScaleDimensions = System.Drawing.SizeF(6F, 13F)
		self.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
		self.ClientSize = System.Drawing.Size(730, 428)
		self.Controls.Add(self.labelMessage)
		self.Controls.Add(self.labelMultipleWarning)
		self.Controls.Add(self.directoryCheckboxes)
		self.Controls.Add(self.cancelButton)
		self.CancelButton = self.cancelButton
		self.Controls.Add(self.openButton)
		self.Controls.Add(self.selectAllCheckbox)
		self.Name = "Form1"
		self.Text = windowTitle
		#self.ShowInTaskbar = False;
		self.MaximizeBox = False
		self.MinimizeBox = False
		self.MinimumSize = System.Drawing.Size(746, 467)
		self.MaximumSize = System.Drawing.Size(2500, 2000)
		self.ControlBox = True
		self.Icon = windowIconResource
		self.CenterToScreen()
		self.ResumeLayout(False)
		self.PerformLayout()

	def clickCloseButton(self, sender, e):
		self.Close()

	def clickOpenButton(self, sender, e):
		openMultipleDirsInExplorer(list(self.directoryCheckboxes.CheckedItems))
		self.Close()
