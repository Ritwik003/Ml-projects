import sys

def error_message_details(error,error_detalis:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code
    error_message="Error occured in python script name[{0}] line number [{1}] error message[{2}]."format()
