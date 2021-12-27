import sys
from PySide6.QtCore import  QDir, QMimeData, QStandardPaths, Qt, Slot
from PySide6.QtWidgets import (QApplication, QDialog, QFileDialog, QLabel,
                               QMainWindow, QMenuBar, QMessageBox, QScrollArea,
                               QScrollBar, QSizePolicy, QStatusBar)
from PySide6.QtGui import (QAction, QClipboard, QColorSpace, QGuiApplication,
                           QImage, QImageReader, QImageWriter, QKeySequence,
                           QPalette, QPainter, QPixmap, QScreen)
from PySide6.QtPrintSupport import QPrintDialog, QPrinter

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


