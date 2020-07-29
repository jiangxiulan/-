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
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

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
        bSizer3.Add(self.m_staticText2, 0, wx.ALL | wx.EXPAND, 5)

        self.m_button11 = wx.Button(self, wx.ID_ANY, u"记录1:空", wx.DefaultPosition, wx.DefaultSize, 0)
        self.Bind(wx.EVT_BUTTON, self.Onclick_3, self.m_button11)
        self.m_button11.SetBackgroundColour("white")
        bSizer3.Add(self.m_button11, 0, wx.ALL | wx.EXPAND, 5)

        self.m_button12 = wx.Button(self, wx.ID_ANY, u"记录2:空", wx.DefaultPosition, wx.DefaultSize, 0)
        self.Bind(wx.EVT_BUTTON, self.Onclick_3, self.m_button12)
        self.m_button12.SetBackgroundColour("white")
        bSizer3.Add(self.m_button12, 0, wx.ALL | wx.EXPAND, 5)

        self.m_button13= wx.Button(self, wx.ID_ANY, u"记录3:空", wx.DefaultPosition, wx.DefaultSize, 0)
        self.Bind(wx.EVT_BUTTON, self.Onclick_3, self.m_button13)
        self.m_button13.SetBackgroundColour("white")
        bSizer3.Add(self.m_button13, 0, wx.ALL | wx.EXPAND, 5)

        self.m_button14 = wx.Button(self, wx.ID_ANY, u"记录4:空", wx.DefaultPosition, wx.DefaultSize, 0)
        self.Bind(wx.EVT_BUTTON, self.Onclick_3, self.m_button14)
        self.m_button14.SetBackgroundColour("white")
        bSizer3.Add(self.m_button14, 0, wx.ALL | wx.EXPAND, 5)

        self.m_button15 = wx.Button(self, wx.ID_ANY, u"记录5:空", wx.DefaultPosition, wx.DefaultSize, 0)
        self.Bind(wx.EVT_BUTTON, self.Onclick_3, self.m_button15)
        self.m_button15.SetBackgroundColour("white")
        bSizer3.Add(self.m_button15, 0, wx.ALL | wx.EXPAND, 5)

        self.m_button16 = wx.Button(self, wx.ID_ANY, u"记录6:空", wx.DefaultPosition, wx.DefaultSize, 0)
        self.Bind(wx.EVT_BUTTON, self.Onclick_3, self.m_button16)
        self.m_button16.SetBackgroundColour("white")
        bSizer3.Add(self.m_button16, 0, wx.ALL | wx.EXPAND, 5)

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
        self.Bind(wx.EVT_BUTTON, self.Onclick_2, self.m_button3)
        bSizer5.Add(self.m_button3, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText10 = wx.StaticText(self, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10.Wrap(-1)
        bSizer5.Add(self.m_staticText10, 0, wx.ALL | wx.EXPAND, 5)

        bSizer1.Add(bSizer5, 3, wx.EXPAND, 5)
        if userone.username!="":
            self.m_staticText1.SetLabel(userone.username)
            self.connect(userone.username)
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
        select = 'SELECT purchase_inf.`商品编号`,user_inf.`收货地址`,purchase_inf.`评价`,purchase_inf.`时间` ' \
                 'FROM purchase_inf,user_inf ' \
                 'WHERE purchase_inf.`用户账号`=user_inf.`用户账号` and user_inf.`用户账号`=\''+value+'\'' \
                 'GROUP BY purchase_inf.`时间` order by purchase_inf.`时间` desc '
        my = PyMySQL(select)
        self.list=[('','','',''),('','','',''),('','','',''),('','','',''),('','','',''),('','','','')]
        self.list = my.select_data2(self.list)

        self.total=0
        select1='SELECT COUNT(*) FROM purchase_inf WHERE purchase_inf.`用户账号`=\''+value+'\''
        my1 = PyMySQL(select1)
        self.total=my1.select_data(self.total)

        self.str1=""
        select2 = 'SELECT `收货地址` FROM user_inf WHERE user_inf.`用户账号`=\'' + value + '\''
        my2 = PyMySQL(select2)
        self.str1 = my2.select_data(self.str1)

        if len(self.list)>=1:
            self.m_button11.SetLabel('购买商品编号：' + self.list[0][0] + "购买时间：" + str(self.list[0][3]))
            if len(self.list) >= 2:
                self.m_button12.SetLabel('购买商品编号：' + self.list[1][0] + "购买时间：" + str(self.list[1][3]))
                if len(self.list) >= 3:
                    self.m_button13.SetLabel('购买商品编号：' + self.list[2][0] + "购买时间：" + str(self.list[2][3]))
                    if len(self.list) >= 4:
                        self.m_button14.SetLabel('购买商品编号：' + self.list[3][0] + "购买时间：" + str(self.list[3][3]))
                        if len(self.list) >= 5:
                            self.m_button15.SetLabel('购买商品编号：' + self.list[4][0] + "购买时间：" + str(self.list[4][3]))
                            if len(self.list) >= 6:
                                self.m_button16.SetLabel('购买商品编号：' + self.list[5][0] + "购买时间：" + str(self.list[5][3]))
        self.m_button1.SetLabel('收货地址：'+self.str1)
        #print(self.list[0][1])
        self.m_button3.SetLabel('购买统计：'+str(self.total))

    def Onclick_1(self, event):
        if userone.username=="":
            dlg = wx.MessageDialog(None, u"未登录", u"提示", wx.OK | wx.ICON_QUESTION)
            if dlg.ShowModal() == wx.ID_OK:
                dlg.Close(True)
            dlg.Destroy()
        elif userone.usertype=="一般用户":
            dlg = wx.MessageDialog(None, u"您不是商家", u"提示", wx.OK | wx.ICON_QUESTION)
            if dlg.ShowModal() == wx.ID_OK:
                dlg.Close(True)
            dlg.Destroy()
        else:
            dialog = SPpage(None, -1, "我的店铺")
            dialog.ShowModal()
            dialog.Destroy()

    def Onclick_2(self, event):
        if userone.username=="":
            dlg = wx.MessageDialog(None, u"未登录", u"提示", wx.OK | wx.ICON_QUESTION)
            if dlg.ShowModal() == wx.ID_OK:
                dlg.Close(True)
            dlg.Destroy()
        else:
            self.connect(userone.username)

    def Onclick_3(self,event):
        if userone.username == "":
            dlg = wx.MessageDialog(None, u"未登录", u"提示", wx.OK | wx.ICON_QUESTION)
            if dlg.ShowModal() == wx.ID_OK:
                dlg.Close(True)
            dlg.Destroy()
            return
        if event.GetEventObject() == self.m_button11:
            if self.list[0][2]=="0":
                dlg = MessDialog(None, -1,self.list[0][0])
                dlg.ShowModal()
                dlg.Destroy()
                self.connect(userone.username)
            elif self.list[0][2]!="":
                dlg = wx.MessageDialog(None, "已评价，评分："+self.list[0][2], u"提示", wx.OK | wx.ICON_QUESTION)
                if dlg.ShowModal() == wx.ID_OK:
                    dlg.Close(True)
                dlg.Destroy()
        elif event.GetEventObject() == self.m_button12:
            if self.list[1][2]=="0":
                dlg = MessDialog(None, -1,self.list[1][0])
                dlg.ShowModal()
                dlg.Destroy()
            elif self.list[1][2]!="":
                dlg = wx.MessageDialog(None, "已评价，评分：" + self.list[1][2], u"提示", wx.OK | wx.ICON_QUESTION)
                if dlg.ShowModal() == wx.ID_OK:
                    dlg.Close(True)
                dlg.Destroy()
        elif event.GetEventObject() == self.m_button13:
            if self.list[2][2]=="0":
                dlg = MessDialog(None, -1,self.list[2][0])
                dlg.ShowModal()
                dlg.Destroy()
            elif self.list[2][2]!="":
                dlg = wx.MessageDialog(None, "已评价，评分：" + self.list[2][2], u"提示", wx.OK | wx.ICON_QUESTION)
                if dlg.ShowModal() == wx.ID_OK:
                    dlg.Close(True)
                dlg.Destroy()
        elif event.GetEventObject() == self.m_button14:
            if self.list[3][2]=="0":
                dlg = MessDialog(None, -1,self.list[3][0])
                dlg.ShowModal()
                dlg.Destroy()
            elif self.list[3][2]!="":
                dlg = wx.MessageDialog(None, "已评价，评分：" + self.list[3][2], u"提示", wx.OK | wx.ICON_QUESTION)
                if dlg.ShowModal() == wx.ID_OK:
                    dlg.Close(True)
                dlg.Destroy()
        elif event.GetEventObject() == self.m_button15:
            if self.list[4][2]=="0":
                dlg = MessDialog(None, -1,self.list[4][0])
                dlg.ShowModal()
                dlg.Destroy()
            elif self.list[4][2]!="":
                dlg = wx.MessageDialog(None, "已评价，评分：" + self.list[4][2], u"提示", wx.OK | wx.ICON_QUESTION)
                if dlg.ShowModal() == wx.ID_OK:
                    dlg.Close(True)
                dlg.Destroy()
        elif event.GetEventObject() == self.m_button16:
            if self.list[5][2]=="0":
                dlg = MessDialog(None, -1,self.list[5][0])
                dlg.ShowModal()
                dlg.Destroy()
            elif self.list[5][2]!="":
                dlg = wx.MessageDialog(None, "已评价，评分：" + self.list[5][2], u"提示", wx.OK | wx.ICON_QUESTION)
                if dlg.ShowModal() == wx.ID_OK:
                    dlg.Close(True)
                dlg.Destroy()
        else:
            print("No Button is clicked")

class MessDialog(wx.Dialog):
    def __init__(self, parent, id,value):
        self.value1=value
        wx.Dialog.__init__(self, parent, id, '评价', size=(300, 200))
        self.sizer1 = wx.BoxSizer(wx.VERTICAL)
        self.sizer1.Add(wx.StaticText(self, -1, u"未评价！"),
                        0, wx.ALIGN_CENTER_HORIZONTAL | wx.TOP, border=20)
        self.sizer1.Add(wx.StaticText(self, -1, u"请评价："),
                        0, wx.ALIGN_CENTER_HORIZONTAL | wx.TOP, border=10)

        self.slider=wx.Slider( self, wx.ID_ANY, 1.0, 1.2, 5.0,style=wx.SL_AUTOTICKS|wx.SL_LABELS)
        self.sizer1.Add(self.slider,0, wx.ALIGN_CENTER_HORIZONTAL | wx.TOP, border=10)
        self.button1=wx.Button(self, wx.ID_ANY,"确认")
        self.sizer1.Add(self.button1, 0, wx.ALIGN_CENTER | wx.BOTTOM, border=20)
        self.Bind(wx.EVT_BUTTON, self.Onclick, self.button1)
        self.SetSizer(self.sizer1)

    def GetValue(self):
        return self.slider.GetValue()

    def Onclick(self,event):
        self.value = str(self.GetValue())

        update1 = 'UPDATE purchase_inf SET `评价`=\'' + self.value + '\' WHERE `商品编号`=\'' + self.value1 + '\''
        my = PyMySQL(update1)
        my.update_data()
        str_1=[]
        select='SELECT `评价` FROM item_inf WHERE `商品编号`=\''+self.value1+'\''
        my2 = PyMySQL(select)
        str_1=my2.select_data(str_1)
        if str_1=="0":
            update2='' \
                    'UPDATE item_inf SET `评价`=\''+self.value+'\' WHERE `商品编号`=\''+ self.value1 +'\''
        else:
            update2 ='UPDATE item_inf SET `评价`=CAST(((CAST(`评价` AS FLOAT)+' + self.value + ')/2.0)AS CHAR)' \
                                                                                        'WHERE `商品编号`=\'' + \
                  self.value1+ '\''
        #print(update2)
        my = PyMySQL(update2)
        my.update_data()
        self.Close(True)

    def OnMenuExit(self, event):
        self.Close()
    def OnCloseWindow(self, event):
        self.Destroy()




