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

class MyFrame2(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(578, 508), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        bSizer2 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button1 = wx.Button(self, wx.ID_ANY, u"搜索", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.m_button1, 0, wx.ALL | wx.EXPAND, 5)

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

        self.m_button2 = wx.Button(self, wx.ID_ANY, u"商品1", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer1.Add(self.m_button2, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)

        self.m_button3 = wx.Button(self, wx.ID_ANY, u"店铺1", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer1.Add(self.m_button3, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)

        self.m_button4 = wx.Button(self, wx.ID_ANY, u"商品2", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer1.Add(self.m_button4, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)

        self.m_button5 = wx.Button(self, wx.ID_ANY, u"店铺2", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer1.Add(self.m_button5, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)

        self.m_button6 = wx.Button(self, wx.ID_ANY, u"商品3", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer1.Add(self.m_button6, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)

        self.m_button7 = wx.Button(self, wx.ID_ANY, u"店铺3", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer1.Add(self.m_button7, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)

        self.m_button8 = wx.Button(self, wx.ID_ANY, u"商品4", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer1.Add(self.m_button8, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)

        self.m_button9 = wx.Button(self, wx.ID_ANY, u"店铺4", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer1.Add(self.m_button9, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)

        self.m_button10 = wx.Button(self, wx.ID_ANY, u"商品5", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer1.Add(self.m_button10, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)

        self.m_button11 = wx.Button(self, wx.ID_ANY, u"店铺5", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer1.Add(self.m_button11, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)

        bSizer1.Add(gSizer1, 10, wx.EXPAND, 5)

        sbSizer3 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"广告页"), wx.VERTICAL)

        bSizer1.Add(sbSizer3, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass


if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame2(None)
    frame.Show()
    app.MainLoop()
