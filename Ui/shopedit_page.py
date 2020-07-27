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
from info_page import InfoPage
from user_list import userone

cwd=os.getcwd()
###########################################################################
class SPpage(wx.Dialog):
    def __init__(self,parent, id,title):
        wx.Dialog.__init__(self, parent, id,title, size=(500,600))
        self.username=""
        if userone.username!="":
            self.username=userone.username

        self.list = [("",""), ("",""), ("",""), ("",""),("",""),("",""),("",""),("","")]
        self.initdb()


        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        bSizer12 = wx.BoxSizer(wx.VERTICAL)
        bSizer13 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText24 = wx.StaticText(self, wx.ID_ANY, self.username+"商铺", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText24.Wrap(-1)
        bSizer13.Add(self.m_staticText24, 1, wx.ALL | wx.EXPAND, 5)

        bSizer12.Add(bSizer13, 1, wx.EXPAND, 5)

        bSizer14 = wx.BoxSizer(wx.HORIZONTAL)

        gSizer3 = wx.GridSizer(0, 2, 0, 0)

        self.m_bpButton10 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap(cwd+"\\images\\商品.png"), wx.DefaultPosition, wx.DefaultSize,
                                            wx.BU_AUTODRAW)
        self.m_bpButton10.SetBackgroundColour("white")
        self.Bind(wx.EVT_BUTTON, self.Onclick, self.m_bpButton10)
        gSizer3.Add(self.m_bpButton10, 0, wx.ALL|  wx.EXPAND, 5)

        self.m_bpButton11 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap(cwd+"\\images\\商品.png"), wx.DefaultPosition, wx.DefaultSize,
                                            wx.BU_AUTODRAW)
        self.m_bpButton11.SetBackgroundColour("white")
        self.Bind(wx.EVT_BUTTON, self.Onclick, self.m_bpButton11)
        gSizer3.Add(self.m_bpButton11, 0, wx.ALL|  wx.EXPAND, 5)

        self.m_bpButton12 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap(cwd+"\\images\\商品.png"), wx.DefaultPosition, wx.DefaultSize,
                                            wx.BU_AUTODRAW)
        self.m_bpButton12.SetBackgroundColour("white")
        self.Bind(wx.EVT_BUTTON, self.Onclick, self.m_bpButton12)
        gSizer3.Add(self.m_bpButton12, 0, wx.ALL|  wx.EXPAND, 5)

        self.m_bpButton13 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap(cwd+"\\images\\商品.png"), wx.DefaultPosition, wx.DefaultSize,
                                            wx.BU_AUTODRAW)
        self.m_bpButton13.SetBackgroundColour("white")
        self.Bind(wx.EVT_BUTTON, self.Onclick, self.m_bpButton13)
        gSizer3.Add(self.m_bpButton13, 0, wx.ALL|  wx.EXPAND, 5)

        self.m_bpButton14 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap(cwd+"\\images\\商品.png"), wx.DefaultPosition, wx.DefaultSize,
                                            wx.BU_AUTODRAW)
        self.m_bpButton14.SetBackgroundColour("white")
        self.Bind(wx.EVT_BUTTON, self.Onclick, self.m_bpButton14)
        gSizer3.Add(self.m_bpButton14, 0, wx.ALL|  wx.EXPAND, 5)

        self.m_bpButton15 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap(cwd+"\\images\\商品.png"), wx.DefaultPosition, wx.DefaultSize,
                                            wx.BU_AUTODRAW)
        self.m_bpButton15.SetBackgroundColour("white")
        self.Bind(wx.EVT_BUTTON, self.Onclick, self.m_bpButton15)
        gSizer3.Add(self.m_bpButton15, 0, wx.ALL|  wx.EXPAND, 5)

        self.m_bpButton16 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap(cwd+"\\images\\商品.png"), wx.DefaultPosition, wx.DefaultSize,
                                            wx.BU_AUTODRAW)
        self.m_bpButton16.SetBackgroundColour("white")
        self.Bind(wx.EVT_BUTTON, self.Onclick, self.m_bpButton16)
        gSizer3.Add(self.m_bpButton16, 0, wx.ALL|  wx.EXPAND, 5)

        self.m_bpButton17 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap(cwd+"\\images\\商品.png"), wx.DefaultPosition, wx.DefaultSize,
                                            wx.BU_AUTODRAW)
        self.m_bpButton17.SetBackgroundColour("white")
        self.Bind(wx.EVT_BUTTON, self.Onclick, self.m_bpButton17)
        gSizer3.Add(self.m_bpButton17, 0, wx.ALL|  wx.EXPAND, 5)

        bSizer14.Add(gSizer3, 4, wx.EXPAND, 5)

        bSizer17 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText25 = wx.StaticText(self, wx.ID_ANY, u"管理", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText25.Wrap(-1)
        bSizer17.Add(self.m_staticText25, 0, wx.ALL | wx.EXPAND, 5)

        self.m_button11 = wx.Button(self, wx.ID_ANY, u"删除商品"
                                                     u"", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button11.SetBackgroundColour("#FF6600")
        self.m_button11.SetForegroundColour("white")
        self.Bind(wx.EVT_BUTTON, self.Onclick, self.m_button11)
        bSizer17.Add(self.m_button11, 0, wx.ALL, 5)

        self.m_button13 = wx.Button(self, wx.ID_ANY, u"添加商品", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button13.SetBackgroundColour("#FF6600")
        self.m_button13.SetForegroundColour("white")
        self.Bind(wx.EVT_BUTTON, self.Onclick, self.m_button13)
        bSizer17.Add(self.m_button13, 0, wx.ALL, 5)

        self.m_button12 = wx.Button(self, wx.ID_ANY, u"修改信息", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button12.SetBackgroundColour("#FF6600")
        self.m_button12.SetForegroundColour("white")
        self.Bind(wx.EVT_BUTTON, self.Onclick, self.m_button12)
        bSizer17.Add(self.m_button12, 0, wx.ALL, 5)

        bSizer14.Add(bSizer17, 4, wx.EXPAND, 5)

        bSizer12.Add(bSizer14, 4, wx.EXPAND, 5)

        gSizer4 = wx.GridSizer(0, 2, 0, 0)

        self.m_staticText28 = wx.StaticText(self, wx.ID_ANY, u"增加修改商品", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText28.Wrap(-1)


        gSizer4.Add(self.m_staticText28, 0, wx.ALL, 5)

        self.m_staticText33 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText33.Wrap(-1)
        gSizer4.Add(self.m_staticText33, 0, wx.ALL, 5)

        self.m_bpButton18 = wx.BitmapButton(self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize,
                                            wx.BU_AUTODRAW)
        self.m_bpButton18.SetBackgroundColour("white")
        gSizer4.Add(self.m_bpButton18, 0, wx.ALL, 5)

        self.m_staticText35 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText35.Wrap(-1)
        gSizer4.Add(self.m_staticText35, 0, wx.ALL, 5)

        self.m_staticText29 = wx.StaticText(self, wx.ID_ANY, u"商品编号", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText29.Wrap(-1)
        gSizer4.Add(self.m_staticText29, 0, wx.ALL, 5)

        self.m_textCtrl3 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer4.Add(self.m_textCtrl3, 0, wx.ALL, 5)

        self.m_staticText32 = wx.StaticText(self, wx.ID_ANY, u"商品名称", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText32.Wrap(-1)
        gSizer4.Add(self.m_staticText32, 0, wx.ALL, 5)

        self.m_textCtrl6 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer4.Add(self.m_textCtrl6, 0, wx.ALL, 5)

        self.m_staticText30 = wx.StaticText(self, wx.ID_ANY, u"商品数量", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText30.Wrap(-1)
        gSizer4.Add(self.m_staticText30, 0, wx.ALL, 5)

        self.m_textCtrl4 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer4.Add(self.m_textCtrl4, 0, wx.ALL, 5)

        self.m_staticText31 = wx.StaticText(self, wx.ID_ANY, u"商品价格", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText31.Wrap(-1)
        gSizer4.Add(self.m_staticText31, 0, wx.ALL, 5)

        self.m_textCtrl5 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer4.Add(self.m_textCtrl5, 0, wx.ALL, 5)

        bSizer12.Add(gSizer4, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer12)
        self.Layout()

        self.Centre(wx.BOTH)
    def OnMenuExit(self, event):
        self.Close()
    def OnCloseWindow(self, event):
        self.Destroy()

    def Onclick(self, event):
        if event.GetEventObject() == self.m_bpButton10:
            dialog = InfoPage(None, -1, "商品信息",self.list[1][0])
            dialog.ShowModal()
            dialog.Destroy()
        elif event.GetEventObject() == self.m_bpButton11:
            dialog = InfoPage(None, -1, "商品信息",self.list[2][0])
            dialog.ShowModal()
            dialog.Destroy()
        elif event.GetEventObject() == self.m_bpButton12:
            dialog = InfoPage(None, -1, "商品信息",self.list[3][0])
            dialog.ShowModal()
            dialog.Destroy()
        elif event.GetEventObject() == self.m_bpButton13:
            dialog = InfoPage(None, -1, "商品信息",self.list[4][0])
            dialog.ShowModal()
            dialog.Destroy()
        elif event.GetEventObject() == self.m_bpButton14:
            dialog = InfoPage(None, -1, "商品信息",self.list[5][0])
            dialog.ShowModal()
            dialog.Destroy()
        elif event.GetEventObject() == self.m_bpButton15:
            dialog = InfoPage(None, -1, "商品信息",self.list[6][0])
            dialog.ShowModal()
            dialog.Destroy()
        elif event.GetEventObject() == self.m_bpButton16:
            dialog = InfoPage(None, -1, "商品信息",self.list[7][0])
            dialog.ShowModal()
            dialog.Destroy()
        elif event.GetEventObject() == self.m_bpButton17:
            dialog = InfoPage(None, -1, "商品信息",self.list[8][0])
            dialog.ShowModal()
            dialog.Destroy()
        elif event.GetEventObject() == self.m_button11:
            self.initdb2()
        elif event.GetEventObject() == self.m_button12:
            self.initdb3()
        elif event.GetEventObject() == self.m_button13:
            self.initdb4()
        else:
            print("No Button is clicked")

    def initdb(self):
        select = 'SELECT item_inf.`商品编号`,shop_info.`店铺编号` FROM shop_info,item_inf ' \
                 'WHERE shop_info.`店铺编号`=item_inf.`所属店铺` ' \
                 'AND shop_info.`所属用户`=\''+self.username+'\''
        my = PyMySQL(select)
        self.list = my.select_data2(self.list)
        print(self.list)

    def initdb2(self):
        delete = 'DELETE FROM item_inf WHERE 商品编号 =\''+self.m_textCtrl3.GetValue()+'\''
        my = PyMySQL(delete)
        my.delete_data()

    def initdb3(self):
        update = 'UPDATE item_inf set `数量` =\''+self.m_textCtrl4.GetValue()+'\',`价格`=\''\
                 +self.m_textCtrl5.GetValue()+'\' WHERE `商品编号`=\''+self.m_textCtrl3.GetValue()+'\''
        my = PyMySQL(update)
        my.update_data()
    def initdb4(self):
        insert = 'INSERT INTO item_inf VALUES (\''+self.m_textCtrl3.GetValue()+'\',\''+self.m_textCtrl6.GetValue()\
                 +'\',\''+self.list[0][1]+'\',\''+self.m_textCtrl5.GetValue()+'\',\'0\',\''+self.m_textCtrl4.GetValue()\
                    +'\',\'0\')'
        my = PyMySQL(insert)
        my.insert_date()








