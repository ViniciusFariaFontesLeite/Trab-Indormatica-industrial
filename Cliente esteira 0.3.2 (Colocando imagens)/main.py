from kivy.app import App
from numpy import True_
from mainwidget import MainWidget
from kivy.lang.builder import Builder


class MainApp(App):
    """
    classe com o aplicativo
    """
    def build(self):
        """
        Método que gera o aplicativo com base no widget principal
        """

        self._widget = MainWidget()
        return self._widget

if __name__ == '__main__':
    Builder.load_string(open("mainwidget.kv",encoding="utf-8").read(),rulesonly=True)
    MainApp().run()