unit Principal;

interface

uses
  Winapi.Windows, Winapi.Messages, System.SysUtils, System.Variants, System.Classes, Vcl.Graphics,
  Vcl.Controls, Vcl.Forms, Vcl.Dialogs, Vcl.Menus, Vcl.ComCtrls, About;

type
  TfrmPrincipal = class(TForm)
    MainMenu1: TMainMenu;
    File1: TMenuItem;
    New1: TMenuItem;
    Open1: TMenuItem;
    Save1: TMenuItem;
    N1: TMenuItem;
    Exit1: TMenuItem;
    Run1: TMenuItem;
    Execute1: TMenuItem;
    Help1: TMenuItem;
    About1: TMenuItem;
    StatusBar1: TStatusBar;
    procedure About1Click(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  frmPrincipal: TfrmPrincipal;
  frmAobut: TfrmAbout;

implementation

{$R *.dfm}

procedure TfrmPrincipal.About1Click(Sender: TObject);
var
    ModalForm: TfrmAbout;
begin
    ModalForm := TfrmAbout.Create(nil);
    try
        ModalForm.ShowModal;
    finally
        ModalForm.Free;
    end;
end;

end.
