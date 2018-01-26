"""
用面向对象的思想实现博客系统
"""
import sys
import datetime

# 保存用户的数据
users = []
# 保存文章的信息
articles = []

# 保存当前登录用户数据
loginUser = {}

# 定义一个类菜单类
class Menu:
    # 初始化数据
    def __init__(self):
        self.s = Server()
        self.s.ReadUFile()
        self.s.ReadaFile()
    # 显示开始界面
    def showMenu(self):
        print("~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~")
        print("\t1.用户注册")
        print("\t2.用户登录")
        print("\t3.退出系统")
        print("~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~")

        c = input("请输入您的选择：")
        if c == "1": #用户注册
            self.showRegistMenu()
            self.ShowbolgMenu()
        elif c == "2": # 用户登录
            self.showlogin()
            self.ShowbolgMenu()
        elif c == "3":
            self.s.WriteuFile()
            input("退出")
            sys.exit(0)
        else:
            input("输入非法！按任意键返回主界面")
            self.showMenu()

    # 展示博客界面
    def ShowbolgMenu(self):
        print("~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~")
        print("尊敬的用户：%s您好" %loginUser.nickName)
        print("欢迎使用洪立哥编写的博客系统")
        print("时间：%s" % datetime.datetime.now())
        print("\t1.查看所有文章内容\n")
        print("\t2.查看自己的文章\n")
        print("\t3.发布一篇文章\n")
        print("\t4.删除一篇文章\n")
        print("\t5.修改一篇文章\n")
        print("\t6.返回登录界面\n")
        print("~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~")

        c = input("请输入您的选择：")
        if c == "1": # 查看所有的文章
            self.chickAllarticles()
        elif c == "2":  # 查看自己发布的文章
            self.ShowloginUser()
        elif c == "3": # 发布一条文章
            self.ShowpublishMenu()
        elif c == "4": # 删除一条文章
            self.ShowRemove()
        elif c == "5": # 修改数据
            self.ShowAmend()
        elif c == "6":
            input("按任意键返回登录界面\n")
            self.showMenu()
        else:
            print("输入非法！！")
            self.showMenu()

    # 展示用户注册界面
    def showRegistMenu(self):
        global loginUser
        print("***********************")
        print("\t欢迎进行注册")
        print("***********************")
        # 用户注册
        userName = input("请输入账号：").strip()
        for u in users:
            if userName == u.userName:
                input("此账号已经被注册，请重新注册\n")
                self.showMenu()
        password = input("请输入密码：").strip()
        Qpassword = input("确认密码：").strip()
        nickName = input("请输入昵称：")
        u = User(userName, password, Qpassword, nickName)
        # 用户注册
        if password == Qpassword:
            res = self.s.regist(u)
            self.showMenu()
        else:
            input("注册失败，返回主界面")
            self.showMenu()

    # 用户登录
    def showlogin(self):
        userName = input("请输入账号：").strip()
        password = input("请输入密码：").strip()
        if len(userName) == 0 and len(password) == 0:
            input("账号或密码不能为空,请重新输入")
            self.showMenu()
        u = User(userName, password, None, None)
        res = self.s.login(u)
        if res == "登录成功":
             # 进入博客界面
            self.ShowbolgMenu()
        else:
            self.showMenu()

    # 查找所有的文章
    def chickAllarticles(self):
        self.s.chickAllarticle()
        input("查询完成，返回博客界面")
        self.ShowbolgMenu()

    # 查看当前用户的发布的文章
    def ShowloginUser(self):
        for a in articles:
            print(loginUser)
            if a.author == loginUser.nickName:
                print("你发布的文章是：%s" % a)
        #else:
            #input("没有发过文章")

    # 发布文章
    def ShowpublishMenu(self):
        title = input("标题：")
        publish = datetime.datetime.now()
        content = input("内容：")
        author = loginUser.nickName
        a = Article(title, publish, content, author)
        res = self.s.PublishArticle(a)
        print("%s" %res)
        self.ShowbolgMenu()


    # 删除文章
    def ShowRemove(self):
        self.ShowloginUser()
        title = input("请输入要删除的文章标题：")
        for a in articles:
            if a.title == title and loginUser.nickName == a.author:
                self.s.remove(a)
                self.ShowbolgMenu()
        else:
            input("没有发布这篇文章")
            self.ShowbolgMenu()

    # 修改文章
    def ShowAmend(self):
            global articles
            title = input("要修改的文章：")
            for a in articles:
                if a.title == title and loginUser.nickName == a.author:
                    content = input("修改的内容是：")
                    a.content = content
                    input("修改成功")
                    self.s.WriteaFile()
                    self.ShowbolgMenu()
                    #self.s.Amend(date, x)
            else:
                input("失败")
                self.ShowbolgMenu()
            



