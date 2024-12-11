import sys, os, re, csv
import yt_dlp as downloader
from urllib.request import urlopen

from PySide6.QtWidgets import QApplication, QWidget, QFileDialog

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

class Download():
    def cd(self, newdir):
        if not os.path.exists(newdir):
            os.makedirs(newdir)
        os.chdir(newdir)
        
    def get(self, uri, options):
        with downloader.YoutubeDL(options) as file:
            try:
                file.download([uri])
            except:
                print(f'{uri} not downloaded')
        
class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.options = {
            'format': 'm4a',
            'outtmpl': '%(title)s.%(ext)s',
        }
        
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.dw = Download()
        
        self.ui.download.clicked.connect(self.dfurl)
        self.ui.search.clicked.connect(self.sftext)
        self.ui.getf.clicked.connect(self.sfscv)
        self.ui.chd.clicked.connect(self.cd)
        self.ui.comboBox.currentIndexChanged.connect(self.cformat)
        
    def cd(self):
        newpath = QFileDialog.getExistingDirectory(self, "Cambiar directorio", os.getcwd())
        if newpath:
            self.dw.cd(newpath)
            self.ui.chd.setText(newpath.split("/")[-1])
            
    def cformat(self):
        self.options['format'] = self.ui.comboBox.currentText()
        
    def dfurl(self):
        uri = self.ui.getu.toPlainText()
        uri = uri.replace('\n', '')
        uri = uri.replace(' ', '')
        uri = uri.replace('\t', '')
        if 'https://' in uri:
            self.dw.get(uri, self.options)
            
    def dftext(self, text):
        text = text.replace('\n', '')
        text = text.replace(' ', '%20')
        text = text.replace('\t', '')
        if len(text) > 0:
            try:
                text = urlopen('https://www.youtube.com/results?search_query=' + text)
                opts = 'https://www.youtube.com/watch?v=' + re.findall(r"watch\?v=(\S{11})", text.read().decode())[0]
                self.dw.get(opts, self.options)
            except:
                pass
            
    def sftext(self):
        search = self.ui.gets.toPlainText()
        self.dftext(search)
            
    def sfscv(self):
        QTFile = QFileDialog.getOpenFileName(self, 'Abrir archivo CSV', '', 'CSV Files (*.csv)')
        QTFile = QTFile[0]
        
        if QTFile:
            with open(QTFile, newline = '') as file:
                self.ui.getf.setText(file.name.split("/")[-1])
                data = list(csv.reader(file))
                
        else:
            data = []
        for i in data:
            if i != 'Artist name':
                self.dw.cd(i[1])
                self.dftext(''.join(i[:3]))
                os.chdir('../')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
