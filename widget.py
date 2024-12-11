import sys, os, re
import yt_dlp as downloader
from urllib.request import urlopen

from PySide6.QtWidgets import QApplication, QWidget

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

class Download():
    def cd(self, newdir):
        print(newdir)
        if not os.path.exists(newdir):
            os.makedir(newdir)
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
            'format': 'best*',
            'outtmpl': '%(title)s.%(ext)s',
        }
        
        self.ui = Ui_Widget()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
