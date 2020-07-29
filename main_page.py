#!/usr/bin/env python
# -*- coding: utf-8 -*-

#########################################################################################
import wx
import time
import os

from Mypage import MYpage
from firstpage import FTpage
from notebook import FXNoteBook

######################################################
from recommendpage import RCpage
from user_list import userone

Version = "1.0"
ReleaseDate = "2020-7-29"
######################################################

cwd = os.getcwd()

ID_EXIT = 200
ID_ABOUT = 201


class MainFrame(wx.Frame):
    def __init__(self, parent, id, title=''):
        wx.Frame.__init__(self, parent, id, title, size=(600, 600))
        ###########################################################################################
        ###########################################################################################
        ## 状态栏的创建
        self.setupStatusBar()
        ###########################################################################################
        ###########################################################################################
        ## 创建菜单栏
        self.setupMenuBar()
        ###########################################################################################
        ###########################################################################################
        ## 显示按钮功能
        self.InitUI()
        ###########################################################################################
        ###########################################################################################
        ## 图标的实现
        self.setupIcon()




    def InitUI(self):
        ###########################################################################################
        ###########################################################################################
        ## 面板的显示
        # Attributes
        self.SetBackgroundColour("white")
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer2 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        self.m_bpButton1 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap(cwd + "\\images\\shop.png"), wx.DefaultPosition, wx.DefaultSize,
                                           wx.BU_AUTODRAW)
        bSizer3.Add(self.m_bpButton1, 0, wx.ALL| wx.EXPAND, 5)

        self.m_button4 = wx.Button(self, wx.ID_ANY, u"首页", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button4.SetBackgroundColour("#FFA500")
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.m_button4)
        bSizer3.Add(self.m_button4, 0, wx.ALL | wx.EXPAND, 5)

        self.m_button5 = wx.Button(self, wx.ID_ANY, u"推荐", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button5.SetBackgroundColour("#FFA500")
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.m_button5)
        bSizer3.Add(self.m_button5, 0, wx.ALL |  wx.EXPAND, 5)

        self.m_button6 = wx.Button(self, wx.ID_ANY, u"账号", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button6.SetBackgroundColour("#FFA500")
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.m_button6)
        bSizer3.Add(self.m_button6, 0, wx.ALL |  wx.EXPAND, 5)

        bSizer2.Add(bSizer3, 1, wx.EXPAND, 5)
        self.fxnotebook = FXNoteBook(self, -1)

        bSizer2.Add(self.fxnotebook, 5, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer2)
        self.Layout()

        self.Centre(wx.BOTH)


    def setupIcon(self):
        ###########################################################################################
        ###########################################################################################
        ## 图标的实现
        self.img_path = os.path.abspath(cwd + "\\images\\购物.png")

        icon = wx.Icon(self.img_path, type=wx.BITMAP_TYPE_PNG)
        self.SetIcon(icon)

    ###########################################################################################
    ###########################################################################################

    def setupMenuBar(self):
        ###########################################################################################
        ###########################################################################################
        ## 创建菜单栏
        ###########################################################################################
        ## 主菜单
        menubar = wx.MenuBar()
        ###########################################################################################
        ## 子菜单 ：退出(Quit)
        fmenu = wx.Menu()
        quit_menu = wx.MenuItem(fmenu, ID_EXIT, u'退出(&Q)')
        quit_menu.SetBitmap(wx.Bitmap(cwd + "\\images\\quit.png"))  # 添加一个图标
        fmenu.Append(quit_menu)  # 将选项添加到菜单中
        # fmenu.Append(ID_EXIT, u'退出(&Q)','Terminate the program')
        ## 将子菜单添加到文件(File)中
        menubar.Append(fmenu, u'文件(&F)')
        ###########################################################################################
        # 子菜单 ： 关于(About)
        hmenu = wx.Menu()
        about_menu = wx.MenuItem(fmenu, ID_ABOUT, u'关于(&A)')
        about_menu.SetBitmap(wx.Bitmap(cwd + "\\images\\about.png"))  # 添加一个图标
        hmenu.Append(about_menu)  # 将选项添加到菜单中
        ## 将子菜单添加到帮助(Help)中
        # hmenu.Append(ID_ABOUT, u'关于(&A)','More information about this program')
        menubar.Append(hmenu, u'帮助(&H)')
        ###########################################################################################
        self.SetMenuBar(menubar)
        # 菜单中子菜单，事件行为的绑定即实现
        self.Bind(wx.EVT_MENU,self.OnMenuExit,id=ID_EXIT)
        self.Bind(wx.EVT_MENU, self.OnMenuAbout, id=ID_ABOUT)
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

    ###########################################################################################
    ###########################################################################################

    def setupStatusBar(self):
        ###########################################################################################
        ###########################################################################################
        ## 状态栏的创建
        sb = self.CreateStatusBar(2)
        self.SetStatusWidths([-1, -1])
        self.SetStatusText("Ready", 0)
        # timer
        self.timer = wx.PyTimer(self.Notify)  # derived from wx.Timer
        self.timer.Start(1000, wx.TIMER_CONTINUOUS)
        self.Notify()

    ## 状态栏中时间显示格式
    def Notify(self):
        t = time.localtime(time.time())
        st = time.strftime('%Y-%m-%d   %H:%M:%S', t)
        self.SetStatusText(st, 1)

    def OnMenuExit(self, event):
        self.Close()

    def OnMenuAbout(self, event):
        dlg = AboutDialog(None, -1)
        dlg.ShowModal()
        dlg.Destroy()

    def OnCloseWindow(self, event):
        self.Destroy()

    def OnClick(self,event):
        if event.GetEventObject() == self.m_button4:
            self.fxnotebook.DeleteAllPages()
            self.txPanel = FTpage(self.fxnotebook, -1)
            self.fxnotebook.panels[0]=self.txPanel
            self.fxnotebook.AddPage(self.fxnotebook.panels[0], u"首页")
        elif event.GetEventObject() == self.m_button5:
            self.fxnotebook.DeleteAllPages()
            self.rcPanel = RCpage(self.fxnotebook, -1)
            self.fxnotebook.panels[0]=self.rcPanel
            self.fxnotebook.AddPage(self.fxnotebook.panels[0], u"推荐")
        elif   event.GetEventObject() == self.m_button6:
            self.fxnotebook.DeleteAllPages()
            self.myPanel = MYpage(self.fxnotebook, -1)
            self.fxnotebook.panels[0]=self.myPanel
            self.fxnotebook.AddPage(self.fxnotebook.panels[0], u"账号")


