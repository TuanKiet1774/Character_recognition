# 🔤 Character_Recognition

**Hệ thống nhận diện chữ viết tiếng Anh từ hình ảnh, kiểm tra lỗi chính tả và đề xuất sửa lỗi.**

---

## 🧠 Tính năng chính
- 📷 Nhận diện văn bản tiếng Anh từ hình ảnh bằng công nghệ OCR.
- 🪄 Phân tích và kiểm tra lỗi chính tả từ đoạn văn bản nhận diện được.
- ✍️ Tự động gợi ý từ đúng thay cho từ sai chính tả.

---

## 🧰 Công nghệ & Thư viện sử dụng

| Thư viện             | Mô tả                                                                                     |
|----------------------|--------------------------------------------------------------------------------------------|
| `pytesseract`        | Giao diện Python cho Tesseract OCR - nhận diện văn bản từ hình ảnh.                      |
| `Pillow`             | Xử lý hình ảnh trong Python (mở, chỉnh sửa, lưu trữ, v.v.).                              |
| `OpenCV`             | Xử lý ảnh nâng cao, giúp tiền xử lý hình ảnh trước khi OCR.                              |
| `pyspellchecker`     | Kiểm tra và gợi ý sửa lỗi chính tả đơn giản, nhanh chóng.                                |

---

## ⚙️ Hướng dẫn cài đặt

### 1. Cài đặt các thư viện Python:

Mở `Command Prompt` (Win + R → `cmd`) và chạy lệnh sau: pip install pytesseract pillow opencv-python pyspellchecker

### 2. Cài Tesseract: 

Truy cập trang tải: 👉 https://github.com/UB-Mannheim/tesseract/wiki
Sau khi cài đặt, thêm đoạn sau vào mã Python để định nghĩa đường dẫn: pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

![image](https://github.com/user-attachments/assets/b95a37aa-0f6d-44ab-b2b7-2e10e10b127a)

