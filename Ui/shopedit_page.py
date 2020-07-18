# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################
import os

import wx
import wx.xrc
cwd=os.getcwd()
###########################################################################
class SPpage(wx.Panel):
    def __init__(self,parent,id):
        wx.Panel.__init__(self,parent,id)
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer12 = wx.BoxSizer(wx.VERTICAL)

        bSizer13 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText24 = wx.StaticText(self, wx.ID_ANY, u"商铺", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText24.Wrap(-1)
        bSizer13.Add(self.m_staticText24, 1, wx.ALL | wx.EXPAND, 5)

        bSizer12.Add(bSizer13, 1, wx.EXPAND, 5)

        bSizer14 = wx.BoxSizer(wx.HORIZONTAL)

        gSizer3 = wx.GridSizer(0, 2, 0, 0)

        self.m_bpButton10 = wx.BitmapButton(self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize,
                                            wx.BU_AUTODRAW)
        gSizer3.Add(self.m_bpButton10, 0, wx.ALL, 5)

        self.m_bpButton11 = wx.BitmapButton(self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize,
                                            wx.BU_AUTODRAW)
        gSizer3.Add(self.m_bpButton11, 0, wx.ALL, 5)

        self.m_bpButton12 = wx.BitmapButton(self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize,
                                            wx.BU_AUTODRAW)
        gSizer3.Add(self.m_bpButton12, 0, wx.ALL, 5)

        self.m_bpButton13 = wx.BitmapButton(self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize,
                                            wx.BU_AUTODRAW)
        gSizer3.Add(self.m_bpButton13, 0, wx.ALL, 5)

        self.m_bpButton14 = wx.BitmapButton(self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize,
                                            wx.BU_AUTODRAW)
        gSizer3.Add(self.m_bpButton14, 0, wx.ALL, 5)

        self.m_bpButton15 = wx.BitmapButton(self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize,
                                            wx.BU_AUTODRAW)
        gSizer3.Add(self.m_bpButton15, 0, wx.ALL, 5)

        self.m_bpButton16 = wx.BitmapButton(self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize,
                                            wx.BU_AUTODRAW)
        gSizer3.Add(self.m_bpButton16, 0, wx.ALL, 5)

        self.m_bpButton17 = wx.BitmapButton(self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize,
                                            wx.BU_AUTODRAW)
        gSizer3.Add(self.m_bpButton17, 0, wx.ALL, 5)

        bSizer14.Add(gSizer3, 4, wx.EXPAND, 5)

        bSizer17 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText25 = wx.StaticText(self, wx.ID_ANY, u"管理", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText25.Wrap(-1)
        bSizer17.Add(self.m_staticText25, 0, wx.ALL | wx.EXPAND, 5)

        self.m_button11 = wx.Button(self, wx.ID_ANY, u"删除", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer17.Add(self.m_button11, 0, wx.ALL, 5)

        self.m_button12 = wx.Button(self, wx.ID_ANY, u"修改数量", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer17.Add(self.m_button12, 0, wx.ALL, 5)

        bSizer14.Add(bSizer17, 4, wx.EXPAND, 5)

        bSizer12.Add(bSizer14, 4, wx.EXPAND, 5)

        gSizer4 = wx.GridSizer(0, 2, 0, 0)

        self.m_staticText28 = wx.StaticText(self, wx.ID_ANY, u"增加修改商品", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText28.Wrap(-1)
        gSizer4.Add(self.m_staticText28, 0, wx.ALL, 5)

        self.m_staticText33 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText33.Wrap(-1)
        gSizer4.Add(self.m_staticText33, 0, wx.ALL, 5)

        self.m_bpButton18 = wx.BitmapButton(self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize,
                                            wx.BU_AUTODRAW)
        gSizer4.Add(self.m_bpButton18, 0, wx.ALL, 5)

        self.m_staticText35 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText35.Wrap(-1)
        gSizer4.Add(self.m_staticText35, 0, wx.ALL, 5)

        self.m_staticText29 = wx.StaticText(self, wx.ID_ANY, u"商品名", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText29.Wrap(-1)
        gSizer4.Add(self.m_staticText29, 0, wx.ALL, 5)

        self.m_textCtrl3 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer4.Add(self.m_textCtrl3, 0, wx.ALL, 5)

        self.m_staticText30 = wx.StaticText(self, wx.ID_ANY, u"商品数量", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText30.Wrap(-1)
        gSizer4.Add(self.m_staticText30, 0, wx.ALL, 5)

        self.m_textCtrl4 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer4.Add(self.m_textCtrl4, 0, wx.ALL, 5)

        self.m_staticText31 = wx.StaticText(self, wx.ID_ANY, u"商品价格", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText31.Wrap(-1)
        gSizer4.Add(self.m_staticText31, 0, wx.ALL, 5)

        self.m_textCtrl5 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer4.Add(self.m_textCtrl5, 0, wx.ALL, 5)

        bSizer12.Add(gSizer4, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer12)
        self.Layout()

        self.Centre(wx.BOTH)
