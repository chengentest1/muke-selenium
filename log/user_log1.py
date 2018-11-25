import logging
import os,sys
import datetime
sys.path.append("..")
class UserLog(object):
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        log_dir = os.path.join(base_dir,"logs")
        now_time = datetime.datetime.now().strftime("%Y-%m-%d")# -%H-%M-%S
        log_name = log_dir+"/"+str(now_time)+".log"

        self.logger=logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        #控制台输出日志
        # consle=logging.StreamHandler()
        # logger.addHandler(consle)
        #文件输出日志
        self.file_handler=logging.FileHandler(log_name,'a',encoding='utf-8')
        self.file_handler.setLevel(logging.INFO)
        #对象
        formatter = logging.Formatter('%(asctime)s %(filename)s--> %(funcName)s %(levelno)s: %(levelname)s %(message)s')
        self.file_handler.setFormatter(formatter)
        self.logger.addHandler(self.file_handler)
    def get_log(self):
        return self.logger
    def close_handle(self):
        self.file_handler.close()
        self.logger.removeHandler(self.file_handler)