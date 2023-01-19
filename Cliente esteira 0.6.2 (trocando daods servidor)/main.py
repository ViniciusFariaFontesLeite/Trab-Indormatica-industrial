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

        self._widget = MainWidget(scan_time = 1000, server_ip='192.168.011',server_port=502,
        modbus_addrs = {
            'es_esteira':724,
            'es_temp_r':702,
            'es_temp_s': 702,
            'es_temp_t': 704,
            'es_temp_carc': 706,
            'es_le_carga': 710,
            'es_carga': 1302,
            'es_p':  1304,
            'es_i': 1306,   
            'es_encoder':884,
            'es_texto_pid':722,
            'es_d':1308 

        },
        

        db_path="H:\\Arquivos de programas\\UFJF\\Disciplinas\\2022 - 3\\InformaticaIndustrial\\trabalho\\Trab-Indormatica-industrial\\Cliente esteira 0.6.2 (trocando daods servidor)\\db\\scada.db"
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