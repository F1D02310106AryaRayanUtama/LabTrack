"""
main.py - Entry point LabTrack: Sistem Inventaris & Peminjaman Laboratorium
Jalankan: python main.py
"""

import sys
import os

# Pastikan working directory benar agar import modul lokal berhasil
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

import database
from windows.login_window import LoginWindow


def main():
    # Inisialisasi database
    database.init_database()

    app = QApplication(sys.argv)
    app.setApplicationName("LabTrack")
    app.setOrganizationName("LabTrack Systems")

    # Font global
    font = QFont("Segoe UI", 10)
    app.setFont(font)

    # Tampilkan login
    window = LoginWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
