import os
import cv2
from PIL import Image, ImageTk
import pytesseract
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.ttk import Progressbar
from Grammar import suggest_corrections
import threading  

# Đường dẫn tới tesseract executable (cần thiết trên Windows)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def select_and_process_image():
    image_path = filedialog.askopenfilename(
        title="Chọn hình ảnh để nhận diện chữ viết",
        filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp")]
    )
    if not image_path:
        messagebox.showwarning("Cảnh báo", "Bạn chưa chọn hình ảnh!")
        return

    input_path_var.set(image_path)  
    display_image(image_path, input_canvas)  

    
    progressbar.pack(pady=20)  
    progressbar["value"] = 0 

    threading.Thread(target=process_image, args=(image_path,)).start()

def process_image(image_path):
    try:
        image = cv2.imread(image_path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Áp dụng nhị phân hóa (binarization) để làm rõ chữ viết
        _, binary_image = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

        # Sử dụng Tesseract để nhận diện chữ viết tay
        text = pytesseract.image_to_string(Image.fromarray(binary_image), lang='eng')

        progressbar["value"] = 70 

        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, text)

        threading.Thread(target=process_corrections, args=(text,)).start()

    except Exception as e:
        messagebox.showerror("Lỗi", f"Đã xảy ra lỗi: {e}")
        progressbar.pack_forget() 

def process_corrections(text):
    try:
        # Sửa lỗi ngữ pháp bằng Grammar.py
        corrected_text = suggest_corrections(text)

        progressbar["value"] = 90  

        correct_text.delete(1.0, tk.END)
        correct_text.insert(tk.END, corrected_text)


        progressbar["value"] = 100  
        progressbar.pack_forget()

    except Exception as e:
        messagebox.showerror("Lỗi", f"Đã xảy ra lỗi khi sửa lỗi ngữ pháp: {e}")
        progressbar.pack_forget()  #

def display_image(image_path, canvas):
    """Hiển thị hình ảnh lên Canvas."""
    img = Image.open(image_path)
    img = img.resize((500, 300), Image.Resampling.LANCZOS)  
    tk_img = ImageTk.PhotoImage(img)
    canvas.image = tk_img
    canvas.create_image(0, 0, anchor="nw", image=tk_img)

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Nhận diện chữ viết từ hình ảnh")
root.geometry("1300x600")

# Biến lưu trữ đường dẫn tệp
input_path_var = tk.StringVar()

# Chia giao diện thành 2 khung
frame_left = tk.Frame(root, width=350, height=400, bg="lightgray")
frame_left.pack(side="left", fill="both", expand=True)
frame_right = tk.Frame(root, width=350, height=400, bg="white")
frame_right.pack(side="right", fill="both", expand=True)

# Khung bên trái: hiển thị hình ảnh và thanh tiến độ
tk.Label(frame_left, text="Hình ảnh đầu vào", font=("Arial", 14), bg="lightgray").pack(pady=10)
input_canvas = tk.Canvas(frame_left, width=500, height=300, bg="white")
input_canvas.pack(pady=10)
tk.Button(frame_left, text="Chọn hình ảnh", command=select_and_process_image, font=("Arial", 12), bg="blue", fg="white").pack(pady=10)

# Thêm thanh tiến độ vào khung bên trái
progressbar = Progressbar(frame_left, orient="horizontal", length=300, mode="determinate")

# Khung bên phải: hiển thị văn bản
tk.Label(frame_right, text="Văn bản nhận diện", font=("Arial", 14), bg="white").pack(pady=10)
output_text = tk.Text(frame_right, height=10, width=55, wrap="word", font=("Arial", 12), bg="lightyellow")
output_text.pack(pady=10, padx=10)

# Khung bên phải: hiển thị văn bản
tk.Label(frame_right, text="Đề xuất", font=("Arial", 14), bg="white").pack(pady=10)
correct_text = tk.Text(frame_right, height=10, width=55, wrap="word", font=("Arial", 12), bg="lightblue")
correct_text.pack(pady=10, padx=10)

# Chạy giao diện
root.mainloop()
