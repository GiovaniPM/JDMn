# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.0.0-0-g0efcecf)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid
import wx.adv

ID_NEW = 1000
ID_OPEN = 1001
ID_SAVE = 1002
ID_EXIT = 1003
ID_EXECUTE = 1004
ID_ABOUT = 1005

###########################################################################
## Class JDMnSetup
###########################################################################

class JDMnSetup ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"JDMn Setup", pos = wx.DefaultPosition, size = wx.Size( 1000,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Inputs:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		self.m_staticText1.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer2.Add( self.m_staticText1, 0, wx.ALL, 5 )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_panel6 = wx.Panel( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_panel7 = wx.Panel( self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		self.m_grid4 = wx.grid.Grid( self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )

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
		self.m_grid4.SetColLabelValue( 0, u"Label" )
		self.m_grid4.SetColLabelValue( 1, u"Type" )
		self.m_grid4.SetColLabelSize( 30 )
		self.m_grid4.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid4.EnableDragRowSize( True )
		self.m_grid4.SetRowLabelSize( 80 )
		self.m_grid4.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

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

		self.m_button1.SetBitmap( wx.Bitmap( u"Glyphs/+.png", wx.BITMAP_TYPE_ANY ) )
		self.m_button1.SetBitmapPosition( wx.TOP )
		bSizer8.Add( self.m_button1, 0, wx.BOTTOM|wx.EXPAND, 5 )

		self.m_button2 = wx.Button( self.m_panel8, wx.ID_ANY, u"Remove", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.m_button2.SetBitmap( wx.Bitmap( u"Glyphs/x.png", wx.BITMAP_TYPE_ANY ) )
		self.m_button2.SetBitmapPosition( wx.TOP )
		bSizer8.Add( self.m_button2, 0, 0, 5 )


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

		self.m_staticText2.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

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
		self.m_grid7.SetColLabelValue( 0, u"Output" )
		self.m_grid7.SetColLabelSize( 30 )
		self.m_grid7.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid7.EnableDragRowSize( True )
		self.m_grid7.SetRowLabelSize( 80 )
		self.m_grid7.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

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

		self.m_button4.SetBitmap( wx.Bitmap( u"Glyphs/+.png", wx.BITMAP_TYPE_ANY ) )
		self.m_button4.SetBitmapPosition( wx.TOP )
		bSizer12.Add( self.m_button4, 0, wx.BOTTOM|wx.EXPAND, 5 )

		self.m_button5 = wx.Button( self.m_panel11, wx.ID_ANY, u"Remove", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.m_button5.SetBitmap( wx.Bitmap( u"Glyphs/x.png", wx.BITMAP_TYPE_ANY ) )
		self.m_button5.SetBitmapPosition( wx.TOP )
		bSizer12.Add( self.m_button5, 0, wx.BOTTOM, 5 )

		self.m_button62 = wx.Button( self.m_panel11, wx.ID_ANY, u"Up", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.m_button62.SetBitmap( wx.Bitmap( u"Glyphs/u.png", wx.BITMAP_TYPE_ANY ) )
		self.m_button62.SetBitmapPosition( wx.TOP )
		bSizer12.Add( self.m_button62, 0, wx.EXPAND|wx.BOTTOM, 5 )

		self.m_button61 = wx.Button( self.m_panel11, wx.ID_ANY, u"Down", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.m_button61.SetBitmap( wx.Bitmap( u"Glyphs/d.png", wx.BITMAP_TYPE_ANY ) )
		self.m_button61.SetBitmapPosition( wx.TOP )
		bSizer12.Add( self.m_button61, 0, wx.EXPAND, 5 )


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
		self.new = wx.MenuItem( self.file, ID_NEW, u"New", wx.EmptyString, wx.ITEM_NORMAL )
		self.new.SetBitmap( wx.Bitmap( u"Glyphs/new.png", wx.BITMAP_TYPE_ANY ) )
		self.file.Append( self.new )

		self.open = wx.MenuItem( self.file, ID_OPEN, u"Open", wx.EmptyString, wx.ITEM_NORMAL )
		self.open.SetBitmap( wx.Bitmap( u"Glyphs/open.png", wx.BITMAP_TYPE_ANY ) )
		self.file.Append( self.open )

		self.save = wx.MenuItem( self.file, ID_SAVE, u"Save", wx.EmptyString, wx.ITEM_NORMAL )
		self.save.SetBitmap( wx.Bitmap( u"Glyphs/save.png", wx.BITMAP_TYPE_ANY ) )
		self.file.Append( self.save )

		self.file.AppendSeparator()

		self.exit = wx.MenuItem( self.file, ID_EXIT, u"Exit", wx.EmptyString, wx.ITEM_NORMAL )
		self.exit.SetBitmap( wx.Bitmap( u"Glyphs/exit.png", wx.BITMAP_TYPE_ANY ) )
		self.file.Append( self.exit )

		self.m_menubar1.Append( self.file, u"File" )

		self.run = wx.Menu()
		self.execute = wx.MenuItem( self.run, ID_EXECUTE, u"Execute", wx.EmptyString, wx.ITEM_NORMAL )
		self.execute.SetBitmap( wx.Bitmap( u"Glyphs/p.png", wx.BITMAP_TYPE_ANY ) )
		self.run.Append( self.execute )
		self.execute.Enable( False )

		self.m_menubar1.Append( self.run, u"Run" )

		self.help = wx.Menu()
		self.about = wx.MenuItem( self.help, ID_ABOUT, u"About", wx.EmptyString, wx.ITEM_NORMAL )
		self.help.Append( self.about )

		self.m_menubar1.Append( self.help, u"Help" )

		self.SetMenuBar( self.m_menubar1 )


		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_ACTIVATE, self.appEntry )
		self.m_grid4.Bind( wx.grid.EVT_GRID_CELL_CHANGED, self.labelChanged )
		self.m_grid4.Bind( wx.EVT_KEY_DOWN, self.keyPress1 )
		self.m_button1.Bind( wx.EVT_BUTTON, self.addInput )
		self.m_button2.Bind( wx.EVT_BUTTON, self.delInput )
		self.m_grid7.Bind( wx.grid.EVT_GRID_CELL_LEFT_DCLICK, self.ruleColSelect )
		self.m_grid7.Bind( wx.EVT_KEY_DOWN, self.keyPress2 )
		self.m_button4.Bind( wx.EVT_BUTTON, self.addRule )
		self.m_button5.Bind( wx.EVT_BUTTON, self.delRule )
		self.m_button62.Bind( wx.EVT_BUTTON, self.upRule )
		self.m_button61.Bind( wx.EVT_BUTTON, self.downRule )
		self.Bind( wx.EVT_MENU, self.newFile, id = self.new.GetId() )
		self.Bind( wx.EVT_MENU, self.openFile, id = self.open.GetId() )
		self.Bind( wx.EVT_MENU, self.saveFile, id = self.save.GetId() )
		self.Bind( wx.EVT_MENU, self.exitApp, id = self.exit.GetId() )
		self.Bind( wx.EVT_MENU, self.execTests, id = self.execute.GetId() )
		self.Bind( wx.EVT_MENU, self.aboutFile, id = self.about.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def appEntry( self, event ):
		event.Skip()

	def labelChanged( self, event ):
		event.Skip()

	def keyPress1( self, event ):
		event.Skip()

	def addInput( self, event ):
		event.Skip()

	def delInput( self, event ):
		event.Skip()

	def ruleColSelect( self, event ):
		event.Skip()

	def keyPress2( self, event ):
		event.Skip()

	def addRule( self, event ):
		event.Skip()

	def delRule( self, event ):
		event.Skip()

	def upRule( self, event ):
		event.Skip()

	def downRule( self, event ):
		event.Skip()

	def newFile( self, event ):
		event.Skip()

	def openFile( self, event ):
		event.Skip()

	def saveFile( self, event ):
		event.Skip()

	def exitApp( self, event ):
		event.Skip()

	def execTests( self, event ):
		event.Skip()

	def aboutFile( self, event ):
		event.Skip()


###########################################################################
## Class Input
###########################################################################

class Input ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Input", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

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

		self.m_staticText3.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer14.Add( self.m_staticText3, 0, 0, 5 )

		self.m_textCtrl1 = wx.TextCtrl( self.m_panel13, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		bSizer14.Add( self.m_textCtrl1, 0, 0, 5 )


		bSizer21.Add( bSizer14, 1, wx.EXPAND|wx.TOP|wx.BOTTOM, 5 )

		bSizer15 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText4 = wx.StaticText( self.m_panel13, wx.ID_ANY, u"TypeDef:", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText4.Wrap( -1 )

		self.m_staticText4.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer15.Add( self.m_staticText4, 0, 0, 5 )

		m_comboBox1Choices = [ u"date", u"number", u"string", u"boolean" ]
		self.m_comboBox1 = wx.ComboBox( self.m_panel13, wx.ID_ANY, u"Types", wx.DefaultPosition, wx.DefaultSize, m_comboBox1Choices, 0 )
		self.m_comboBox1.SetSelection( 0 )
		bSizer15.Add( self.m_comboBox1, 0, 0, 5 )


		bSizer21.Add( bSizer15, 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5 )

		bSizer25 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_panel15 = wx.Panel( self.m_panel13, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer25.Add( self.m_panel15, 0, wx.EXPAND, 5 )


		bSizer21.Add( bSizer25, 1, wx.EXPAND|wx.TOP|wx.BOTTOM, 5 )

		bSizer16 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button7 = wx.Button( self.m_panel13, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.m_button7.SetBitmap( wx.Bitmap( u"Glyphs/s.png", wx.BITMAP_TYPE_ANY ) )
		self.m_button7.SetBitmapPosition( wx.TOP )
		bSizer16.Add( self.m_button7, 0, wx.RIGHT, 5 )

		self.m_button8 = wx.Button( self.m_panel13, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.m_button8.SetBitmap( wx.Bitmap( u"Glyphs/r.png", wx.BITMAP_TYPE_ANY ) )
		self.m_button8.SetBitmapPosition( wx.TOP )
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
		self.Bind( wx.EVT_ACTIVATE, self.inputEntry )
		self.m_button7.Bind( wx.EVT_BUTTON, self.InputSave )
		self.m_button8.Bind( wx.EVT_BUTTON, self.InputCancel )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def inputEntry( self, event ):
		event.Skip()

	def InputSave( self, event ):
		event.Skip()

	def InputCancel( self, event ):
		event.Skip()


###########################################################################
## Class Rule
###########################################################################

class Rule ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Rule", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

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

		self.m_staticText4.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer15.Add( self.m_staticText4, 0, 0, 5 )

		m_comboBox1Choices = [ u"==", u"< ", u"<=", u"> ", u">=", u"not in", u"in" ]
		self.m_comboBox1 = wx.ComboBox( self.m_panel13, wx.ID_ANY, u"Types", wx.DefaultPosition, wx.DefaultSize, m_comboBox1Choices, 0 )
		self.m_comboBox1.SetSelection( 2 )
		bSizer15.Add( self.m_comboBox1, 0, 0, 5 )


		bSizer21.Add( bSizer15, 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5 )

		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText3 = wx.StaticText( self.m_panel13, wx.ID_ANY, u"Rule:", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText3.Wrap( -1 )

		self.m_staticText3.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

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

		self.m_button7.SetBitmap( wx.Bitmap( u"Glyphs/s.png", wx.BITMAP_TYPE_ANY ) )
		self.m_button7.SetBitmapPosition( wx.TOP )
		bSizer16.Add( self.m_button7, 0, wx.RIGHT, 5 )

		self.m_button8 = wx.Button( self.m_panel13, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.m_button8.SetBitmap( wx.Bitmap( u"Glyphs/r.png", wx.BITMAP_TYPE_ANY ) )
		self.m_button8.SetBitmapPosition( wx.TOP )
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
		self.Bind( wx.EVT_ACTIVATE, self.ruleEntry )
		self.m_button7.Bind( wx.EVT_BUTTON, self.RuleSave )
		self.m_button8.Bind( wx.EVT_BUTTON, self.RuleCancel )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def ruleEntry( self, event ):
		event.Skip()

	def RuleSave( self, event ):
		event.Skip()

	def RuleCancel( self, event ):
		event.Skip()


###########################################################################
## Class About
###########################################################################

class About ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer26 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel23 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer26.Add( self.m_panel23, 1, wx.EXPAND, 5 )

		self.m_panel24 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer28 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_panel26 = wx.Panel( self.m_panel24, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer28.Add( self.m_panel26, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel27 = wx.Panel( self.m_panel24, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer29 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText8 = wx.StaticText( self.m_panel27, wx.ID_ANY, u"JDMn", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText8.Wrap( -1 )

		self.m_staticText8.SetFont( wx.Font( 22, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer29.Add( self.m_staticText8, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_panel29 = wx.Panel( self.m_panel27, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer29.Add( self.m_panel29, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText9 = wx.StaticText( self.m_panel27, wx.ID_ANY, u"A DMn implementation with JSON", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText9.Wrap( -1 )

		bSizer29.Add( self.m_staticText9, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_hyperlink1 = wx.adv.HyperlinkCtrl( self.m_panel27, wx.ID_ANY, u"https://github.com/GiovaniPM/JDMn", u"https://github.com/GiovaniPM/JDMn", wx.DefaultPosition, wx.DefaultSize, wx.adv.HL_ALIGN_CENTRE|wx.adv.HL_DEFAULT_STYLE )
		bSizer29.Add( self.m_hyperlink1, 0, wx.ALL, 5 )

		self.m_panel30 = wx.Panel( self.m_panel27, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer29.Add( self.m_panel30, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText10 = wx.StaticText( self.m_panel27, wx.ID_ANY, u"Version: 1.0.9", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText10.Wrap( -1 )

		bSizer29.Add( self.m_staticText10, 0, wx.ALL|wx.EXPAND, 5 )


		self.m_panel27.SetSizer( bSizer29 )
		self.m_panel27.Layout()
		bSizer29.Fit( self.m_panel27 )
		bSizer28.Add( self.m_panel27, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel28 = wx.Panel( self.m_panel24, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer28.Add( self.m_panel28, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel24.SetSizer( bSizer28 )
		self.m_panel24.Layout()
		bSizer28.Fit( self.m_panel24 )
		bSizer26.Add( self.m_panel24, 1, wx.EXPAND, 5 )

		self.m_panel25 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer26.Add( self.m_panel25, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer26 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class Execute
###########################################################################

class Execute ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"DMn Test", pos = wx.DefaultPosition, size = wx.Size( 600,600 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer29 = wx.BoxSizer( wx.VERTICAL )

		bSizer31 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"JSON:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		bSizer31.Add( self.m_staticText10, 0, wx.ALL, 5 )

		self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.m_textCtrl4.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer31.Add( self.m_textCtrl4, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer29.Add( bSizer31, 0, wx.EXPAND, 5 )

		self.m_panel31 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer30 = wx.BoxSizer( wx.VERTICAL )

		self.m_grid4 = wx.grid.Grid( self.m_panel31, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid4.CreateGrid( 0, 3 )
		self.m_grid4.EnableEditing( True )
		self.m_grid4.EnableGridLines( True )
		self.m_grid4.EnableDragGridSize( False )
		self.m_grid4.SetMargins( 0, 0 )

		# Columns
		self.m_grid4.SetColSize( 0, 143 )
		self.m_grid4.SetColSize( 1, 111 )
		self.m_grid4.SetColSize( 2, 224 )
		self.m_grid4.EnableDragColMove( False )
		self.m_grid4.EnableDragColSize( True )
		self.m_grid4.SetColLabelValue( 0, u"Name" )
		self.m_grid4.SetColLabelValue( 1, u"Type" )
		self.m_grid4.SetColLabelValue( 2, u"Value" )
		self.m_grid4.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid4.EnableDragRowSize( True )
		self.m_grid4.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid4.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer30.Add( self.m_grid4, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel31.SetSizer( bSizer30 )
		self.m_panel31.Layout()
		bSizer30.Fit( self.m_panel31 )
		bSizer29.Add( self.m_panel31, 1, wx.EXPAND |wx.ALL, 5 )

		bSizer311 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText101 = wx.StaticText( self, wx.ID_ANY, u"Result:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText101.Wrap( -1 )

		bSizer311.Add( self.m_staticText101, 0, wx.ALL, 5 )

		self.m_textCtrl41 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		bSizer311.Add( self.m_textCtrl41, 1, wx.ALL, 5 )

		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Time Elapsed:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		bSizer311.Add( self.m_staticText12, 0, wx.ALL, 5 )

		self.m_textCtrl5 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		bSizer311.Add( self.m_textCtrl5, 0, wx.ALL, 5 )


		bSizer29.Add( bSizer311, 0, wx.EXPAND, 5 )

		bSizer33 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button13 = wx.Button( self, wx.ID_ANY, u"Execute", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.m_button13.SetBitmap( wx.Bitmap( u"Glyphs/p.png", wx.BITMAP_TYPE_ANY ) )
		self.m_button13.SetBitmapPosition( wx.TOP )
		bSizer33.Add( self.m_button13, 1, wx.ALL, 5 )

		self.m_checkBox1 = wx.CheckBox( self, wx.ID_ANY, u"Log", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer33.Add( self.m_checkBox1, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_checkBox2 = wx.CheckBox( self, wx.ID_ANY, u"Generate API call", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer33.Add( self.m_checkBox2, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_checkBox3 = wx.CheckBox( self, wx.ID_ANY, u"PUML", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer33.Add( self.m_checkBox3, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer29.Add( bSizer33, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer29 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_grid4.Bind( wx.EVT_KEY_DOWN, self.keyPress3 )
		self.m_button13.Bind( wx.EVT_BUTTON, self.runForest )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def keyPress3( self, event ):
		event.Skip()

	def runForest( self, event ):
		event.Skip()


