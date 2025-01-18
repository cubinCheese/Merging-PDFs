import sys
from PyQt5.QtWidgets import QApplication
from interface import PDFMergerApp

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = PDFMergerApp()
    window.resize(400, 300)
    window.show()

    sys.exit(app.exec_())
