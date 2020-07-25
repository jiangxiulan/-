#!/usr/bin/env python
# -*- coding: utf-8 -*-

#########################################################################################
import wx
import time
import os, sys
from Ui.notebook import FXNoteBook

######################################################
Version = "1.0"
ReleaseDate = "2020-7-29"
######################################################

cwd = os.getcwd()

ID_EXIT = 200
ID_ABOUT = 201


class MainFrame(wx.Frame):
    def __init__(self, parent, id, title=''):
        wx.Frame.__init__(self, parent, id, title, size=(500, 600))
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
        self.fxnotebook = FXNoteBook(self, -1)

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
        fmenu.AppendItem(quit_menu)  # 将选项添加到菜单中
        # fmenu.Append(ID_EXIT, u'退出(&Q)','Terminate the program')
        ## 将子菜单添加到文件(File)中
        menubar.Append(fmenu, u'文件(&F)')
        ###########################################################################################
        # 子菜单 ： 关于(About)
        hmenu = wx.Menu()
        about_menu = wx.MenuItem(fmenu, ID_ABOUT, u'关于(&A)')
        about_menu.SetBitmap(wx.Bitmap(cwd + "\\images\\about.png"))  # 添加一个图标
        hmenu.AppendItem(about_menu)  # 将选项添加到菜单中
        ## 将子菜单添加到帮助(Help)中
        # hmenu.Append(ID_ABOUT, u'关于(&A)','More information about this program')
        menubar.Append(hmenu, u'帮助(&H)')
        ###########################################################################################
        self.SetMenuBar(menubar)
        # 菜单中子菜单，事件行为的绑定即实现
        wx.EVT_MENU(self, ID_EXIT, self.OnMenuExit)
        wx.EVT_MENU(self, ID_ABOUT, self.OnMenuAbout)
        wx.EVT_CLOSE(self, self.OnCloseWindow)

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