import time

import wx

from url_page import init_url


class RCpage(wx.Panel):
    def __init__(self, parent, id):
        wx.Panel.__init__(self, parent, id)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        bSizer2 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button1 = wx.Button(self, wx.ID_ANY, u"搜索", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.m_button1, 0, wx.ALL, 5)
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.m_button1)

        self.m_textCtrl1 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.m_textCtrl1, 1, wx.ALL, 5)

        self.m_button2 = wx.Button(self, wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.m_button2, 0, wx.ALL, 5)

        bSizer1.Add(bSizer2, 1, wx.EXPAND, 5)

        self.m_textCtrl2 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,  style=wx.TE_MULTILINE)
        bSizer1.Add(self.m_textCtrl2, 9, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

    def OnClick(self,event):
        if self.m_textCtrl1.GetValue()!="":
            self.m_textCtrl2.SetLabel("等待搜索...")
            time.sleep(2)
            init_url(self.m_textCtrl1.GetValue())
            self.m_textCtrl2.LoadFile('jd.txt')


