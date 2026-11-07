# ==========================================
# AES Encryption/Decryption App với Gradio
# Chạy trên Google Colab
# ==========================================

# Cài thư viện
#!pip install pycryptodome gradio -q

# ==========================================
# IMPORT
# ==========================================
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import hashlib
import base64
import gradio as gr
import os

# ==========================================
# HÀM XỬ LÝ KHÓA AES
# AES hỗ trợ:
# 16 bytes = AES-128
# 24 bytes = AES-192
# 32 bytes = AES-256
#
# Dùng SHA-256 để tạo khóa 32 bytes
# ==========================================
def format_key(key_text):
    return hashlib.sha256(
        key_text.encode("utf-8")
    ).digest()


# ==========================================
# MÃ HÓA TEXT
# ==========================================
def encrypt_text(plain_text, key_text):
    try:
        key = format_key(key_text)

        cipher = AES.new(key, AES.MODE_CBC)

        padded_text = pad(
            plain_text.encode("utf-8"),
            AES.block_size
        )

        encrypted_bytes = cipher.encrypt(padded_text)

        # Ghép IV + ciphertext
        result = base64.b64encode(
            cipher.iv + encrypted_bytes
        ).decode("utf-8")

        return result

    except Exception as e:
        return f"Lỗi: {str(e)}"


# ==========================================
# GIẢI MÃ TEXT
# ==========================================
def decrypt_text(cipher_text, key_text):
    try:
        key = format_key(key_text)

        data = base64.b64decode(cipher_text)

        # AES dùng IV 16 bytes
        iv = data[:16]
        encrypted_data = data[16:]

        cipher = AES.new(
            key,
            AES.MODE_CBC,
            iv
        )

        decrypted = unpad(
            cipher.decrypt(encrypted_data),
            AES.block_size
        )

        return decrypted.decode("utf-8")

    except Exception as e:
        return f"Lỗi: {str(e)}"


# ==========================================
# MÃ HÓA FILE
# ==========================================
def encrypt_file(file_obj, key_text):
    try:
        if file_obj is None:
            return "Chưa chọn file"

        key = format_key(key_text)

        input_path = file_obj.name

        with open(input_path, "rb") as f:
            file_data = f.read()

        cipher = AES.new(key, AES.MODE_CBC)

        encrypted_data = cipher.encrypt(
            pad(file_data, AES.block_size)
        )

        output_path = "encrypted.aes"

        with open(output_path, "wb") as f:
            # Lưu IV + dữ liệu mã hóa
            f.write(cipher.iv + encrypted_data)

        return output_path

    except Exception as e:
        return f"Lỗi: {str(e)}"


# ==========================================
# GIẢI MÃ FILE
# ==========================================
def decrypt_file(file_obj, key_text):
    try:
        if file_obj is None:
            return "Chưa chọn file"

        key = format_key(key_text)

        input_path = file_obj.name

        with open(input_path, "rb") as f:
            file_data = f.read()

        # AES IV = 16 bytes
        iv = file_data[:16]
        encrypted_data = file_data[16:]

        cipher = AES.new(
            key,
            AES.MODE_CBC,
            iv
        )

        decrypted_data = unpad(
            cipher.decrypt(encrypted_data),
            AES.block_size
        )

        output_path = "decrypted_output"

        with open(output_path, "wb") as f:
            f.write(decrypted_data)

        return output_path

    except Exception as e:
        return f"Lỗi: {str(e)}"


# ==========================================
# GIAO DIỆN GRADIO
# ==========================================
with gr.Blocks(title="AES Encryption App") as demo:

    gr.Markdown("# 🔐 AES Encryption & Decryption")

    # =========================
    # TAB TEXT
    # =========================
    with gr.Tab("Text Encryption"):

        gr.Markdown("## Mã hóa / Giải mã Text")

        txt_input = gr.Textbox(
            label="Nhập văn bản",
            lines=5
        )

        txt_key = gr.Textbox(
            label="Khóa AES",
            type="password"
        )

        with gr.Row():
            btn_encrypt_text = gr.Button("Mã hóa")
            btn_decrypt_text = gr.Button("Giải mã")

        txt_output = gr.Textbox(
            label="Kết quả",
            lines=5
        )

        btn_encrypt_text.click(
            encrypt_text,
            inputs=[txt_input, txt_key],
            outputs=txt_output
        )

        btn_decrypt_text.click(
            decrypt_text,
            inputs=[txt_input, txt_key],
            outputs=txt_output
        )

    # =========================
    # TAB FILE
    # =========================
    with gr.Tab("File Encryption"):

        gr.Markdown("## Mã hóa / Giải mã File")

        file_input = gr.File(
            label="Chọn file"
        )

        file_key = gr.Textbox(
            label="Khóa AES",
            type="password"
        )

        with gr.Row():
            btn_encrypt_file = gr.Button("Mã hóa File")
            btn_decrypt_file = gr.Button("Giải mã File")

        file_output = gr.File(
            label="Tải file kết quả"
        )

        btn_encrypt_file.click(
            encrypt_file,
            inputs=[file_input, file_key],
            outputs=file_output
        )

        btn_decrypt_file.click(
            decrypt_file,
            inputs=[file_input, file_key],
            outputs=file_output
        )

# ==========================================
# CHẠY APP
# ==========================================
demo.launch(share=True)