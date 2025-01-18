from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QListWidget, QFileDialog, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QDragEnterEvent, QDropEvent
import sys
from pdf_merge import merge_pdfs

class PDFMergerApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PDF Merger")

        # Layout for the window
        layout = QVBoxLayout(self)

        # ListWidget for displaying PDF files
        self.pdfList = QListWidget(self)
        layout.addWidget(self.pdfList)

        # Button to select files
        selectButton = QPushButton("Select PDF Files", self)
        layout.addWidget(selectButton)

        # Button to merge files
        mergeButton = QPushButton("Merge PDFs", self)
        layout.addWidget(mergeButton)

        # Set up drag and drop
        self.setAcceptDrops(True)

        # Connect buttons to corresponding actions
        selectButton.clicked.connect(self.selectFiles)
        mergeButton.clicked.connect(self.mergePDFs)

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):
        urls = event.mimeData().urls()
        for url in urls:
            if url.isLocalFile():
                self.pdfList.addItem(url.toLocalFile())

    def selectFiles(self):
        files, _ = QFileDialog.getOpenFileNames(self, "Select PDF Files", "", "PDF Files (*.pdf)")
        for file in files:
            self.pdfList.addItem(file)

    def mergePDFs(self):
        if self.pdfList.count() < 2:
            QMessageBox.warning(self, "Error", "Please add at least two PDF files to merge.")
            return

        outputFile, _ = QFileDialog.getSaveFileName(self, "Save Merged PDF", "", "PDF Files (*.pdf)")
        if not outputFile:
            return

        input_files = [self.pdfList.item(i).text() for i in range(self.pdfList.count())]
        try:
            # Call merge_pdfs from pdf_merge
            merge_pdfs(input_files, outputFile)
            QMessageBox.information(self, "Success", f"PDFs merged successfully into {outputFile}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred while merging PDFs: {str(e)}")
