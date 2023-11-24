from cmd import Cmd
from Controller import Controller

LGREEN = '\033[92m'
LRED = '\033[91m'
RESET = '\033[0m'


class CLI(Cmd):

    doc_header = "Ayuda de comandos documentados"
    undoc_header = "Ayuda de comandos no documentados"
    ruler = "="

    def __init__(self):

        super().__init__()
        self.completekey = "tab"
        self.controlador = Controller()


    def do_addAudio(self, args):
        """Añade un audio al dataset."""

        input("Para comenzar a grabar presionar enter. El audio se grabará durante 3 segundos.")
        self.controlador.addAudio()


    def do_resetKnowledge(self, args):
        """Reinicia el conocimiento del sistema."""

        print("Se ha reiniciado el conocimiento del sistema.")
        self.controlador.resetKnowledge()

    def do_exit(self, args):
        """Salir de la CLI."""

        print("Cerrando CLI...")
        return True

    def do_help(self, args):
        """Muestra la ayuda de los comandos disponibles."""

        print(f"{LGREEN}===== {RESET}Comandos disponibles{LGREEN} ====={RESET}")

        for attr in dir(self):
            if attr[:3] == "do_":
                print(f"{LGREEN}:: {RESET}{attr[3:]}")

    def default(self, args):
        """Comando por defecto."""

        print(f"{LRED}--> {RESET}Comando no reconocido.")

    def precmd(self, args):

        if args != "help":
            self.do_help(None)

        return args

    def preloop(self):
        """Inicializa la CLI."""

        print("Inicializando CLI...")


