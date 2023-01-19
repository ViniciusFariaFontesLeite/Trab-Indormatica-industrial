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

        self._widget = MainWidget(scan_time = 1000, server_ip='127.0.0.1',server_port=502,
        modbus_addrs = {
            'es_esteira': 1000,
            'es_encoder': 4,
            'es_torque': 20,
            'es_temp_r': 0,
            'es_temp_s': 2,
            'es_temp_t': 4,
            'es_temp_carc': 6,
            'es_le_carga': 10,
            'es_carga': 2,
            'es_p':  4,
            'es_i': 6,
            'es_d': 8,
        },
        
        )
        return self._widget
    
    def on_stop(self):
        """
        Método executado quando a aplicação é fechada
        """
        self._widget.stopRefresh()
    
if __name__ == '__main__':
    Builder.load_string(open("mainwidget.kv",encoding="utf-8").read(),rulesonly=True)
    Builder.load_string(open("popups.kv",encoding="utf-8").read(),rulesonly=True)
    MainApp().run()