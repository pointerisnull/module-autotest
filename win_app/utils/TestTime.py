from datetime import datetime
from datetime import timedelta
import time

from common.Singleton import Singleton


class TestTime(metaclass=Singleton):
    __fstart = datetime.now().strftime('%m/%d/%Y %H:%M:%S')
    start_time = time.monotonic()
    
    
    def get_fstart() -> str:
        '''
        This method returns the formatted start time of the test.
        
        **Returns**:
        - **str**: A string representation of the start time in the format 'MM/DD/YYYY HH:MM:SS'.
        '''
        return TestTime.__fstart
    
    def get_now() -> float:
        return time.monotonic()
    
    def get_fnow() -> str:
        '''
        This method returns the current date and time in a formatted string.

        **Returns**:
        - **str**: A string representation of the current date and time in the format 'MM/DD/YYYY HH:MM:SS'.
        '''
        return datetime.now().strftime('%m/%d/%Y %H:%M:%S')
    
    def get_timediff(start_time: float) -> str:
        '''
        This method calculates the difference in time from start to current.
        
        **Parameters**:  
        - *start_time* -- `float`
            - A float representing a start time
        ---
        **Returns**:
        - **str**: A string representing the total time.
        '''
        __end_time = time.monotonic()
        timediff = str(timedelta(seconds=__end_time - start_time))
        
        timediff = timediff.split(":")

        hours = int(timediff[0])
        minutes = int(timediff[1])
        seconds_ms = float(timediff[2])

        if (hours == 0 and minutes == 0):
            return f'{seconds_ms} seconds'
        elif (hours == 0):
            if minutes == 1:
                return f'{minutes} minute and {seconds_ms} seconds'
            else:
                return f'{minutes} minutes and {seconds_ms} seconds'
        elif (hours == 1):
            if minutes == 1:
                return f'{hours} hour, {minutes} minute, and {seconds_ms} seconds'
            else:
                return f'{hours} hour, {minutes} minutes, and {seconds_ms} seconds'
        else:
            return f'{hours} hours, {minutes} minutes, and {seconds_ms} seconds'