import wx

class NameDialog(wx.Dialog):
    def __init__(self, parent):
        # Create a dialog with a title
        wx.Dialog.__init__(self, parent, title="Name Dialog")
        # Create a panel in the dialog
        panel = wx.Panel(self)
        # Create a text control for the user input
        self.text = wx.TextCtrl(panel, pos=(50, 50))
        # Create a button to submit the input
        button = wx.Button(panel, label="OK", pos=(50, 100))
        # Bind a handler to the button click event
        button.Bind(wx.EVT_BUTTON, self.OnOK)

    def OnOK(self, event):
        # Get the user input from the text control
        name = self.text.GetValue()
        # Set the return code of the dialog as the name
        self.SetReturnCode(name)
        # Close the dialog
        self.Close()

# Create an app object and start the main loop
app = wx.App()
frame = wx.Frame(None, title="Main Window")
dialog = NameDialog(frame)
name = dialog.ShowModal()
print(f"The name is {name}")
