program JDMn;

uses
  Vcl.Forms,
  Principal in 'Principal.pas' {frmPrincipal},
  About in 'About.pas' {frmAbout};

{$R *.res}

begin
  Application.Initialize;
  Application.MainFormOnTaskbar := True;
  Application.CreateForm(TfrmPrincipal, frmPrincipal);
  Application.CreateForm(TfrmAbout, frmAbout);
  Application.Run;
end.
