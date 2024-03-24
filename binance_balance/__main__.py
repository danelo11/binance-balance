import logging

from binance_balance import CFG_PATH
from binance_balance.logging.logging_setup import logging_setup

logging_setup(CFG_PATH)

logger = logging.getLogger(__name__)

logger.error("Probando logging")
