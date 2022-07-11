import logging, time, os



BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# 定义日志文件路径
LOG_BASE_PATH = os.path.join(BASE_PATH, "log")
if not os.path.exists(LOG_BASE_PATH):
    os.mkdir(LOG_BASE_PATH)


class Logger:

    def __init__(self, module_name: str = "log"):  # Eg: title = u'注册测试'

        module_log_file = os.path.join(LOG_BASE_PATH, module_name)

        if not os.path.exists(module_log_file):
            os.mkdir(module_log_file)

        file_name = os.path.join(module_log_file, (time.strftime("%Y_%m_%d", time.localtime(time.time())) + '.log'))

        # 创建日志对象
        self.logger = logging.Logger(module_name)
        # 创建日志级别
        self.logger.setLevel(logging.DEBUG)
        # 创建handler对象
        self.file_handler = logging.FileHandler(file_name, mode='a', encoding="UTF-8")
        # 设置handler录制级别
        self.file_handler.setLevel(logging.DEBUG)
        # 创建控制台control对象
        self.stream_handler = logging.StreamHandler()
        # 设置控制台录制级别
        self.stream_handler.setLevel(logging.DEBUG)

        # self.fmt = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.fmt = logging.Formatter("[%(asctime)s] - %(filename)s[%(lineno)d] - %(levelname)s;  %(message)s")

        self.file_handler.setFormatter(self.fmt)
        self.stream_handler.setFormatter(self.fmt)

        self.logger.addHandler(self.file_handler)
        self.logger.addHandler(self.stream_handler)

    # def debug(self, message):
    #     self.logger.debug(message)
    #
    # def info(self, message):
    #     self.logger.info(message)
    #
    # def warning(self, message):
    #     self.logger.warning(message)
    #
    # def error(self, message):
    #     self.logger.error(message)


if __name__ == '__main__':
    logger = Logger().logger
    logger.info("---测试开始---")
    logger.debug("---测试结束---")
