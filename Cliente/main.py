from kivy.app import App
from mainwidget import MainWidget
from kivy.lang.builder import Builder


class MainApp(App):
 """
 Classe coom o aplicativo
 """
 def build(self):
     """
     Método que gera o aplicativo com o widget principal
     """
     self.widget = MainWidget()
     return self.widget

if __name__ == '__main__':
    Builder.load_string(open("mainwidget.kv", encoding="utf-8").read(), rulesonly=True) ## inicialização manual do programa / linha está com problema
    MainApp().run()
   