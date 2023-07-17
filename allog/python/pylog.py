import sys
import loguru


class Level():
    Debug = "DEBUG"
    Info = "INFO"
    Warn = "WARNING"
    Error = "ERROR"
    Critical = "CRITICAL"

    def get_level(level):
        if type(level).__name__ != 'str':
            print("Error: get level failed, invalid parameter")
        if level.upper() == Level.Debug:
            return Level.Debug
        elif level.upper() == Level.Info:
            return Level.Info
        elif level.upper() == Level.Warn:
            return Level.Warn
        elif level.upper() == Level.Error:
            return Level.Error
        elif level.upper() == Level.Critical:
            return Level.Critical
        else:
            print("Error: get level failed, unsupport level")


class log(object):
    # file: log file name
    # rotation:
    #   500 MB, Automatically rotate too big file
    #   12:00, New file is created each day at noon
    #   1 week, Once the file is too old, it's rotated
    # compression, Save some loved space, default zip
    # retention, Cleanup after some time
    def __init__(self, file, level):
        if file:
            sink = file
        else:
            sink = sys.stdout
        self.logger = self.newLogger()
        # logger.add("logs/myapp_{time:YYYY-MM-DD}.log", rotation="500 MB")
        # 删除原始的handler
        self.logger.remove()
        self.logger.add(sink=sink, 
                        level=level,
                        format="{time:YYYY-MM-DD HH:mm:ss,SSS} | {level} | [{thread}] | - {message}",
                        enqueue=True)

    def originLogger(self):
        return self.logger

    def newLogger(self):
        return loguru.logger
    
    def debug(self, text):
        return self.logger.debug(text)
        
    def info(self, text):
        return self.logger.info(text)

    def warning(self, text):
        return self.logger.warning(text)

    def error(self, text):
        return self.logger.error(text)

    def critical(self, text):
        return self.logger.critical(text)

    def exception(self, text):
        return self.logger.exception(text)

    def catch(self):
        return self.logger.catch
