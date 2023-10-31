#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
from telegram.ext import Updater, CommandHandler

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

updater = Updater('6763041623:AAH_s7vJ0iGR_dke-7UnAoeKDbxPH9vzkXY', use_context=True)