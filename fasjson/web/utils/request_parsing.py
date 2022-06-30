from copy import deepcopy


def add_exact_arguments(parser):
    for argument in parser.args:
        if argument.name in ("page_size", "page_number"):
            continue
        if "__" in argument.name:
            continue
        new_argument = deepcopy(argument)
        new_argument.name = f"{argument.name}__exact"
        new_argument.help = f"{argument.help} (exact match)"
        parser.add_argument(new_argument)
