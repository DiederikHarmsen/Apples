
from argparse import ArgumentParser, RawTextHelpFormatter
import sys
from PySide6.QtCore import  QDir, QMimeData, QStandardPaths, Qt, Slot
from PySide6.QtWidgets import (QApplication, QDialog, QFileDialog, QLabel,
                               QMainWindow, QMenuBar, QMessageBox, QScrollArea,
                               QScrollBar, QSizePolicy, QStatusBar)
from PySide6.QtGui import (QAction, QClipboard, QColorSpace, QGuiApplication,
                           QImage, QImageReader, QImageWriter, QKeySequence,
                           QPalette, QPainter, QPixmap, QScreen)
from PySide6.QtPrintSupport import QPrintDialog, QPrinter

from Start import TuinOverzicht

if __name__ == '__main__':
    arg_parser = ArgumentParser(description="Image Viewer",
                                formatter_class=RawTextHelpFormatter)
    arg_parser.add_argument('file', type=str, nargs='?', help='Image file')
    args = arg_parser.parse_args()

    app = QApplication(sys.argv)
    image_viewer = TuinOverzicht()

    if args.file and not image_viewer.load_file(args.file):
        sys.exit(-1)

    image_viewer.show()
    sys.exit(app.exec())