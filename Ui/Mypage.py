# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc


###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame4(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(716, 510), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        bSizer2 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_bpButton1 = wx.BitmapButton(self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize,
                                           wx.BU_AUTODRAW)
        bSizer2.Add(self.m_bpButton1, 1, wx.ALL | wx.EXPAND, 5)

        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"昵称", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        bSizer2.Add(self.m_staticText1, 8, wx.ALL | wx.EXPAND , 5)

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

    def __del__(self):
        pass


if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame4(None)
    frame.Show()
    app.MainLoop()
