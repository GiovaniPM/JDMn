import wx
import wx.grid

class GridData(wx.grid.PyGridTableBase):
    _cols = "a b c".split()
    _data = [
        "1 2 3".split(),
        "4 5 6".split(),
        "7 8 9".split()
    ]

    def GetNumberRows(self):
        return len(self._data)

    def GetNumberCols(self):
        return len(self._cols)

    def GetValue(self, row, col):
        return self._data[row][col]

    def SetValue(self, row, col, val):
        self._data[row][col] = val

    def AppendRows(self, numRows=1):
        self._data.append(["new"] * len(self._cols))
        msg = wx.grid.GridTableMessage(self, wx.grid.GRIDTABLE_NOTIFY_ROWS_APPENDED, numRows)
        self.GetView().ProcessTableMessage(msg)
        return True

class TestFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None)
        self.grid = wx.grid.Grid(self)
        self.grid.SetTable(GridData())

        btn = wx.Button(self, label="Adicionar Linha")
        btn.Bind(wx.EVT_BUTTON, self.OnAddRow)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.grid, 1, wx.EXPAND)
        sizer.Add(btn)
        self.SetSizer(sizer)

    def OnAddRow(self, event):
        self.grid.GetTable().AppendRows()

app = wx.App()
frm = TestFrame()
frm.Show()
app.MainLoop()
