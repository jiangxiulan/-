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
## Class MyFrame2
###########################################################################

class MyFrame5(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(562, 534), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer6 = wx.BoxSizer(wx.VERTICAL)

        self.m_bpButton8 = wx.BitmapButton(self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize,
                                           wx.BU_AUTODRAW)
        bSizer6.Add(self.m_bpButton8, 10, wx.ALL | wx.EXPAND, 5)

        gSizer1 = wx.GridSizer(0, 2, 0, 0)

        self.m_staticText11 = wx.StaticText(self, wx.ID_ANY, u"所属商铺", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11.Wrap(-1)
        gSizer1.Add(self.m_staticText11, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText12 = wx.StaticText(self, wx.ID_ANY, u"价格", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText12.Wrap(-1)
        gSizer1.Add(self.m_staticText12, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText16 = wx.StaticText(self, wx.ID_ANY, u"位置", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText16.Wrap(-1)
        gSizer1.Add(self.m_staticText16, 0, wx.ALL | wx.EXPAND, 5)

        bSizer6.Add(gSizer1, 1, wx.EXPAND, 5)

        bSizer7 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText13 = wx.StaticText(self, wx.ID_ANY, u"评价", wx.DefaultPosition, wx.DefaultSize, 0)
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

    def __del__(self):
        pass


if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame5(None)
    frame.Show()
    app.MainLoop()
