import sys
import ast
from typing import get_type_hints, Any, Callable


class CLI:
    def __init__(self):
        self.commands = {}
        self.add_help_command()

    def convert_type(self, value: str, expected_type: Any):
        """
        Konwertuje wartość na odpowiedni typ, uwzględniając listy, krotki, słowniki oraz inne typy.

        Args:
            value (str): Wartość, która ma zostać przekonwertowana.
            expected_type (Any): Oczekiwany typ, do którego wartość powinna zostać przekonwertowana.

        Returns:
            Odpowiednią wartość przekonwertowaną na oczekiwany typ.

        Raises:
            TypeError: Jeśli typ konwersji jest nieprawidłowy lub niezgodny.
        """
        try:
            simple_types = {str: str, int: int, float: float, bool: lambda v: v.lower() in ("true", "1", "yes")}
            if expected_type in simple_types:
                return simple_types[expected_type](value)

            if hasattr(expected_type, '__origin__'):
                origin, args = expected_type.__origin__, expected_type.__args__
                if origin is list:
                    return [self.convert_type(x.strip(), args[0]) for x in value.strip("[]").split(",") if x.strip()]
                if origin is tuple:
                    elements = value.strip("()").split(",")
                    return tuple(self.convert_type(elements[i].strip(), args[i]) for i in range(len(args)))
                if origin is dict:
                    return ast.literal_eval(value)

            return ast.literal_eval(value)
        except (ValueError, SyntaxError, IndexError):
            raise TypeError(f"Nieprawidłowy typ dla wartości '{value}', oczekiwano {expected_type}")

    def parse_arguments(self, func: Callable, args) -> list:
        """
        Parsuje argumenty funkcji na podstawie adnotacji typów i konwertuje je na odpowiedni typ.

        Args:
            func (Callable): Funkcja, dla której będą analizowane argumenty.
            args (list): Lista argumentów wejściowych przekazanych z linii poleceń.

        Returns:
            list: Lista przekonwertowanych argumentów zgodnych z adnotacjami typów funkcji.

        Raises:
            ValueError: Jeśli liczba argumentów nie pasuje do liczby oczekiwanych przez funkcję.
        """
        type_hints = get_type_hints(func)
        
        if len(args) != len(type_hints):
            raise ValueError(f"Oczekiwano {len(type_hints)} argumentów, ale podano {len(args)}.")
        
        return [self.convert_type(arg, expected_type) for arg, expected_type in zip(args, type_hints.values())]

    def command(self, check_args=True):
        """
        Dekorator do rejestracji komend i sprawdzania argumentów.

        Args:
            check_args (bool): Jeśli True, sprawdza poprawność argumentów przekazanych do funkcji.

        Returns:
            Callable: Zdecorowana funkcja.
        """
        def decorator(func):
            def wrapper():
                if check_args and func.__name__ in sys.argv:
                    args = sys.argv[sys.argv.index(func.__name__) + 1:]
                    func(*self.parse_arguments(func, args))
                elif not check_args:
                    func()
            self.add(func)
            return wrapper
        return decorator

    def add(self, func: Callable):
        """
        Dodaje funkcję do grupy komend.

        Args:
            func (Callable): Funkcja, którą należy dodać do grupy komend.
        """
        self.commands[func.__name__] = func

    def add_help_command(self):
        """
        Rejestruje komendę `help` automatycznie, aby była dostępna w każdej instancji CLI.
        """
        def help():
            """
            Funkcja wyświetlająca pomoc dla dostępnych komend.
            """
            self.show_help()

        self.add(help)

    def run(self, name: str):
        """
        Uruchamia funkcję zarejestrowaną w grupie komend.

        Args:
            name (str): Nazwa komendy, którą należy uruchomić.
        """
        if name in self.commands:
            self.commands[name]()
        else:
            print(f"Nie znaleziono komendy: {name}")

    def run_all(self):
        """
        Uruchamia wszystkie komendy przekazane przez argumenty wejściowe w terminalu.
        """
        for name in sys.argv[1:]:
            if name in self.commands:
                func = self.commands[name]
                if len(get_type_hints(func)) > 0:
                    # Parsowanie argumentów tylko wtedy, gdy są one przekazane w terminalu
                    args = sys.argv[sys.argv.index(name) + 1:]
                    func(*self.parse_arguments(func, args))
                else:
                    func()

    def show_help(self):
        """
        Wyświetla pomoc dla wszystkich komend wraz z typami argumentów w formie sformatowanej dokumentacji.
        """
        print(f"\n{'=' * 40}\nCOMMANDS\n{'=' * 40}")

        for command_name in self.commands:
            command = self.commands[command_name]
            
            print(f"\n{'-' * 40}\nCommand: {command_name}\n{'-' * 40}")
            doc = command.__doc__ or "No description available."
            cleaned_doc = "\n".join(line.strip() for line in doc.split("\n") if line.strip())
            print(f"\nDescription:\n    {cleaned_doc.replace('\n', '\n    ')}")

            type_hints = get_type_hints(command)
            if type_hints:
                print("\nArguments:")
                for param, param_type in type_hints.items():
                    print(f"    {param}: <{param_type.__name__}>")

                arg_list = [f"<{t.__name__}>" for t in type_hints.values()]
                print(f"\nUsage:\n    {command_name} {' '.join(arg_list)}")
            else:
                print("\nThis command has no arguments.")

        print(f"\n{'=' * 40}\n")