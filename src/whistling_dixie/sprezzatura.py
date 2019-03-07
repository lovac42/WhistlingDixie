# -*- coding: utf-8 -*-
# Copyright: (C) 2019 Lovac42
# Support: https://github.com/lovac42/WhistlingDixie
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html


import copy
import aqt
from aqt.qt import *
from aqt import mw
from aqt.utils import showInfo, showWarning
from anki.utils import intTime
from anki.hooks import addHook
from .config import *
from .const import *


class Dixie():
    loaded=None
    card=None
    lastId=0


    def __init__(self):
        self.conf=Config(ADDON_NAME)
        addHook(ADDON_NAME+".configLoaded", self.onConfigLoaded)
        addHook('beforeStateChange', self.onBeforeStateChange)


    def onBeforeStateChange(self, newS, oldS, *args):
        self.card=None #clear


    def onConfigLoaded(self):
        if not self.loaded:
            self.setupMenu()
            self.loaded=True


    def setupMenu(self):
        menu=None
        for a in mw.form.menubar.actions():
            if '&Study' == a.text():
                menu=a.menu()
                # menu.addSeparator()
                break
        if not menu:
            menu=mw.form.menubar.addMenu('&Study')

        self.state=QAction("Whistle Dixie: Redo Failed Cards", mw)
        self.state.setCheckable(True)
        self.state.triggered.connect(self.showWarning)
        menu.addAction(self.state)


    def showWarning(self):
        if self.state.isChecked():
            showInfo("""Warning! Whistling Dixie is a dangerous addon that may not be compatible with other addons. Even if they are compatible now, it does not guarantee that it will always be compatible. Please backup/export your database first to prevent unknown addon conflict(s).""")


    def whistle(self, card, ease):
        FG=self.conf.get('failed_grade',1)
        if self.state.isChecked() and ease<=FG:
            if self.conf.get('do_all_cards',False) or \
            (card.type in self.conf.get('do_type',(0,1,2,3)) and \
             card.queue in self.conf.get('do_queue',(2,3))):

                def nullFn():
                    showWarning("Something tried to modifiy the phantom card!")

                #make copy of card and note
                self.card=copy.copy(card)
                self.card.id=self.lastId=intTime(1000)
                note=self.card._note=copy.copy(card.note())
                self.card.nid=self.card._note.id=intTime(1000)+1

                #prevent mods to phantom card
                self.card.flush=nullFn
                self.card.flushSched=nullFn
                note._postFlush=nullFn
                note._preFlush=nullFn
                note.flush=nullFn

