def get_color(color_name):
    # Map color names to RGB tuples (case-insensitive)
    colors = {
        "black": (0, 0, 0),
        "gray": (0.5, 0.5, 0.5),
        "grey": (0.5, 0.5, 0.5),
        "white": (1, 1, 1),
        "red": (1, 0, 0),
        "blue": (0, 0, 1),
        "green": (0, 1, 0)
    }
    if isinstance(color_name, str):
        return colors.get(color_name.strip().lower(), (0.5, 0.5, 0.5))
    return (0.5, 0.5, 0.5)