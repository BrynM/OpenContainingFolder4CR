# Ocf4crLang.py
# A plugin script for ComicRack
# (c) 2017 Bryn Mosher (BadMonkey0001)
# GPL v3 License
################################################################################

class Ocf4crLang:
	languages = {
		"en" : {
			"us": {
				"browseDotDotDot": "Browse...",
				"cancel": "Cancel",
				"command": "Command",
				"commandArgumentsLabel": "Command arguments (\"@path@\" or \"@list\" can be used here - if blank, \"@path@\" will be assumed)",
				"commandExecutableLabel": "Command executable (must exist on disk; i.e. \"C:\\Windows\\explorer.exe\")",
				"customCommandGroupBox": "Custom File Explorer Command",
				"customCommandLabel1": "If you do not wish to use explorer.exe, you can set a custom command line here. A custom command consists of the command executable itself and command arguments.\n\nThere are two \"template variables\" for your command arguments that you can use, however they cannot be used together. They are:",
				"customCommandLabel2": "@path@ The path to a single directory. If multiple directories are found, selected, and opened, your custom command will be called multiple times - once for each directory to be opened.\n\n@list@ If multiple directories are found, selected, and opened, the entire list will be passed to your custom command and it will only be run once.",
				"customCommandNotFound": "Using a custom command is enabled, but the custom command pointed to does not exist on the filesystem. Please select an existing file or turn custom commands off. The file looked for was:",
				"default": "Default",
				"defaultChecked": "Default: on",
				"defaults": "Defaults",
				"defaultPlug": "Default: @value@",
				"defaultUnchecked": "Default: off",
				"enableCustomCommand": "Enable Custom Command",
				"enableMultipleWindows": "Enable opening multiple windows if multiple books are selected",
				"enableOnlyFirstBook": "When multiple books are selected only open the first directory",
				"error": "Error",
				"explorerExe": "explorer.exe",
				"explorerExeSeparate": "Open explorer.exe windows in their own separate process using \"/separate\"",
				"failedCommand": "Could not run explore.exe command!!!",
				"failedLoadingSettings": "Failed loading settings!!!",
				"failedSavingSettings": "Failed saving settings!!!",
				"generalSettings": "General Settings",
				"ignoreMultiple": "Ignore multiple selection - Don\'t open any windows at all",
				"invalidList": "Not a valid list.\n",
				"maxWindowsNotification": "Maximum @maxWindows@ windows will open as applied from settings.",
				"maxWindowsUnlimitedNotification": "No maximum number of windows applied from settings.",
				"maxWinNumericLabel": "Maximum number of windows to open - 0 is unlimited",
				"multipleSelected": "Multiple directories found. Please select the ones you which to open. @maxWindowsNotification@",
				"multipleSelections": "Multiple Selections",
				"multipleWarning": "Warning! This could open many windows at once and may be slow for large numbers of directories. Open multiple at your own risk!",
				"nobooks": "You don't have any books selected.\n\nPlease select at least one book.",
				"nodirs": "Couldn't find any directories.\n\nPlease select at least one book with a file.",
				"openCommandExecDialogFilter": "Executable file (*.exe)|*.exe|PowerShell Script (*.ps1)|*.ps1|Batch file (*.bat)|*.bat|Windows Script Host (*.wsf;*.wsh)|*.wsf;wfh|Bash script (*.sh)|*.sh|All files (*.*)|*.*",
				"openSelected": "Open selected directories",
				"save": "Save",
				"selectAll": "Select All",
				"windowTitle": "Open Containing Folder for ComicRack",
				"windowTitleSettings": "Open Containing Folder for ComicRack Settings",
			},
		},
	}

	def str(self, language, variant, wantString):
		if not language or not wantString:
			return ""

		if language in self.languages:
			if variant is None:
				if wantString in self.languages[language]:
					return self.languages[language][wantString]

			if variant in self.languages[language] and wantString in self.languages[language][variant]:
				return self.languages[language][variant][wantString]

		return "Ocf4crLang.languages."+language+"."+str(variant)+"."+wantString

	def enUs(self, wantString):
		return self.str("en", "us", wantString)

lang = Ocf4crLang()
