from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
import sys
from logic import load_image_to_label

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        loader = QUiLoader()
        ui_file = QFile("ui_main.ui")
        ui_file.open(QFile.ReadOnly)
        self.ui = loader.load(ui_file, self)
        ui_file.close()

        self.ui.btnCapture.clicked.connect(self.on_capture)

    def on_capture(self):
        print("📸 Đã bấm nút CHỤP ẢNH (giả lập)")
        image_path = "/home/ducanh/Desktop/DATN/captured_images/5.bmp"
        load_image_to_label(image_path, self.ui.lblImage)

        # Bạn có thể update txtResult nếu muốn mô phỏng thêm:
        self.ui.txtResult.setText("Ảnh đã được hiển thị từ thư mục.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.ui.show()  
    sys.exit(app.exec())
