from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
import os

def load_image_to_label(image_path, label_widget):
    if os.path.exists(image_path):
        pixmap = QPixmap(image_path)

        # 👇 Scale ảnh vừa với QLabel nhưng giữ đúng tỷ lệ
        scaled_pixmap = pixmap.scaled(
            label_widget.size(),        # Kích thước của QLabel
            Qt.KeepAspectRatio,         # 👈 Giữ tỷ lệ gốc
            Qt.SmoothTransformation     # 👈 Làm mượt ảnh khi scale
        )

        label_widget.setPixmap(scaled_pixmap)
        print("✅ Ảnh đã load với tỷ lệ đúng")
    else:
        print("❌ Ảnh không tồn tại:", image_path)
