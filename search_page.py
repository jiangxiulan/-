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

class MyFrame3(wx.Frame):

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

        bSizer7 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button12 = wx.Button(self, wx.ID_ANY, u"价格", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer7.Add(self.m_button12, 1, wx.ALL, 5)

        self.m_button13 = wx.Button(self, wx.ID_ANY, u"销量", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer7.Add(self.m_button13, 1, wx.ALL, 5)

        self.m_button14 = wx.Button(self, wx.ID_ANY, u"信用", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer7.Add(self.m_button14, 1, wx.ALL, 5)

        self.m_button15 = wx.Button(self, wx.ID_ANY, u"综合", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer7.Add(self.m_button15, 1, wx.ALL, 5)

        bSizer1.Add(bSizer7, 1, wx.EXPAND, 5)

        bSizer9 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer10 = wx.BoxSizer(wx.VERTICAL)

        self.m_bitmap4 = wx.StaticBitmap(self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer10.Add(self.m_bitmap4, 1, wx.ALL | wx.EXPAND, 5)

        self.m_bitmap5 = wx.StaticBitmap(self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer10.Add(self.m_bitmap5, 1, wx.ALL | wx.EXPAND, 5)

        self.m_bitmap6 = wx.StaticBitmap(self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer10.Add(self.m_bitmap6, 1, wx.ALL | wx.EXPAND, 5)

        self.m_bitmap7 = wx.StaticBitmap(self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer10.Add(self.m_bitmap7, 1, wx.ALL | wx.EXPAND, 5)

        self.m_bitmap8 = wx.StaticBitmap(self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer10.Add(self.m_bitmap8, 1, wx.ALL | wx.EXPAND, 5)

        bSizer9.Add(bSizer10, 1, wx.EXPAND, 5)

        bSizer11 = wx.BoxSizer(wx.VERTICAL)

        self.m_button23 = wx.Button(self, wx.ID_ANY, u"商品1", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer11.Add(self.m_button23, 1, wx.ALL | wx.EXPAND, 5)

        self.m_button24 = wx.Button(self, wx.ID_ANY, u"商品2", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer11.Add(self.m_button24, 1, wx.ALL | wx.EXPAND, 5)

        self.m_button25 = wx.Button(self, wx.ID_ANY, u"商品3", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer11.Add(self.m_button25, 1, wx.ALL | wx.EXPAND, 5)

        self.m_button26 = wx.Button(self, wx.ID_ANY, u"商品4", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer11.Add(self.m_button26, 1, wx.ALL | wx.EXPAND, 5)

        self.m_button27 = wx.Button(self, wx.ID_ANY, u"商品5", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer11.Add(self.m_button27, 1, wx.ALL | wx.EXPAND, 5)

        bSizer9.Add(bSizer11, 10, wx.EXPAND, 5)

        bSizer1.Add(bSizer9, 10, wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass


if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame3(None)
    frame.Show()
    app.MainLoop()