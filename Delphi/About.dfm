object frmAbout: TfrmAbout
  Left = 0
  Top = 0
  Caption = 'About'
  ClientHeight = 441
  ClientWidth = 640
  Color = clBtnFace
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -12
  Font.Name = 'Segoe UI'
  Font.Style = []
  TextHeight = 15
  object Panel1: TPanel
    Left = 0
    Top = 0
    Width = 640
    Height = 441
    Align = alClient
    DockSite = True
    TabOrder = 0
    ExplicitLeft = -56
    ExplicitTop = -24
    object Label1: TLabel
      Left = 270
      Top = 112
      Width = 146
      Height = 71
      Alignment = taCenter
      Caption = 'JDMn'
      Font.Charset = DEFAULT_CHARSET
      Font.Color = clWindowText
      Font.Height = -53
      Font.Name = 'Segoe UI'
      Font.Style = [fsBold]
      ParentFont = False
    end
    object Label2: TLabel
      Left = 200
      Top = 221
      Width = 287
      Height = 25
      Alignment = taCenter
      Caption = 'A DMn implementation with JSON'
      Font.Charset = DEFAULT_CHARSET
      Font.Color = clWindowText
      Font.Height = -19
      Font.Name = 'Segoe UI'
      Font.Style = []
      ParentFont = False
    end
    object Label3: TLabel
      Left = 288
      Top = 320
      Width = 110
      Height = 25
      Alignment = taCenter
      Caption = 'Version: 1.0.9'
      Font.Charset = DEFAULT_CHARSET
      Font.Color = clWindowText
      Font.Height = -19
      Font.Name = 'Segoe UI'
      Font.Style = []
      ParentFont = False
    end
    object LinkLabel1: TLinkLabel
      Left = 241
      Top = 252
      Width = 204
      Height = 19
      BevelInner = bvNone
      BevelKind = bkTile
      BevelOuter = bvNone
      Caption = 
        '<A HREF="https://github.com/GiovaniPM/JDMn">https://github.com/G' +
        'iovaniPM/JDMn</A>'
      Font.Charset = DEFAULT_CHARSET
      Font.Color = clWindowText
      Font.Height = -19
      Font.Name = 'Segoe UI'
      Font.Style = []
      ParentFont = False
      TabOrder = 0
      UseVisualStyle = True
      OnLinkClick = LinkLabel1LinkClick
    end
  end
end
