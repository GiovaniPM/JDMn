import JDMn
import JDmnGen
import json
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
    
    def OpenFile(self,event):
        openFrame = wx.Frame(None, title="Open File Dialog Example")
        
        openFileDialog = wx.FileDialog(openFrame, "Open", "", "", "JSON files (*.json)|*.json", wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        
        if openFileDialog.ShowModal() == wx.ID_OK:
            filePath = openFileDialog.GetPath()
        
        openFileDialog.Destroy()
        
        decisionTable = JDMn.getDefinitionsJDMn(filePath)
        
        inputs  = decisionTable ['input'  ]
        rules   = decisionTable ['rule'   ]
        
        row = self.m_grid4.GetNumberRows()
        
        for input in inputs:
            expression = input         ['inputExpression']
            label      = expression    ['label'          ]
            typeValue  = expression    ['typeRef'        ]
            
            self.m_grid4.AppendRows(1)
            self.m_grid7.AppendCols(1)
            
            self.m_grid4.SetCellValue(row, 0, label)
            self.m_grid4.SetCellValue(row, 1, typeValue)
            self.m_grid7.SetColLabelValue(row+1, label)
            
            row += 1
        
        row = 0
        
        for rule in rules:
            entrys = rule['inputEntry']
            output = rule['outputEntry']
            
            col = 1
            
            if row > 0:
                self.m_grid7.AppendRows(1)
            
            for entry in entrys:
                self.m_grid7.SetCellValue(row, col, entry['text'])
                
                col += 1
            
            self.m_grid7.SetCellValue(row, 0, str(output['text']))
            
            row += 1
    
    def SaveFile(self,event):
        saveFrame = wx.Frame(None, title="Open File Dialog Example")
        
        saveFileDialog = wx.FileDialog(saveFrame, "Save", "", "", "JSON files (*.json)|*.json", wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
        
        if saveFileDialog.ShowModal() == wx.ID_OK:
            filePath = saveFileDialog.GetPath()
        
        saveFileDialog.Destroy()
        
        row = 0
        col = 0
        
        maxRow = self.m_grid4.GetNumberRows()
        maxCol = self.m_grid4.GetNumberCols()
        
        inputs = []
        
        for row in range(0, maxRow):
            inputExpression = {}
            input = {}
            input['label'] = self.m_grid4.GetCellValue(row, 0)
            input['typeRef'] = self.m_grid4.GetCellValue(row, 1)
            inputExpression['inputExpression'] = input
            inputs.append(inputExpression)
        
        maxRow = self.m_grid7.GetNumberRows()
        maxCol = self.m_grid7.GetNumberCols()
        
        rules = []
        
        for row in range(0, maxRow):
            rule = {}
            input = []
            output = {}
            for col in range(1, maxCol):
                entry = {}
                entry['text'] = self.m_grid7.GetCellValue(row, col)
                input.append(entry)
            rule['inputEntry'] = input
            output['text'] = self.m_grid7.GetCellValue(row, 0)
            rule['outputEntry'] = output
            rules.append(rule)
        
        decisionTable = {}
        decisionTable ['input'  ] = inputs
        decisionTable ['rule'   ] = rules
        
        decision = {}
        decision      ['decisionTable' ] = decisionTable
        
        definitions = {}
        definitions   ['decision'      ] = decision
        
        dados = {}
        dados         ['definitions'   ] = definitions
        
        with open(filePath, "w") as f:
            json.dump(dados, f)

app = wx.App()
frame = FramePrincipal(None)
frame.Show()
app.MainLoop()