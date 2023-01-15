import wx

class main_frame(wx.Frame):
    def __init__(self):
        global cl
        self.val_lost="1"
        self.cl = cl
        super().__init__(parent=None, title='Hello main frame')

        # variable gui
        self.size = self.cl.anzahl+1

        self.SetSize((700, self.size*40))
        self.SetTitle("oh helloooo")

        self.panel_1 = wx.Panel(self, wx.ID_ANY)

        sizer_1 = wx.BoxSizer(wx.VERTICAL)



        grid_sizer_1 = wx.GridSizer(self.size, 4, 0, 0)
        sizer_1.Add(grid_sizer_1, 1, wx.EXPAND, 0)

        label_1 = wx.StaticText(self.panel_1, wx.ID_ANY, "Adresse:")
        grid_sizer_1.Add(label_1, 0, 0, 0)

        label_2 = wx.StaticText(self.panel_1, wx.ID_ANY, "Spannung:")
        grid_sizer_1.Add(label_2, 0, 0, 0)

        label_3 = wx.StaticText(self.panel_1, wx.ID_ANY, "Verlorene Anfragen:")
        grid_sizer_1.Add(label_3, 0, 0, 0)

        label_4 = wx.StaticText(self.panel_1, wx.ID_ANY, "Latenz:")
        grid_sizer_1.Add(label_4, 0, 0, 0)

        for i in range(self.size-1):
            w = self.cl.ip_val.split(".")
            w[-1] = str(int(w[-1]) + i)
            if (int(w[-1]) > 255):
                w[-1] = str(int(w[-1]) - 255)
                w[-2] = str(int(w[-2]) + 1)
            ip_val = w[0] + "." + w[1] + "." + w[2] + "." + w[3]

            name_1 = wx.StaticText(self.panel_1, wx.ID_ANY, ip_val)
            grid_sizer_1.Add(name_1, 0, 0, 0)



            self.__dict__["label_spannung_" + str(i)] = wx.StaticText(self.panel_1, wx.ID_ANY, "x")
            grid_sizer_1.Add(self.__dict__["label_spannung_" + str(i)], 0, 0, 0)

            self.__dict__["label_verloren_"+str(i)] = wx.StaticText(self.panel_1, wx.ID_ANY, "x")
            grid_sizer_1.Add(self.__dict__["label_verloren_"+str(i)], 0, 0, 0)

            self.__dict__["label_ping_" + str(i)] = wx.StaticText(self.panel_1, wx.ID_ANY, "x")
            grid_sizer_1.Add(self.__dict__["label_ping_" + str(i)], 0, 0, 0)


        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.panel_1.SetSizer(sizer_1)

        self.Layout()
        self.on_timer()

    def on_timer(self):
        for i in range(self.size - 1):
            self.__dict__["label_ping_" + str(i)].SetLabel(self.cl.list_latenz[i])
            self.__dict__["label_verloren_"+str(i)].SetLabel(str(self.cl.list_loss[i]))
            self.__dict__["label_spannung_" + str(i)].SetLabel(str(self.cl.list_spannung[i]))

        wx.CallLater(1000, self.on_timer)


        # end wxGlade

    def init(self, event):  # wxGlade: config_frame.<event_handler>
        print(self.val_lost)

    def OnClose(self, event):
        self.cl.terminate=True
        self.Destroy()
        return


        # end wxGlade

# end of class main_frame

class main_frame_init(wx.App):
    def OnInit(self):
        self.frame = main_frame()
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

# end of class MyApp


def start_main(cll):
    global cl
    cl=cll
    app = main_frame_init()
    #app.frame.cl=cl
    app.MainLoop()

if __name__ == "__main__":
    app = start_main(0)
    app.MainLoop()
