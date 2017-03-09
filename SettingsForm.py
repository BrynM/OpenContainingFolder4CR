# SettingsForm.py
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

import System.Windows.Forms
from System.Windows.Forms import *

import System.Drawing
from System.Drawing import *

from System.IO import Path, FileInfo

from Ocf4crLang import lang

class SettingsForm(Form):
	ocf4cr = None
	settings = None
	currentSettings = {}
	pendingSettings = {}

	def __init__(self, ocf4cr, settingsObj):
		self.ocf4cr = ocf4cr
		self.settings = settingsObj
		self.currentSettings = settingsObj.getAll()
		self.pendingSettings = settingsObj.getAll()
		self.InitializeComponent()
		self.handleEnableCustomCommandCheckboxCheckChanged(None, None)

	def langDefault(self, setting):
		if not setting in self.settings.defaultValues:
			return ""
		return " ("+lang.enUs("defaultPlug").replace('@value@', str(self.settings.defaultValues[setting]))+")"

	def checkSettings(self):
		pendingAreActive = self.settings.givenAreActive(self.pendingSettings)
		pendingAreDefaults = self.settings.givenAreDefaults(self.pendingSettings)
		self.saveButton.Enabled = not pendingAreActive
		self.defaultsButton.Enabled = not pendingAreDefaults
		return pendingAreDefaults and pendingAreActive

	def handleBrowseCommandExecButtonClick(self, sender, e):
		self.openCommandExecDialog.ShowDialog()

	def handleCancelButtonClick(self, sender, e):
		self.Close()

	def handleCommandExecutableTextboxTextChanged(self, sender, e):
		if self.commandExecutableTextbox.Text != self.pendingSettings["customExec"]:
			self.pendingSettings["customExec"] = str(self.commandExecutableTextbox.Text)
			self.ocf4cr.dbg("pendingSettings[\"customExec\"] set to \""+self.pendingSettings["customExec"]+"\"")
		self.checkSettings()

	def handleCommandArgumentsTextboxTextChanged(self, sender, e):
		if self.commandArgumentsTextbox.Text != self.pendingSettings["customArgs"]:
			self.pendingSettings["customArgs"] = str(self.commandArgumentsTextbox.Text)
			self.ocf4cr.dbg("pendingSettings[\"customArgs\"] set to \""+self.pendingSettings["customArgs"]+"\"")
		self.checkSettings()

	def handleDefaultsButtonClick(self, sender, e):
		self.ocf4cr.dbg("Settings form loading defaults.")
		defaults = self.settings.getDefaults()

		self.maxWinNumeric.Value = defaults["maxWindows"]
		# radio buttons need true to be set only once
		if self.ignoreMultipleRadioButton.Checked != defaults["ignoreMultiSelected"]:
			self.ignoreMultipleRadioButton.Checked = bool(defaults["ignoreMultiSelected"])
		if self.enableMultipleWindowsRadioButton.Checked != defaults["enableMultiWinForMultiSelected"]:
			self.enableMultipleWindowsRadioButton.Checked = bool(defaults["enableMultiWinForMultiSelected"])
		if self.enableOnlyFirstBookRadioButton.Checked != defaults["onlyUseFirstDir"]:
			self.enableOnlyFirstBookRadioButton.Checked = bool(defaults["onlyUseFirstDir"])
		# end the radio set
		self.explorerSeparateCheckbox.Checked = bool(defaults["explorerSeparateProcess"])
		self.enableCustomCommandCheckbox.Checked = bool(defaults["enableCustomCommand"])
		self.commandExecutableTextbox.Text = str(defaults["customExec"])
		self.commandArgumentsTextbox.Text = str(defaults["customArgs"])
		self.checkSettings()

	def handleEnableCustomCommandCheckboxCheckChanged(self, sender, e):
		self.customCommandPartsGroupBox.Enabled = bool(self.enableCustomCommandCheckbox.Checked)
		self.explorerExeGroupBox.Enabled = bool(not self.enableCustomCommandCheckbox.Checked)
		if self.enableCustomCommandCheckbox.Checked != self.pendingSettings["enableCustomCommand"]:
			self.pendingSettings["enableCustomCommand"] = bool(self.enableCustomCommandCheckbox.Checked)
			self.ocf4cr.dbg("pendingSettings[\"enableCustomCommand\"] set to "+str(self.pendingSettings["enableCustomCommand"]))
		self.checkSettings()

	def handleEnableMultipleWindowsRadioButtonCheckedChanged(self, sender, e):
		if self.enableMultipleWindowsRadioButton.Checked != self.pendingSettings["enableMultiWinForMultiSelected"]:
			self.pendingSettings["enableMultiWinForMultiSelected"] = bool(self.enableMultipleWindowsRadioButton.Checked)
			self.ocf4cr.dbg("pendingSettings[\"enableMultiWinForMultiSelected\"] set to "+str(self.pendingSettings["enableMultiWinForMultiSelected"]))
		self.checkSettings()

	def handleEnableOnlyFirstBookRadioButtonCheckedChanged(self, sender, e):
		if self.enableOnlyFirstBookRadioButton.Checked != self.pendingSettings["onlyUseFirstDir"]:
			self.pendingSettings["onlyUseFirstDir"] = bool(self.enableOnlyFirstBookRadioButton.Checked)
			self.ocf4cr.dbg("pendingSettings[\"onlyUseFirstDir\"] set to "+str(self.pendingSettings["onlyUseFirstDir"]))
		self.checkSettings()

	def handleExplorerSeparateCheckboxCheckedChanged(self, sender, e):
		if self.explorerSeparateCheckbox.Checked != self.pendingSettings["explorerSeparateProcess"]:
			self.pendingSettings["explorerSeparateProcess"] = bool(self.explorerSeparateCheckbox.Checked)
			self.ocf4cr.dbg("pendingSettings[\"explorerSeparateProcess\"] set to "+str(self.pendingSettings["explorerSeparateProcess"]))
		self.checkSettings()

	def handleIgnoreMultipleRadioButtonCheckedChanged(self, sender, e):
		if self.ignoreMultipleRadioButton.Checked != self.pendingSettings["ignoreMultiSelected"]:
			self.pendingSettings["ignoreMultiSelected"] = bool(self.ignoreMultipleRadioButton.Checked)
			self.ocf4cr.dbg("pendingSettings[\"ignoreMultiSelected\"] set to "+str(self.pendingSettings["ignoreMultiSelected"]))

	def handleMaxWinNumericValueChanged(self, sender, e):
		if self.maxWinNumeric.Value != self.pendingSettings["maxWindows"]:
			self.pendingSettings["maxWindows"] = int(self.maxWinNumeric.Value)
			self.ocf4cr.dbg("pendingSettings[\"maxWindows\"] set to "+str(self.pendingSettings["maxWindows"]))
		self.checkSettings()

	def handleOpenCommandExecDialogFileOk(self, sender, e):
		self.commandExecutableTextbox.Text = sender.FileName

	def handleSaveButtonClick(self, sender, e):
		self.ocf4cr.dbg("Settings form saving settings.")
		self.settings.setAll(self.pendingSettings)

		if self.settings.saveSettingsFile():
			self.Close()

	def InitializeComponent(self):
		self.ocf4cr.dbg("Showing SettingsForm.")
		# General
		self.generalGroupBox = System.Windows.Forms.GroupBox()
		self.maxWinNumeric = System.Windows.Forms.NumericUpDown()
		self.maxWinNumericLabel = System.Windows.Forms.Label()
		self.multipleGroupBox = System.Windows.Forms.GroupBox()
		self.ignoreMultipleRadioButton = System.Windows.Forms.RadioButton()
		self.enableMultipleWindowsRadioButton = System.Windows.Forms.RadioButton()
		self.enableOnlyFirstBookRadioButton = System.Windows.Forms.RadioButton()
		# Explorer.exe
		self.explorerExeGroupBox = System.Windows.Forms.GroupBox()
		self.explorerSeparateCheckbox = System.Windows.Forms.CheckBox()
		# Custom Command
		self.customCommandGroupBox = System.Windows.Forms.GroupBox()
		self.customCommandLabel1 = System.Windows.Forms.Label()
		self.customCommandLabel2 = System.Windows.Forms.Label()
		self.enableCustomCommandCheckbox = System.Windows.Forms.CheckBox()
		self.customCommandPartsGroupBox = System.Windows.Forms.GroupBox()
		self.commandExecutableLabel = System.Windows.Forms.Label()
		self.commandExecutableTextbox = System.Windows.Forms.TextBox()
		self.openCommandExecDialog = System.Windows.Forms.OpenFileDialog()
		self.browseCommandExecButton = System.Windows.Forms.Button()
		self.commandArgumentsLabel = System.Windows.Forms.Label()
		self.commandArgumentsTextbox = System.Windows.Forms.TextBox()
		# Buttons
		self.saveButton = System.Windows.Forms.Button()
		self.defaultsButton = System.Windows.Forms.Button()
		self.cancelButton = System.Windows.Forms.Button()
		# Suspend our layouts
		self.generalGroupBox.SuspendLayout()
		self.explorerExeGroupBox.SuspendLayout()
		self.multipleGroupBox.SuspendLayout()
		self.SuspendLayout()
		#
		# generalGroupBox
		#
		self.generalGroupBox.Anchor = System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left | System.Windows.Forms.AnchorStyles.Right
		self.generalGroupBox.Controls.Add(self.maxWinNumeric)
		self.generalGroupBox.Controls.Add(self.maxWinNumericLabel)
		self.generalGroupBox.Controls.Add(self.multipleGroupBox)
		self.generalGroupBox.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point)
		self.generalGroupBox.Location = System.Drawing.Point(12, 12)
		self.generalGroupBox.Name = "generalGroupBox"
		self.generalGroupBox.Size = System.Drawing.Size(550, 135)
		self.generalGroupBox.TabIndex = 0
		self.generalGroupBox.Text = lang.enUs("generalSettings")
		#
		# maxWinNumeric
		#
		self.maxWinNumeric.Anchor = System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left
		self.maxWinNumeric.Location = System.Drawing.Point(6, 19)
		self.maxWinNumeric.Name = "maxWinNumeric"
		self.maxWinNumeric.Size = System.Drawing.Size(59, 20)
		self.maxWinNumeric.TabIndex = 1
		self.maxWinNumeric.Minimum = 0
		self.maxWinNumeric.TextAlign = System.Windows.Forms.HorizontalAlignment.Right
		self.maxWinNumeric.Value = self.settings.get("maxWindows")
		self.maxWinNumeric.ValueChanged += System.EventHandler(self.handleMaxWinNumericValueChanged)
		#
		# maxWinNumericLabel
		#
		self.maxWinNumericLabel.Anchor = System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left
		self.maxWinNumericLabel.AutoSize = True
		self.maxWinNumericLabel.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point)
		self.maxWinNumericLabel.Location = System.Drawing.Point(67, 22)
		self.maxWinNumericLabel.Name = "maxWinNumericLabel"
		self.maxWinNumericLabel.Size = System.Drawing.Size(253, 13)
		self.maxWinNumericLabel.TabIndex = 2
		self.maxWinNumericLabel.Text = lang.enUs("maxWinNumericLabel")+self.langDefault("maxWindows")
		#
		# multipleGroupBox
		#
		self.multipleGroupBox.Anchor = System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left | System.Windows.Forms.AnchorStyles.Right
		self.multipleGroupBox.Controls.Add(self.ignoreMultipleRadioButton)
		self.multipleGroupBox.Controls.Add(self.enableMultipleWindowsRadioButton)
		self.multipleGroupBox.Controls.Add(self.enableOnlyFirstBookRadioButton)
		self.multipleGroupBox.Cursor = System.Windows.Forms.Cursors.Default
		self.multipleGroupBox.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point)
		self.multipleGroupBox.Location = System.Drawing.Point(6, 45)
		self.multipleGroupBox.Name = "multipleGroupBox"
		self.multipleGroupBox.Size = System.Drawing.Size(538, 84)
		self.multipleGroupBox.TabIndex = 3
		self.multipleGroupBox.Text = lang.enUs("multipleSelections")
		#
		# ignoreMultipleRadioButton
		#
		self.ignoreMultipleRadioButton.AutoSize = True
		if self.settings.get("ignoreMultiSelected"):
			self.ignoreMultipleRadioButton.Checked = True
		self.ignoreMultipleRadioButton.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point)
		self.ignoreMultipleRadioButton.Location = System.Drawing.Point(6, 17)
		self.ignoreMultipleRadioButton.Name = "ignoreMultipleRadioButton"
		self.ignoreMultipleRadioButton.Size = System.Drawing.Size(268, 17)
		self.ignoreMultipleRadioButton.TabIndex = 4
		self.ignoreMultipleRadioButton.Text = lang.enUs("ignoreMultiple")
		if self.settings.defaultValues["ignoreMultiSelected"]:
			self.ignoreMultipleRadioButton.Text += " ("+lang.enUs("default")+")"
		self.ignoreMultipleRadioButton.UseVisualStyleBackColor = True
		self.ignoreMultipleRadioButton.CheckedChanged += System.EventHandler(self.handleIgnoreMultipleRadioButtonCheckedChanged)
		#
		# enableMultipleWindowsRadioButton
		#
		self.enableMultipleWindowsRadioButton.AutoSize = True
		if self.settings.get("enableMultiWinForMultiSelected"):
			self.enableMultipleWindowsRadioButton.Checked = True
		self.enableMultipleWindowsRadioButton.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point)
		self.enableMultipleWindowsRadioButton.Location = System.Drawing.Point(6, 40)
		self.enableMultipleWindowsRadioButton.Name = "enableMultipleWindowsRadioButton"
		self.enableMultipleWindowsRadioButton.Size = System.Drawing.Size(320, 17)
		self.enableMultipleWindowsRadioButton.TabIndex = 5
		self.enableMultipleWindowsRadioButton.Text = lang.enUs("enableMultipleWindows")
		if self.settings.defaultValues["enableMultiWinForMultiSelected"]:
			self.enableMultipleWindowsRadioButton.Text += " ("+lang.enUs("default")+")"
		self.enableMultipleWindowsRadioButton.UseVisualStyleBackColor = True
		self.enableMultipleWindowsRadioButton.CheckedChanged += System.EventHandler(self.handleEnableMultipleWindowsRadioButtonCheckedChanged)
		#
		# enableOnlyFirstBookRadioButton
		#
		self.enableOnlyFirstBookRadioButton.AutoSize = True
		if self.settings.get("onlyUseFirstDir"):
			self.enableOnlyFirstBookRadioButton.Checked = True
		self.enableOnlyFirstBookRadioButton.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point)
		self.enableOnlyFirstBookRadioButton.Location = System.Drawing.Point(6, 63)
		self.enableOnlyFirstBookRadioButton.Name = "enableOnlyFirstBookRadioButton"
		self.enableOnlyFirstBookRadioButton.Size = System.Drawing.Size(314, 17)
		self.enableOnlyFirstBookRadioButton.TabIndex = 6
		self.enableOnlyFirstBookRadioButton.Text = lang.enUs("enableOnlyFirstBook")
		if self.settings.defaultValues["onlyUseFirstDir"]:
			self.enableOnlyFirstBookRadioButton.Text += " ("+lang.enUs("default")+")"
		self.ignoreMultipleRadioButton.UseVisualStyleBackColor = True
		self.enableOnlyFirstBookRadioButton.UseVisualStyleBackColor = True
		self.enableOnlyFirstBookRadioButton.CheckedChanged += System.EventHandler(self.handleEnableOnlyFirstBookRadioButtonCheckedChanged)
		#
		# explorerExeGroupBox
		#
		self.explorerExeGroupBox.Anchor = System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left | System.Windows.Forms.AnchorStyles.Right
		self.explorerExeGroupBox.Controls.Add(self.explorerSeparateCheckbox)
		self.explorerExeGroupBox.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point)
		self.explorerExeGroupBox.Location = System.Drawing.Point(12, 153)
		self.explorerExeGroupBox.Name = "explorerExeGroupBox"
		self.explorerExeGroupBox.Size = System.Drawing.Size(550, 46)
		self.explorerExeGroupBox.TabIndex = 7
		self.explorerExeGroupBox.Text = lang.enUs("explorerExe")
		#
		# explorerSeparateCheckbox
		#
		self.explorerSeparateCheckbox.AutoSize = True
		self.explorerSeparateCheckbox.Checked = self.settings.get("explorerSeparateProcess")
		self.explorerSeparateCheckbox.Cursor = System.Windows.Forms.Cursors.Default
		self.explorerSeparateCheckbox.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point)
		self.explorerSeparateCheckbox.Location = System.Drawing.Point(6, 19)
		self.explorerSeparateCheckbox.Name = "explorerSeparateCheckbox"
		self.explorerSeparateCheckbox.Size = System.Drawing.Size(362, 17)
		self.explorerSeparateCheckbox.TabIndex = 8
		self.explorerSeparateCheckbox.Text = lang.enUs("explorerExeSeparate")
		if self.settings.defaultValues["explorerSeparateProcess"]:
			self.explorerSeparateCheckbox.Text += " ("+lang.enUs("defaultChecked")+")"
		else:
			self.explorerSeparateCheckbox.Text += " ("+lang.enUs("defaultUnchecked")+")"
		self.explorerSeparateCheckbox.UseVisualStyleBackColor = True
		self.explorerSeparateCheckbox.CheckedChanged += System.EventHandler(self.handleExplorerSeparateCheckboxCheckedChanged)
		#
		# customCommandGroupBox
		#
		self.explorerExeGroupBox.Anchor = System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left | System.Windows.Forms.AnchorStyles.Right
		self.customCommandGroupBox.Controls.Add(self.customCommandPartsGroupBox)
		self.customCommandGroupBox.Controls.Add(self.enableCustomCommandCheckbox)
		self.customCommandGroupBox.Controls.Add(self.customCommandLabel2)
		self.customCommandGroupBox.Controls.Add(self.customCommandLabel1)
		self.customCommandGroupBox.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point)
		self.customCommandGroupBox.Location = System.Drawing.Point(12, 205)
		self.customCommandGroupBox.Name = "customCommandGroupBox"
		self.customCommandGroupBox.Size = System.Drawing.Size(550, 291)
		self.customCommandGroupBox.TabIndex = 9
		self.customCommandGroupBox.Text = lang.enUs("customCommandGroupBox")
		#
		# customCommandLabel1
		#
		self.customCommandLabel1.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point)
		self.customCommandLabel1.Location = System.Drawing.Point(6, 16)
		self.customCommandLabel1.Name = "customCommandLabel1"
		self.customCommandLabel1.Size = System.Drawing.Size(538, 70)
		self.customCommandLabel1.TabIndex = 10
		self.customCommandLabel1.Text = lang.enUs("customCommandLabel1")
		#
		# customCommandLabel2
		#
		self.customCommandLabel2.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point)
		self.customCommandLabel2.Location = System.Drawing.Point(16, 88)
		self.customCommandLabel2.Name = "customCommandLabel2"
		self.customCommandLabel2.Size = System.Drawing.Size(528, 72)
		self.customCommandLabel2.TabIndex = 11
		self.customCommandLabel2.Text = lang.enUs("customCommandLabel2")
		#
		# enableCustomCommandCheckbox
		#
		self.enableCustomCommandCheckbox.AutoSize = True
		self.enableCustomCommandCheckbox.Checked = self.settings.get("enableCustomCommand")
		self.enableCustomCommandCheckbox.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point)
		self.enableCustomCommandCheckbox.Location = System.Drawing.Point(6, 163)
		self.enableCustomCommandCheckbox.Name = "enableCustomCommandCheckbox"
		self.enableCustomCommandCheckbox.Size = System.Drawing.Size(147, 17)
		self.enableCustomCommandCheckbox.TabIndex = 12
		self.enableCustomCommandCheckbox.Text = lang.enUs("enableCustomCommand")
		if self.settings.defaultValues["enableCustomCommand"]:
			self.enableCustomCommandCheckbox.Text += " ("+lang.enUs("defaultChecked")+")"
		else:
			self.enableCustomCommandCheckbox.Text += " ("+lang.enUs("defaultUnchecked")+")"
		self.enableCustomCommandCheckbox.UseVisualStyleBackColor = True
		self.enableCustomCommandCheckbox.CheckedChanged += System.EventHandler(self.handleEnableCustomCommandCheckboxCheckChanged)
		#
		# customCommandPartsGroupBox
		#
		self.explorerExeGroupBox.Anchor = System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left | System.Windows.Forms.AnchorStyles.Right
		self.customCommandPartsGroupBox.Controls.Add(self.browseCommandExecButton)
		self.customCommandPartsGroupBox.Controls.Add(self.commandExecutableTextbox)
		self.customCommandPartsGroupBox.Controls.Add(self.commandArgumentsLabel)
		self.customCommandPartsGroupBox.Controls.Add(self.commandArgumentsTextbox)
		self.customCommandPartsGroupBox.Controls.Add(self.commandExecutableLabel)
		self.customCommandPartsGroupBox.Location = System.Drawing.Point(6, 186)
		self.customCommandPartsGroupBox.Name = "customCommandPartsGroupBox"
		self.customCommandPartsGroupBox.Size = System.Drawing.Size(538, 99)
		self.customCommandPartsGroupBox.TabIndex = 13
		self.customCommandPartsGroupBox.Text = lang.enUs("command")
		#
		# commandExecutableLabel
		#
		self.commandExecutableLabel.AutoSize = True
		self.commandExecutableLabel.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point)
		self.commandExecutableLabel.Location = System.Drawing.Point(3, 16)
		self.commandExecutableLabel.Name = "commandExecutableLabel"
		self.commandExecutableLabel.Size = System.Drawing.Size(355, 13)
		self.commandExecutableLabel.TabIndex = 14
		self.commandExecutableLabel.Text = lang.enUs("commandExecutableLabel")
		#
		# commandExecutableTextbox
		#
		self.commandExecutableTextbox.Anchor = System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left | System.Windows.Forms.AnchorStyles.Right
		self.commandExecutableTextbox.AutoCompleteMode = System.Windows.Forms.AutoCompleteMode.Suggest
		self.commandExecutableTextbox.AutoCompleteSource = System.Windows.Forms.AutoCompleteSource.FileSystem
		self.commandExecutableTextbox.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point)
		self.commandExecutableTextbox.Location = System.Drawing.Point(6, 32)
		self.commandExecutableTextbox.Name = "commandExecutableTextbox"
		self.commandExecutableTextbox.Size = System.Drawing.Size(445, 20)
		self.commandExecutableTextbox.TabIndex = 15
		self.commandExecutableTextbox.TextChanged += System.EventHandler(self.handleCommandExecutableTextboxTextChanged)
		self.commandExecutableTextbox.Text = str(self.settings.get("customExec"))
		#
		# openCommandExecDialog
		#
		self.openCommandExecDialog.FileName = "openFileDialog1"
		self.openCommandExecDialog.InitialDirectory = self.ocf4cr.rootDirectory.ToString()
		self.openCommandExecDialog.FileOk += System.ComponentModel.CancelEventHandler(self.handleOpenCommandExecDialogFileOk)
		self.openCommandExecDialog.Filter = lang.enUs("openCommandExecDialogFilter")
		self.openCommandExecDialog.FilterIndex = 6
		self.openCommandExecDialog.Multiselect = False
		#
		# browseCommandExecButton
		#
		self.browseCommandExecButton.Location = System.Drawing.Point(457, 30)
		self.browseCommandExecButton.Name = "browseCommandExecButton"
		self.browseCommandExecButton.Size = System.Drawing.Size(75, 23)
		self.browseCommandExecButton.TabIndex = 16
		self.browseCommandExecButton.Text = lang.enUs("browseDotDotDot")
		self.browseCommandExecButton.UseVisualStyleBackColor = True
		self.browseCommandExecButton.Click += System.EventHandler(self.handleBrowseCommandExecButtonClick)
		#
		# commandArgumentsLabel
		#
		self.commandArgumentsLabel.AutoSize = True
		self.commandArgumentsLabel.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point)
		self.commandArgumentsLabel.Location = System.Drawing.Point(3, 55)
		self.commandArgumentsLabel.Name = "commandArgumentsLabel"
		self.commandArgumentsLabel.Size = System.Drawing.Size(371, 13)
		self.commandArgumentsLabel.TabIndex = 17
		self.commandArgumentsLabel.Text = lang.enUs("commandArgumentsLabel")
		#
		# commandArgumentsTextbox
		#
		self.commandArgumentsTextbox.Anchor = System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left | System.Windows.Forms.AnchorStyles.Right
		self.commandArgumentsTextbox.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point)
		self.commandArgumentsTextbox.Location = System.Drawing.Point(6, 71)
		self.commandArgumentsTextbox.Name = "commandArgumentsTextbox"
		self.commandArgumentsTextbox.Size = System.Drawing.Size(526, 20)
		self.commandArgumentsTextbox.TabIndex = 18
		self.commandArgumentsTextbox.TextChanged += System.EventHandler(self.handleCommandArgumentsTextboxTextChanged)
		self.commandArgumentsTextbox.Text = str(self.settings.get("customArgs"))
		##
		## saveButton
		##
		self.saveButton.Anchor = System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left | System.Windows.Forms.AnchorStyles.Right
		self.saveButton.Enabled = False
		self.saveButton.Location = System.Drawing.Point(10, 508)
		self.saveButton.Name = "saveButton"
		self.saveButton.Size = System.Drawing.Size(555, 24)
		self.saveButton.TabIndex = 19
		self.saveButton.Text = lang.enUs("save")
		self.saveButton.UseVisualStyleBackColor = True
		self.saveButton.Click += System.EventHandler(self.handleSaveButtonClick)
		##
		## defaultsButton
		##
		self.defaultsButton.Anchor = System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left | System.Windows.Forms.AnchorStyles.Right
		self.defaultsButton.Enabled = False
		self.defaultsButton.Location = System.Drawing.Point(10, 537)
		self.defaultsButton.Name = "defaultsButton"
		self.defaultsButton.Size = System.Drawing.Size(555, 24)
		self.defaultsButton.TabIndex = 20
		self.defaultsButton.Text = lang.enUs("defaults")
		self.defaultsButton.UseVisualStyleBackColor = True
		self.defaultsButton.Click += System.EventHandler(self.handleDefaultsButtonClick)
		##
		## cancelButton
		##
		self.defaultsButton.Anchor = System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left | System.Windows.Forms.AnchorStyles.Right
		self.cancelButton.DialogResult = System.Windows.Forms.DialogResult.Cancel
		self.cancelButton.Location = System.Drawing.Point(10, 566)
		self.cancelButton.Name = "settingsCancelButton"
		self.cancelButton.Size = System.Drawing.Size(555, 24)
		self.cancelButton.TabIndex = 21
		self.cancelButton.Text = lang.enUs("cancel")
		self.cancelButton.UseVisualStyleBackColor = True
		self.cancelButton.Click += System.EventHandler(self.handleCancelButtonClick)
		##
		## SettingsForm
		##
		self.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
		self.CancelButton = self.cancelButton
		self.Size = System.Drawing.Size(590, 640)
		self.Controls.Add(self.generalGroupBox)
		self.Controls.Add(self.saveButton)
		self.Controls.Add(self.defaultsButton)
		self.Controls.Add(self.cancelButton)
		self.Controls.Add(self.explorerExeGroupBox)
		self.Controls.Add(self.customCommandGroupBox)
		self.Icon = self.ocf4cr.windowIconResource
		self.MaximizeBox = False
		self.MaximumSize = System.Drawing.Size(3000, 640)
		self.MinimizeBox = False
		self.MinimumSize = System.Drawing.Size(590, 640)
		self.Name = "SettingsForm"
		self.ShowInTaskbar = True
		self.Margin = Padding(0, 0, 0, 0)
		self.Padding = Padding(0, 0, 0, 0)
		self.Text = lang.enUs("windowTitleSettings")
		self.multipleGroupBox.ResumeLayout(False)
		self.multipleGroupBox.PerformLayout()
		self.generalGroupBox.ResumeLayout(False)
		self.generalGroupBox.PerformLayout()
		self.customCommandGroupBox.ResumeLayout(False)
		self.customCommandGroupBox.PerformLayout()
		self.customCommandPartsGroupBox.ResumeLayout(False)
		self.customCommandPartsGroupBox.PerformLayout()
		self.explorerExeGroupBox.ResumeLayout(False)
		self.explorerExeGroupBox.PerformLayout()
		self.CenterToScreen()
		self.ResumeLayout(False)
		self.PerformLayout()
