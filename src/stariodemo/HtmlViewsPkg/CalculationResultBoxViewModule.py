from stario.html import Div


def CalculationResultBoxView(
    result,
):
    """
    docstring
    """

    return Div(
        {"class": "bg-green-100 p-4 border border-gray-800"},
        {"id": "_calculation_result_box"},
        result,
    )
