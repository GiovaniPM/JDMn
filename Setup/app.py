import JDMn
import JDmnGen
import json
import time
import wx
import wx.grid

def changeRowGrid(self, from_pos, to_pos):
    data = [self.GetCellValue(from_pos, col) for col in range(self.GetNumberCols())]
    self.DeleteRows(from_pos)
    self.InsertRows(to_pos)
    for col, value in enumerate(data):
        self.SetCellValue(to_pos, col, value)
    self.ForceRefresh()

def eraseGrid(self):
    num_rows = self.m_grid4.GetNumberRows()
    if num_rows > 0:
        self.m_grid4.DeleteRows(0, num_rows)
    num_rows = self.m_grid7.GetNumberRows()
    if num_rows > 0:
        self.m_grid7.DeleteRows(0, num_rows)
        self.m_grid7.AppendRows(numRows=1)
    num_cols = self.m_grid7.GetNumberCols()
    if num_cols > 1:
        self.m_grid7.DeleteCols(1, num_cols)
    self.Title = 'JDMn Setup'

class FrameAbout(JDmnGen.Rule):
    def __init__(self, parent):
        JDmnGen.About.__init__(self, parent)

class FrameExecute(JDmnGen.Rule):
    def __init__(self, parent):
        JDmnGen.Execute.__init__(self, parent)
    
    def runForest( self, event ):
        JDMnDefs = JDMn.getDefinitionsJDMn(self.m_textCtrl4.Value)
        
        dados = {}
        for row in range(self.m_grid4.GetNumberRows()):
            value = self.m_grid4.GetCellValue(row, 2)
            if value == '' or value == 'None':
                dados[self.m_grid4.GetCellValue(row, 0)] = None
            elif self.m_grid4.GetCellValue(row, 1) == 'number':
                try:
                    dados[self.m_grid4.GetCellValue(row, 0)] = int(value)
                except:
                    dados[self.m_grid4.GetCellValue(row, 0)] = float(value)
            else:
                dados[self.m_grid4.GetCellValue(row, 0)] = value
        
        startTime = time.time()
        answer, prove = JDMn.evaluateJDMn(JDMnDefs, dados, 'S')
        endTime = time.time()
        
        self.m_textCtrl5.Value = str((endTime - startTime) * 1000)[0:5] + ' ms'
        
        try:
            self.m_textCtrl41.Value = answer
        except:
            self.m_textCtrl41.Value = str(answer)

class FrameRule(JDmnGen.Rule):
    ruleReg = {}
    
    def __init__(self, parent):
        JDmnGen.Rule.__init__(self, parent)
    
    def RuleSave(self, event):
        self.ruleReg['rule'] = self.m_textCtrl1.Value
        self.ruleReg['operator'] = self.m_comboBox1.Value.strip(' ') + ' '
        self.Close()
    
    def RuleCancel(self, event):
        self.ruleReg = {}
        self.Close()

class FrameInput(JDmnGen.Input):
    inputReg = {}
    
    def __init__(self, parent):
        JDmnGen.Input.__init__(self, parent)
    
    def inputEntry( self, event ):
        self.m_comboBox1.Clear()
        for row in JDMn.valid_types:
            self.m_comboBox1.Append(row.strip())
        self.m_comboBox1.Selection = 0
    
    def InputSave(self, event):
        self.inputReg['label'] = self.m_textCtrl1.Value
        self.inputReg['typeDef'] = self.m_comboBox1.Value
        self.Close()
    
    def InputCancel(self, event):
        self.inputReg = {}
        self.Close()

