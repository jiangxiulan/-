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

cwd=os.getcwd()
###########################################################################
class ITDialog(wx.Dialog):
    def __init__(self,parent, id,value):

        wx.Dialog.__init__(self, parent, id, size=(500,600))
        self.value=value

        self.list=[]
        self.initdb()

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer6 = wx.BoxSizer(wx.VERTICAL)

        self.m_bpButton8 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap(cwd + "\\images\\1.jpg"), wx.DefaultPosition, size=(300,200))
        bSizer6.Add(self.m_bpButton8, 10, wx.ALL | wx.EXPAND, 5)

        gSizer1 = wx.GridSizer(0, 2, 0, 0)

        self.m_staticText11 = wx.StaticText(self, wx.ID_ANY, u"商品编号:" + self.value, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11.Wrap(-1)
        gSizer1.Add(self.m_staticText11, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText12 = wx.StaticText(self, wx.ID_ANY, "价格:"+self.list[0][1]+"元", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText12.Wrap(-1)
        gSizer1.Add(self.m_staticText12, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText16 = wx.StaticText(self, wx.ID_ANY, u"位置:"+self.list[0][4], wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText16.Wrap(-1)
        gSizer1.Add(self.m_staticText16, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText17 = wx.StaticText(self, wx.ID_ANY, "所属商铺:"+self.list[0][0]+"_"+self.list[0][4], wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText17.Wrap(-1)
        gSizer1.Add(self.m_staticText17, 0, wx.ALL | wx.EXPAND, 5)

        bSizer6.Add(gSizer1, 1, wx.EXPAND, 5)

        bSizer7 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText13 = wx.StaticText(self, wx.ID_ANY, u"评分："+self.list[0][2], wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText13.Wrap(-1)
        bSizer7.Add(self.m_staticText13, 0, wx.ALL, 5)

        self.m_staticText14 = wx.StaticText(self, wx.ID_ANY, u"评价1", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText14.Wrap(-1)
        bSizer7.Add(self.m_staticText14, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText15 = wx.StaticText(self, wx.ID_ANY, u"评价2", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText15.Wrap(-1)
        bSizer7.Add(self.m_staticText15, 0, wx.ALL | wx.EXPAND, 5)

        bSizer6.Add(bSizer7, 1, wx.EXPAND, 5)

        self.m_button4 = wx.Button(self, wx.ID_ANY, u"购买", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer6.Add(self.m_button4, 0, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(bSizer6)
        self.Layout()

        self.Centre(wx.BOTH)

    def OnMenuExit(self, event):
        self.Close()
    def OnCloseWindow(self, event):
        self.Destroy()
    def getValue(self,value):
        self.value=value
        print(self.value)

    def initdb(self):
        select = 'select `所属店铺`,item_inf.`价格`,item_inf.`评价`,shop_info.`店铺名称`,shop_info.`地址`' \
                 'FROM shop_info,item_inf ' \
                 'where shop_info.`店铺编号`=item_inf.`所属店铺` AND ' \
                 'item_inf.`商品编号`=\''+self.value+'\''
        my = PyMySQL(select)
        self.list = my.select_data2(self.list)
        #print(self.list)
        #print("41545")
        #print(type(list[0]))
