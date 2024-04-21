# importing required libraries...

from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys

from PyQt5.QtWidgets import QWidget

# Main class

class Window(QMainWindow):
    # Constructor method
    def __init__(self) -> None:
        # Inheriting methods and properties from the superclass
        super().__init__()
        # Setting the title
        self.setWindowTitle("Loan Calculator")
        # Setting the geometry of the app
        self.width = 400
        self.height = 550
        self.setGeometry(100,100,self.width,self.height)
        self.UIComponents()

        # Showing the window
        self.show()

     # Function to add widgets
    def UIComponents(self):
        # Head
        head = QLabel("Loan Calculator \n NCBA Bank",self)
        head.setGeometry(0,10,400,60)
        font = QFont('Times',15)
        font.setBold(True)
        head.setFont(font)
        head.setAlignment(Qt.AlignCenter)
        color = QGraphicsColorizeEffect(self)
        color.setColor(Qt.darkBlue)
        head.setGraphicsEffect(color)

        # Interest label...
        i_label = QLabel("Annual Interest",self)
        # Properties
        i_label.setAlignment(Qt.AlignCenter)
        i_label.setGeometry(20,100,170,40)
        i_label.setStyleSheet( "QLabel" "{"
                              
                              "border: 2px solid black;"
                              "background: rgba(70,70,70,35);"
        "}")
        i_label.setFont(QFont('Times', 9))

        # Interest input field..
        self.rate = QLineEdit(self)
        # Validation for only integers
        onlyInt = QIntValidator()
        self.rate.setValidator(onlyInt)
        # Setting properties for the input field
        self.rate.setGeometry(200,100,180,40)
        self.rate.setAlignment(Qt.AlignCenter)
        self.rate.setFont(QFont('Times', 9))



        # Years label...
        y_label = QLabel("Years",self)
        # Properties
        y_label.setAlignment(Qt.AlignCenter)
        y_label.setGeometry(20,150,170,40)
        y_label.setStyleSheet( "QLabel" "{"
                              
                              "border: 2px solid black;"
                              "background: rgba(70,70,70,35);"
        "}")
        y_label.setFont(QFont('Times', 9))

        # Years input field..
        self.year = QLineEdit(self)
        # Validation for only integers
        onlyInt = QIntValidator()
        self.year.setValidator(onlyInt)
        # Setting properties for the input field
        self.year.setGeometry(200,150,180,40)
        self.year.setAlignment(Qt.AlignCenter)
        self.year.setFont(QFont('Times', 9))


        # Amount label...
        a_label = QLabel("Amount",self)
        # Properties
        a_label.setAlignment(Qt.AlignCenter)
        a_label.setGeometry(20,200,170,40)
        a_label.setStyleSheet( "QLabel" "{"
                              
                              "border: 2px solid black;"
                              "background: rgba(70,70,70,35);"
        "}")
        a_label.setFont(QFont('Times', 9))

        # Amount input field..
        self.amount = QLineEdit(self)
        # Validation for only integers
        onlyInt = QIntValidator()
        self.amount.setValidator(onlyInt)
        # Setting properties for the input field
        self.amount.setGeometry(200,200,180,40)
        self.amount.setAlignment(Qt.AlignCenter)
        self.amount.setFont(QFont('Times', 9))


        # Compute-payment button
        calculate = QPushButton("Compute Payment",self)
        calculate.setGeometry(125,270,150,40)
        # Add action for the button
        calculate.clicked.connect(self.calculate_action)

        # Output Widgets

        # Monthly payment label
        self.m_payment = QLabel(self)
        self.m_payment.setAlignment(Qt.AlignCenter)
        self.m_payment.setGeometry(50,340,300,60)
        self.m_payment.setStyleSheet( "QLabel" "{"
                              
                              "border: 2px solid black;"
                              "background: rgba(70,70,70,35);"
        "}")
        self.m_payment.setFont(QFont('Times', 9))


        # Total payment label
        self.t_payment = QLabel(self)
        self.t_payment.setAlignment(Qt.AlignCenter)
        self.t_payment.setGeometry(50,440,300,60)
        self.t_payment.setStyleSheet( "QLabel" "{"
                              
                              "border: 2px solid black;"
                              "background: rgba(70,70,70,35);"
        "}")
        self.t_payment.setFont(QFont('Times', 9))

    def calculate_action(self):
        # Getting annual interest rate
        annualInterestRate = self.rate.text()
        # Checking for empty fields
        if len(annualInterestRate) == 0 or annualInterestRate == '0':
            # QMessageBox.critical(self, "Alert!", "Fill the blanks!")
            return


        # Getting number of years
        noOfYears = self.year.text()
        # Checking for empty fields
        if len(noOfYears) == 0 or noOfYears == '0':
            # QMessageBox.critical(self, "Alert!", "Fill the blanks!")
            return

        
        # Getting the amount
        amt = self.amount.text()
        # Checking for empty fields
        if len(amt) == 0 or amt == '0':
            # QMessageBox.critical(self, "Alert!", "Fill the blanks!")
            return
        
        # Get calculations
        # ######
        # Convert text into integer
        r = int(annualInterestRate)
        n = int(noOfYears)
        p = int(amt)

        # Monthly interest rate
        mIr = r / 1200  # Rate = x/100%

        # Calculate monthly payments
        # monthlyPayment = (p * mIr * ((1 + mIr)**n)) / (((1 + mIr)**n) - 1)
        monthlyPayment = p * mIr /  (1 - 1 / (1 + mIr) ** (n * 12))
        # Set the format for monthlyPayments for 2dp float
        monthlyPayment = "{:.2f}".format(monthlyPayment)
        # Add text to monthlyPayment calculation
        self.m_payment.setText("Monthly Payment(Kshs) : " + str(monthlyPayment))
        # Getting total payment
        totalPayment = float(monthlyPayment) *12 * n

        totalPayment = "{:.2f}".format(totalPayment)

        self.t_payment.setText("Total Payment(Kshs) : " + str(totalPayment))


# Create app object
App = QApplication(sys.argv)

# Instantiate window class
window = Window()

# Start the app
sys.exit(App.exec())



