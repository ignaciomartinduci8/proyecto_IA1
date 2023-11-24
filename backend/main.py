import sys
from CLI import CLI

LGREEN = '\033[92m'
RESET = '\033[0m'


def main(args):

    if len(args) != 2:
        print(f"{LGREEN} --> {RESET}Uso: python main.py [puerto].")
        return

    try:
        port = int(args[1])
    except ValueError:
        print(f"{LGREEN} --> {RESET}El puerto debe ser un número.")
        return

    cli = CLI()
    cli.prompt = f"{LGREEN} --> {RESET} "
    cli.cmdloop(f"{LGREEN} --> {RESET}Iniciando entrada de comandos. Usar help para ver comandos.")


if __name__ == '__main__':

    main(sys.argv)
