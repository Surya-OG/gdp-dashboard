"""Broker connectivity imports.

Central place for the client classes used to talk to Dhan, Zerodha Kite,
Groww and Interactive Brokers. Import from here so the nest_asyncio patch is
always applied before any of the async broker clients are constructed.
"""

import nest_asyncio

# Lets the async clients (ib_insync, MarketFeed, GrowwFeed, KiteTicker) run
# inside an already-running event loop, e.g. Streamlit or Jupyter.
nest_asyncio.apply()

# Dhan — DhanContext carries the client_id/access_token pair that the rest of
# the v2 API objects are built from.
from dhanhq import DhanContext, dhanhq, marketfeed

# Zerodha Kite — REST client plus the streaming ticker.
from kiteconnect import KiteConnect, KiteTicker

# Groww — REST client plus the live feed.
from growwapi import GrowwAPI, GrowwFeed

# Interactive Brokers. ib_insync has no `FNO` class; Indian-style F&O maps onto
# the individual contract types below.
from ib_insync import IB, Stock, Future, Option, FuturesOption, util

__all__ = [
    "DhanContext",
    "dhanhq",
    "marketfeed",
    "KiteConnect",
    "KiteTicker",
    "GrowwAPI",
    "GrowwFeed",
    "IB",
    "Stock",
    "Future",
    "Option",
    "FuturesOption",
    "util",
]
