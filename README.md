# DevSecOps Inventory API

Aplikasi REST API sederhana untuk manajemen inventaris perangkat keamanan (security items) yang dibangun menggunakan FastAPI dan dikelola menggunakan `uv`. Repository ini dikembangkan sebagai pemenuhan Tugas Praktikum Pertemuan 5 Mata Kuliah DevSecOps.

## 1. Nama Aplikasi & Fungsi

- **Nama Aplikasi:** DevSecOps Inventory API (`devsecops-p5-0110225097`)
- **Fungsi Utama:**
  - Mengelola daftar inventaris barang melalui RESTful API (In-Memory Database).
  - Menyediakan endpoint health check (`GET /`).
  - Mendukung enkapsulasi data, validasi skema input, dan penanganan HTTP Exception.
  - Menyediakan pengujian otomatis (unit testing) untuk memastikan fungsionalitas seluruh endpoint API.

---

## 2. Bahasa & Framework

- **Language:** Python `>=3.14`
- **Web Framework:** [FastAPI](https://fastapi.tiangolo.com/)
- **Data Validation:** [Pydantic](https://docs.pydantic.dev/)
- **ASGI Server:** [Uvicorn](https://www.uvicorn.org/)
- **Package Manager:** [uv](https://github.com/astral-sh/uv)
- **Testing Framework:** [Pytest](https://docs.pytest.org/) & [HTTPX](https://www.python-httpx.org/)

---

## 3. Cara Menjalankan Aplikasi

### Prasyarat

Pastikan `uv` dan `git` telah terinstall di sistem Anda.

### Langkah-Langkah

1. **Clone Repository:**

   ```bash
   git clone https://github.com/UlwanLuthfi/devsecops-p5-0110225097.git
   cd devsecops-p5-0110225097

   ```

2. **Install Dependensi:**

   ```bash
   uv sync
   ```

3. **Jalankan Aplikasi (Development Server):**

   ```bash
   uv run uvicorn app.main:app --reload
   ```

   Aplikasi akan berjalan di <http://127.0.0.1:8000>. Dokumentasi OpenAPI/Swagger UI dapat diakses di <http://127.0.0.1:8000/docs>.

4. **Jalankan Unit Test:**

   ```bash
   uv run pytest
   ```

## 4. Overview Pipeline CI/CD (DevSecOps Workflow)

Pipeline CI/CD pada repository ini diimplementasikan menggunakan **GitHub Actions** (`.github/workflows/devsecops.yml`) untuk memastikan pengujian kode otomatis serta analisis keamanan statis sebelum kode disatukan (_merge_) ke branch utama.

### Event Trigger

Pipeline terpicu secara otomatis pada kondisi berikut:

- `push` ke branch `main`
- `pull_request` ke branch `main`

### Arsitektur Job & Alur Eksekusi

Pipeline dibagi menjadi dua job utama yang berjalan berurutan (_sequential dependency_):

1. **Job `build` (Runner: `ubuntu-latest`)**
   - Melakukan _checkout_ kode sumber dari repository.
   - Melakukan setup environment Python dan memasang `uv` package manager.
   - Mengisolasi dan menginstal seluruh dependensi aplikasi dari `pyproject.toml`.
   - Mengeksekusi unit test secara otomatis menggunakan `uv run pytest`. Jika terjadi kegagalan test, workflow dihentikan.

2. **Job `sast-scan` (Runner: `ubuntu-latest`)**
   - Bergantung pada keberhasilan job `build` (`needs: build`).
   - Menjalankan analisis Static Application Security Testing (SAST) menggunakan **Bandit** untuk memindai kerentanan keamanan pada kode Python.
   - Mengimplementasikan **Quality Gate**: Workflow akan _failed_ jika terdeteksi kerentanan dengan tingkat keparahan tinggi (_high severity/confidence_) untuk mencegah masuknya _vulnerable code_ ke branch `main`.
