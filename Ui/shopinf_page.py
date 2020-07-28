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

from datebase import PyMySQL
from item_page import ITDialog

cwd = os.getcwd()
#print(cwd[0:18])
###########################################################################
class SIDialog(wx.Dialog):
    def __init__(self,parent,title,id,value):
        wx.Dialog.__init__(self, parent,title, id, size=(500, 600))
        self.value=value

        self.list = [('',''),('',''),('',''),('',''),('',''),('','')]
        self.initdb()
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer8 = wx.BoxSizer(wx.VERTICAL)

        bSizer9 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_bpButton9 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap(cwd + "\\images\\购物.png"), wx.DefaultPosition, wx.DefaultSize,
                                           wx.BU_AUTODRAW)
        self.m_bpButton9.SetBackgroundColour("white")
        bSizer9.Add(self.m_bpButton9, 1, wx.ALL | wx.EXPAND, 5)

        self.m_staticText17 = wx.StaticText(self, wx.ID_ANY, self.value+"商铺信息", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText17.Wrap(-1)
        bSizer9.Add(self.m_staticText17, 8, wx.ALL | wx.EXPAND, 5)

        bSizer8.Add(bSizer9, 1, wx.EXPAND, 5)

        bSizer10 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText18 = wx.StaticText(self, wx.ID_ANY, u"商品一览", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText18.Wrap(-1)
        bSizer10.Add(self.m_staticText18, 0, wx.ALL, 5)

        gSizer2 = wx.GridSizer(0, 2, 0, 0)

        self.m_button5 = wx.Button(self, wx.ID_ANY, self.list[0][0]+":"+self.list[0][1], wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button5.SetBackgroundColour("#FF6600")
        self.m_button5.SetForegroundColour("white")
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.m_button5)
        gSizer2.Add(self.m_button5, 0, wx.ALL | wx.EXPAND, 5)

        self.m_button6 = wx.Button(self, wx.ID_ANY, self.list[1][0]+":"+self.list[1][1], wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button6.SetBackgroundColour("#FF6600")
        self.m_button6.SetForegroundColour("white")
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.m_button6)
        gSizer2.Add(self.m_button6, 0, wx.ALL | wx.EXPAND, 5)

        self.m_button7 = wx.Button(self, wx.ID_ANY, self.list[2][0]+":"+self.list[2][1], wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button7.SetBackgroundColour("#FF6600")
        self.m_button7.SetForegroundColour("white")
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.m_button7)
        gSizer2.Add(self.m_button7, 0, wx.ALL | wx.EXPAND, 5)

        self.m_button8 = wx.Button(self, wx.ID_ANY, self.list[3][0]+":"+self.list[3][1], wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button8.SetBackgroundColour("#FF6600")
        self.m_button8.SetForegroundColour("white")
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.m_button8)
        gSizer2.Add(self.m_button8, 0, wx.ALL | wx.EXPAND, 5)

        self.m_button9 = wx.Button(self, wx.ID_ANY, self.list[4][0]+":"+self.list[4][1], wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button9.SetBackgroundColour("#FF6600")
        self.m_button9.SetForegroundColour("white")
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.m_button9)
        gSizer2.Add(self.m_button9, 0, wx.ALL | wx.EXPAND, 5)

        self.m_button10 = wx.Button(self, wx.ID_ANY, self.list[5][0]+":"+self.list[5][1], wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button10.SetBackgroundColour("#FF6600")
        self.m_button10.SetForegroundColour("white")
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.m_button10)
        gSizer2.Add(self.m_button10, 0, wx.ALL | wx.EXPAND, 5)

        bSizer10.Add(gSizer2, 1, wx.EXPAND, 5)

        bSizer8.Add(bSizer10, 7, wx.EXPAND, 5)


        self.SetSizer(bSizer8)
        self.Layout()

        self.Centre(wx.BOTH)
    def OnMenuExit(self, event):
        self.Close()
    def OnCloseWindow(self, event):
        self.Destroy()

    def initdb(self):
        select = 'SELECT  `商品编号`,`商品名称` FROM item_inf  WHERE `所属店铺`=\''+self.value+'\''
        my = PyMySQL(select)
        self.list = my.select_data2(self.list)
       # print(self.list)

    def OnClick(self, event):
        if event.GetEventObject() == self.m_button5:
            print(self.list[0][1])
            item = ITDialog(None, -1, "商品信息", self.list[0][0])
            item.ShowModal()
            item.Destroy()
        elif event.GetEventObject() == self.m_button6:
            item = ITDialog(None, -1, "商品信息", self.list[1][0])
            item.ShowModal()
            item.Destroy()
        elif event.GetEventObject() == self.m_button7:
            item = ITDialog(None, -1, "商品信息", self.list[2][0])
            item.ShowModal()
            item.Destroy()
        elif event.GetEventObject() == self.m_button8:
            item = ITDialog(None, -1, "商品信息", self.list[3][0])
            item.ShowModal()
            item.Destroy()
        elif event.GetEventObject() == self.m_button9:
            item = ITDialog(None, -1, "商品信息", self.list[4][0])
            item.ShowModal()
            item.Destroy()
        elif event.GetEventObject() == self.m_button10:
            item = ITDialog(None, -1, "商品信息", self.list[5][0])
            item.ShowModal()
            item.Destroy()
        else:
            print("No Button is clicked")
