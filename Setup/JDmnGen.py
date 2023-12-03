# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

ID_OPEN = 1000
ID_SAVE = 1001
ID_EXIT = 1002

###########################################################################
## Class JDMnSetup
###########################################################################

class JDMnSetup ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"JDMn Setup", pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText1 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Inputs:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		self.m_staticText1.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer2.Add( self.m_staticText1, 0, wx.ALL, 5 )
		
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_panel6 = wx.Panel( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_panel7 = wx.Panel( self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_grid4 = wx.grid.Grid( self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.m_grid4.CreateGrid( 0, 2 )
		self.m_grid4.EnableEditing( True )
		self.m_grid4.EnableGridLines( True )
		self.m_grid4.EnableDragGridSize( False )
		self.m_grid4.SetMargins( 0, 0 )
		
		# Columns
		self.m_grid4.SetColSize( 0, 188 )
		self.m_grid4.SetColSize( 1, 202 )
		self.m_grid4.EnableDragColMove( False )
		self.m_grid4.EnableDragColSize( True )
		self.m_grid4.SetColLabelSize( 30 )
		self.m_grid4.SetColLabelValue( 0, u"Label" )
		self.m_grid4.SetColLabelValue( 1, u"Type" )
		self.m_grid4.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_grid4.EnableDragRowSize( True )
		self.m_grid4.SetRowLabelSize( 80 )
		self.m_grid4.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_grid4.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer7.Add( self.m_grid4, 1, wx.EXPAND, 5 )
		
		
		self.m_panel7.SetSizer( bSizer7 )
		self.m_panel7.Layout()
		bSizer7.Fit( self.m_panel7 )
		bSizer5.Add( self.m_panel7, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel8 = wx.Panel( self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button1 = wx.Button( self.m_panel8, wx.ID_ANY, u"Add", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.m_button1, 0, wx.BOTTOM, 5 )
		
		self.m_button2 = wx.Button( self.m_panel8, wx.ID_ANY, u"Remove", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.m_button2, 0, wx.TOP|wx.BOTTOM, 5 )
		
		self.m_button3 = wx.Button( self.m_panel8, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.m_button3, 0, wx.TOP, 5 )
		
		
		self.m_panel8.SetSizer( bSizer8 )
		self.m_panel8.Layout()
		bSizer8.Fit( self.m_panel8 )
		bSizer5.Add( self.m_panel8, 0, wx.EXPAND, 5 )
		
		
		self.m_panel6.SetSizer( bSizer5 )
		self.m_panel6.Layout()
		bSizer5.Fit( self.m_panel6 )
		bSizer4.Add( self.m_panel6, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer2.Add( bSizer4, 1, wx.EXPAND, 5 )
		
		
		self.m_panel2.SetSizer( bSizer2 )
		self.m_panel2.Layout()
		bSizer2.Fit( self.m_panel2 )
		bSizer1.Add( self.m_panel2, 1, wx.EXPAND, 5 )
		
		self.m_panel4 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,50 ), wx.TAB_TRAVERSAL )
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText2 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"Rules:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		self.m_staticText2.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer3.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_panel9 = wx.Panel( self.m_panel4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_panel10 = wx.Panel( self.m_panel9, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer11 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_grid7 = wx.grid.Grid( self.m_panel10, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.m_grid7.CreateGrid( 1, 1 )
		self.m_grid7.EnableEditing( True )
		self.m_grid7.EnableGridLines( True )
		self.m_grid7.EnableDragGridSize( False )
		self.m_grid7.SetMargins( 0, 0 )
		
		# Columns
		self.m_grid7.SetColSize( 0, 125 )
		self.m_grid7.EnableDragColMove( False )
		self.m_grid7.EnableDragColSize( True )
		self.m_grid7.SetColLabelSize( 30 )
		self.m_grid7.SetColLabelValue( 0, u"Output" )
		self.m_grid7.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_grid7.EnableDragRowSize( True )
		self.m_grid7.SetRowLabelSize( 80 )
		self.m_grid7.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_grid7.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer11.Add( self.m_grid7, 1, wx.EXPAND, 5 )
		
		
		self.m_panel10.SetSizer( bSizer11 )
		self.m_panel10.Layout()
		bSizer11.Fit( self.m_panel10 )
		bSizer10.Add( self.m_panel10, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_panel11 = wx.Panel( self.m_panel9, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer12 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button4 = wx.Button( self.m_panel11, wx.ID_ANY, u"Add", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.m_button4, 0, wx.BOTTOM, 5 )
		
		self.m_button5 = wx.Button( self.m_panel11, wx.ID_ANY, u"Remove", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.m_button5, 0, wx.TOP|wx.BOTTOM, 5 )
		
		self.m_button6 = wx.Button( self.m_panel11, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.m_button6, 0, wx.TOP, 5 )
		
		
		self.m_panel11.SetSizer( bSizer12 )
		self.m_panel11.Layout()
		bSizer12.Fit( self.m_panel11 )
		bSizer10.Add( self.m_panel11, 0, wx.EXPAND, 5 )
		
		
		self.m_panel9.SetSizer( bSizer10 )
		self.m_panel9.Layout()
		bSizer10.Fit( self.m_panel9 )
		bSizer9.Add( self.m_panel9, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer3.Add( bSizer9, 1, wx.EXPAND, 5 )
		
		
		self.m_panel4.SetSizer( bSizer3 )
		self.m_panel4.Layout()
		bSizer1.Add( self.m_panel4, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		self.m_menubar1 = wx.MenuBar( 0 )
		self.file = wx.Menu()
		self.open = wx.MenuItem( self.file, ID_OPEN, u"Open", wx.EmptyString, wx.ITEM_NORMAL )
		self.file.AppendItem( self.open )
		
		self.save = wx.MenuItem( self.file, ID_SAVE, u"Save", wx.EmptyString, wx.ITEM_NORMAL )
		self.file.AppendItem( self.save )
		
		self.exit = wx.MenuItem( self.file, ID_EXIT, u"Exit", wx.EmptyString, wx.ITEM_NORMAL )
		self.file.AppendItem( self.exit )
		
		self.m_menubar1.Append( self.file, u"File" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_grid4.Bind( wx.grid.EVT_GRID_CELL_CHANGED, self.LabelAlterado )
		self.m_button1.Bind( wx.EVT_BUTTON, self.AdicionaInput )
		self.m_button2.Bind( wx.EVT_BUTTON, self.RemoveInput )
		self.m_grid7.Bind( wx.grid.EVT_GRID_CELL_LEFT_DCLICK, self.ruleColSelect )
		self.m_button4.Bind( wx.EVT_BUTTON, self.AdicionaRule )
		self.m_button5.Bind( wx.EVT_BUTTON, self.RemoveRule )
		self.Bind( wx.EVT_MENU, self.OpenFile, id = self.open.GetId() )
		self.Bind( wx.EVT_MENU, self.SaveFile, id = self.save.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def LabelAlterado( self, event ):
		event.Skip()
	
	def AdicionaInput( self, event ):
		event.Skip()
	
	def RemoveInput( self, event ):
		event.Skip()
	
	def ruleColSelect( self, event ):
		event.Skip()
	
	def AdicionaRule( self, event ):
		event.Skip()
	
	def RemoveRule( self, event ):
		event.Skip()
	
	def OpenFile( self, event ):
		event.Skip()
	
	def SaveFile( self, event ):
		event.Skip()
	

###########################################################################
## Class Input
###########################################################################

class Input ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Input", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer12 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel10 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer12.Add( self.m_panel10, 1, wx.EXPAND, 5 )
		
		self.m_panel9 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer13 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_panel12 = wx.Panel( self.m_panel9, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer13.Add( self.m_panel12, 1, wx.EXPAND, 5 )
		
		self.m_panel13 = wx.Panel( self.m_panel9, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer21 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText3 = wx.StaticText( self.m_panel13, wx.ID_ANY, u"Label name:", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText3.Wrap( -1 )
		self.m_staticText3.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer14.Add( self.m_staticText3, 0, 0, 5 )
		
		self.m_textCtrl1 = wx.TextCtrl( self.m_panel13, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		bSizer14.Add( self.m_textCtrl1, 0, 0, 5 )
		
		
		bSizer21.Add( bSizer14, 1, wx.EXPAND|wx.TOP|wx.BOTTOM, 5 )
		
		bSizer15 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText4 = wx.StaticText( self.m_panel13, wx.ID_ANY, u"TypeDef:", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText4.Wrap( -1 )
		self.m_staticText4.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer15.Add( self.m_staticText4, 0, 0, 5 )
		
		m_comboBox1Choices = [ u"date", u"number", u"string" ]
		self.m_comboBox1 = wx.ComboBox( self.m_panel13, wx.ID_ANY, u"Types", wx.DefaultPosition, wx.DefaultSize, m_comboBox1Choices, 0 )
		self.m_comboBox1.SetSelection( 2 )
		bSizer15.Add( self.m_comboBox1, 0, 0, 5 )
		
		
		bSizer21.Add( bSizer15, 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5 )
		
		bSizer25 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_panel15 = wx.Panel( self.m_panel13, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer25.Add( self.m_panel15, 0, wx.EXPAND, 5 )
		
		
		bSizer21.Add( bSizer25, 1, wx.EXPAND|wx.TOP|wx.BOTTOM, 5 )
		
		bSizer16 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button7 = wx.Button( self.m_panel13, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer16.Add( self.m_button7, 0, wx.RIGHT, 5 )
		
		self.m_button8 = wx.Button( self.m_panel13, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer16.Add( self.m_button8, 0, wx.LEFT, 5 )
		
		
		bSizer21.Add( bSizer16, 0, wx.ALIGN_RIGHT|wx.TOP|wx.BOTTOM, 5 )
		
		
		self.m_panel13.SetSizer( bSizer21 )
		self.m_panel13.Layout()
		bSizer21.Fit( self.m_panel13 )
		bSizer13.Add( self.m_panel13, 1, wx.EXPAND, 5 )
		
		self.m_panel14 = wx.Panel( self.m_panel9, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer13.Add( self.m_panel14, 1, wx.EXPAND, 5 )
		
		
		self.m_panel9.SetSizer( bSizer13 )
		self.m_panel9.Layout()
		bSizer13.Fit( self.m_panel9 )
		bSizer12.Add( self.m_panel9, 1, wx.EXPAND, 5 )
		
		self.m_panel11 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer12.Add( self.m_panel11, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer12 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button7.Bind( wx.EVT_BUTTON, self.InputSave )
		self.m_button8.Bind( wx.EVT_BUTTON, self.InputCancel )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def InputSave( self, event ):
		event.Skip()
	
	def InputCancel( self, event ):
		event.Skip()
	

###########################################################################
## Class Rule
###########################################################################

class Rule ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Rule", pos = wx.DefaultPosition, size = wx.Size( 500,400 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer12 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel10 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer12.Add( self.m_panel10, 1, wx.EXPAND, 5 )
		
		self.m_panel9 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer13 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_panel12 = wx.Panel( self.m_panel9, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer13.Add( self.m_panel12, 1, wx.EXPAND, 5 )
		
		self.m_panel13 = wx.Panel( self.m_panel9, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer21 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer15 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText4 = wx.StaticText( self.m_panel13, wx.ID_ANY, u"Operator:", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText4.Wrap( -1 )
		self.m_staticText4.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer15.Add( self.m_staticText4, 0, 0, 5 )
		
		m_comboBox1Choices = [ u"==", u"< ", u"<=", u"> ", u">=", u"NOT IN", u"IN" ]
		self.m_comboBox1 = wx.ComboBox( self.m_panel13, wx.ID_ANY, u"Types", wx.DefaultPosition, wx.DefaultSize, m_comboBox1Choices, 0 )
		self.m_comboBox1.SetSelection( 2 )
		bSizer15.Add( self.m_comboBox1, 0, 0, 5 )
		
		
		bSizer21.Add( bSizer15, 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5 )
		
		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText3 = wx.StaticText( self.m_panel13, wx.ID_ANY, u"Rule:", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText3.Wrap( -1 )
		self.m_staticText3.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer14.Add( self.m_staticText3, 0, 0, 5 )
		
		self.m_textCtrl1 = wx.TextCtrl( self.m_panel13, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		bSizer14.Add( self.m_textCtrl1, 0, 0, 5 )
		
		
		bSizer21.Add( bSizer14, 1, wx.EXPAND|wx.TOP|wx.BOTTOM, 5 )
		
		bSizer25 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_panel15 = wx.Panel( self.m_panel13, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer25.Add( self.m_panel15, 0, wx.EXPAND, 5 )
		
		
		bSizer21.Add( bSizer25, 1, wx.EXPAND|wx.TOP|wx.BOTTOM, 5 )
		
		bSizer16 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button7 = wx.Button( self.m_panel13, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer16.Add( self.m_button7, 0, wx.RIGHT, 5 )
		
		self.m_button8 = wx.Button( self.m_panel13, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer16.Add( self.m_button8, 0, wx.LEFT, 5 )
		
		
		bSizer21.Add( bSizer16, 0, wx.ALIGN_RIGHT|wx.TOP|wx.BOTTOM, 5 )
		
		
		self.m_panel13.SetSizer( bSizer21 )
		self.m_panel13.Layout()
		bSizer21.Fit( self.m_panel13 )
		bSizer13.Add( self.m_panel13, 1, wx.EXPAND, 5 )
		
		self.m_panel14 = wx.Panel( self.m_panel9, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer13.Add( self.m_panel14, 1, wx.EXPAND, 5 )
		
		
		self.m_panel9.SetSizer( bSizer13 )
		self.m_panel9.Layout()
		bSizer13.Fit( self.m_panel9 )
		bSizer12.Add( self.m_panel9, 1, wx.EXPAND, 5 )
		
		self.m_panel11 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer12.Add( self.m_panel11, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer12 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button7.Bind( wx.EVT_BUTTON, self.RuleSave )
		self.m_button8.Bind( wx.EVT_BUTTON, self.RuleCancel )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def RuleSave( self, event ):
		event.Skip()
	
	def RuleCancel( self, event ):
		event.Skip()
	

