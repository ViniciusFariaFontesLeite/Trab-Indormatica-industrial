from ast import Pass
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy_garden.graph import LinePlot

class ModbusPopup(Popup):
    """
    Popup da configuração do protocolo MODBUS
    """
    _info_lb = None
    def __init__(self, server_ip, server_port, **kwargs):
        """
        Construtor da classe ModbusPopup
        """
        super().__init__(**kwargs)        
        self.ids.txt_ip.text = str(server_ip)
        self.ids.txt_porta.text = str(server_port)

    def setInfo(self, message):
        self._info_lb = Label(text=message)
        self.ids.layout.add_widget(self._info_lb)

    def clearInfo(self):
        if self._info_lb is not None:
            self.ids.layout.remove_widget(self._info_lb)
    

class ScanPopup(Popup):
    """
    Popup do tempo de leitura das informações da esteira
    """
    def __init__(self,scantime, **kwargs):
        """
        Construtor da classe ScanPopup
        """
        super().__init__(**kwargs)
        self.ids.txt_st.text = str(scantime) 

class DataGraphPopup(Popup):
    def __init__(self,xmax, plot_color,**kwargs):
        super().__init__(**kwargs)
        self.plot = LinePlot(line_width=1.5, color=plot_color)
        self.ids.graph.add_plot(self.plot)
        self.ids.graph.xmax = xmax


class TorquePopup(Popup):
    """
    Popup do torque gerado pelo motor
    """
    pass