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

cwd = os.getcwd()
#print(cwd[0:18])
###########################################################################
class SIDialog(wx.Dialog):
    def __init__(self,parent,id):
        wx.Dialog.__init__(self, parent, id, size=(500, 600))
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer8 = wx.BoxSizer(wx.VERTICAL)

        bSizer9 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_bpButton9 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap(cwd + "\\images\\购物.png"), wx.DefaultPosition, wx.DefaultSize,
                                           wx.BU_AUTODRAW)
        bSizer9.Add(self.m_bpButton9, 1, wx.ALL | wx.EXPAND, 5)

        self.m_staticText17 = wx.StaticText(self, wx.ID_ANY, u"商铺信息", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText17.Wrap(-1)
        bSizer9.Add(self.m_staticText17, 8, wx.ALL | wx.EXPAND, 5)

        bSizer8.Add(bSizer9, 1, wx.EXPAND, 5)

        bSizer10 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText18 = wx.StaticText(self, wx.ID_ANY, u"商品一览", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText18.Wrap(-1)
        bSizer10.Add(self.m_staticText18, 0, wx.ALL, 5)

        gSizer2 = wx.GridSizer(0, 2, 0, 0)

        self.m_button5 = wx.Button(self, wx.ID_ANY, u"商品1", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer2.Add(self.m_button5, 0, wx.ALL | wx.EXPAND, 5)

        self.m_button6 = wx.Button(self, wx.ID_ANY, u"商品2", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer2.Add(self.m_button6, 0, wx.ALL | wx.EXPAND, 5)

        self.m_button7 = wx.Button(self, wx.ID_ANY, u"商品3", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer2.Add(self.m_button7, 0, wx.ALL | wx.EXPAND, 5)

        self.m_button8 = wx.Button(self, wx.ID_ANY, u"商品4", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer2.Add(self.m_button8, 0, wx.ALL | wx.EXPAND, 5)

        self.m_button9 = wx.Button(self, wx.ID_ANY, u"商品5", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer2.Add(self.m_button9, 0, wx.ALL | wx.EXPAND, 5)

        self.m_button10 = wx.Button(self, wx.ID_ANY, u"商品6", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer2.Add(self.m_button10, 0, wx.ALL | wx.EXPAND, 5)

        bSizer10.Add(gSizer2, 1, wx.EXPAND, 5)

        bSizer8.Add(bSizer10, 4, wx.EXPAND, 5)

        bSizer11 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText19 = wx.StaticText(self, wx.ID_ANY, u"评价一览", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText19.Wrap(-1)
        bSizer11.Add(self.m_staticText19, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText20 = wx.StaticText(self, wx.ID_ANY, u"评价1", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText20.Wrap(-1)
        bSizer11.Add(self.m_staticText20, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText21 = wx.StaticText(self, wx.ID_ANY, u"评价2", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText21.Wrap(-1)
        bSizer11.Add(self.m_staticText21, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText22 = wx.StaticText(self, wx.ID_ANY, u"评价3", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText22.Wrap(-1)
        bSizer11.Add(self.m_staticText22, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText23 = wx.StaticText(self, wx.ID_ANY, u"评价4", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText23.Wrap(-1)
        bSizer11.Add(self.m_staticText23, 0, wx.ALL | wx.EXPAND, 5)

        bSizer8.Add(bSizer11, 4, wx.EXPAND, 5)

        self.SetSizer(bSizer8)
        self.Layout()

        self.Centre(wx.BOTH)
    def OnMenuExit(self, event):
        self.Close()
    def OnCloseWindow(self, event):
        self.Destroy()
