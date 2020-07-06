import wx
import time
import os
############
Version="0.1"
ReleaseDate="2020-7-5"
############

cwd=os.getcwd()

ID_EXIT=200
ID_ABOUT=201


class Mainframe(wx.Frame):
    def __init__(self,parent,id,title):
        wx.Frame.__init__(self,parent,id,title,size=(500,300))
        ###########################################################
        # 状态栏
        self.setupStatusBar()
        ###########################################################
        ##创建菜单栏
        self.setupMenuBar()
        ###########################################################
        # 显示按钮功能
        self.initUI()
        ###########################################################
        # 图标的实现
        self.setupIcon()

    def initUI(self):
        ###########################################################
        # 面板显示
        self.panel=MyPanel(self, -1)
        wx.StaticText(self.panel,label="Username",pos=(20,20))
        wx.StaticText(self.panel,label="Password",pos=(20,50))
        self.panel._username = wx.TextCtrl(self.panel, pos=(85, 15))
        self.panel._password = wx.TextCtrl(self.panel, pos=(85, 45), style=wx.TE_PASSWORD)
        self.panel.submit_btn = wx.Button(self.panel, label=u"提交", pos=(20, 80), size=(50, 30))
        self.Bind(wx.EVT_BUTTON, self.panel.OnClick, self.panel.submit_btn)



    def setupIcon(self):
        ###########################################################
        ##图标的实现
        self.img_path=os.path.abspath("./alienware.png")
        icon=wx.Icon(self.img_path,type=wx.BITMAP_TYPE_PNG)
        self.SetIcon(icon)

    def setupMenuBar(self):
        ###########################################################
        ##创建菜单栏
        # 主菜单
        menubar = wx.MenuBar()
        # 子菜单
        fmenu = wx.Menu()
        quit_menu=wx.MenuItem(fmenu,ID_EXIT, u'退出(&Q)')
        quit_menu.SetBitmap(wx.Bitmap('quit.png'))
        fmenu.AppendItem(quit_menu)

        #fmenu.Append(ID_EXIT, u'退出(&Q)', 'Teminate the program')
        # 将子菜单添加到文件中
        menubar.Append(fmenu, u'文件(&F)')
        # 子菜单：关于(About)
        hmenu = wx.Menu()
        about_menu = wx.MenuItem(fmenu, ID_ABOUT, u'关于(&A)')
        about_menu.SetBitmap(wx.Bitmap('about.png'))
        hmenu.AppendItem(about_menu)
        # 将子菜单添加到帮助中
        #hmenu.Append(ID_ABOUT, u'关于(&A)', 'More information about this program')
        menubar.Append(hmenu, u'帮助(&H)')
        self.SetMenuBar(menubar)
        # 菜单中子菜单，事件行为的绑定即实现
        wx.EVT_MENU(self, ID_EXIT, self.OnMenuExit)
        wx.EVT_MENU(self, ID_ABOUT, self.OnMenuAbout)
        wx.EVT_CLOSE(self, self.OnCloseWindow)

    def setupStatusBar(self):
        ################################################    ###########
        # 状态栏
        sb = self.CreateStatusBar(2)
        self.SetStatusWidths([-2, -1])
        self.SetStatusText("Ready", 0)
        # timer
        self.timer = wx.PyTimer(self.Notify)
        self.timer.Start(1000, wx.TIMER_CONTINUOUS)
        self.Notify()

    def OnClick(self,event):
        if event.GetEventObject()==self.buttonOK:
            print("{}" .format(event.GetEventObject().GetLabel()))
        elif event.GetEventObject()==self.buttonCancel:
            print("{}".format(event.GetEventObject().GetLabel()))
        else:
            print("No Button is clicked")

    def Notify(self):
        t=time.localtime(time.time())
        st=time.strftime('%Y-%m-%d  %H:%M:%S',t)
        self.SetStatusText(st,1)

    def OnMenuExit(self,event):
        self.Close()

    def OnMenuAbout(self,event):
        dlg=AboutDialog(None,-1)
        dlg.ShowModal()
        dlg.Destroy()

    def OnCloseWindow(self,event):
        self.Destroy()



#定义一个对话框
class AboutDialog(wx.Dialog):
    def __init__(self,parent,id):
        wx.Dialog.__init__(self,parent,id,'About Me',size=(200,200))

        self.sizerl=wx.BoxSizer(wx.VERTICAL)
        self.sizerl.Add(wx.StaticText(self,-1,u'wxPython初级教程'),
                        0,wx.ALIGN_CENTER_HORIZONTAL|wx.Top,border=20)
        self.sizerl.Add(wx.StaticText(self, -1, u'(C)2020 工作室))'),
                        0, wx.ALIGN_CENTER_HORIZONTAL | wx.Top, border=10)
        self.sizerl.Add(wx.StaticText(self, -1, u"Version,%s %s"%(Version,ReleaseDate)),
                         0, wx.ALIGN_CENTER_HORIZONTAL | wx.Top, border=10)
        self.sizerl.Add(wx.StaticText(self, -1, u'Author:樊晓鑫'),
                         0, wx.ALIGN_CENTER_HORIZONTAL | wx.Top, border=10)
        self.sizerl.Add(wx.Button(self, wx.ID_OK),0, wx.ALIGN_CENTER|wx.BOTTOM, border=20)
        self.SetSizer(self.sizerl)

class MyPanel(wx.Panel):
    def __init__(self,parent,id):
        super(MyPanel,self).__init__(parent,id)

    def GetUsername(self):
        return self._username.GetValue()

    def GetPassword(self):
        return self._password.GetValue()
    def OnClick(self,event):
        if event.GetEventObject()==self.submit_btn:
            dlg=LoginDialog(None,-1)
            dlg.ShowModal()
            dlg.Destroy()
        else:
            print("No Button is clicked")


class LoginDialog(wx.Dialog):
    def __init__(self,parent, id):
        super(LoginDialog, self).__init__(parent, id, u'显示', size=(200, 200))
        self.app=wx.GetApp()
        self.panel=self.app.frame.panel
        self._username_dlg=wx.StaticText(self, label=u"用户名:"+self.GetUsername(), pos=(20, 20))
        self._password_dlg=wx.StaticText(self, label=u"密 码:"+self.GetPassword(), pos=(20, 50))
        wx.Button(self, wx.ID_OK,pos=(20, 80))

    def GetUsername(self):
        return self.panel.GetUsername()

    def GetPassword(self):
        return self.panel.GetPassword()



class App(wx.App):
    def __init__(self):
        super(self.__class__,self).__init__()

    def OnInit(self):
        self.version=u"第二堂课"
        self.title=u"wxPython初级教程之"+self.version
        self.frame=Mainframe(None,-1,self.title)
        self.frame.Center()
        self.frame.Show(True)

        return True

if __name__=="__main__":
    app=App()
    app.MainLoop()
