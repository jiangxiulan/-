import wx
import time
from wx import GetApp
############
from datebase import PyMySQL

Version="0.1"
ReleaseDate="2020-7-5"
############

ID_EXIT=200
ID_ABOUT=201
ID_MR=100

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


    def initUI(self):
        ###########################################################
        # 显示按钮功能
        self.panel=wx.Panel(self, -1)
        wx.StaticText(self.panel, label="Username",pos=(20, 20))
        wx.StaticText(self.panel, label="Password",pos=(20, 50))
        self._username=wx.TextCtrl(self.panel,pos=(85,15))
        self._password=wx.TextCtrl(self.panel,pos=(85,45),style=wx.TE_PASSWORD)
        self.submit_btn=wx.Button(self.panel,label=u"提交", pos=(20, 80), size=(50, 30))
        self.panel.Bind(wx.EVT_BUTTON, self.OnClick, self.submit_btn)

    def GetUsername(self):
        return self._username.GetValue()
    def GetPassword(self):
        return self._password.GetValue()


    def setupMenuBar(self):
        ###########################################################
        ##创建菜单栏
        # 主菜单
        menubar = wx.MenuBar()
        # 子菜单
        fmenu = wx.Menu()
        fmenu.Append(ID_EXIT, u'退出(&Q)', 'Teminate the program')
        # 将子菜单添加到文件中
        menubar.Append(fmenu, u'文件(&F)')
        # 子菜单：关于(About)
        hmenu = wx.Menu()
        # 将子菜单添加到帮助中
        hmenu.Append(ID_ABOUT, u'关于(&A)', 'More information about this program')
        menubar.Append(hmenu, u'帮助(&H)')
        self.SetMenuBar(menubar)
        # 菜单中子菜单，事件行为的绑定即实现
        wx.EVT_MENU(self, ID_EXIT, self.OnMenuExit)
        wx.EVT_MENU(self, ID_ABOUT, self.OnMenuAbout)
        wx.EVT_CLOSE(self, self.OnCloseWindow)

    def setupStatusBar(self):
        ###########################################################
        # 状态栏
        sb = self.CreateStatusBar(2)
        self.SetStatusWidths([-1, -2])
        self.SetStatusText("Ready", 0)
        # timer
        self.timer = wx.PyTimer(self.Notify)
        self.timer.Start(100, wx.TIMER_CONTINUOUS)
        self.Notify()

    def OnClick(self,event):
        if event.GetEventObject()==self.submit_btn:
            dlg = LoginDialog(None, -1)
            dlg.ShowModal()
            dlg.Destroy()
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
        wx.Dialog.__init__(self,parent,id,'About Me',size=(200,300))

        self.sizerl=wx.BoxSizer(wx.VERTICAL)
        self.sizerl.Add(wx.StaticText(self,-1,u'wxPython初级教程'),
                        0,wx.ALIGN_CENTER_HORIZONTAL|wx.Top,border=20)
        self.sizerl.Add(wx.StaticText(self, -1, u'(C)2020 工作室))'),
                        0, wx.ALIGN_CENTER_HORIZONTAL | wx.Top, border=10)
        self.sizerl.Add(wx.StaticText(self, -1, u"Version,%s %s"%(Version,ReleaseDate)),
                         0, wx.ALIGN_CENTER_HORIZONTAL | wx.Top, border=10)
        self.sizerl.Add(wx.StaticText(self, -1, u'Author:曹文胜'),
                         0, wx.ALIGN_CENTER_HORIZONTAL | wx.Top, border=10)
        self.sizerl.Add(wx.Button(self, wx.ID_OK),0, wx.ALIGN_CENTER|wx.BOTTOM, border=20)
        self.SetSizer(self.sizerl)


class LoginDialog(wx.Dialog):
    def __init__(self,parent, id,):
        wx.Dialog.__init__(self, parent, id, size=( 411,160))
        ###########################################################


        ###########################################################
        # 显示按钮功能
        self.initUI()

    def initUI(self):

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        bSizer2 = wx.BoxSizer(wx.VERTICAL)
        gSizer1 = wx.GridSizer(0, 2, 0, 0)
        ###########################################################
        # 显示按钮功能
        #self.panel = wx.Panel(self, -1)
        self.m_staticText1 =wx.StaticText(self, label="Username")
        self.m_staticText1.Wrap(-1)
        gSizer1.Add(self.m_staticText1, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)
        self._username = wx.TextCtrl(self)
        gSizer1.Add(self._username, 0, wx.ALL | wx.EXPAND, 5)
        self.m_staticText2 = wx.StaticText(self, label="Password")
        self.m_staticText2.Wrap(-1)
        gSizer1.Add(self.m_staticText2, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)
        self._password = wx.TextCtrl(self, pos=(85, 45), style=wx.TE_PASSWORD)
        gSizer1.Add(self._password, 0, wx.ALL | wx.EXPAND, 5)




        m_choice1Choices = ["商家","一般用户"]
        self.m_choice1 = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice1Choices, 0)
        self.m_choice1.SetSelection(0)
        gSizer1.Add(self.m_choice1, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.submit_btn = wx.Button(self, label=u"提交")
       # bSizer2.Add(self.submit_btn, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.submit_btn)
        gSizer1.Add(self.submit_btn, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)
        bSizer2.Add(gSizer1, 1, wx.EXPAND, 5)

        self.m_staticText3 = wx.StaticText(self, wx.ID_ANY,wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)
        bSizer2.Add(self.m_staticText3, 0, wx.ALL , 5)


        self.SetSizer(bSizer2)
        self.Layout()
        self.Centre(wx.BOTH)

    def GetUsername(self):
        return self._username.GetValue()

    def GetPassword(self):
        return self._password.GetValue()



    #
    # def OnClick(self, event):
    #     if event.GetEventObject() == self.submit_btn:
    #         self.Destroy()
    #     else:
    #         print("No Button is clicked")

    def OnMenuExit(self, event):
        self.Close()
    def OnCloseWindow(self, event):
        self.Destroy()

    # 定义一个对话框

    def OnClick(self,event):
        create_table = 'create table stu(id int not null primary key auto_increment,name varchar(255) not null,age int, sex varchar(255))default charset=utf8'
        select = 'select * from user_inf where 用户账号=\''+self.GetUsername()+'\''
        update = 'update stu set name="明明" where id=2'
        delete = 'delete from stu where id=9'
        insert = 'insert into stu(name,age,sex) values("%s","%d","%s")' % ('小明', 2, "男")
        print(select)

        order=select
        my = PyMySQL(order)
        #my.create_table_func()
        #my.insert_date()
        #my.update_data()
        #my.delete_data()
        str="12"
        str=my.select_data(str)
        print(str)
        if str==self.GetPassword():
            self.m_staticText3.SetLabel(u"欢迎"+self.GetUsername())
            #time.sleep(3)
            self.Destroy()
        else:
            self.m_staticText3.SetLabel(u"输入错误")





