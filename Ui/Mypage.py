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
from log_in import LoginDialog
from shopedit_page import SPpage
from user_list import  userone

cwd = os.getcwd()
###########################################################################
class MYpage(wx.Panel):
    #value = ""
    def __init__(self,parent,id):

        wx.Panel.__init__(self,parent,id)
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        bSizer2 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_bpButton1 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap(cwd + "\\images\\用户.png"), wx.DefaultPosition, wx.DefaultSize,
                                           wx.BU_AUTODRAW)
        self.m_bpButton1.SetBackgroundColour("white")
        bSizer2.Add(self.m_bpButton1, 1, wx.ALL | wx.EXPAND, 5)
        self.Bind(wx.EVT_BUTTON, self.Onclick, self.m_bpButton1)

        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"昵称", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        bSizer2.Add(self.m_staticText1, 8, wx.ALL | wx.EXPAND, 5)

        bSizer1.Add(bSizer2, 1, wx.EXPAND, 5)

        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, u"购买记录", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)
        bSizer3.Add(self.m_staticText2, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText3 = wx.StaticText(self, wx.ID_ANY, u"记录1:空", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)
        bSizer3.Add(self.m_staticText3, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText4 = wx.StaticText(self, wx.ID_ANY, u"记录2:空", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText4.Wrap(-1)
        bSizer3.Add(self.m_staticText4, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText5 = wx.StaticText(self, wx.ID_ANY, u"记录3:空", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)
        bSizer3.Add(self.m_staticText5, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText6 = wx.StaticText(self, wx.ID_ANY, u"记录4:空", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText6.Wrap(-1)
        bSizer3.Add(self.m_staticText6, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText7 = wx.StaticText(self, wx.ID_ANY, u"记录5:空", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText7.Wrap(-1)
        bSizer3.Add(self.m_staticText7, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText8 = wx.StaticText(self, wx.ID_ANY, u"记录6:空", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText8.Wrap(-1)
        bSizer3.Add(self.m_staticText8, 0, wx.ALL | wx.EXPAND, 5)

        bSizer1.Add(bSizer3, 3, wx.EXPAND, 5)

        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        self.m_button1 = wx.Button(self, wx.ID_ANY, u"购买地址", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button1.SetBackgroundColour("#FF6600")
        self.m_button1.SetForegroundColour("white")
        bSizer5.Add(self.m_button1, 0, wx.ALL | wx.EXPAND, 5)

        self.m_button2 = wx.Button(self, wx.ID_ANY, u"我的店铺", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button2.SetBackgroundColour("#FF6600")
        self.m_button2.SetForegroundColour("white")
        self.Bind(wx.EVT_BUTTON, self.Onclick_1, self.m_button2)
        bSizer5.Add(self.m_button2, 0, wx.ALL | wx.EXPAND, 5)

        self.m_button3 = wx.Button(self, wx.ID_ANY, u"购买统计", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button3.SetBackgroundColour("#FF6600")
        self.m_button3.SetForegroundColour("white")
        bSizer5.Add(self.m_button3, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText10 = wx.StaticText(self, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10.Wrap(-1)
        bSizer5.Add(self.m_staticText10, 0, wx.ALL | wx.EXPAND, 5)

        bSizer1.Add(bSizer5, 3, wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)
    def Onclick(self,event):
        dialog = LoginDialog(None,-1,"登录")
        dialog.ShowModal()
        if userone.username!="":
            self.m_staticText1.SetLabel(userone.username)
            self.connect(userone.username)
        dialog.Destroy()

    def connect(self,value):
        select = 'SELECT `商品编号`,`收货地址` ,count(*) FROM purchase_inf,user_inf ' \
                 'WHERE purchase_inf.`用户账号`=user_inf.`用户账号` ' \
                 ' AND purchase_inf.`用户账号` =\''+value+'\''
        my = PyMySQL(select)
        self.list=[]
        self.list = my.select_data2(self.list)
        #print(self.list)
        self.m_staticText3.SetLabel('购买商品编号：'+self.list[0][0])
        self.m_button1.SetLabel('收货地址：'+self.list[0][1])
        self.m_button3.SetLabel('购买统计：'+str(self.list[0][2]))

    def Onclick_1(self, event):
        dialog = SPpage(None, -1,"我的店铺")
        dialog.ShowModal()
        dialog.Destroy()





