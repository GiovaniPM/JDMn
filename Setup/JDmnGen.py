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
		bSizer1.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel4 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,50 ), wx.TAB_TRAVERSAL )
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText2 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"Rules:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
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
		bSizer1.Add( self.m_panel4, 1, wx.EXPAND |wx.ALL, 5 )
		
		
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
		self.m_button4.Bind( wx.EVT_BUTTON, self.AdicionaRule )
		self.m_button5.Bind( wx.EVT_BUTTON, self.RemoveRule )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def LabelAlterado( self, event ):
		event.Skip()
	
	def AdicionaInput( self, event ):
		event.Skip()
	
	def RemoveInput( self, event ):
		event.Skip()
	
	def AdicionaRule( self, event ):
		event.Skip()
	
	def RemoveRule( self, event ):
		event.Skip()
	