class FramePrincipal(JDmnGen.JDMnSetup):
    msgTypes = ''
    areFile = False
    fileName = ''
    
    def __init__(self, parent):
        JDmnGen.JDMnSetup.__init__(self, parent)
    
    def aboutFile( self, event ):
        frame = FrameAbout(self)
        frame.ShowModal()
    
    def execTests( self, event ):
        frame = FrameExecute(self)
        frame.m_grid4.AppendRows(numRows=self.m_grid4.GetNumberRows())
        frame.m_textCtrl4.Value = self.fileName
        for row in range(self.m_grid4.GetNumberRows()):
            frame.m_grid4.SetCellBackgroundColour(row, 0, wx.Colour(255, 255, 224))
            frame.m_grid4.SetCellBackgroundColour(row, 1, wx.Colour(255, 255, 224))
            frame.m_grid4.SetReadOnly(row, 0, True)
            frame.m_grid4.SetReadOnly(row, 1, True)
            for col in range(self.m_grid4.GetNumberCols()):
                value = self.m_grid4.GetCellValue(row, col)
                frame.m_grid4.SetCellValue(row, col, value)
        frame.ShowModal()
    
    def downRule( self, event ):
        selected_rows = self.m_grid7.GetSelectedRows()
        qty = self.m_grid7.GetNumberRows() - 1
        if selected_rows:
            from_pos = selected_rows[0]
            if from_pos < qty:
                to_pos = selected_rows[0] + 1
                changeRowGrid(self.m_grid7, from_pos, to_pos)
    
    def upRule( self, event ):
        selected_rows = self.m_grid7.GetSelectedRows()
        if selected_rows:
            from_pos = selected_rows[0]
            if from_pos > 0:
                to_pos = selected_rows[0] - 1
                changeRowGrid(self.m_grid7, from_pos, to_pos)
    
    def appEntry( self, event ):
        self.msgTypes = 'Type invalid!\n\nValid Types:\n'
        for row in JDMn.valid_types:
            self.msgTypes += '    - ' +  row + '\n'
    
    def ruleColSelect(self, event):
        row = event.GetRow()
        col = event.GetCol()
        if col > 0:
            frame = FrameRule(self)
            frame.m_comboBox1.Clear()
            for operator in JDMn.dmnOperators:
                frame.m_comboBox1.Append(operator.strip())
            value = self.m_grid7.GetCellValue(row, col)
            if value != "":
                operator, rule = JDMn.splitRule(value)
                if operator != "":
                    frame.m_comboBox1.Value = operator
                    frame.m_textCtrl1.Value = rule.strip()
                else:
                    frame.m_comboBox1.Value = '== '
                    frame.m_textCtrl1.Value = value.strip()
            frame.ShowModal()
            if frame.ruleReg != {}:
                self.m_grid7.SetCellValue( row, col, frame.ruleReg['operator'] + frame.ruleReg['rule'] )
    
    def addInput(self, event):
        frame = FrameInput(self)
        frame.ShowModal()
        if frame.inputReg != {}:
            self.m_grid4.AppendRows(1)
            self.m_grid7.AppendCols(1)
            row = self.m_grid4.GetNumberRows()
            self.m_grid7.SetColLabelValue(row, frame.inputReg['label'])
            self.m_grid4.SetCellValue(row-1, 0, frame.inputReg['label'])
            self.m_grid4.SetCellValue(row-1, 1, frame.inputReg['typeDef'])
    
    def delInput(self, event):
        selected_rows = self.m_grid4.GetSelectedRows()
        selected_rows.reverse()
        if selected_rows:
            for pos in selected_rows:
                self.m_grid4.DeleteRows(pos)
                self.m_grid7.DeleteCols(pos+1)
    
    def labelChanged(self, event):
        row = event.GetRow()
        col = event.GetCol()
        value = self.m_grid4.GetCellValue(row, col)
        if col == 0:
            self.m_grid7.SetColLabelValue(row+1, value)
            self.m_grid4.SetCellValue(row, 1, 'string')
        elif col == 1:
            self.m_grid4.SetCellBackgroundColour(row, col, wx.NullColour)
            value = value.lower()
            if value not in JDMn.valid_types:
                wx.MessageBox(self.msgTypes, 'Error')
                self.m_grid4.SetCellBackgroundColour(row, col, wx.RED)
    
    def addRule(self, event):
        self.m_grid7.AppendRows(1)
    
    def delRule(self, event):
        selected_rows = self.m_grid7.GetSelectedRows()
        selected_rows.reverse()
        if selected_rows:
            for pos in selected_rows:
                self.m_grid7.DeleteRows(pos)
    
    def newFile(self, event):
        eraseGrid(self)
    
    def exitApp(self, event):
        self.Close()
    
    def openFile(self,event):
        
        openFrame = wx.Frame(None, title="Open File Dialog Example")
        
        openFileDialog = wx.FileDialog(openFrame, "Open", "", "", "JSON files (*.json)|*.json", wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        
        if openFileDialog.ShowModal() == wx.ID_OK:
            filePath = openFileDialog.GetPath()
        else:
            filePath = ''
        
        if filePath != '':
            eraseGrid(self)
            
            self.areFile = True
            self.m_menubar1.Enable(1004,True)
            self.fileName = filePath
            
            self.Title = 'JDMn Setup - ' + filePath
            
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
        
        openFileDialog.Destroy()
    
    def saveFile(self,event):
        saveFrame = wx.Frame(None, title="Open File Dialog Example")
        
        saveFileDialog = wx.FileDialog(saveFrame, "Save", "", "", "JSON files (*.json)|*.json", wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
        
        if saveFileDialog.ShowModal() == wx.ID_OK:
            filePath = saveFileDialog.GetPath()
        else:
            filePath = ''
        
        if filePath != '':        
            self.Title = 'JDMn Setup - ' + filePath
            
            self.areFile = True
            self.m_menubar1.Enable(1004,True)
            self.fileName = filePath
            
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
        
        saveFileDialog.Destroy()

app = wx.App()
frame = FramePrincipal(None)
frame.Show()
app.MainLoop()