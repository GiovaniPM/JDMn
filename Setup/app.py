import JDmnGen
import wx

valid_types = ['string', 'number']

class FramePrincipal(JDmnGen.JDMnSetup):
    def __init__(self, parent):
        JDmnGen.JDMnSetup.__init__(self, parent)
    
    def AdicionaInput(self, event):
        self.m_grid4.AppendRows(1)
        self.m_grid7.AppendCols(1)
    
    def RemoveInput(self, event):
        selected_rows = self.m_grid4.GetSelectedRows()
        selected_rows.reverse()
        if selected_rows:
            for pos in selected_rows:
                self.m_grid4.DeleteRows(pos)
                self.m_grid7.DeleteCols(pos+1)
    
    def LabelAlterado(self, event):
        row = event.GetRow()
        col = event.GetCol()
        value = self.m_grid4.GetCellValue(row, col)
        if col == 0:
            self.m_grid7.SetColLabelValue(row+1, value)
            self.m_grid4.SetCellValue(row, 1, 'string')
        elif col == 1:
            self.m_grid4.SetCellBackgroundColour(row, col, wx.NullColour)
            value = value.lower()
            if value not in valid_types:
                wx.MessageBox('Type invalid!\n\nValid Types:\n    - string\n    - number', 'Error')
                self.m_grid4.SetCellBackgroundColour(row, col, wx.RED)
    
    def AdicionaRule(self, event):
        self.m_grid7.AppendRows(1)
    
    def RemoveRule(self, event):
        selected_rows = self.m_grid7.GetSelectedRows()
        selected_rows.reverse()
        if selected_rows:
            for pos in selected_rows:
                self.m_grid7.DeleteRows(pos)

app = wx.App()
frame = FramePrincipal(None)
frame.Show()
app.MainLoop()