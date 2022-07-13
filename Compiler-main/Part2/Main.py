from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets
from Regex import isID, isLogical, isComparison
from AST import AST
from ParseTree import generateParseTree

class Ui_P(object):
    def __init__(self):
        self.inputString = None
        self.token = None
        self.state = 'A'
        self.work = None

    def resetPressed(self):
        self.inputString = None
        self.token = None
        self.work = None
        self.state = 'A'
        self.webEngineView1.setHtml('')
        self.webEngineView2.setHtml('')
        self.tokenList.clear()
        self.stateLabel.setText('')
        self.inputText.clear()
        self.inputText.setEnabled(True)
        self.tokenizeButton.setEnabled(True)
        self.parseButton.setEnabled(False)
        self.treesButton.setEnabled(False)

    def tokenizePressed(self):
        self.tokenizeButton.setEnabled(False)
        self.inputString = self.inputText.text().split()
        for x in self.inputString:
            if x == ' ':
                self.inputString.remove(x)
        self.inputText.setEnabled(False)
        # call a function to tokenize the list
        self.tokenize()
        # view the token list
        for x in self.token:
            self.tokenList.addItem(str(x))
        # proceed if tokenization is ok
        self.parseButton.setEnabled(True)
        if self.state == 'R':
            self.parseButton.setEnabled(False)
            self.stateLabel.setText('Rejected')

    def parsePressed(self):
        self.parseButton.setEnabled(False)
        s = generateParseTree(self.work, 'ParseTree.html',self.repeated())
        if s == 'R':
            self.stateLabel.setText("Rejected")
            return
        self.stateLabel.setText("Accepted")
        self.treesButton.setEnabled(True)


    def showTreesPressed(self):
        self.treesButton.setEnabled(False)
        # generate the abstract syntax tree
        AST(self.inputString, 'AST.html')
        # show the parse tree
        with open('ParseTree.html', 'r')as f:
            parseTreeFile = f.read()
            self.webEngineView1.setHtml(parseTreeFile)
        # show the AST
        with open('AST.html', 'r')as f:
            ASTFile = f.read()
            self.webEngineView2.setHtml(ASTFile)

    def repeated(self):
        orcount = 0
        andcount = 0
        for x in self.inputString:
            if x == '||':
                orcount += 1
            if x == '&&':
                andcount += 1
            if orcount > 1 or andcount > 1:
                return True
        return False


    def tokenize(self):
        self.token = []
        self.work = []
        for lexeme in self.inputString:
            if isID(lexeme):
                self.token.append(('Identifier', lexeme))
                self.work.append('id')
            elif isLogical(lexeme):
                self.token.append(('Logic', lexeme))
                self.work.append(lexeme)
            elif lexeme == '!':
                self.token.append(('Logic', lexeme))
                self.work.append(lexeme)
            elif isComparison(lexeme):
                self.token.append(('Compop', lexeme))
                self.work.append(lexeme)
            else:
                self.token.append(('Unrecognizable', lexeme))
                self.state = 'R'


    def setupUi(self, P):
        P.setObjectName("P")
        P.resize(1874, 952)
        self.centralwidget = QtWidgets.QWidget(P)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 40, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.inputText = QtWidgets.QLineEdit(self.centralwidget)
        self.inputText.setGeometry(QtCore.QRect(210, 40, 851, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.inputText.setFont(font)
        self.inputText.setObjectName("inputText")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 180, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 90, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.stateLabel = QtWidgets.QLabel(self.centralwidget)
        self.stateLabel.setGeometry(QtCore.QRect(210, 90, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.stateLabel.setFont(font)
        self.stateLabel.setObjectName("stateLabel")
        self.tokenList = QtWidgets.QListWidget(self.centralwidget)
        self.tokenList.setGeometry(QtCore.QRect(10, 220, 231, 661))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.tokenList.setFont(font)
        self.tokenList.setObjectName("tokenList")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(250, 190, 841, 691))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(1100, 190, 761, 691))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(1179, 40, 581, 42))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tokenizeButton = QtWidgets.QPushButton(self.horizontalLayoutWidget, clicked=lambda: self.tokenizePressed())
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.tokenizeButton.setFont(font)
        self.tokenizeButton.setObjectName("tokenizeButton")
        self.horizontalLayout.addWidget(self.tokenizeButton)
        self.parseButton = QtWidgets.QPushButton(self.horizontalLayoutWidget, clicked=lambda: self.parsePressed())
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.parseButton.setFont(font)
        self.parseButton.setObjectName("parseButton")
        self.horizontalLayout.addWidget(self.parseButton)
        self.parseButton.setEnabled(False)
        self.resetButton = QtWidgets.QPushButton(self.horizontalLayoutWidget, clicked=lambda: self.resetPressed())
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.resetButton.setFont(font)
        self.resetButton.setObjectName("resetButton")
        self.horizontalLayout.addWidget(self.resetButton)
        self.treesButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.showTreesPressed())
        self.treesButton.setGeometry(QtCore.QRect(1370, 100, 191, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.treesButton.setFont(font)
        self.treesButton.setObjectName("treesButton")
        P.setCentralWidget(self.centralwidget)
        self.treesButton.setEnabled(False)
        self.menubar = QtWidgets.QMenuBar(P)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1874, 26))
        self.menubar.setObjectName("menubar")
        P.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(P)
        self.statusbar.setObjectName("statusbar")
        P.setStatusBar(self.statusbar)

        self.webEngineView1 = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.webEngineView1.setGeometry(270, 220, 800, 650)

        self.webEngineView2 = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.webEngineView2.setGeometry(1115, 220, 730, 650)

        self.retranslateUi(P)
        QtCore.QMetaObject.connectSlotsByName(P)

    def retranslateUi(self, P):
        _translate = QtCore.QCoreApplication.translate
        P.setWindowTitle(_translate("P", "MainWindow"))
        self.label.setText(_translate("P", "Input String:"))
        self.label_3.setText(_translate("P", "Token List"))
        self.label_4.setText(_translate("P", "State:"))
        self.stateLabel.setText(_translate("P", ""))
        self.groupBox.setTitle(_translate("P", "Parse Tree"))
        self.groupBox_2.setTitle(_translate("P", "Abstract Syntax Tree"))
        self.tokenizeButton.setText(_translate("P", "Tokenize"))
        self.parseButton.setText(_translate("P", "Parse"))
        self.resetButton.setText(_translate("P", "Reset"))
        self.treesButton.setText(_translate("P", "Show Trees"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    P = QtWidgets.QMainWindow()
    ui = Ui_P()
    ui.setupUi(P)
    P.show()
    sys.exit(app.exec_())
