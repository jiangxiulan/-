import wx
############
from datebase import PyMySQL
from user_list import userone

Version="0.1"
ReleaseDate="2020-7-5"
############

ID_EXIT=200
ID_ABOUT=201
ID_MR=100

class LoginDialog(wx.Dialog):
    def __init__(self,parent,id, title):
        wx.Dialog.__init__(self, parent, id,title, size=( 411,160))
        ###########################################################


        ###########################################################
        # 显示按钮功能
        self.initUI()

    def initUI(self):

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        bSizer2 = wx.BoxSizer(wx.VERTICAL)
        gSizer1 = wx.GridSizer(0, 2, 0, 0)
        ###########################################################
        # 显示按钮功能
        #self.panel = wx.Panel(self, -1)
        self.m_staticText1 =wx.StaticText(self, label="用户名")
        self.m_staticText1.Wrap(-1)
        gSizer1.Add(self.m_staticText1, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)
        self._username = wx.TextCtrl(self)
        gSizer1.Add(self._username, 0, wx.ALL | wx.EXPAND, 5)
        self.m_staticText2 = wx.StaticText(self, label="密码")
        self.m_staticText2.Wrap(-1)
        gSizer1.Add(self.m_staticText2, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)
        self._password = wx.TextCtrl(self, pos=(85, 45), style=wx.TE_PASSWORD)
        gSizer1.Add(self._password, 0, wx.ALL | wx.EXPAND, 5)




        self.m_choice1Choices = ["商家","一般用户"]
        self.m_choice1 = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, self.m_choice1Choices, 0)
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
        # create_table = 'create table stu(id int not null primary key auto_increment,name varchar(255) not null,age int, sex varchar(255))default charset=utf8'
        select = 'select * from user_inf where 用户账号=\''+self.GetUsername()+'\''
        # update = 'update stu set name="明明" where id=2'
        # delete = 'delete from stu where id=9'
        # insert = 'insert into stu(name,age,sex) values("%s","%d","%s")' % ('小明', 2, "男")
        # #print(select)

        my = PyMySQL(select)
        #my.create_table_func()
        #my.insert_date()
        #my.update_data()
        #my.delete_data()
        str=['',]
        str=my.select_data2(str)
        if str==['']:
            self.m_staticText3.SetLabel(u"未输入或账号不存在")
            self.m_staticText3.SetForegroundColour("red")
        elif str[0][1]==self.GetPassword() and str[0][2]==self.m_choice1Choices[self.m_choice1.Selection]:
            self.m_staticText3.SetLabel(u"欢迎" + self.GetUsername())
            userone.username = self.GetUsername()
            self.Close(True)
            self.Destroy()
        else:
            self.m_staticText3.SetLabel(u"密码错误或者身份错误")
            self.m_staticText3.SetForegroundColour("red")

        # if str[0][1]==self.GetPassword():
        #     self.m_staticText3.SetLabel(u"欢迎"+self.GetUsername())
        #     userone.username=self.GetUsername()
        #     self.Destroy()
        # else:
        #     self.m_staticText3.SetLabel(u"输入错误")
        #     self.m_staticText3.SetForegroundColour("red")



