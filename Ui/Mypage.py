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
###########################################################################
class MYpage(wx.Panel):
    def __init__(self,parent,id):
        wx.Panel.__init__(self,parent,id)
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        bSizer2 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_bpButton1 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap(cwd + "\\images\\用户.png"), wx.DefaultPosition, wx.DefaultSize,
                                           wx.BU_AUTODRAW)
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

        self.m_staticText3 = wx.StaticText(self, wx.ID_ANY, u"记录1", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)
        bSizer3.Add(self.m_staticText3, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText4 = wx.StaticText(self, wx.ID_ANY, u"记录2", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText4.Wrap(-1)
        bSizer3.Add(self.m_staticText4, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText5 = wx.StaticText(self, wx.ID_ANY, u"记录3", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)
        bSizer3.Add(self.m_staticText5, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText6 = wx.StaticText(self, wx.ID_ANY, u"记录4", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText6.Wrap(-1)
        bSizer3.Add(self.m_staticText6, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText7 = wx.StaticText(self, wx.ID_ANY, u"记录5", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText7.Wrap(-1)
        bSizer3.Add(self.m_staticText7, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText8 = wx.StaticText(self, wx.ID_ANY, u"记录6", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText8.Wrap(-1)
        bSizer3.Add(self.m_staticText8, 0, wx.ALL | wx.EXPAND, 5)

        bSizer1.Add(bSizer3, 3, wx.EXPAND, 5)

        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        self.m_button1 = wx.Button(self, wx.ID_ANY, u"购买地址", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer5.Add(self.m_button1, 0, wx.ALL | wx.EXPAND, 5)

        self.m_button2 = wx.Button(self, wx.ID_ANY, u"购买评估", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer5.Add(self.m_button2, 0, wx.ALL | wx.EXPAND, 5)

        self.m_button3 = wx.Button(self, wx.ID_ANY, u"购买统计", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer5.Add(self.m_button3, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText10 = wx.StaticText(self, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10.Wrap(-1)
        bSizer5.Add(self.m_staticText10, 0, wx.ALL | wx.EXPAND, 5)

        bSizer1.Add(bSizer5, 3, wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)
    def Onclick(self,event):
        dialog = LoginDialog(None,-1)
        dialog.ShowModal()
        dialog.Destroy()

class LoginDialog(wx.Dialog):
    def __init__(self,parent, id,):
        wx.Dialog.__init__(self, parent, id, size=(355,166))
        ###########################################################


        ###########################################################
        # 显示按钮功能
        self.initUI()

    def initUI(self):

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        bSizer2 = wx.BoxSizer(wx.VERTICAL)
        gSizer1 = wx.GridSizer(0, 2, 0, 0)
        ###########################################################
        # 显示按钮功能
        #self.panel = wx.Panel(self, -1)
        self.m_staticText1 =wx.StaticText(self, label="Username")
        self.m_staticText1.Wrap(-1)
        gSizer1.Add(self.m_staticText1, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)
        self._username = wx.TextCtrl(self)
        gSizer1.Add(self._username, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText2 = wx.StaticText(self, label="Password")
        self.m_staticText2.Wrap(-1)
        gSizer1.Add(self.m_staticText2, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)
        self._password = wx.TextCtrl(self, pos=(85, 45), style=wx.TE_PASSWORD)
        gSizer1.Add(self._password, 0, wx.ALL | wx.EXPAND, 5)
        bSizer2.Add(gSizer1, 1, wx.EXPAND, 5)
        self.submit_btn = wx.Button(self, label=u"提交", pos=(20, 80), size=(50, 30))
        bSizer2.Add(self.submit_btn, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.submit_btn)
        self.SetSizer(bSizer2)
        self.Layout()
        self.Centre(wx.BOTH)

    def GetUsername(self):
        return self._username.GetValue()

    def GetPassword(self):
        return self._password.GetValue()




    def OnClick(self, event):
        if event.GetEventObject() == self.submit_btn:
            self.Destroy()
        else:
            print("No Button is clicked")

    def OnMenuExit(self, event):
        self.Close()
    def OnCloseWindow(self, event):
        self.Destroy()

    # 定义一个对话框


