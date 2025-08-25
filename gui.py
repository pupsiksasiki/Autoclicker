from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QTabWidget, QLabel, QPushButton,
    QLineEdit, QHBoxLayout, QComboBox, QGroupBox, QRadioButton, QGridLayout
)
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtGui import QIcon
import sys, os
app = QApplication([])

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)




okno = QWidget()
okno.setWindowTitle("Almazus clicker")
okno.setWindowIcon(QIcon(resource_path("almazus.ico")))
okno.setGeometry(200, 200, 600, 400)
okno.setFixedSize(600, 400)
paleta1 = okno.palette()
paleta1.setColor(QPalette.Window, QColor(25, 25, 30))
paleta1.setColor(QPalette.WindowText, QColor(220, 220, 230))
okno.setPalette(paleta1)

tabki = QTabWidget()
tabclick = QWidget()
tabmuz = QWidget()
tabki.addTab(tabclick, "Автокликер")
tabki.addTab(tabmuz, "сылки")

layout_gl = QVBoxLayout()
layout_gl.addWidget(tabki)
okno.setLayout(layout_gl)


figa = QVBoxLayout()

grup1 = QGroupBox("Интервал кликов")
grid1 = QGridLayout()
muzic_ms = QLineEdit("100")
muzic_sec = QLineEdit("0")
muzic_min = QLineEdit("0")
muzic_hour = QLineEdit("0")
#интеравал кликов
grid1.addWidget(QLabel("Миллисекунды:"), 0, 0)
grid1.addWidget(muzic_ms, 0, 1)
grid1.addWidget(QLabel("Секунды"), 0, 2)
grid1.addWidget(muzic_sec, 0, 3)
grid1.addWidget(QLabel("Минуты:"), 1, 0)
grid1.addWidget(muzic_min, 1, 1)
grid1.addWidget(QLabel("Часы"), 1, 2)
grid1.addWidget(muzic_hour, 1, 3)
grup1.setLayout(grid1)
figa.addWidget(grup1)
# тута раздеал для тип выбор мыши и тд
grup2 = QGroupBox("Параметры клика")
hl1 = QHBoxLayout()
knopka1 = QComboBox()
knopka1.addItems(["Левая", "Правая"])
knopka2 = QComboBox()
knopka2.addItems(["Одиночный", "Двойной", "КПС"])
hl1.addWidget(QLabel("Кнопка мыши:"))
hl1.addWidget(knopka1)
hl1.addWidget(QLabel("Тип клика:"))
hl1.addWidget(knopka2)
grup2.setLayout(hl1)
figa.addWidget(grup2)
# тута отвечает за кол кликов 
grup3 = QGroupBox("Режим работы")
hl2 = QHBoxLayout()
radio1 = QRadioButton("До остановки")
radio2 = QRadioButton("Повторить")
radio1.setChecked(True)
stopcik1 = QLineEdit("1")
hl2.addWidget(radio1)
hl2.addWidget(radio2)
hl2.addWidget(QLabel("Раз:"))
hl2.addWidget(stopcik1)
grup3.setLayout(hl2)
figa.addWidget(grup3)
# тута раздел для этого стара или стопа
hl3 = QHBoxLayout()
startcik = QLabel("Старт (F6)")
stopcik2 = QLabel("Стоп (F6)")
hl3.addWidget(startcik)
hl3.addWidget(stopcik2)
figa.addLayout(hl3)

tabclick.setLayout(figa)

#для музыки разлкд
fignea2 = QVBoxLayout()
from PyQt5.QtCore import Qt, QUrl, QTimer, QSize

silka = QLabel(''
    '<center>'
    '<h3 style="font-size: 24px; margin: 15px;">соцсети:</h3>'
    '<a href="https://github.com/pupsiksasiki/Almazus-Click" style="color: blue; text-decoration: none; margin: 0 60px; font-size: 20px;">GitHubs</a>  '
    '</center>'
'')
silka.setOpenExternalLinks(True)
silka.setTextFormat(Qt.RichText)
silka.setTextInteractionFlags(Qt.TextBrowserInteraction)
fignea2.addWidget(silka)









tabmuz.setLayout(fignea2)

#тута стиль
okno.setStyleSheet("""
    QTabWidget::pane { border: 1px solid #444; }
    QTabBar::tab { background: #333; color: #bbb; padding: 8px; }
    QTabBar::tab:selected { background: #444; color: white; }
    QLabel { color: #ddd; }
    QLineEdit { background: #222; color: #eee; border: 1px solid #555; padding: 4px; }
    QPushButton { background: #2ecc71; color: white; border-radius: 5px; padding: 6px; }
    QPushButton:hover { background: #27ae60; }
    QComboBox { background: #222; color: #eee; border: 1px solid #555; padding: 4px; }
    QGroupBox { border: 1px solid #555; margin-top: 10px; padding: 8px; color: #bbb; }
    QRadioButton, QCheckBox { color: #ddd; }
""")




grup_kps = QGroupBox("(КПС)")
hl_kps = QHBoxLayout()
kps_input = QLineEdit("10") 
hl_kps.addWidget(QLabel("КПС"))
hl_kps.addWidget(kps_input)
grup_kps.setLayout(hl_kps)
figa.addWidget(grup_kps)
grup_kps.hide() 



def obnovittext():
    if knopka2.currentText() == "КПС":
        grup1.hide()
        grup_kps.show()
    else:
        grup1.show()
        grup_kps.hide()


knopka2.currentIndexChanged.connect(obnovittext)







stopcik2.setEnabled(False)
