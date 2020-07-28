import wx

from datebase import PyMySQL


class InfoPage(wx.Dialog):
    def __init__(self,parent,title ,id,value):
        wx.Dialog.__init__(self, parent,title, id, size=( 300, 240))
        #print(value)
        self.value=value
        self.list = [("","","","","")]
        self.initdb()
        self.sizer1 = wx.BoxSizer(wx.VERTICAL)
        self.sizer1.Add(wx.StaticText(self, -1, "商品编号："+self.list[0][0]),
                        0, wx.ALIGN_CENTER_HORIZONTAL | wx.TOP, border=20)
        self.sizer1.Add(wx.StaticText(self, -1, "商品名称："+self.list[0][1]),
                        0, wx.ALIGN_CENTER_HORIZONTAL | wx.TOP, border=10)
        self.sizer1.Add(wx.StaticText(self, -1, "数量："+self.list[0][2]),
                        0, wx.ALIGN_CENTER_HORIZONTAL | wx.TOP, border=10)
        self.sizer1.Add(wx.StaticText(self, -1, "单价："+self.list[0][3]),
                        0, wx.ALIGN_CENTER_HORIZONTAL | wx.TOP, border=10)
        self.sizer1.Add(wx.StaticText(self, -1, "评价："+self.list[0][4]),
                        0, wx.ALIGN_CENTER_HORIZONTAL | wx.TOP, border=10)
        self.sizer1.Add(wx.Button(self, wx.ID_OK), 0, wx.ALIGN_CENTER | wx.BOTTOM, border=20)
        self.SetSizer(self.sizer1)

    def OnMenuExit(self, event):
        self.Close()
    def OnCloseWindow(self, event):
        self.Destroy()

    def initdb(self):
        select = 'SELECT `商品编号`,`商品名称`,item_inf.数量,`价格`,item_inf.`评价` FROM item_inf WHERE `商品编号`=\''+self.value+'\''
        my = PyMySQL(select)
        self.list = my.select_data2(self.list)
        #print(self.list)