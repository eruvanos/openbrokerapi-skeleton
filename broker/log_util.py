import logging
import os
import sys

DEFAULT_FORMAT = '%(asctime)s - %(levelname)s - %(name)s - %(message)s'
NO_TIME_FORMAT = '%(levelname)s - %(name)s - %(message)s'


def configure(logger: logging.Logger = logging.root,
              log_level="INFO",
              log_format=DEFAULT_FORMAT
              ):
    class InfoFilter(logging.Filter):
        def filter(self, rec):
            return rec.levelno in (logging.DEBUG, logging.INFO)

    formatter = logging.Formatter(log_format)
    log_level_name=os.environ.get("LOG_LEVEL", log_level)
    logger.setLevel(logging.getLevelName(log_level_name))

    std_out_handler = logging.StreamHandler(sys.stdout)
    std_out_handler.setLevel(logging.DEBUG)
    std_out_handler.setFormatter(formatter)
    std_out_handler.addFilter(InfoFilter())

    std_err_handler = logging.StreamHandler()
    std_err_handler.setLevel(logging.WARNING)
    std_err_handler.setFormatter(formatter)

    logger.addHandler(std_out_handler)
    logger.addHandler(std_err_handler)

    return logger