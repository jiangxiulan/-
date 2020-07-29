import time

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
        wx.Dialog.__init__(self, parent, id,title, size=( 411,200))
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

        self.m_staticText4 = wx.StaticText(self)
        self.m_staticText4.Wrap(-1)
        gSizer1.Add(self.m_staticText4, 0, wx.ALL , 5)

        self.submit_btn2 = wx.Button(self, label=u"注册")
        self.Bind(wx.EVT_BUTTON, self.OnClick2, self.submit_btn2)
        gSizer1.Add(self.submit_btn2, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

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
        self.m_staticText4.SetLabel("")
        self.m_staticText3.SetLabel("")
        if str==['']:
            self.m_staticText3.SetLabel(u"未输入或账号不存在")
            self.m_staticText3.SetForegroundColour("red")
        elif str[0][1]==self.GetPassword() and str[0][2]==self.m_choice1Choices[self.m_choice1.Selection]:
            self.m_staticText3.SetLabel(u"欢迎" + self.GetUsername())
            userone.username = self.GetUsername()
            userone.usertype = self.m_choice1Choices[self.m_choice1.Selection]
            self.Close(True)
            self.Destroy()
        else:
            self.m_staticText3.SetLabel(u"密码错误或者身份错误")
            self.m_staticText3.SetForegroundColour("red")
    def OnClick2(self, event):
        self.m_staticText3.SetLabel("")
        self.m_staticText4.SetLabel("")
        if self.GetUsername()!="" and self.GetPassword()!="":
            test_i = 0
            if self.m_choice1Choices[self.m_choice1.Selection]=="一般用户":
                insert='INSERT INTO user_inf VALUES(\''+self.GetUsername()+'\',\''+self.GetPassword()+'\',\''+self.m_choice1Choices[self.m_choice1.Selection]+'\',\'\')'
                my = PyMySQL(insert)
                test_i=my.insert_date()
                if test_i==0:
                    test_2 = 0
                    while test_2 == 0:
                        dlg = InfoDialog(None, -1, self.GetUsername(),test_2)
                        dlg.ShowModal()
                        test_2 = dlg.set()
                        dlg.Destroy()
                    self.m_staticText4.SetLabel(u"注册成功" + self.GetUsername())
                    self.m_staticText4.SetForegroundColour("red")
                else:
                    self.m_staticText4.SetLabel("用户已存在！")
                    self.m_staticText4.SetForegroundColour("red")
                pass
            else:
                insert = 'INSERT INTO user_inf VALUES(\'' + self.GetUsername() + '\',\'' + self.GetPassword() + '\',\'' + \
                         self.m_choice1Choices[self.m_choice1.Selection] + '\',\'\')'
                my = PyMySQL(insert)
                test_i=my.insert_date()
                if test_i==0:
                    test_2=0
                    while test_2==0:
                        dlg = InfoDialog1(None, -1, self.GetUsername(),test_2)
                        dlg.ShowModal()
                        test_2=dlg.set()
                        dlg.Destroy()
                    self.m_staticText4.SetLabel(u"注册成功" + self.GetUsername())
                    self.m_staticText4.SetForegroundColour("red")
                else:
                    self.m_staticText4.SetLabel("用户已存在！")
                    self.m_staticText4.SetForegroundColour("red")
                pass

        else:
            self.m_staticText4.SetLabel(u"输入有误" + self.GetUsername())
            self.m_staticText4.SetForegroundColour("red")

class InfoDialog(wx.Dialog):
    def __init__(self, parent, id,value,value2):
        self.value=value
        self.value2=value2
        wx.Dialog.__init__(self, parent, id, '填写信息', size=(300, 200))
        self.sizer1 = wx.BoxSizer(wx.VERTICAL)
        self.sizer1.Add(wx.StaticText(self, -1, u"请填写收货地址"),
                        0, wx.ALIGN_CENTER_HORIZONTAL | wx.TOP, border=20)
        self._address = wx.TextCtrl(self)
        self.sizer1.Add(self._address,
                        0, wx.ALIGN_CENTER_HORIZONTAL | wx.TOP, border=10)
        self.button1=wx.Button(self, wx.ID_ANY,"确认")
        self.sizer1.Add(self.button1, 0, wx.ALIGN_CENTER | wx.TOP, border=10)
        self.Bind(wx.EVT_BUTTON, self.Onclick, self.button1)
        self.m_staticText = wx.StaticText(self)
        self.m_staticText.Wrap(-1)
        self.sizer1.Add(self.m_staticText, 0, wx.ALL, 5)
        self.SetSizer(self.sizer1)

    def Onclick(self,event):
        if event.GetEventObject() == self.button1:
            if self._address.GetValue() != "":
                update1 = 'UPDATE user_inf SET `收货地址`=\'' + self._address.GetValue() + '\' WHERE `用户账号`=\'' + self.value + '\''
                my = PyMySQL(update1)
                my.update_data()
                self.value2 = 1
                self.Close(True)
            else:
                self.m_staticText.SetLabel(u"有信息未填完")
                self.m_staticText.SetForegroundColour("red")

    def set(self):
#        print(self.value1)
        return self.value2
    def OnMenuExit(self, event):
        self.Close()
    def OnCloseWindow(self, event):
        self.Destroy()

class InfoDialog1(wx.Dialog):
    def __init__(self, parent, id,value,value1):
        self.value=value
        self.value1=value1
        wx.Dialog.__init__(self, parent, id, '填写信息', size=(300, 400))
        self.sizer1 = wx.BoxSizer(wx.VERTICAL)
        self.sizer1 = wx.BoxSizer(wx.VERTICAL)
        self.sizer1.Add(wx.StaticText(self, -1, u"请填写收货地址"),
                        0, wx.ALIGN_CENTER_HORIZONTAL | wx.TOP, border=20)
        self._address = wx.TextCtrl(self)
        self.sizer1.Add(self._address,
                        0, wx.ALIGN_CENTER_HORIZONTAL | wx.TOP, border=10)
        self.sizer1.Add(wx.StaticText(self, -1, u"请填写店铺编号"),
                        0, wx.ALIGN_CENTER_HORIZONTAL | wx.TOP, border=20)
        self._shopid = wx.TextCtrl(self)
        self.sizer1.Add(self._shopid,
                        0, wx.ALIGN_CENTER_HORIZONTAL | wx.TOP, border=10)
        self.sizer1.Add(wx.StaticText(self, -1, u"请填写店铺名称"),
                        0, wx.ALIGN_CENTER_HORIZONTAL | wx.TOP, border=20)
        self._shopname = wx.TextCtrl(self)
        self.sizer1.Add(self._shopname,
                        0, wx.ALIGN_CENTER_HORIZONTAL | wx.TOP, border=10)
        self.sizer1.Add(wx.StaticText(self, -1, u"请填写店铺地址"),
                        0, wx.ALIGN_CENTER_HORIZONTAL | wx.TOP, border=20)
        self._shopaddress = wx.TextCtrl(self)
        self.sizer1.Add(self._shopaddress,
                        0, wx.ALIGN_CENTER_HORIZONTAL | wx.TOP, border=10)
        self.button1=wx.Button(self, wx.ID_ANY,"确认")
        self.sizer1.Add(self.button1, 0, wx.ALIGN_CENTER | wx.TOP, border=10)
        self.Bind(wx.EVT_BUTTON, self.Onclick, self.button1)
        self.m_staticText = wx.StaticText(self)
        self.m_staticText.Wrap(-1)
        self.sizer1.Add(self.m_staticText, 0, wx.ALL, 5)
        self.SetSizer(self.sizer1)

    def Onclick(self,event):
        test_2=0
        if self._address.GetValue()!="" and self._shopid.GetValue()!="" and self._shopname.GetValue()!=""and\
                self._shopaddress.GetValue()!="":
            update1 = 'UPDATE user_inf SET `收货地址`=\'' + self._address.GetValue() + '\' WHERE `用户账号`=\'' + self.value + '\''
            my = PyMySQL(update1)
            my.update_data()
            insert = 'INSERT INTO shop_info  VALUES(\'' + self._shopid.GetValue() \
                     + '\',\'' + self._shopname.GetValue() + '\',\'' + self.value + '\',\'' \
                     + self._shopaddress.GetValue() + '\')'

            my = PyMySQL(insert)
            test_2 = my.insert_date()
            if test_2 == 1:
                self.m_staticText.SetLabel(u"商铺编号已存在！")
                self.m_staticText.SetForegroundColour("red")
            else:
                self.value1=1
                self.Close(True)
        else:
            self.m_staticText.SetLabel(u"有信息未填完")
            self.m_staticText.SetForegroundColour("red")
    def set(self):
 #       print(self.value1)
        return self.value1





    def OnMenuExit(self, event):
        self.Close()
    def OnCloseWindow(self, event):
        self.Destroy()


