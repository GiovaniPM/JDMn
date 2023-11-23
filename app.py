import JDmnGen
import wx

class FramePrincipal(JDmnGen.JDMnSetup):
    def __init__(self, parent):
        JDmnGen.JDMnSetup.__init__(self, parent)
    
    def AdicionaInput(self, event):
        print('Ola')

app = wx.App()
frame = FramePrincipal(None)
frame.Show()
app.MainLoop()