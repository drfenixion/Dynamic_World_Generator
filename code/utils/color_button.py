try:
    from PySide.QtWidgets import QPushButton, QColorDialog
    from PySide.QtGui import QColor
except ImportError:
    from PySide6.QtWidgets import QPushButton, QColorDialog
    from PySide6.QtGui import QColor


DEFAULT_RGB = (0.5, 0.5, 0.5)


class ColorButton(QPushButton):
    """A button that shows the current color and opens a color picker.

    The selected color is stored as an (r, g, b) tuple of floats in the
    0.0..1.0 range, which is the same representation used by SDF materials.
    """

    def __init__(self, initial=DEFAULT_RGB, parent=None):
        super().__init__(parent)
        self._rgb = DEFAULT_RGB
        self.setToolTip("Click to choose a color")
        self.clicked.connect(self._choose_color)
        self.set_rgb(initial)

    def _choose_color(self):
        r, g, b = self._rgb
        color = QColorDialog.getColor(QColor.fromRgbF(r, g, b), self, "Select Color")
        if color.isValid():
            self.set_rgb((color.redF(), color.greenF(), color.blueF()))

    def set_rgb(self, rgb):
        try:
            r, g, b = (float(rgb[0]), float(rgb[1]), float(rgb[2]))
        except (TypeError, ValueError, IndexError):
            r, g, b = DEFAULT_RGB
        # Clamp to the valid range to avoid invalid QColor values.
        self._rgb = (
            min(max(r, 0.0), 1.0),
            min(max(g, 0.0), 1.0),
            min(max(b, 0.0), 1.0),
        )
        self._update_appearance()

    def get_rgb(self):
        return self._rgb

    def _update_appearance(self):
        r, g, b = self._rgb
        color = QColor.fromRgbF(r, g, b)
        # Pick a contrasting text color for readability.
        luminance = 0.299 * r + 0.587 * g + 0.114 * b
        text_color = "black" if luminance > 0.5 else "white"
        self.setText(color.name().upper())
        self.setStyleSheet(
            f"QPushButton {{ background-color: {color.name()}; "
            f"color: {text_color}; border: 1px solid #555555; padding: 4px; }}"
        )
