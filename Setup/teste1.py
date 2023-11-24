import wx
import wx.grid

class TestFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="Grid", size=(640,480))
        self.grid = wx.grid.Grid(self)
        self.grid.CreateGrid(50,50)

        for row in range(20):
            for col in range(6):
                self.grid.SetCellValue(row, col, "cell (%d,%d)" % (row, col))

        # Alterando o rótulo da coluna
        self.grid.SetColLabelValue(0, "Nova Coluna")

app = wx.App(False)
frame = TestFrame()
frame.Show()
app.MainLoop()
