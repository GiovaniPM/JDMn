unit Unit1;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, ExtCtrls, StdCtrls,
  ValEdit, Grids, Buttons, Menus;

type

  { TForm1 }

  TForm1 = class(TForm)
    Button1: TButton;
    GroupBox1: TGroupBox;
    GroupBox2: TGroupBox;
    MainMenu1: TMainMenu;
    MenuItem1: TMenuItem;
    MenuItem2: TMenuItem;
    MenuItem3: TMenuItem;
    MenuItem4: TMenuItem;
    StringGrid1: TStringGrid;
    StringGrid2: TStringGrid;
    procedure Button1Click(Sender: TObject);
    procedure FormCreate(Sender: TObject);
    procedure GroupBox1Click(Sender: TObject);
    procedure GroupBox2Click(Sender: TObject);
    procedure SpeedButton1Click(Sender: TObject);
    procedure StringGrid1ColRowExchanged(Sender: TObject; IsColumn: Boolean;
      sIndex, tIndex: Integer);
    procedure StringGrid1EditingDone(Sender: TObject);
  private
    procedure GridDeleteRow(RowNumber: Integer; Grid: TstringGrid);
  public

  end;

var
  Form1: TForm1;

implementation

{$R *.frm}

{ TForm1 }
procedure TForm1.GridDeleteRow(RowNumber: Integer; Grid: TstringGrid);
var
  i: Integer;
begin
  Grid.Row := RowNumber;
  if (Grid.Row = Grid.RowCount - 1) then
    { On the last row}
    Grid.RowCount := Grid.RowCount - 1
  else
  begin
    { Not the last row}
    for i := RowNumber to Grid.RowCount - 1 do
      Grid.Rows[i] := Grid.Rows[i + 1];
    Grid.RowCount := Grid.RowCount - 1;
  end;
end;

procedure TForm1.GroupBox1Click(Sender: TObject);
begin

end;

procedure TForm1.GroupBox2Click(Sender: TObject);
begin

end;

procedure TForm1.SpeedButton1Click(Sender: TObject);
begin

end;

procedure TForm1.StringGrid1ColRowExchanged(Sender: TObject; IsColumn: Boolean;
  sIndex, tIndex: Integer);
begin

end;

procedure TForm1.StringGrid1EditingDone(Sender: TObject);
var
  lin, col: integer;
begin
  lin := StringGrid1.Row;
  col := StringGrid1.Col;
  if col = 1 then begin
     if StringGrid2.ColCount-1 <= lin then begin
       StringGrid2.Columns.Add;
     end;
     StringGrid2.Columns.Items[lin].Title.Caption := StringGrid1.Cells[col,lin];
     StringGrid2.Columns.Items[lin].Width := 150;
  end;
end;

procedure TForm1.FormCreate(Sender: TObject);
begin

end;

procedure TForm1.Button1Click(Sender: TObject);
var
  lin: integer;
begin
  lin := StringGrid1.Row;
  StringGrid1.Rows[lin].Delete(0);
  GridDeleteRow(lin, StringGrid1);
end;

end.

