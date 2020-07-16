# -*- coding: utf-8 -*-

import wx
from firstpage import FTpage
from shopedit_page import SPpage
from Mypage import MYpage
from search_page import SEpage
from shopinf_page import SIpage
from item_page import ITpage

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
        self.itemPanel = ITpage(self, -1)
        self.panels.append(self.itemPanel)
        self.AddPage(self.panels[3], u"商品")
        ############################################################
        self.siPanel = SIpage(self, -1)
        self.panels.append(self.siPanel)
        self.AddPage(self.panels[4], u"商铺")
        ############################################################
        self.sePanel = SEpage(self, -1)
        self.panels.append(self.sePanel)
        self.AddPage(self.panels[5], u"搜索")
    ############################################################