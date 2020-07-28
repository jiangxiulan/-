# -*- coding: utf-8 -*-

###########################################################################

import wx
import wx.xrc
import os

from datebase import PyMySQL
from item_page import ITDialog
from search_page import SEDialog
from shopinf_page import SIDialog

cwd = os.getcwd()
###########################################################################




class FTpage(wx.Panel):
    def __init__(self,parent,id):
        wx.Panel.__init__(self,parent,id)
        #self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBack)
        self.list = [('',''),('',''),('',''),('',''),('','')]
        self.list2 = [('',''),('',''),('',''),('',''),('','')]
        self.initdb()
        self.value=""


        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        bSizer2 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button1 = wx.Button(self, wx.ID_ANY, u"搜索", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button1.SetBackgroundColour("#FF6600")
        self.m_button1.SetForegroundColour("white")
        bSizer2.Add(self.m_button1, 0, wx.ALL | wx.EXPAND, 5)
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.m_button1)

        self.m_textCtrl1 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.m_textCtrl1, 1, wx.ALL | wx.EXPAND, 5)

        bSizer1.Add(bSizer2, 1, wx.EXPAND, 5)

        gSizer1 = wx.GridSizer(0, 2, 0, 0)

        self.m_staticText20 = wx.StaticText(self, wx.ID_ANY, u"商品推荐页", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText20.Wrap(-1)
        gSizer1.Add(self.m_staticText20, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText21 = wx.StaticText(self, wx.ID_ANY, u"店铺推荐页", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText21.Wrap(-1)
        gSizer1.Add(self.m_staticText21, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_button2 = wx.Button(self, wx.ID_ANY, self.list[0][1]+":"+self.list[0][0], wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button2.SetBackgroundColour("#FF6600")
        self.m_button2.SetForegroundColour("white")
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.m_button2)
        gSizer1.Add(self.m_button2, 0, wx.ALL |  wx.EXPAND, 5)

        self.m_button3 = wx.Button(self, wx.ID_ANY, self.list2[0][1]+":"+self.list2[0][0], wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button3.SetBackgroundColour("#FF6600")
        self.m_button3.SetForegroundColour("white")
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.m_button3)
        gSizer1.Add(self.m_button3, 0, wx.ALL |  wx.EXPAND, 5)

        self.m_button4 = wx.Button(self, wx.ID_ANY, self.list[1][1]+":"+self.list[1][0], wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button4.SetBackgroundColour("#FF6600")
        self.m_button4.SetForegroundColour("white")
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.m_button4)
        gSizer1.Add(self.m_button4, 0, wx.ALL | wx.EXPAND, 5)

        self.m_button5 = wx.Button(self, wx.ID_ANY, self.list2[1][1]+":"+self.list2[1][0], wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button5.SetBackgroundColour("#FF6600")
        self.m_button5.SetForegroundColour("white")
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.m_button5)
        gSizer1.Add(self.m_button5, 0, wx.ALL |  wx.EXPAND, 5)

        self.m_button6 = wx.Button(self, wx.ID_ANY, self.list[2][1]+":"+self.list[2][0], wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button6.SetBackgroundColour("#FF6600")
        self.m_button6.SetForegroundColour("white")
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.m_button6)
        gSizer1.Add(self.m_button6, 0, wx.ALL |  wx.EXPAND, 5)

        self.m_button7 = wx.Button(self, wx.ID_ANY, self.list2[2][1]+":"+self.list2[2][0], wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button7.SetBackgroundColour("#FF6600")
        self.m_button7.SetForegroundColour("white")
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.m_button7)
        gSizer1.Add(self.m_button7, 0, wx.ALL | wx.EXPAND, 5)

        self.m_button8 = wx.Button(self, wx.ID_ANY, self.list[3][1]+":"+self.list[3][0], wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button8.SetBackgroundColour("#FF6600")
        self.m_button8.SetForegroundColour("white")
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.m_button8)
        gSizer1.Add(self.m_button8, 0, wx.ALL |  wx.EXPAND, 5)

        self.m_button9 = wx.Button(self, wx.ID_ANY, self.list2[3][1]+":"+self.list2[3][0], wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button9.SetBackgroundColour("#FF6600")
        self.m_button9.SetForegroundColour("white")
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.m_button9)
        gSizer1.Add(self.m_button9, 0, wx.ALL |  wx.EXPAND, 5)

        self.m_button10 = wx.Button(self, wx.ID_ANY, self.list[4][1]+":"+self.list[4][0], wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button10.SetBackgroundColour("#FF6600")
        self.m_button10.SetForegroundColour("white")
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.m_button10)
        gSizer1.Add(self.m_button10, 0, wx.ALL |  wx.EXPAND, 5)

        self.m_button11 = wx.Button(self, wx.ID_ANY, self.list2[4][1]+":"+self.list2[4][0], wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button11.SetBackgroundColour("#FF6600")
        self.m_button11.SetForegroundColour("white")
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.m_button11)
        gSizer1.Add(self.m_button11, 0, wx.ALL | wx.EXPAND, 5)

        bSizer1.Add(gSizer1, 10, wx.EXPAND, 5)

        sbSizer3 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"广告页"), wx.VERTICAL)

        bSizer1.Add(sbSizer3, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

    def initdb(self):
        select = 'SELECT  `商品名称`,`商品编号` FROM item_inf  order by `评价` DESC LIMIT 5'
        my = PyMySQL(select)
        self.list = my.select_data2(self.list)
        #print(self.list)

        select2 = 'SELECT  `店铺名称`,`店铺编号` FROM shop_info   LIMIT 5'
        my2 = PyMySQL(select2)
        self.list2 = my2.select_data2(self.list2)
        #print(self.list2)
    def GetValue0(self):
        return self.m_textCtrl1.GetValue()

    def OnClick(self, event):
        if event.GetEventObject() == self.m_button1:
            item = SEDialog(None,-1, "搜索",self.GetValue0())
            item.ShowModal()
            item.Destroy()
        elif event.GetEventObject() == self.m_button2:
            item = ITDialog(None, -1,"商品信息",self.list[0][1])
            #item.getValue(self.list[0][1])
            item.ShowModal()
            item.Destroy()
        elif event.GetEventObject() == self.m_button3:
            item=SIDialog(None,-1,"店铺信息",self.list2[0][1])
            #item.getValue(self.list2[0][1])
            item.ShowModal()
            item.Destroy()
        elif event.GetEventObject() == self.m_button4:
            item = ITDialog(None, -1,"商品信息",self.list[1][1])
            #item.getValue(self.list[1][1])
            item.ShowModal()
            item.Destroy()
        elif event.GetEventObject() == self.m_button5:
            item = SIDialog(None, -1,"店铺信息",self.list2[1][1])
            #item.getValue(self.list2[1][1])
            item.ShowModal()
            item.Destroy()
        elif event.GetEventObject() == self.m_button6:
            item = ITDialog(None, -1,"商品信息",self.list[2][1])
            #item.getValue(self.list[2][1])
            item.ShowModal()
            item.Destroy()
        elif event.GetEventObject() == self.m_button7:
            item = SIDialog(None, -1,"店铺信息",self.list2[2][1])
            #item.getValue(self.list2[2][1])
            item.ShowModal()
            item.Destroy()
        elif event.GetEventObject() == self.m_button8:
            item = ITDialog(None, -1,"商品信息",self.list[3][1])
            #item.getValue(self.list[3][1])
            item.ShowModal()
            item.Destroy()
        elif event.GetEventObject() == self.m_button9:
            item = SIDialog(None, -1,"店铺信息",self.list2[3][1])
            #item.getValue(self.list2[3][1])
            item.ShowModal()
            item.Destroy()
        elif event.GetEventObject() == self.m_button10:
            item = ITDialog(None, -1,"商品信息",self.list[4][1])
           # item.getValue(self.list[4][1])
            item.ShowModal()
            item.Destroy()
        elif event.GetEventObject() == self.m_button11:
            item = SIDialog(None, -1,"店铺信息",self.list2[4][1])
            #item.getValue(self.list2[4][1])
            item.ShowModal()
            item.Destroy()
        else:


            print("No Button is clicked")



    #
    # def Onclick_1(self,event):
    #     item=ITDialog(None,-1)
    #     item.getValue(self.value)
    #     item.ShowModal()
    #     item.Destroy()
    #
    # def Onclick_2(self,event):
    #     item=SIDialog(None,-1)
    #     item.ShowModal()
    #     item.Destroy()
    #
    # def Onclick(self, event):
    #     item = SEDialog(None, -1)
    #     item.ShowModal()
    #     item.Destroy()

