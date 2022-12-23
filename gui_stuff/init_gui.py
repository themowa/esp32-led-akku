import wx
class config_frame(wx.Frame):
    def __init__(self,cl):
        self.cl = "error"
        # begin wxGlade: config_frame.__init__
       # kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        super().__init__(parent=None, title='Hello World')
        self.SetSize((400, 300))
        self.SetTitle("frame")

        self.panel_1 = wx.Panel(self, wx.ID_ANY)

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        grid_sizer_1 = wx.GridSizer(6, 5, 0, 0)
        sizer_1.Add(grid_sizer_1, 1, wx.EXPAND, 0)

        label_1 = wx.StaticText(self.panel_1, wx.ID_ANY, "start_ip:")
        grid_sizer_1.Add(label_1, 0, 0, 0)

        self.start_ip_val = wx.TextCtrl(self.panel_1, wx.ID_ANY, "192.168.178.152")
        grid_sizer_1.Add(self.start_ip_val, 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        label_2 = wx.StaticText(self.panel_1, wx.ID_ANY, "Anzahl:")
        grid_sizer_1.Add(label_2, 0, 0, 0)

        self.anzahl_val = wx.SpinCtrlDouble(self.panel_1, wx.ID_ANY, initial=0, min=0.0, max=100.0)
        self.anzahl_val.SetDigits(0)
        grid_sizer_1.Add(self.anzahl_val, 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        self.ok_button = wx.Button(self.panel_1, wx.ID_ANY, "let's party")
        self.ok_button.SetToolTip("already a easteregg here?")
        grid_sizer_1.Add(self.ok_button, 0, wx.ALIGN_BOTTOM | wx.ALIGN_RIGHT, 0)

        self.panel_1.SetSizer(sizer_1)

        self.Layout()

        self.Bind(wx.EVT_BUTTON, self.init, self.ok_button)
        # end wxGlade

    def init(self, event):  # wxGlade: config_frame.<event_handler>
        self.cl.anzahl=str(self.anzahl_val.GetTextValue())
        wx.CallAfter(self.Close)

# end of class config_frame

class init_frame(wx.App):


    def OnInit(self):
        self.frame = config_frame("1234")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

# end of class MyApp
def start(cl):
    app = init_frame()
    app.frame.cl=cl
    app.MainLoop()


if __name__ == "__main__":
    app = init_frame(0)
    app.MainLoop()
