object frmPrincipal: TfrmPrincipal
  Left = 0
  Top = 0
  Caption = 'JDMn'
  ClientHeight = 441
  ClientWidth = 640
  Color = clBtnFace
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -12
  Font.Name = 'Segoe UI'
  Font.Style = []
  Menu = MainMenu1
  TextHeight = 15
  object StatusBar1: TStatusBar
    Left = 0
    Top = 422
    Width = 640
    Height = 19
    Panels = <>
    ExplicitLeft = 152
    ExplicitTop = 408
    ExplicitWidth = 0
  end
  object MainMenu1: TMainMenu
    Left = 576
    Top = 368
    object File1: TMenuItem
      Caption = '&File'
      object New1: TMenuItem
        Caption = '&New'
      end
      object Open1: TMenuItem
        Caption = '&Open'
      end
      object Save1: TMenuItem
        Caption = '&Save'
      end
      object N1: TMenuItem
        Caption = '-'
      end
      object Exit1: TMenuItem
        Caption = 'E&xit'
      end
    end
    object Run1: TMenuItem
      Caption = '&Run'
      object Execute1: TMenuItem
        Caption = '&Execute'
      end
    end
    object Help1: TMenuItem
      Caption = '&Help'
      object About1: TMenuItem
        Caption = '&About'
        OnClick = About1Click
      end
    end
  end
end
