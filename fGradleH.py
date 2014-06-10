﻿from __future__ import print_function


import pythonHelper
import colorama

from collections import OrderedDict
from src import setupForge, nothingToSeeHereReallyNopeSoEmptyAndNothingness, config, setupBuild, buildMod, landscape, \
    title

__author__ = 'SanAndreasP'


colorama.init()
config.read_config()

menuItm = dict()
menuItm["0"] = exit
menuItm["1"] = setupForge.call
menuItm["2"] = setupBuild.call
menuItm["3"] = buildMod.call
menuItm["4"] = landscape.call
menuItm["5"] = nothingToSeeHereReallyNopeSoEmptyAndNothingness.call

menuTxt = OrderedDict()
menuTxt["1"] = "setup forge"
menuTxt["2"] = "setup mod building"
menuTxt["3"] = "build mod"
menuTxt["0"] = "exit"


def mainmenu():
    global menuItm, menuTxt
    title.show()
    choice = pythonHelper.printmenu_and_getchoice("Menu:", menuTxt, "Please choose an item from above")
    menuItm[choice]()

while True:
    mainmenu()
    if not pythonHelper.get_yesno_input("Continue working?"):
        break

colorama.deinit()
config.write_config()