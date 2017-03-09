# OpenContainingFolder4CR.py
# A plugin script for ComicRack
# (c) 2017 Bryn Mosher (BadMonkey0001)
# GPL v3 License
################################################################################

import clr
from ocf4cr import ocf4cr

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

