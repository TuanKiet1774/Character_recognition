# Character_recognition
Nhận diện chữ viết tiếng anh, kiểm tra lỗi chính tả và đề xuất sữa lỗi.

- cài đặt thư viện pytesseract, pillow và OpenCV: Win + R -> cmd -> pip install pytesseract pillow opencv-python
- Cài Tesseract bằng file tesseract-ocr-w64-setup-5.5.0.20241111 (trong folder setup)
- Cài đặt thư viện language_tool_python: Win + R -> cmd -> pip install language_tool_python
- Cài đặt phiên bản Java Development Kit (trong folder setup)
- Sau khi cài xong JDK thì 
  + Bật search của máy tính tìm kiếm và bật: Edit the system Environment Variables
  + Chọn Environment Variables
  + Mục system variables -> tìm tới Path -> Edit 
  + Chọn New -> Paste C:\Program Files\Java\jdk-23\bin 
  + Chọn Ok
