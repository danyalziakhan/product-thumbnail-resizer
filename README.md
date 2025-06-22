# Product Thumbnail Resizer

A Python-based utility that automatically downloads, resizes, and optimizes product thumbnail images from Excel data. Perfect for e-commerce platforms, product catalogs, or any application requiring standardized product image dimensions.

Processes Excel files containing product information, downloads images from URLs, resizes them to meet specific requirements, and generates updated Excel files with new image URLs.

Supports **CLI** interface for automation and batch processing of large product catalogs.

---

## ✨ Features

- 📄 Parse Excel `.xlsx` input files with product data
- 🌐 Download product thumbnail images from URLs with intelligent error handling
- 📏 Automatically resize images to 1000x1000px if dimensions are ≤600px
- 🎨 Handle transparent backgrounds by converting to white
- 🔄 Process images in parallel for improved performance
- 📁 Organize images by brand name in structured directories
- 🔗 Generate new URLs for resized images
- 📊 Update Excel files with new thumbnail URLs
- 📝 Comprehensive logging and error tracking
- 🚫 Handle bad links and network errors gracefully

---

## 📦 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/danyalziakhan/product-thumbnail-resizer.git
   cd product-thumbnail-resizer
   ```

2. Install [uv](https://github.com/astral-sh/uv) package manager:

   ```bash
   # macOS/Linux
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

   ```powershell
   # Windows (PowerShell)
   irm https://astral.sh/uv/install.ps1 | iex
   ```

   Or use pip:

   ```bash
   pip install uv
   ```

3. Create a virtual environment and sync dependencies:

   ```bash
   uv venv
   uv sync
   ```

---

## 🚀 Usage

### ✅ CLI Mode

Use the CLI mode to process product catalogs and resize thumbnail images:

```bash
python run.py ^
  --brand_name "BRAND_NAME" ^
  --input_file "INPUT_FILE.xlsx" ^
  --sheet_name "Sheet1" ^
  --thumbnail_column "Thumbnail URL Column" ^
  --thumbnail_new_column "New Thumbnail URL Column" ^
  --model_name_column "Model Name Column" ^
  --brand_name_column "Brand Name Column"
```

Or use the preconfigured batch file:

```bash
run.bat
```

### 🔧 Parameters

- `--brand_name`: Brand name for organizing images
- `--input_file`: Path to the Excel file containing product data
- `--sheet_name`: Name of the worksheet to process
- `--thumbnail_column`: Column name containing original image URLs
- `--thumbnail_new_column`: Column name for new resized image URLs
- `--model_name_column`: Column name containing product model names
- `--brand_name_column`: Column name containing brand names
- `--test_mode`: Enable verbose logging (optional)
- `--log_file`: Custom log file path (optional)

---

## 📁 Output Structure

```
product-thumbnail-resizer/
├── downloaded_images/
│   └── BRAND_NAME/
│       ├── model1.jpg
│       ├── model2.jpg
│       └── model_bad_link.jpg
├── resized_images/
│   └── BRAND_NAME/
│       ├── model1.jpg
│       ├── model2.jpg
│       └── model_checked.jpg
├── RESULT.xlsx
├── bad_links.txt
└── logs/
    └── YYYYMMDD.log
```

---

## 🛠 Requirements

- Python 3.10
- All dependencies managed through `pyproject.toml`

### Key Dependencies

- **Pillow**: Image processing and manipulation
- **OpenCV**: Advanced image operations and resizing
- **Pandas**: Excel file processing and data manipulation
- **OpenPyXL**: Excel file reading and writing
- **Requests**: HTTP image downloading with caching
- **Loguru**: Advanced logging capabilities

---

## 📁 Project Structure

```
product-thumbnail-resizer/
│
├── run.py                           # Main entry point
├── run.bat                          # Windows batch launcher
├── pyproject.toml                   # Project configuration
├── README.md                        # This file
├── LICENSE                          # MIT License
│
├── downloaded_images/               # Downloaded original images
├── resized_images/                  # Processed and resized images
├── logs/                            # Application logs
│
├── INPUT_FILE.xlsx                  # Sample input file
├── RESULT.xlsx                      # Output file with new URLs
├── bad_links.txt                    # Failed download URLs
│
└── product_thumbnail_resizer/
    ├── __init__.py
    ├── main.py                      # Core processing logic
    ├── settings.py                  # Configuration settings
    └── log.py                       # Logging configuration
```

---

## 🔄 Image Processing Logic

1. **Download**: Images are downloaded from URLs in the Excel file
2. **Validation**: Invalid URLs are logged and marked as "NOT PRESENT"
3. **Resizing**: Images ≤600px are resized to 1000x1000px
4. **Format Conversion**: Transparent backgrounds are converted to white
5. **Organization**: Images are organized by brand name
6. **URL Generation**: New URLs are generated for resized images
7. **Excel Update**: The input file is updated with new thumbnail URLs

---

## 🚨 Error Handling

- **Network Errors**: Automatic retry with exponential backoff
- **Invalid URLs**: Logged to `bad_links.txt` and marked as "NOT PRESENT"
- **Missing Images**: Graceful handling with placeholder files
- **File System Errors**: Comprehensive error logging and recovery
- **Data Validation**: Ensures column existence and data integrity

---

## 🤝 License

MIT License. Free to use, modify, and distribute in personal or commercial projects.
