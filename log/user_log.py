import logging
#日志对象
logger = logging.getLogger()
#设置日志等级
logger.setLevel(logging.DEBUG)
#设置流
consle = logging.StreamHandler()
#日志对象与流相结合
logger.addHandler(consle)
logger.debug("test")
consle.close()
logger.removeHandler(consle)