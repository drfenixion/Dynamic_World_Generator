def get_color(color):
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
    if isinstance(color, str):
        return colors.get(color.strip().lower(), (0.5, 0.5, 0.5))
    # Accept an already-resolved RGB/RGBA tuple or list (0.0..1.0).
    if isinstance(color, (tuple, list)) and len(color) >= 3:
        try:
            return (float(color[0]), float(color[1]), float(color[2]))
        except (TypeError, ValueError):
            return (0.5, 0.5, 0.5)
    return (0.5, 0.5, 0.5)