import sys
import yaml
from loguru import logger


def conf_reader():
    try:
        with open("conf.yml", encoding="utf-8") as f:
            conf = yaml.safe_load(f)
            key = conf["openai_key"]
    except Exception as e:
        logger.error(e)
        sys.exit("Exiting...")
    return key
