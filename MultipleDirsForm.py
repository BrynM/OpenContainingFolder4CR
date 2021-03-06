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
	_dirList = None
	_checkList = None
	_maxString = None
	_maxWindows = 0
	ocf4cr = None

	def __init__(self, ocf4cr, dirList):
		self._dirList = dirList
		self._checkList = []
		self._maxString = lang.enUs("unlimited")
		self._selectingAll = False
		self.ocf4cr = ocf4cr
		self._maxWindows = self.ocf4cr.settings.get("maxWindows")
		self.ocf4cr.settings.loadSettingsFromFile()
		self.InitializeComponent(dirList)
		self.updateMaxStrings(0)

	def updateMaxStrings(self, checkedCount):
		unlimited = self._maxWindows < 1
		if unlimited:
			self._maxString = lang.enUs("unlimited");
		else:
			self._maxString = str(self._maxWindows);
		self.labelSelectedCounted.Text =lang.enUs("selectAllCount").replace('@count@', str(int(checkedCount))).replace('@max@', self._maxString)
		self.selectNoneButton.Enabled = checkedCount > 0;
		self.selectAllButton.Enabled = checkedCount < self._maxWindows and checkedCount < len(self.directoryCheckboxes.Items);
		if unlimited or self._maxWindows >= len(self.directoryCheckboxes.Items):
			self.selectAllButton.Text = lang.enUs("selectAll")
		else:
			self.selectAllButton.Text = lang.enUs("selectMax")

	def directoryCheckboxesItemCheck(self, sender, e):
		unlimited = self._maxWindows < 1
		checkedCount = len(self.directoryCheckboxes.CheckedItems)
		# the checkbox is on its way to changing state, but hasn't yet
		isGettingChecked = not self.directoryCheckboxes.GetItemCheckState(e.Index)
		if isGettingChecked and checkedCount + 1 >= self._maxWindows:
			self.labelSelectedCounted.ForeColor = System.Drawing.Color.FromName("Red")
		else:
			self.labelSelectedCounted.ForeColor = System.Drawing.Color.FromName("Black")
		if isGettingChecked:
			if not unlimited and not self._selectingAll and checkedCount >= self._maxWindows:
				self.ocf4cr.dbg("Preventing check beyond maxWindows ("+str(self._maxWindows)+") for index "+str(e.Index))
				e.NewValue = e.CurrentValue
				return
			self.updateMaxStrings(checkedCount+1)
		else:
			self.updateMaxStrings(checkedCount-1)

	def clickCloseButton(self, sender, e):
		self.Close()

	def clickOpenButton(self, sender, e):
		self.ocf4cr.dbg("Opening directories:\n"+"\n".join(list(self.directoryCheckboxes.CheckedItems)))
		self.ocf4cr.openMultipleDirsWithCommand(list(self.directoryCheckboxes.CheckedItems))
		self.Close()

	def clickOpenSettingsButton(self, sender, e):
		self.ocf4cr.showSettingsForm()
		self._maxWindows = self.ocf4cr.settings.get("maxWindows")
		self.updateMaxStrings(len(self.directoryCheckboxes.CheckedItems))
		if not self.ocf4cr.settings.get("enableMultiWinForMultiSelected"):
			self.Close()

	def setAllTimesChecked(self, setToChecked):
		idx = 0
		self._selectingAll = True
		while idx < len(self.directoryCheckboxes.Items):
			if bool(self.directoryCheckboxes.GetItemCheckState(idx)) != bool(setToChecked):
				self.directoryCheckboxes.SetItemChecked(idx, setToChecked)
				self.ocf4cr.dbg("Setting checked index "+self.directoryCheckboxes.GetItemText(idx)+" to "+str(setToChecked))
			idx += 1
			if setToChecked and self._maxWindows > 0 and idx >= self._maxWindows:
				self.ocf4cr.dbg("Hit max number of items that can be selected with select all.")
				break
		self._selectingAll = False

	def clickSelectAllButton(self, sender, e):
		self.setAllTimesChecked(True)
		self.updateMaxStrings(len(self.directoryCheckboxes.CheckedItems))

	def clickSelectNoneButton(self, sender, e):
		self.setAllTimesChecked(False)
		self.updateMaxStrings(len(self.directoryCheckboxes.CheckedItems))

	def InitializeComponent(self, dirList):
		self.labelSelectedCounted = System.Windows.Forms.Label()
		self.labelMessage = System.Windows.Forms.Label()
		self.labelMultipleWarning = System.Windows.Forms.Label()
		self.selectAllButton = System.Windows.Forms.Button()
		self.selectNoneButton = System.Windows.Forms.Button()
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
		self.labelMessage.Text = lang.enUs("multipleSelected")
		self.labelMessage.TabStop = False

		#
		# selectAllButton
		#
		self.selectAllButton.Location = System.Drawing.Point(12, 40)
		self.selectAllButton.Name = "selectAllButton"
		self.selectAllButton.Size = System.Drawing.Size(200, 23)
		self.selectAllButton.Text = lang.enUs("selectMax")
		self.selectAllButton.Anchor = System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left
		self.selectAllButton.Click += System.EventHandler(self.clickSelectAllButton)
		#
		# selectNoneButton
		#
		self.selectNoneButton.Location = System.Drawing.Point(515, 40)
		self.selectNoneButton.Name = "selectNoneButton"
		self.selectNoneButton.Size = System.Drawing.Size(200, 23)
		self.selectNoneButton.Text = lang.enUs("selectNone")
		self.selectNoneButton.Enabled = False
		self.selectNoneButton.Anchor = System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right
		self.selectNoneButton.Click += System.EventHandler(self.clickSelectNoneButton)
		#
		# labelSelectedCounted
		#
		self.labelSelectedCounted.Name = "labelSelectedCounted"
		self.labelSelectedCounted.AutoSize = False
		self.labelSelectedCounted.Anchor = System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left | System.Windows.Forms.AnchorStyles.Right
		self.labelSelectedCounted.ForeColor = System.Drawing.Color.FromName("Black")
		self.labelSelectedCounted.Location = System.Drawing.Point(208, 44)
		self.labelSelectedCounted.Size = System.Drawing.Size(300, 17)
		self.labelSelectedCounted.Text = lang.enUs("selectAllCount").replace('@count@', "0").replace('@max@', str(self._maxWindows))
		self.labelSelectedCounted.TextAlign = System.Drawing.ContentAlignment.TopCenter
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
		self.Controls.Add(self.selectNoneButton)
		self.Controls.Add(self.selectAllButton)
		self.Controls.Add(self.labelSelectedCounted)
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
