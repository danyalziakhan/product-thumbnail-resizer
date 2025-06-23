from __future__ import annotations

import os
import sys

from typing import TYPE_CHECKING

from loguru import logger


if TYPE_CHECKING:
    from typing import Final

logger.remove()

LOGGER_FORMAT_STR: Final[
    str
] = "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line} [Process ID {extra[id]}]</cyan> - <level>{message}</level>"

logger.add(
    sys.stderr,
    format=LOGGER_FORMAT_STR,
    level="INFO",
    colorize=True,
    enqueue=True,
)

PROCESS_ID: Final[int] = os.getpid()
logger = logger.bind(id=PROCESS_ID)
logger = logger.opt(colors=True)

info = logger.info
debug = logger.debug
warning = logger.warning
error = logger.error
success = logger.success

logger.level("ACTION", no=38, color="<yellow><dim>")
logger.level("UNHANDLED ERROR", no=39, color="<d><red>")
