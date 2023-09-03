import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel

class MyAndroidApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Number Converter")
        self.setGeometry(100, 100, 400, 200)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.input_field = QLineEdit()
        layout.addWidget(self.input_field)

        button_binary = QPushButton("Binary")
        button_octal = QPushButton("Octal")
        button_hexadecimal = QPushButton("Hexadecimal")

        button_binary.clicked.connect(self.convert_to_binary)
        button_octal.clicked.connect(self.convert_to_octal)
        button_hexadecimal.clicked.connect(self.convert_to_hexadecimal)

        layout.addWidget(button_binary)
        layout.addWidget(button_octal)
        layout.addWidget(button_hexadecimal)

        self.display_label = QLabel()
        layout.addWidget(self.display_label)


    def convert_to_binary(self):
        try:
            decimal_num = float(self.input_field.text())
            binary_representation = ''
            if decimal_num >= 0:
                sign_bit = '0'
            else:
                sign_bit = '1'
                decimal_num = -decimal_num

            integer_part = int(decimal_num)
            binary_representation += bin(integer_part)[2:] + '.'

            fractional_part = decimal_num - integer_part
            for _ in range(4):
                fractional_part *= 2
                bit = '1' if fractional_part >= 1 else '0'
                binary_representation += bit
                fractional_part -= int(fractional_part)
            self.display_label.setText(f"Binary: {sign_bit + binary_representation}")
            
        except ValueError:
            self.display_label.setText("Invalid input. Please enter a valid decimal number.")

        
    def convert_to_octal(self):
        try:
            decimal_num = float(self.input_field.text())
            is_negative = False
            if decimal_num < 0:
                is_negative = True
                decimal_num = abs(decimal_num)


            integer_part = int(decimal_num)
            fractional_part = decimal_num - integer_part


            octal_integer = oct(integer_part)[2:]


            octal_fractional = ''
            for _ in range(4):
                fractional_part *= 8
                octal_digit = int(fractional_part)
                octal_fractional += str(octal_digit)
                fractional_part -= octal_digit


            octal_representation = octal_integer
            if octal_fractional:
                octal_representation += '.' + octal_fractional


            if is_negative:
                octal_representation = '-' + octal_representation
            self.display_label.setText(f"Octal: {octal_representation}")
        except ValueError:
                self.display_label.setText("Invalid input. Please enter a valid decimal number.")


    def convert_to_hexadecimal(self):
        try:
            decimal_num = float(self.input_field.text())

            is_negative = False
            if decimal_num < 0:
                is_negative = True
                decimal_num = abs(decimal_num)


            integer_part = int(decimal_num)
            fractional_part = decimal_num - integer_part


            hexadecimal_integer = hex(integer_part)[2:].upper()


            hexadecimal_fractional = ''
            for _ in range(4):
                fractional_part *= 16
                hexadecimal_digit = int(fractional_part)
                hexadecimal_fractional += hex(hexadecimal_digit)[2:].upper()
                fractional_part -= hexadecimal_digit


            hexadecimal_representation = hexadecimal_integer
            if hexadecimal_fractional:
                hexadecimal_representation += '.' + hexadecimal_fractional


            if is_negative:
                hexadecimal_representation = '-' + hexadecimal_representation
            self.display_label.setText(f"Hexadecimal: {hexadecimal_representation}")
            
        except ValueError:
                self.display_label.setText("Invalid input. Please enter a valid decimal number.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyAndroidApp()
    window.show()
    sys.exit(app.exec_())
