def solid_example_1(*, example_param_1: str, example_param_2: int):
    # the star (keyword argument) obliges us to pass the arguments explicitly
    # by saying example_param_1=type, ...
    """

    :param example_param_1: this is the first parameter
    :param example_param_2: this is the second parameter
    :return:
    """



def solid_example_2(example_param_1: float) -> int:
    """

    :param example_param_1:
    :return:
    """

    # Here we do not need to explicitly say example_param_1=3.50
    # The arrow (->) specifies the return type
    return example_param_1


def solid_example_3(*, example_param_1: float = 4.0):
    """

    :param example_param_1:
    :return:
    """
    pass
