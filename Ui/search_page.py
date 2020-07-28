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

cwd=os.getcwd()
###########################################################################
class SEDialog(wx.Dialog):
    def __init__(self,parent,id,title,value0):
        wx.Dialog.__init__(self, parent, id,title ,size=(560, 600))
        self.value0=value0
        self.list = [("","","","","",""),("","","","","",""),("","","","","",""),("","","","","",""),("","","","","","")]
        self.list2=['','','','','']
        self.initdb()
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        bSizer2 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button1 = wx.Button(self, wx.ID_ANY, u"搜索", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button1.SetBackgroundColour("#FF6600")
        self.m_button1.SetForegroundColour("white")
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.m_button1)
        bSizer2.Add(self.m_button1, 0, wx.ALL | wx.EXPAND, 5)

        self.m_textCtrl1 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.m_textCtrl1, 1, wx.ALL | wx.EXPAND, 5)

        bSizer1.Add(bSizer2, 1, wx.EXPAND, 5)

        bSizer7 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button12 = wx.Button(self, wx.ID_ANY, u"价格", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button12.SetBackgroundColour("#FF6600")
        self.m_button12.SetForegroundColour("white")
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.m_button12)
        bSizer7.Add(self.m_button12, 1, wx.ALL, 5)

        self.m_button13 = wx.Button(self, wx.ID_ANY, u"销量", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button13.SetBackgroundColour("#FF6600")
        self.m_button13.SetForegroundColour("white")
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.m_button13)
        bSizer7.Add(self.m_button13, 1, wx.ALL, 5)

        self.m_button14 = wx.Button(self, wx.ID_ANY, u"信用", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button14.SetBackgroundColour("#FF6600")
        self.m_button14.SetForegroundColour("white")
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.m_button14)
        bSizer7.Add(self.m_button14, 1, wx.ALL, 5)

        self.m_button15 = wx.Button(self, wx.ID_ANY, u"综合", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button15.SetBackgroundColour("#FF6600")
        self.m_button15.SetForegroundColour("white")
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.m_button15)
        bSizer7.Add(self.m_button15, 1, wx.ALL, 5)

        bSizer1.Add(bSizer7, 1, wx.EXPAND, 5)

        bSizer9 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer10 = wx.BoxSizer(wx.VERTICAL)

        self.m_bitmap4 = wx.StaticBitmap(self, wx.ID_ANY,wx.Bitmap(cwd+"\\images\\商品.png"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_bitmap4.SetBackgroundColour("white")
        bSizer10.Add(self.m_bitmap4, 1, wx.ALL | wx.EXPAND, 5)

        self.m_bitmap5 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(cwd+"\\images\\商品.png"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_bitmap5.SetBackgroundColour("white")
        bSizer10.Add(self.m_bitmap5, 1, wx.ALL | wx.EXPAND, 5)

        self.m_bitmap6 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(cwd+"\\images\\商品.png"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_bitmap6.SetBackgroundColour("white")
        bSizer10.Add(self.m_bitmap6, 1, wx.ALL | wx.EXPAND, 5)

        self.m_bitmap7 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(cwd+"\\images\\商品.png"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_bitmap7.SetBackgroundColour("white")
        bSizer10.Add(self.m_bitmap7, 1, wx.ALL | wx.EXPAND, 5)

        self.m_bitmap8 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(cwd+"\\images\\商品.png"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_bitmap8.SetBackgroundColour("white")
        bSizer10.Add(self.m_bitmap8, 1, wx.ALL | wx.EXPAND, 5)

        bSizer9.Add(bSizer10, 1, wx.EXPAND, 5)

        bSizer11 = wx.BoxSizer(wx.VERTICAL)

        self.m_button23 = wx.Button(self, wx.ID_ANY, "编号："+self.list[0][0]+",名称："+self.list[0][1]
                                    +"，所属店铺："+self.list[0][2]+",价格："+self.list[0][3]+"，评价："+self.list[0][4]+
                                     "，销量："+self.list[0][5]
        , wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button23.SetBackgroundColour("#FF6600")
        self.m_button23.SetForegroundColour("white")
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.m_button23)
        bSizer11.Add(self.m_button23, 1, wx.ALL | wx.EXPAND, 5)

        self.m_button24 = wx.Button(self, wx.ID_ANY, "编号："+self.list[1][0]+",名称："+self.list[1][1]
                                    +"，所属店铺："+self.list[1][2]+",价格："+self.list[1][3]+"，评价："+self.list[1][4]+
                                     "，销量："+self.list[1][5]
        , wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button24.SetBackgroundColour("#FF6600")
        self.m_button24.SetForegroundColour("white")
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.m_button24)
        bSizer11.Add(self.m_button24, 1, wx.ALL | wx.EXPAND, 5)

        self.m_button25 = wx.Button(self, wx.ID_ANY, "编号："+self.list[2][0]+",名称："+self.list[2][1]
                                    +"，所属店铺："+self.list[2][2]+",价格："+self.list[2][3]+"，评价："+self.list[2][4]+
                                     "，销量："+self.list[2][5]
        , wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button25.SetBackgroundColour("#FF6600")
        self.m_button25.SetForegroundColour("white")
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.m_button25)
        bSizer11.Add(self.m_button25, 1, wx.ALL | wx.EXPAND, 5)

        self.m_button26 = wx.Button(self, wx.ID_ANY, "编号："+self.list[3][0]+",名称："+self.list[3][1]
                                    +"，所属店铺："+self.list[3][2]+",价格："+self.list[3][3]+"，评价："+self.list[3][4]+
                                     "，销量："+self.list[3][5]
        , wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button26.SetBackgroundColour("#FF6600")
        self.m_button26.SetForegroundColour("white")
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.m_button26)
        bSizer11.Add(self.m_button26, 1, wx.ALL | wx.EXPAND, 5)

        self.m_button27 = wx.Button(self, wx.ID_ANY, "编号："+self.list[4][0]+",名称："+self.list[4][1]
                                    +"，所属店铺："+self.list[4][2]+",价格："+self.list[4][3]+"，评价："+self.list[4][4]+
                                     "，销量："+self.list[4][5]
        , wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button27.SetBackgroundColour("#FF6600")
        self.m_button27.SetForegroundColour("white")
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.m_button27)
        bSizer11.Add(self.m_button27, 1, wx.ALL | wx.EXPAND, 5)

        bSizer9.Add(bSizer11, 10, wx.EXPAND, 5)

        bSizer1.Add(bSizer9, 10, wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

    def GetValue1(self):
        return self.m_textCtrl1.GetValue()

    def OnClick(self,event):
        self.list = [("","","","","",""),("","","","","",""),("","","","","",""),("","","","","",""),("","","","","","")]
        if self.GetValue1()!="":
            self.value0=self.GetValue1()
        if event.GetEventObject() == self.m_button1:
            select = 'SELECT * FROM item_inf WHERE `商品名称`=\'' + self.value0 + '\''
            my = PyMySQL(select)
            self.list = my.select_data2(self.list)
           # print(self.list)
            self.m_button23.SetLabel("编号："+self.list[0][0]+",名称："+self.list[0][1]
                                    +"，所属店铺："+self.list[0][2]+",价格："+self.list[0][3]+"，评价："+self.list[0][4]+
                                     "，销量："+self.list[0][5])
            self.list2[0] = self.list[0][0]
            self.list2[1] = self.list[1][0]
            self.list2[2] = self.list[2][0]
            self.list2[3] = self.list[3][0]
            self.list2[4] = self.list[4][0]
            self.m_button24.SetLabel("编号：" + self.list[1][0] + ",名称：" + self.list[1][1]
                                     + "，所属店铺：" + self.list[1][2] + ",价格：" + self.list[1][3] + "，评价：" + self.list[1][4]+
                                     "，销量："+self.list[1][5])
            self.m_button25.SetLabel("编号：" + self.list[2][0] + ",名称：" + self.list[2][1]
                                     + "，所属店铺：" + self.list[2][2] + ",价格：" + self.list[2][3] + "，评价：" + self.list[2][4]+
                                     "，销量："+self.list[2][5])
            self.m_button26.SetLabel("编号：" + self.list[3][0] + ",名称：" + self.list[3][1]
                                     + "，所属店铺：" + self.list[3][2] + ",价格：" + self.list[3][3] + "，评价：" + self.list[3][4]+
                                     "，销量："+self.list[3][5])
            self.m_button27.SetLabel("编号：" + self.list[4][0] + ",名称：" + self.list[4][1]
                                     + "，所属店铺：" + self.list[4][2] + ",价格：" + self.list[4][3] + "，评价：" + self.list[4][4]+
                                     "，销量："+self.list[4][5])
        elif event.GetEventObject() == self.m_button12:
            select = 'SELECT * FROM item_inf WHERE `商品名称`=\'' + self.value0 + '\'ORDER BY `价格` DESC'
            my = PyMySQL(select)
            self.list = my.select_data2(self.list)
            #print(self.list)
            self.list2[0] = self.list[0][0]
            self.list2[1] = self.list[1][0]
            self.list2[2] = self.list[2][0]
            self.list2[3] = self.list[3][0]
            self.list2[4] = self.list[4][0]
            self.m_button23.SetLabel("编号：" + self.list[0][0] + ",名称：" + self.list[0][1]
                                     + "，所属店铺：" + self.list[0][2] + ",价格：" + self.list[0][3] + "，评价：" + self.list[0][4]+
                                     "，销量："+self.list[0][5])
            self.m_button24.SetLabel("编号：" + self.list[1][0] + ",名称：" + self.list[1][1]
                                     + "，所属店铺：" + self.list[1][2] + ",价格：" + self.list[1][3] + "，评价：" + self.list[1][4]+
                                     "，销量："+self.list[1][5])
            self.m_button25.SetLabel("编号：" + self.list[2][0] + ",名称：" + self.list[2][1]
                                     + "，所属店铺：" + self.list[2][2] + ",价格：" + self.list[2][3] + "，评价：" + self.list[2][4]+
                                     "，销量："+self.list[2][5])
            self.m_button26.SetLabel("编号：" + self.list[3][0] + ",名称：" + self.list[3][1]
                                     + "，所属店铺：" + self.list[3][2] + ",价格：" + self.list[3][3] + "，评价：" + self.list[3][4]+
                                     "，销量："+self.list[3][5])
            self.m_button27.SetLabel("编号：" + self.list[4][0] + ",名称：" + self.list[4][1]
                                     + "，所属店铺：" + self.list[4][2] + ",价格：" + self.list[4][3] + "，评价：" + self.list[4][4]+
                                     "，销量："+self.list[4][5])
        elif event.GetEventObject() == self.m_button13:
            select = 'SELECT * FROM item_inf WHERE `商品名称`=\'' + self.value0 + '\'ORDER BY `销量` DESC'
            my = PyMySQL(select)
            self.list = my.select_data2(self.list)
          #  print(self.list)
            self.list2[0] = self.list[0][0]
            self.list2[1] = self.list[1][0]
            self.list2[2] = self.list[2][0]
            self.list2[3] = self.list[3][0]
            self.list2[4] = self.list[4][0]
            self.m_button23.SetLabel("编号：" + self.list[0][0] + ",名称：" + self.list[0][1]
                                     + "，所属店铺：" + self.list[0][2] + ",价格：" + self.list[0][3] + "，评价：" + self.list[0][4]+
                                     "，销量："+self.list[0][5])
            self.m_button24.SetLabel("编号：" + self.list[1][0] + ",名称：" + self.list[1][1]
                                     + "，所属店铺：" + self.list[1][2] + ",价格：" + self.list[1][3] + "，评价：" + self.list[1][4]+
                                     "，销量："+self.list[1][5])
            self.m_button25.SetLabel("编号：" + self.list[2][0] + ",名称：" + self.list[2][1]
                                     + "，所属店铺：" + self.list[2][2] + ",价格：" + self.list[2][3] + "，评价：" + self.list[2][4]+
                                     "，销量："+self.list[2][5])
            self.m_button26.SetLabel("编号：" + self.list[3][0] + ",名称：" + self.list[3][1]
                                     + "，所属店铺：" + self.list[3][2] + ",价格：" + self.list[3][3] + "，评价：" + self.list[3][4]+
                                     "，销量："+self.list[3][5])
            self.m_button27.SetLabel("编号：" + self.list[4][0] + ",名称：" + self.list[4][1]
                                     + "，所属店铺：" + self.list[4][2] + ",价格：" + self.list[4][3] + "，评价：" + self.list[4][4]+
                                     "，销量："+self.list[4][5])
        elif event.GetEventObject() == self.m_button14:
            select = 'SELECT * FROM item_inf WHERE `商品名称`=\'' + self.value0 + '\'ORDER BY `评价` DESC'
            my = PyMySQL(select)
            self.list = my.select_data2(self.list)
           # print(self.list)
            self.list2[0] = self.list[0][0]
            self.list2[1] = self.list[1][0]
            self.list2[2] = self.list[2][0]
            self.list2[3] = self.list[3][0]
            self.list2[4] = self.list[4][0]
            self.m_button23.SetLabel("编号：" + self.list[0][0] + ",名称：" + self.list[0][1]
                                     + "，所属店铺：" + self.list[0][2] + ",价格：" + self.list[0][3] + "，评价：" + self.list[0][4]+
                                     "，销量："+self.list[0][5])
            self.m_button24.SetLabel("编号：" + self.list[1][0] + ",名称：" + self.list[1][1]
                                     + "，所属店铺：" + self.list[1][2] + ",价格：" + self.list[1][3] + "，评价：" + self.list[1][4]+
                                     "，销量："+self.list[1][5])
            self.m_button25.SetLabel("编号：" + self.list[2][0] + ",名称：" + self.list[2][1]
                                     + "，所属店铺：" + self.list[2][2] + ",价格：" + self.list[2][3] + "，评价：" + self.list[2][4]+
                                     "，销量："+self.list[2][5])
            self.m_button26.SetLabel("编号：" + self.list[3][0] + ",名称：" + self.list[3][1]
                                     + "，所属店铺：" + self.list[3][2] + ",价格：" + self.list[3][3] + "，评价：" + self.list[3][4]+
                                     "，销量："+self.list[3][5])
            self.m_button27.SetLabel("编号：" + self.list[4][0] + ",名称：" + self.list[4][1]
                                     + "，所属店铺：" + self.list[4][2] + ",价格：" + self.list[4][3] + "，评价：" + self.list[4][4]+
                                     "，销量："+self.list[4][5])
        elif event.GetEventObject() == self.m_button15:
            select = 'SELECT * FROM item_inf WHERE `商品名称`=\'' + self.value0 + '\''
            my = PyMySQL(select)
            self.list = my.select_data2(self.list)
           # print(self.list)
            self.list2[0]= self.list[0][0]
            self.list2[1]= self.list[1][0]
            self.list2[2]= self.list[2][0]
            self.list2[3]= self.list[3][0]
            self.list2[4]= self.list[4][0]
            self.m_button23.SetLabel("编号：" + self.list[0][0] + ",名称：" + self.list[0][1]
                                     + "，所属店铺：" + self.list[0][2] + ",价格：" + self.list[0][3] + "，评价：" + self.list[0][4]+
                                     "，销量："+self.list[0][5])
            self.m_button24.SetLabel("编号：" + self.list[1][0] + ",名称：" + self.list[1][1]
                                     + "，所属店铺：" + self.list[1][2] + ",价格：" + self.list[1][3] + "，评价：" + self.list[1][4]+
                                     "，销量："+self.list[1][5])
            self.m_button25.SetLabel("编号：" + self.list[2][0] + ",名称：" + self.list[2][1]
                                     + "，所属店铺：" + self.list[2][2] + ",价格：" + self.list[2][3] + "，评价：" + self.list[2][4]+
                                     "，销量："+self.list[2][5])
            self.m_button26.SetLabel("编号：" + self.list[3][0] + ",名称：" + self.list[3][1]
                                     + "，所属店铺：" + self.list[3][2] + ",价格：" + self.list[3][3] + "，评价：" + self.list[3][4]+
                                     "，销量："+self.list[3][5])
            self.m_button27.SetLabel("编号：" + self.list[4][0] + ",名称：" + self.list[4][1]
                                     + "，所属店铺：" + self.list[4][2] + ",价格：" + self.list[4][3] + "，评价：" + self.list[4][4]+
                                     "，销量："+self.list[4][5])

        elif event.GetEventObject() ==self.m_button23:
            if self.list2[0]!="":
                item = ITDialog(None, -1, "商品信息", self.list2[0])
                item.ShowModal()
                item.Destroy()

        elif event.GetEventObject() == self.m_button24:
            if self.list2[1]!="":
                item = ITDialog(None, -1, "商品信息", self.list2[1])
                item.ShowModal()
                item.Destroy()
        elif event.GetEventObject() == self.m_button25:
            if self.list2[2]!="":
                item = ITDialog(None, -1, "商品信息", self.list2[2])
                item.ShowModal()
                item.Destroy()
        elif event.GetEventObject() == self.m_button26:
            if self.list2[3]!="":
                item = ITDialog(None, -1, "商品信息", self.list2[3])
                item.ShowModal()
                item.Destroy()
        elif event.GetEventObject() == self.m_button27:
            if self.list2[4]!="":
                item = ITDialog(None, -1, "商品信息", self.list2[4])
                item.ShowModal()
                item.Destroy()
        else:
            print("No Button is clicked")





    def OnMenuExit(self, event):
        self.Close()
    def OnCloseWindow(self, event):
        self.Destroy()

    def initdb(self):
        select = 'SELECT * FROM item_inf WHERE `商品名称`=\''+self.value0+'\''
        my = PyMySQL(select)
        self.list = my.select_data2(self.list)
      #  print(self.list)
        self.list2[0] = self.list[0][0]
        self.list2[1] = self.list[1][0]
        self.list2[2] = self.list[2][0]
        self.list2[3] = self.list[3][0]
        self.list2[4] = self.list[4][0]
