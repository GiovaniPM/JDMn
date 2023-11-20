object Form1: TForm1
  Left = 373
  Height = 580
  Top = 242
  Width = 800
  Caption = 'JDMn Setup'
  ClientHeight = 580
  ClientWidth = 800
  Menu = MainMenu1
  LCLVersion = '8.2'
  OnCreate = FormCreate
  object GroupBox1: TGroupBox
    Left = 8
    Height = 193
    Top = 8
    Width = 777
    Caption = 'Inputs'
    ClientHeight = 173
    ClientWidth = 773
    TabOrder = 0
    OnClick = GroupBox1Click
    object StringGrid1: TStringGrid
      Left = 8
      Height = 128
      Top = 8
      Width = 752
      ColCount = 3
      Columns = <      
        item
          Title.Caption = 'Label'
          Width = 300
        end      
        item
          Title.Caption = 'Type'
          Width = 150
        end>
      Options = [goFixedVertLine, goFixedHorzLine, goVertLine, goHorzLine, goRangeSelect, goEditing, goAutoAddRows, goTabs, goRowSelect, goSmoothScroll]
      RowCount = 2
      TabOrder = 0
      OnEditingDone = StringGrid1EditingDone
    end
    object Button1: TButton
      Left = 680
      Height = 25
      Top = 144
      Width = 75
      Caption = 'Delete'
      TabOrder = 1
      OnClick = Button1Click
    end
  end
  object GroupBox2: TGroupBox
    Left = 8
    Height = 336
    Top = 208
    Width = 777
    Caption = 'Decisions'
    ClientHeight = 316
    ClientWidth = 773
    TabOrder = 1
    OnClick = GroupBox2Click
    object StringGrid2: TStringGrid
      Left = 8
      Height = 296
      Top = 8
      Width = 752
      ColCount = 2
      Columns = <      
        item
          Title.Caption = 'Result'
          Width = 150
        end>
      Options = [goFixedVertLine, goFixedHorzLine, goVertLine, goHorzLine, goRangeSelect, goEditing, goAutoAddRows, goTabs, goRowSelect, goSmoothScroll]
      RowCount = 2
      TabOrder = 0
    end
  end
  object MainMenu1: TMainMenu
    Left = 664
    Top = 464
    object MenuItem1: TMenuItem
      Caption = 'File'
      object MenuItem2: TMenuItem
        Caption = 'Open'
      end
      object MenuItem3: TMenuItem
        Caption = 'Save'
      end
      object MenuItem4: TMenuItem
        Caption = 'Exit'
      end
    end
  end
end
