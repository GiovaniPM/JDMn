///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version Jun 17 2015)
// http://www.wxformbuilder.org/
//
// PLEASE DO "NOT" EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#include "noname.h"

///////////////////////////////////////////////////////////////////////////

JDMn Setup::JDMn Setup( wxWindow* parent, wxWindowID id, const wxString& title, const wxPoint& pos, const wxSize& size, long style ) : wxFrame( parent, id, title, pos, size, style )
{
	this->SetSizeHints( wxDefaultSize, wxDefaultSize );
	
	wxBoxSizer* bSizer1;
	bSizer1 = new wxBoxSizer( wxVERTICAL );
	
	Options = new wxGrid( this, wxID_ANY, wxDefaultPosition, wxDefaultSize, 0 );
	
	// Grid
	Options->CreateGrid( 1, 2 );
	Options->EnableEditing( true );
	Options->EnableGridLines( true );
	Options->EnableDragGridSize( false );
	Options->SetMargins( 0, 0 );
	
	// Columns
	Options->EnableDragColMove( false );
	Options->EnableDragColSize( true );
	Options->SetColLabelSize( 30 );
	Options->SetColLabelValue( 0, wxT("Label") );
	Options->SetColLabelValue( 1, wxT("Type") );
	Options->SetColLabelAlignment( wxALIGN_CENTRE, wxALIGN_CENTRE );
	
	// Rows
	Options->EnableDragRowSize( true );
	Options->SetRowLabelSize( 80 );
	Options->SetRowLabelAlignment( wxALIGN_CENTRE, wxALIGN_CENTRE );
	
	// Label Appearance
	
	// Cell Defaults
	Options->SetDefaultCellAlignment( wxALIGN_LEFT, wxALIGN_TOP );
	bSizer1->Add( Options, 0, wxALL, 5 );
	
	Conditions = new wxGrid( this, wxID_ANY, wxDefaultPosition, wxDefaultSize, 0 );
	
	// Grid
	Conditions->CreateGrid( 5, 5 );
	Conditions->EnableEditing( true );
	Conditions->EnableGridLines( true );
	Conditions->EnableDragGridSize( false );
	Conditions->SetMargins( 0, 0 );
	
	// Columns
	Conditions->EnableDragColMove( false );
	Conditions->EnableDragColSize( true );
	Conditions->SetColLabelSize( 30 );
	Conditions->SetColLabelAlignment( wxALIGN_CENTRE, wxALIGN_CENTRE );
	
	// Rows
	Conditions->EnableDragRowSize( true );
	Conditions->SetRowLabelSize( 80 );
	Conditions->SetRowLabelAlignment( wxALIGN_CENTRE, wxALIGN_CENTRE );
	
	// Label Appearance
	
	// Cell Defaults
	Conditions->SetDefaultCellAlignment( wxALIGN_LEFT, wxALIGN_TOP );
	bSizer1->Add( Conditions, 0, wxALL, 5 );
	
	
	this->SetSizer( bSizer1 );
	this->Layout();
	
	this->Centre( wxBOTH );
}

JDMn Setup::~JDMn Setup()
{
}
