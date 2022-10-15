import view
import rational
import logger


match view.item_sel():
    case 0:
        expr = view.get_expr()
        res = rational.parse_all(expr)
        logger.write(f"Результат вычисления: {expr} = {res}")
        view.show(f"Результат вычисления: {expr} = {res}")
    case 1:
        view.show(logger.read_all())
    case 2:
        logger.clear()