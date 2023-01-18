from kivy.uix.boxlayout import BoxLayout
from popups import ModbusPopup,ScanPopup
from pyModbusTCP.client import ModbusClient
from kivy.core.window import Window
from threading import Thread
from time import sleep

class MainWidget(BoxLayout):
    """
    Widget principal da aplicação
    """
    _updateThread = None
    _updateWidgets = True
    def __init__(self, **kwargs):
        """
        Construtor do widget principal
        """
        super().__init__()
        self._serverIP = kwargs.get('server_ip')
        self._serverPort = kwargs.get('server_port')
        self._scan_time = kwargs.get('scan_time')
        self._modbusPopup = ModbusPopup(self._serverIP,self._serverPort)
        self._scanPopup = ScanPopup(scantime=self._scan_time)
        self._modbusClient = ModbusClient(host=self._serverIP,port=self._serverPort)

    def startDataRead(self, ip, port):
        """
        Método utilizado para a configuração do IP e porta do servidor MODBUS e 
        inicializar uma thread para a leitura dos dados e atualização da interface
        grafica
        """

        self._serverIP = ip
        self._serverPort = port
        self._modbusClient.host = self._serverIP
        self._modbusClient.port = self._serverPort
        try:
            Window.set_system_cursor("wait")
            self._modbusClient.open()
            Window.set_system_cursor("arrow")
            if self._modbusClient.is_open():
                self._updateThread = Thread(target=self.updater)
                self._updateThread.start()
                self.ids.img_con.source = 'imgs/conectado.png'
                self._modbusPopup.dismiss()
            else:
                self._modbusPopup.setInfo("Falha na conexão")
        except Exception as e:
            print("Erro: ",e.args)

    def updater(self):
        """
        Método que invoca as rotinas de leitura dos dados, atualização da interface e
        inserção dos dados no Banco de dados
        """    
        try:
            while self._updateWidgets:
                #ler os dados MODBUS
                #atualizar a inteface
                #inserir os dados no BD
                sleep(self._scan_time/1000)
        except Exception as e:
            self._modbusClient.close()
            print("Erro: ",e.args)