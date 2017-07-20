from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtChart import *

import sys

class Ui_Qcharts(QtWidgets.QWidget):

    def __init__(self):
        super(Ui_Qcharts,self).__init__()
        self.setWindowTitle(u"Qcharts Realtime Demo")
        m_chart = QChart
        chartView = QChartView(m_chart)
        chartView.setRubberBand(QChartView.RectangleRubberBand)

        m_series = QLineSeries
        m_chart.addSeries(m_series)


    def timerEvent(self, event):
        pass

    def getData(self, t):
        pass



def main():
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    # ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()