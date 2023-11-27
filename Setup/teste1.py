import wx

# Create an application object
app = wx.App()

# Create a frame as the parent window
frame = wx.Frame(None, title="Open File Dialog Example")

# Create the open file dialog
openFileDialog = wx.FileDialog(frame, "Open", "", "", "Python files (*.py)|*.py", wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

# Show the dialog and get the user input
if openFileDialog.ShowModal() == wx.ID_OK:
    # Get the selected file path
    filePath = openFileDialog.GetPath()
    # Do something with the file
    print(f"You chose the file: {filePath}")

# Destroy the dialog
openFileDialog.Destroy()
