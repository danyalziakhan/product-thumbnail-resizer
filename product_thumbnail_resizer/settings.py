from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True, kw_only=True)
class Settings:
    test_mode: bool
    log_file: str
    brand_name: str
    input_file: str
    sheet_name: str
    thumbnail_column: str
    thumbnail_new_column: str
    model_name_column: str
    brand_name_column: str
