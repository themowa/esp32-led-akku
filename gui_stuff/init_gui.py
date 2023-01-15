import wx
global cl
class config_frame(wx.Frame):
    def __init__(self):
        global cl
        print(cl)
        super().__init__(parent=None, title='Hello World')
        self.SetSize((400, 300))
        self.SetTitle("config")

        self.panel_1 = wx.Panel(self, wx.ID_ANY)

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        grid_sizer_1 = wx.GridSizer(6, 5, 0, 0)
        sizer_1.Add(grid_sizer_1, 1, wx.EXPAND, 0)

        label_1 = wx.StaticText(self.panel_1, wx.ID_ANY, "start_ip:")
        grid_sizer_1.Add(label_1, 0, 0, 0)

        self.start_ip_val = wx.TextCtrl(self.panel_1, wx.ID_ANY, cl.ip_val)
        grid_sizer_1.Add(self.start_ip_val, 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        label_2 = wx.StaticText(self.panel_1, wx.ID_ANY, "Anzahl:")
        grid_sizer_1.Add(label_2, 0, 0, 0)

        self.anzahl_val = wx.SpinCtrlDouble(self.panel_1, wx.ID_ANY, initial=cl.anzahl, min=0.0, max=40.0)
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
        self.cl.anzahl=int(self.anzahl_val.GetTextValue())
        self.cl.ip_val = str(self.start_ip_val.GetValue())
        latenz=[]
        spannung=[]
        list_loss=[]
        for i in range(self.cl.anzahl):
            latenz.append("x")
            spannung.append("x")
            list_loss.append(0)
        self.cl.list_latenz=latenz
        self.cl.list_spannung=spannung
        self.cl.list_loss= list_loss
        self.cl.go=True
        wx.CallAfter(self.Close)




# end of class config_frame

class init_frame(wx.App):


    def OnInit(self):
        global cl
        self.frame = config_frame()
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

# end of class MyApp
def start(cll):
    global cl
    cl = cll
    app = init_frame()

    app.frame.cl=cll
    app.MainLoop()


if __name__ == "__main__":
    app = init_frame(0)
    app.MainLoop()
