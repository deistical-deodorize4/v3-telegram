"""
Centralised configuration for pi02w Hub.

All paths, environment variables, and performance tunables live here
so there is a single source of truth across CLI and Telegram modes.
"""

from __future__ import annotations

import os
from pathlib import Path
from zoneinfo import ZoneInfo

# ---------------------------------------------------------------------------
# Project root – resolved from this file's location
# ---------------------------------------------------------------------------
PROJECT_ROOT: Path = Path(__file__).resolve().parent

# ---------------------------------------------------------------------------
# Directory layout
# ---------------------------------------------------------------------------
DATA_DIR: Path = PROJECT_ROOT / "data"

# CSV data files
STUDY_LOG: Path = DATA_DIR / "study_log.csv"
FINANCE_LOG: Path = DATA_DIR / "finance_log.csv"

# Temporary directory (maps to tmpfs on Pi — protects SD card from wear)
TEMP_DIR: Path = Path("/tmp") / PROJECT_ROOT.name

# Price watch
PRICE_WATCH_INTERVAL_SECONDS: int = 3600  # hourly checks

# Timezone
TIMEZONE: ZoneInfo = ZoneInfo("Europe/Madrid")

# ---------------------------------------------------------------------------
# Environment variables (with optional .env support)
# ---------------------------------------------------------------------------
try:
    from dotenv import load_dotenv

    load_dotenv(PROJECT_ROOT / ".env")
except ImportError:
    pass

TELEGRAM_BOT_TOKEN: str = os.environ.get("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_USER_ID: int = int(os.environ.get("TELEGRAM_USER_ID", "0"))

# ---------------------------------------------------------------------------
# Ensure essential directories exist
# ---------------------------------------------------------------------------
TEMP_DIR.mkdir(parents=True, exist_ok=True)
DATA_DIR.mkdir(parents=True, exist_ok=True)

