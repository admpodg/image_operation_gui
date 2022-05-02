import wx
# for high dpi usage
import ctypes

try:
    ctypes.windll.shcore.SetProcessDpiAwareness(True)
except:
    pass


class MainWindow(wx.App):
    def __init__(self, redirect=False, filename=None):
        wx.App.__init__(self, redirect, filename)

        img = wx.EmptyImage(500, 500)
        self.frame = wx.Frame(None, title='image show', size=(1000, 1000))
        self.panel = wx.Panel(self.frame)

        # self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.imageCtrl = wx.StaticBitmap(self.frame, wx.ID_ANY, wx.BitmapFromImage(img))

        self.PhotoMaxsize = 500  # ? co to
        # self.CreateStatusBar()  # ???

        filemenu = wx.Menu()
        menuAbout = filemenu.Append(wx.ID_ABOUT, "About", "Information about this program")
        #  filemenu.AppendSeparator()
        menuExit = filemenu.Append(wx.ID_EXIT, "Exit", "Terminate this program")
        menuLoadImage = filemenu.Append(wx.ID_FILE, "Load")

        # menubar
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, "File")

        self.frame.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU, self.onAbout, menuAbout)
        self.frame.Bind(wx.EVT_MENU, self.onExit, menuExit)
        self.Bind(wx.EVT_MENU, self.load_image, menuLoadImage)

        self.frame.Show(True)

        # functions definitions

    def onAbout(self, event):
        dialog = wx.MessageDialog(None, "a small text editor", "about sample text editor", wx.OK)
        dialog.ShowModal()
        dialog.Destroy()

    def onExit(self, event):
        self.frame.Close(True)

    def load_image(self, event):
        pathname: str

        fileDialog = wx.FileDialog(None, "Open image file", wildcard="JPEG files (*.jpg)|*.jpg",
                           style=wx.FD_OPEN)

        if fileDialog.ShowModal() == wx.ID_CANCEL:
            return
        else:
            pathname = fileDialog.GetPath()
        fileDialog.Destroy()

        print("!!!path" + pathname)
        # load and show image

        img = wx.Image(pathname, wx.BITMAP_TYPE_ANY)
        W = img.GetWidth()
        H = img.GetHeight()
        print("chwała na wysokości: " + str(H))
        if W > H:
            NewW = self.PhotoMaxsize
            NewH = self.PhotoMaxsize * H / W
        else:
            NewH = self.PhotoMaxSize
            NewW = self.PhotoMaxSize * W / H

        img = img.Scale(NewW, int(NewH))

        self.imageCtrl.SetBitmap((wx.BitmapFromImage(img)))
        self.panel.Refresh()
