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
		self.ocf4cr = ocf4cr
		self.maxWindows = self.ocf4cr.settings.get("maxWindows")
		self.InitializeComponent(dirList)

	# -- This crashes ComicRack and does not work --
	#def directoryCheckboxesItemCheck(self, sender, e):
	#	if len(self.directoryCheckboxes.CheckedItems) >= self.maxWindows:
	#		self.directoryCheckboxes.SetItemChecked(e.Index, False)

	def freshenmultipleLabelText(self):
		if self.maxWindows > 0:
			self.labelMessage.Text = lang.enUs("multipleSelected").replace("@maxWindowsNotification@", lang.enUs("maxWindowsNotification").replace("@maxWindows@", str(self.maxWindows)))
		else:
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
		while idx < len(self.directoryCheckboxes.Items):
			self.directoryCheckboxes.SetItemChecked(idx, doAll)
			self.ocf4cr.dbg("Selecting "+("all" if doAll else "none")+" checked "+self.directoryCheckboxes.GetItemText(idx))
			idx += 1

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
		self.selectAllCheckbox.Text = lang.enUs("selectAll")
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
		# This crashes ComicRack and does not work
		#self.directoryCheckboxes.ItemCheck += System.Windows.Forms.ItemCheckEventHandler(self.directoryCheckboxesItemCheck)
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

