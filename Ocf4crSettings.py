# Ocf4crSettings.py
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
clr.AddReference("PresentationFramework")
clr.AddReference("PresentationCore")

from System.Diagnostics import Process
import System.Windows.Forms
from System.Windows.Forms import *
from System.IO import *

from Ocf4crLang import lang

class Ocf4crSettings:
	activeSettings = {}
	defaultSettings = {
		"maxWindows": [8, int],
		"ignoreMultiSelected": [False, bool],
		"enableMultiWinForMultiSelected": [True, bool],
		"onlyUseFirstDir": [False, bool],
		"explorerSeparateProcess": [True, bool],
		"enableCustomCommand": [False, bool],
		"customExec": ["", str],
		"customArgs": ["", str],
	}
	defaultValues = {}
	settingsFileContents = None

	def __init__(self, ocf4cr):
		self.ocf4cr = ocf4cr
		self.settingsPath = Path.Combine(self.ocf4cr.rootScriptDirectory, "OCF4C_settings.dat")
		for setting, config in self.defaultSettings.items():
			self.defaultValues[setting] = config[0]
		self.loadSettingsFromFile()

	def activeAreDefaults(self):
		print 'cmp(self.activeSettings, self.defaultValues)'+str(cmp(self.activeSettings, self.defaultValues))
		return cmp(self.activeSettings, self.defaultValues) == 0

	def givenAreActive(self, settingsDict):
		return cmp(settingsDict, self.activeSettings) == 0

	def givenAreDefaults(self, settingsDict):
		return cmp(settingsDict, self.defaultValues) == 0

	def get(self, setting):
		if self.activeSettings.has_key(setting):
			return self.activeSettings[setting]

		return None

	def getAll(self):
		return dict(self.activeSettings)

	def getDefaults(self):
		parsed = {}
		for setting, config in self.defaultSettings.items():
			parsed[setting] = config[1](config[0])
		return parsed

	def loadDefaultSettings(self):
		self.ocf4cr.dbg("Loading default settings")
		for setting, config in self.defaultSettings.items():
			self.activeSettings[setting] = config[0]
		return self.activeSettings

	def loadSettingsFromFile(self):
		self.ocf4cr.dbg("Loading settings")
		self.loadDefaultSettings()
		settingsFileInfo = self.loadSettingsFileInfo()

		if not settingsFileInfo:
			self.ocf4cr.dbg("Saving fresh settings file")
			self.saveSettingsFile()
			return

		try:
			self.settingsFileContents = list(File.ReadAllLines(self.settingsPath))

			for idx, aLine in enumerate(self.settingsFileContents):
				if not re.search(self.ocf4cr.rgxAllWhitespaceOrEmptyOrComment, aLine):
					matches = re.findall(self.ocf4cr.rgxMatchASetting, aLine)
					if matches:
						setting = matches[0][1]
						self.ocf4cr.dbg("Found setting line matching \""+setting+"="+str(matches[0][4])+"\"")
						if self.set(setting, matches[0][4]):
							self.settingsFileContents[idx] = str(setting)+"="+str(self.activeSettings[setting])
							if len(self.defaultSettings[setting]) < 3:
								self.defaultSettings[setting].append(idx)
							else:
								self.defaultSettings[setting][2] = idx
					else:
						self.ocf4cr.warn("Something weird happened for setting found in file "+str(matches))

				else:
					self.ocf4cr.dbg("Skipping settings file line \""+aLine+"\"")
		except:
			errType, errValue, errTrace = sys.exc_info()
			MessageBox.Show(lang.enUs("failedLoadingSettings")+"\n"+str(errType)+"\n"+str(errValue)+"\n"+str(errTrace), lang.enUs("windowTitle"), MessageBoxButtons.OK, MessageBoxIcon.Warning)

	def loadSettingsFileInfo(self):
		settingsFileInfo = FileInfo(self.settingsPath)

		if not settingsFileInfo.Exists:
			return False

		return settingsFileInfo

	def saveSettingsFile(self):
		try:
			# I tried preserving the config while automating saving... therein lies the rub. :/
			#if self.settingsFileContents:
			#	stringsToWrite = list(self.settingsFileContents)
			#	#for setting, value in self.activeSettings.items():
			#	#	stringsToWrite.append(str(setting)+"="+str(value))
			#else:
			stringsToWrite = [
				"################################################################################",
				"# Open Containing Folder for ComicRack Settings",
				"################################################################################",
				"# If you wish to comment out a setting, you can use a pound mark (\"#\") at the",
				"# beginning of the line. You really should use the UI for these though.",
				"################################################################################",
				"",
			]

			for setting, value in self.activeSettings.items():
				stringsToWrite.append(str(setting)+"="+str(value))

			if stringsToWrite[len(stringsToWrite)-1] != "":
				# an empty newline at the end
				stringsToWrite.append("")

			self.ocf4cr.dbg("Writing settings to \""+self.settingsPath+"\"")
			File.WriteAllText(self.settingsPath, "\n".join(stringsToWrite))

			return True
		except:
			errType, errValue, errTrace = sys.exc_info()
			MessageBox.Show(lang.enUs("failedSavingSettings")+"\n"+str(errType)+"\n"+str(errValue)+"\n"+str(errTrace), lang.enUs("windowTitle"), MessageBoxButtons.OK, MessageBoxIcon.Warning)
		return False

	def set(self, setting, value):
		if self.defaultSettings.has_key(setting):
			settingConfig = self.defaultSettings[setting]
			if settingConfig[1] is bool:
				self.activeSettings[setting] = self.ocf4cr.rgxBooleanFalse.match(str(value)) is None
			elif settingConfig[1] is str:
				self.activeSettings[setting] = re.sub(self.ocf4cr.rgxTrimString, '', settingConfig[1](value))
			else:
				self.activeSettings[setting] = settingConfig[1](value)

			if len(self.defaultSettings[setting]) > 2 and type(self.defaultSettings[setting][2]) is int:
				self.settingsFileContents[self.defaultSettings[setting][2]] = setting+"="+str(value)
			else:
				self.settingsFileContents.append(setting+"="+str(value))
				if len(self.defaultSettings[setting]) > 2:
					self.defaultSettings[setting][2] = len(self.settingsFileContents) - 1
				else:
					self.defaultSettings[setting].append(len(self.settingsFileContents) - 1)

			self.ocf4cr.dbg("Setting \""+setting+"\" set to \""+str(self.activeSettings[setting])+"\"")

			return True
		else:
			self.ocf4cr.warn("Setting \""+setting+"\" does not exist")

		return False

	def setAll(self, newSettings):
		if not type(newSettings) is dict:
			self.ocf4cr.warn("Settings passed to setAll() has type of "+str(type(newSettings))+" - dict required")
		for setting in self.defaultSettings:
			if newSettings.has_key(setting):
				self.set(setting, newSettings[setting])
