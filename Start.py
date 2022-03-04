import sys
from PySide6.QtCore import  QDir, QMimeData, QStandardPaths, Qt, Slot
from PySide6.QtWidgets import (QApplication, QDialog, QFileDialog, QLabel,
                               QMainWindow, QMenuBar, QMessageBox, QScrollArea,
                               QScrollBar, QSizePolicy, QStatusBar)
from PySide6.QtGui import (QAction, QClipboard, QColorSpace, QGuiApplication,
                           QImage, QImageReader, QImageWriter, QKeySequence,
                           QPalette, QPainter, QPixmap, QScreen)
from PySide6.QtPrintSupport import QPrintDialog, QPrinter

class TuinOverzicht(QMainWindow):
    # Window information
    def __init__(self, parent = None):
        super().__init__(parent)
        self._scale_factor = 3.0
        self._first_file_dialog = True
        self._image_label = QLabel()
        self._image_label.setBackgroundRole(QPalette.Base)
        self._image_label.setSizePolicy(QSizePolicy.Ignored,
                                       QSizePolicy.Ignored)
        self._image_label.setScaledContents(True)
        self._scroll_area = QScrollArea()
        self._scroll_area.setBackgroundRole(QPalette.Dark)
        self._scroll_area.setWidget(self._image_label)
        self._scroll_area.setVisible(False)
        self.setCentralWidget(self._scroll_area)


        self.resize(QGuiApplication.primaryScreen().availableSize() * 3 / 5)

    
    # Function to add new garden to add and remove trees from. 
    def AddGarden():
        # Give Add tres and fence and other land marks to image.
        # New tab for new garden.
        print("Garden Added")

    def Editgarden():
        #Edits garden
        print("Edited garden")

    # Function to add new tree to garden. 
    def AddTree():        
        # Activated when pressing button "Add Tree"
        # Choose treetype
        # Add images of leaf, tree and apple
        # 
        print("Added tree")
    
    def EditTree():
        print("Edited tree")

    def SaveFile():
        #saves two files, one editorfile and one showcasefile. Showcasefile might need other program to open correctly. 
        #Or just press "Edit file" or "Showcase" when opening project.
        print("Saved file")


    