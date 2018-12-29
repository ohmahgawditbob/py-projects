import wx

#Setup of the application window
class AppWindow():
    app = wx.App()
    titlefnt=wx.Font(); titlefnt = titlefnt.Bold(); titlefnt.PointSize = 32
    main_wind=wx.Frame(None, title="VT Software", size=(1080,720))
    panel=wx.Panel(main_wind); panel.Size = (1080,720)
    
    def __init__(self):
        #titlefnt = wx.Font(); titlefnt = titlefnt.Bold(); titlefnt.PointSize = 32
        #main_wind = wx.Frame(None, title="VT Software", size=(1080,720))
        #panel = wx.Panel(main_wind); panel.Size = (1080,720)
        self.show_main_screen()
        self.create_menubar()
        self.main_wind.Show()
        self.app.MainLoop()

    def show_create_screen(self, x=None):
        self.panel.DestroyChildren()
        title_txt = wx.StaticText(self.panel, label="Create New Sound Profile", pos=(25,25))
        title_txt.SetFont(self.titlefnt)
        #inpt = wx.FileCtrl(panel, pos=(200,25))
        menubtn = wx.Button(self.panel, label="Back", pos=(25,600))
        menubtn.Bind(wx.EVT_BUTTON, self.show_main_screen)

    def show_load_screen(self, x=None):
        self.panel.DestroyChildren()
        title_txt = wx.StaticText(self.panel, label="Load Existing Sound Profile", pos=(25,25))
        title_txt.SetFont(self.titlefnt)
        menubtn = wx.Button(self.panel, label="Back", pos=(25,600))
        menubtn.Bind(wx.EVT_BUTTON, self.show_main_screen)

    def show_main_screen(self, x=None):
        self.panel.DestroyChildren()
        maintxt = wx.StaticText(self.panel, label="VoiceTrain v0.1", pos=(25,25)); maintxt.SetFont(self.titlefnt)
        loadbtn = wx.Button(self.panel, label="Use Existing Sound Profile", pos=(75,90))
        createbtn = wx.Button(self.panel, label="Make New Sound Profile", pos=(75,125))
        createbtn.Bind(wx.EVT_BUTTON, self.show_create_screen)
        #loadbtn.Bind(wx.EVT_BUTTON, mainclick("Load Existing"))

    def controls(cmd):
        if cmd=="Exit":
            self.main_wind.Close()
        elif cmd=="":
            print(" ")

    def create_menubar(self):
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        savebtn = fileMenu.Append(-1,"&Save\tCtrl-S","Save Your Work")
        fileMenu.AppendSeparator()
        exitbtn = fileMenu.Append(-1,"&Exit","Exit Program")
        menubar.Append(fileMenu, "&File")
        window_menu = wx.Menu()
        main_menu_button = window_menu.Append(-1, "&Main Menu", "Go to the Startup Menu of the Program")
        load_menu_button = window_menu.Append(-1, "&Load Profile", "Load an existing sound profile")
        create_menu_button = window_menu.Append(-1, "&Create Profile", "Create a new sound profile")
        menubar.Append(window_menu, "&Windows")
        self.main_wind.SetMenuBar(menubar)

application = AppWindow()
