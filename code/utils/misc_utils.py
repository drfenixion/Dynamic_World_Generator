try:
    from PySide.QtWidgets import QMessageBox
    from PySide.QtWidgets import QApplication
except:
    from PySide6.QtWidgets import QMessageBox
    from PySide6.QtWidgets import QApplication


def gazebo_not_installed_notice():
    QMessageBox.information(
        QApplication.instance().main_window,
        'Gazebo no found',
        'If you want to see map in runtime install Gazebo but you can go further without it.'
    )  
