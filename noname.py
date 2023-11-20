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

###########################################################################
## Class JDMnSetup
###########################################################################

class JDMnSetup ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.Options = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.Options.CreateGrid( 1, 2 )
		self.Options.EnableEditing( True )
		self.Options.EnableGridLines( True )
		self.Options.EnableDragGridSize( False )
		self.Options.SetMargins( 0, 0 )
		
		# Columns
		self.Options.EnableDragColMove( False )
		self.Options.EnableDragColSize( True )
		self.Options.SetColLabelSize( 30 )
		self.Options.SetColLabelValue( 0, u"Label" )
		self.Options.SetColLabelValue( 1, u"Type" )
		self.Options.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.Options.EnableDragRowSize( True )
		self.Options.SetRowLabelSize( 80 )
		self.Options.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.Options.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer1.Add( self.Options, 0, wx.ALL, 5 )
		
		self.Conditions = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.Conditions.CreateGrid( 0, 0 )
		self.Conditions.EnableEditing( True )
		self.Conditions.EnableGridLines( True )
		self.Conditions.EnableDragGridSize( False )
		self.Conditions.SetMargins( 0, 0 )
		
		# Columns
		self.Conditions.EnableDragColMove( False )
		self.Conditions.EnableDragColSize( True )
		self.Conditions.SetColLabelSize( 30 )
		self.Conditions.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.Conditions.EnableDragRowSize( True )
		self.Conditions.SetRowLabelSize( 80 )
		self.Conditions.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.Conditions.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer1.Add( self.Conditions, 0, wx.ALL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