# 定义一个用户类
class User:
    __slots__ = ["__userName", "__password", "__nickName", "__Qpassword"]
    # 初始化用户数据
    def __init__(self, userName, password,  Qpassword, nickName):
        self.__userName = userName
        self.__password = password
        self.__Qpassword = Qpassword
        self.__nickName = nickName


    # 封装
    @property  # 相当于set
    def userName(self):
        return self.__userName
    @userName.setter
    def userName(self, name):
        self.userName = name


    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, p):
        self.__password = p

    @property
    def Qpassword(self):
        return self.__Qpassword
    @Qpassword.setter
    def Qpassswor(self, q):
        self.__Qpassword = q

    @property
    def nickName(self):
        return self.__nickName
    @nickName.setter
    def nickName(self, ni):
        self.__nickName = ni

    # 打印用户信息
    def __str__(self):
        return "账号：%s,密码：%s,昵称：%s" %(self.userName, self.password, \
                self.nickName)

# 定义一个文章类
class Article:

    # 初始化文章数据
    def __init__(self, title, publish, content, author):
        self.title = title
        self.publish = publish
        self.content = content
        self.author = author

    # 封装

    def set_title(self, title):
        self.title = title
    def get_title(self):
        return self.title

    def set_publish(self, pu):
        self.publish = pu
    def get_publish(self):
        return self.publish

    def set_content(self, content):
        self.content = content
    def get_content(self):
        return self.content

    def set_author(self, a):
        self.author = a
    def get_author(self):
        return self.author

        # 打印用户信息

    def __str__(self):
        return "题目：%s,发布日期：%s,内容：%s 作者：%s" \
               % (self.title, self.publish, self.content, self.author)


# 功能实现类
class Server:
    global articles
    global users
    global loginUser
    # 用户注册
    def regist(self, u):
        users.append(u)
        input("注册成功")
        return True

    # 用户登录

    def login(self, user):
        global loginUser
        for u in users:
            if (u.userName == user.userName) \
                    and (u.password == user.password):
                loginUser = u
                input("登录成功")
                return "登录成功"
        else:
            input("登录失败，按任意键继续")



    # 查找看所有博客
    def chickAllarticle(self):
        for a in articles:
            print("文章： %s" %a)


    # 发布文章
    def PublishArticle(self, art):
        articles.append(art)
        input("发布成功！")
        self.WriteaFile()
        return True

    # 删除文章
    def remove(self, art):
        articles.remove(art)
        input("删除成功")
        self.WriteaFile()

    # 修改文章

    def ReadUFile(self):
        import pickle
        global users
        try:
            with open("users.txt", "br") as f:
                users = pickle.load(f)
                #return True
        except:
            users = []

    def ReadaFile(self):
        import pickle
        global articles
        try:
            with open("articles.txt", "br") as f:
                articles = pickle.load(f)
                #return True
        except:
            articles = []
    def WriteuFile(self):

        import pickle
        with open("users.txt", "bw") as f:
            pickle.dump(users, f)
            #return True

    def WriteaFile(self):
        import pickle
        with open("articles.txt", "bw") as f1:
            pickle.dump(articles, f1)
            #return True




#启动程序
if __name__ == "__main__":

    menu = Menu() # 启动菜单
    menu.showMenu()