## 定义一个对话框
class AboutDialog(wx.Dialog):
    def __init__(self, parent, id):
        wx.Dialog.__init__(self, parent, id, 'About Me', size=(300, 200))

        self.sizer1 = wx.BoxSizer(wx.VERTICAL)
        self.sizer1.Add(wx.StaticText(self, -1, u"wxPython智慧购"),
                        0, wx.ALIGN_CENTER_HORIZONTAL | wx.TOP, border=20)
        self.sizer1.Add(wx.StaticText(self, -1, u"(C) 2020 软工小组"),
                        0, wx.ALIGN_CENTER_HORIZONTAL | wx.TOP, border=10)
        self.sizer1.Add(wx.StaticText(self, -1, "Version %s , %s" % (Version, ReleaseDate)),
                        0, wx.ALIGN_CENTER_HORIZONTAL | wx.TOP, border=10)
        self.sizer1.Add(wx.StaticText(self, -1, u"Author:将秀兰 曹文胜 王慧丽 王峰"),
                        0, wx.ALIGN_CENTER_HORIZONTAL | wx.TOP, border=10)
        self.sizer1.Add(wx.Button(self, wx.ID_OK), 0, wx.ALIGN_CENTER | wx.BOTTOM, border=20)
        self.SetSizer(self.sizer1)


class App(wx.App):
    def __init__(self):
        # 如果要重写 __init__, 必须调用wx.App的__init__，否则OnInit方法不会被调用
        super(self.__class__, self).__init__()

    # wx.App.__init__(self)

    def OnInit(self):
        self.version = u"智慧购app"
        self.title = u"wxPython之" + self.version
        self.frame = MainFrame(None, -1, self.title)
        self.SetTopWindow(self.frame)
        self.frame.Center()
        self.frame.Show(True)

        return True


if __name__ == "__main__":
    app = App()
    app.MainLoop()