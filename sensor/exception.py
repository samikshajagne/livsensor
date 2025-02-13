import sys
import os


def error_msg_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename
    error_message = (f"Error occurred in file [{filename}] "
                     f"at line [{exc_tb.tb_lineno}] "
                     f"with error: [{str(error)}]")
    return error_message


class SensorException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_msg_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message
