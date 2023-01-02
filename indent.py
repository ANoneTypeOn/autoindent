from typing import Iterable

# TODO: добавить базовую настройку сепараторов, сделать более удобным
class Indent:
    """Main class for auto indenting"""
    def __init__(self, basic_str: str = "", separator: str = "  ", basic_level: int = 0):
        """"""
        self.separator = separator
        self.basic_level = basic_level

        self.__indent_level = 0  # protection from accidental change of main values
        self.__output_string = basic_str

    def __add_to_output_string(self, string: str, indent: str = "") -> None:
        self.__output_string += f"{indent * self.__indent_level}{string}\n"

    def set_indent_level(self, format_level: int) -> None:
        self.__indent_level = format_level

    def reset_indent_level(self) -> None:
        self.__indent_level = 0  # TODO: maybe it's better to contain basic_level as protected variable?

    def add(self, input_str: str | Iterable[str], format_level: int = 0,
                    increase_formatting_from: int = 0) -> None:

        indent = (self.separator * format_level)

        if isinstance(input_str, str):
            if input_str.count("\n") > 0:
                for num, curr_str in enumerate(input_str.split("\n")):
                    if num < increase_formatting_from:
                        continue

                    self.__add_to_output_string(curr_str, indent)

            self.__add_to_output_string(input_str, indent)

        else:
            for num, curr_str in enumerate(input_str):
                if num < increase_formatting_from:
                    continue

                self.__add_to_output_string(curr_str, indent)

    def get_output(self) -> str:
        return self.__output_string

    def reset_output(self) -> None:
        self.__output_string = ""


    def replace_output(self, replacement: str) -> None:
        self.reset_output()
        self.__output_string = replacement
