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
from user_list import userone

cwd=os.getcwd()
###########################################################################



class ITDialog(wx.Dialog):
    def __init__(self,parent, id,title,value):

        wx.Dialog.__init__(self, parent, id,title, size=(500,600))
        self.value=value

        self.list=[('','','','','','','')]
        self.initdb()

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer6 = wx.BoxSizer(wx.VERTICAL)

        self.m_bpButton8 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap(cwd + "\\images\\1.jpg"), wx.DefaultPosition, size=(300,200))
        bSizer6.Add(self.m_bpButton8, 10, wx.ALL | wx.EXPAND, 5)

        gSizer1 = wx.GridSizer(0, 2, 0, 0)

        self.m_staticText11 = wx.StaticText(self, wx.ID_ANY, u"商品编号:" + self.value, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11.Wrap(-1)
        gSizer1.Add(self.m_staticText11, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText12 = wx.StaticText(self, wx.ID_ANY, "价格:"+self.list[0][1]+"元\t数量："+self.list[0][5], wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText12.Wrap(-1)
        gSizer1.Add(self.m_staticText12, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText16 = wx.StaticText(self, wx.ID_ANY, u"位置:"+self.list[0][4], wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText16.Wrap(-1)
        gSizer1.Add(self.m_staticText16, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText17 = wx.StaticText(self, wx.ID_ANY, "所属商铺:"+self.list[0][0]+"_"+self.list[0][3], wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText17.Wrap(-1)
        gSizer1.Add(self.m_staticText17, 0, wx.ALL | wx.EXPAND, 5)

        bSizer6.Add(gSizer1, 1, wx.EXPAND, 5)

        bSizer7 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText13 = wx.StaticText(self, wx.ID_ANY, u"评分："+self.list[0][2], wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText13.Wrap(-1)
        bSizer7.Add(self.m_staticText13, 0, wx.ALL, 5)

        self.m_staticText14 = wx.StaticText(self, wx.ID_ANY, u"评价1", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText14.Wrap(-1)
        bSizer7.Add(self.m_staticText14, 0, wx.ALL | wx.EXPAND, 5)

        bSizer8 = wx.BoxSizer(wx.HORIZONTAL)
        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"请选择数量", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        bSizer8.Add(self.m_staticText1, 1, wx.ALL, 5)
        self.m_spinCtrl1 = wx.SpinCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                       wx.SP_ARROW_KEYS, 1, int(self.list[0][5]), 1)
        bSizer8.Add(self.m_spinCtrl1, 1, wx.ALL, 5)

        bSizer7.Add(bSizer8, 0, wx.ALL | wx.EXPAND, 5)

        bSizer6.Add(bSizer7, 1, wx.EXPAND, 5)

        self.m_button4 = wx.Button(self, wx.ID_ANY, u"购买", wx.DefaultPosition, wx.DefaultSize, 0)
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.m_button4)
        bSizer6.Add(self.m_button4, 0, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(bSizer6)
        self.Layout()

        self.Centre(wx.BOTH)

    def OnMenuExit(self, event):
        self.Close()
    def OnCloseWindow(self, event):
        self.Destroy()
    def getValue(self,value):
        self.value=value
        #print(self.value)

    def initdb(self):
        select = 'select `所属店铺`,item_inf.`价格`,item_inf.`评价`,shop_info.`店铺名称`,shop_info.`地址`,item_inf.`数量`,item_inf.`销量`' \
                 'FROM shop_info,item_inf ' \
                 'where shop_info.`店铺编号`=item_inf.`所属店铺` AND ' \
                 'item_inf.`商品编号`=\''+self.value+'\''
        my = PyMySQL(select)
        self.list = my.select_data2(self.list)
        #print("41545")
        #print(type(list[0]))

    def OnClick(self,event):
        if userone.username=="":
            dlg = wx.MessageDialog(None, u"未登录", u"提示", wx.OK | wx.ICON_QUESTION)
            if dlg.ShowModal() == wx.ID_OK:
                self.Close(True)
            dlg.Destroy()
        else:
            self.initdb1()
            #print(self.m_spinCtrl1.GetValue())
            dlg = MessageDialog(None, -1, self.m_spinCtrl1.GetValue(), self.list[0][1])
            dlg.ShowModal()
            dlg.Destroy()
            self.Close(True)

    def initdb1(self):
        insert = 'insert into purchase_inf ' \
                 'values(SYSDATE(),\''+userone.username+'\',\''+self.value+'\',\''+str(self.m_spinCtrl1.GetValue())+'\')'
        my = PyMySQL(insert)
        my.insert_date()
        self.value1=int(self.list[0][5])-self.m_spinCtrl1.GetValue()
        self.value2=int(self.list[0][6])+self.m_spinCtrl1.GetValue()
        update = 'UPDATE item_inf SET `数量`=\''+str(self.value1)+'\', `销量`=\''+str(self.value2)+'\' WHERE `商品编号`=\''\
                 +self.value+'\''
        #

        #print(update)
        my1 = PyMySQL(update)
        my1.update_data()


class MessageDialog(wx.Dialog):
    def __init__(self, parent, id,value,value1):
        wx.Dialog.__init__(self, parent, id, 'About Me', size=(300, 200))
        self.sizer1 = wx.BoxSizer(wx.VERTICAL)
        self.sizer1.Add(wx.StaticText(self, -1, u"购买成功！"),
                        0, wx.ALIGN_CENTER_HORIZONTAL | wx.TOP, border=20)
        self.sizer1.Add(wx.StaticText(self, -1, u"共购买"+str(value)),
                        0, wx.ALIGN_CENTER_HORIZONTAL | wx.TOP, border=10)
        self.value=value
        self.value1=float(value1)
        self.value2=self.value1*self.value
        self.sizer1.Add(wx.StaticText(self, -1, "共消费"+str(self.value2)+"元"),
                        0, wx.ALIGN_CENTER_HORIZONTAL | wx.TOP, border=10)
        self.sizer1.Add(wx.Button(self, wx.ID_OK), 0, wx.ALIGN_CENTER | wx.BOTTOM, border=20)
        self.SetSizer(self.sizer1)
