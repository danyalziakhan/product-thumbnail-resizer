from __future__ import annotations

from argparse import ArgumentParser
import os
import shutil

from contextlib import suppress
from multiprocessing import freeze_support

from product_thumbnail_resizer.main import (
    run,
    DOWNLOAD_IMAGES_DIR,
    RESIZED_IMAGES_DIR,
    TODAY_DATE,
)
from product_thumbnail_resizer.settings import Settings
from product_thumbnail_resizer.log import logger


if __name__ == "__main__":
    freeze_support()

    parser = ArgumentParser()

    parser.add_argument(
        "--test_mode",
        help="Run the program with verbose logging output",
        action="store_true",
    )
    parser.add_argument(
        "--log_file",
        help="Log file path which will override the default path",
        type=str,
        default=os.path.join("logs", f"{TODAY_DATE}.log"),
    )
    parser.add_argument(
        "--brand_name",
        help="Brand name",
        type=str,
        required=True,
    )
    parser.add_argument(
        "--input_file",
        help="Input file",
        type=str,
        required=True,
    )
    parser.add_argument(
        "--sheet_name",
        help="Sheet name in the input file",
        type=str,
        required=True,
    )
    parser.add_argument(
        "--thumbnail_column",
        help="Thumbnail column in the input file",
        type=str,
        required=True,
    )
    parser.add_argument(
        "--thumbnail_new_column",
        help="Thumbnail new column in the input file",
        type=str,
        required=True,
    )
    parser.add_argument(
        "--model_name_column",
        help="Model name column in the input file",
        type=str,
        required=True,
    )
    parser.add_argument(
        "--brand_name_column",
        help="Brand name column in the input file",
        type=str,
        required=True,
    )

    args = parser.parse_args()

    with suppress(OSError):
        shutil.rmtree(DOWNLOAD_IMAGES_DIR)

    os.makedirs(DOWNLOAD_IMAGES_DIR, exist_ok=True)

    with suppress(OSError):
        shutil.rmtree(RESIZED_IMAGES_DIR)

    os.makedirs(RESIZED_IMAGES_DIR, exist_ok=True)

    settings = Settings(
        test_mode=args.test_mode,
        log_file=args.log_file,
        brand_name=args.brand_name,
        input_file=args.input_file,
        sheet_name=args.sheet_name,
        thumbnail_column=args.thumbnail_column.replace("\\n", "\n"),
        thumbnail_new_column=args.thumbnail_new_column.replace("\\n", "\n"),
        model_name_column=args.model_name_column.replace("\\n", "\n"),
        brand_name_column=args.brand_name_column.replace("\\n", "\n"),
    )

    try:
        run(settings)
    except Exception as err:
        logger.log("UNHANDLED ERROR", err)
        raise err from err

    logger.success("Program has been run successfully")
