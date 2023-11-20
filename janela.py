# Importa o módulo clr para usar o .NET Framework
import clr

# Adiciona a referência ao assembly PresentationFramework
clr.AddReference("PresentationFramework")

# Importa as classes Window e Application do namespace System.Windows
from System.Windows import Window, Application

# Importa a classe XamlReader do namespace System.Windows.Markup
from System.Windows.Markup import XamlReader

# Define uma classe que herda de Window
class MeuXamlWindow(Window):
    # Define o construtor da classe
    def __init__(self):
        # Lê o arquivo XAML e cria a janela
        self.window = XamlReader.Load(open("MeuXamlWindow.xaml", "r"))
        # Define o título da janela
        self.window.Title = "Exemplo de XAML com Python"
        # Inicia a aplicação com a janela
        Application().Run(self.window)

# Cria uma instância da classe MeuXamlWindow
MeuXamlWindow()