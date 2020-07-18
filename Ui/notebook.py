# -*- coding: utf-8 -*-
import os

import wx
from firstpage import FTpage
from shopedit_page import SPpage
from Mypage import MYpage
cwd = os.getcwd()

class FXNoteBook(wx.Notebook):
    def __init__(self, parent, id):
        wx.Notebook.__init__(self, parent, id)

        self.panels = []

        ############################################################
        self.txPanel = FTpage(self, -1)
        self.panels.append(self.txPanel)
        self.AddPage(self.panels[0], u"首页")
        ############################################################
        self.testPanel = SPpage(self, -1)
        self.panels.append(self.testPanel)
        self.AddPage(self.panels[1], u"我的商铺")
        ############################################################
        self.myPanel = MYpage(self, -1)
        self.panels.append(self.myPanel)
        self.AddPage(self.panels[2], u"账号")

    ############################################################

