# -*- coding: utf-8 -*-
import os

import wx
from firstpage import FTpage
from Mypage import MYpage
from recommendpage import RCpage
cwd = os.getcwd()

class FXNoteBook(wx.Notebook):

    def __init__(self, parent, id):
        wx.Notebook.__init__(self, parent, id, style=wx.NB_FIXEDWIDTH)

        self.panels = []

        ############################################################
        self.txPanel = FTpage(self, -1)
        self.panels.append(self.txPanel)
        self.AddPage(self.panels[0], u"首页")
        ############################################################
        self.rcPanel = RCpage(self, -1)
        self.panels.append(self.rcPanel)
        self.AddPage(self.panels[1], u"推荐")
        ############################################################
        self.myPanel = MYpage(self, -1)
        self.panels.append(self.myPanel)
        self.AddPage(self.panels[2], u"账号")

    ############################################################

