
import os
import cv2
from pypylon import pylon

class PylonCamera:
    def __init__(self, save_dir="/home/ducanh/Desktop/DATN/captured_images"):
        self.save_dir = save_dir
        os.makedirs(self.save_dir, exist_ok=True)

        # Khởi tạo camera nhưng chưa mở
        self.camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())

    def capture_image(self, filename="captured_image.png", timeout=1000):
        try:
            # Mở camera
            self.camera.Open()

            # Chụp ảnh với timeout
            grab_result = self.camera.GrabOne(timeout)

            if grab_result.GrabSucceeded():
                # Lấy ảnh dưới dạng numpy array (OpenCV format)
                img = grab_result.Array

                # Lưu ảnh
                image_path = os.path.join(self.save_dir, filename)
                cv2.imwrite(image_path, img)
                print(f"✅ Ảnh đã được lưu tại: {image_path}")
                return image_path
            else:
                print("❌ Không thể lấy ảnh từ camera.")
                return None
        except Exception as e:
            print(f"⚠️ Lỗi khi chụp ảnh: {e}")
            return None
        finally:
            # Đóng camera để giải phóng tài nguyên
            self.camera.Close()
