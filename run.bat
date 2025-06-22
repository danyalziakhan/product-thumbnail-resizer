chcp 65001
@echo off
rem get current this batch file directory
set dir=%~dp0

CALL .venv\Scripts\activate
CALL .venv\Scripts\python run.py --brand_name "SSAKASPORTS" --input_file "INPUT_FILE.xlsx" --sheet_name "Sheet1" --thumbnail_column "대표이미지\n[필수]" --thumbnail_new_column "종합몰(JPG)이미지" --model_name_column "모델명\n[사방넷]" --brand_name_column "브랜드명\n[필수]"

pause