import maya.OpenMayaUI as omui
from PySide2 import QtWidgets
from shiboken2 import wrapInstance


def maya_main_window():
    """return the maya main window widget"""
    main_window = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window), QtWidgets.QWidget)


class SimpleUI(QtWidgets.QDialog):
    """simple ui class"""

    def __init__(self):
        """contructor"""
        """passing the object simple ui as an argument to super
        makes this line python 2 and 3 compatible"""
        super(SimpleUI, self).__init__(parent=maya_main_window())
        self.setWindowTitle("A simple UI")
