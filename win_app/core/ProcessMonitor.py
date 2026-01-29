import psutil
import pygetwindow
import subprocess
import sys
import time
import win32process
import win32gui
import win32con
import win32api
import logging

from common.Singleton import Singleton
from common import constants
from utils.TestTime import TestTime

#Constants
DEFAULT_ATTEMPTS = 5
DOWNLOAD_WINDOW_TITLE = "Download Database"
CRIMSON_WINDOW_TITLE = "Crimson 3.2"

# Used from automation tester V2.0
class ProcessMonitor(metaclass=Singleton):
    def check_for_download_completion(target_instance_pid: int) -> None:
        target_process = psutil.Process(target_instance_pid)
        logging.log(f'Beginning monitoring of target PID, {target_instance_pid}')
        try:
            while target_process.is_running():
                monitor = ProcessMonitor.__monitor_download(target_instance_pid, DOWNLOAD_WINDOW_TITLE)
                # if monitored window closed naturally or was aborted, without encountering an error, then 1 is returned and monitoring will break
                if monitor == 1:
                    logging.log(f'The {DOWNLOAD_WINDOW_TITLE} window closed successfully')
                    break
                # else if monitored window encountered an error, then -1 is returned and monitoring will break (process has ended)
                elif monitor == -1:
                    logging.log('An error was encountered during process monitoring...')
                    logging.log('Could not verify download completion...')
                    break

        except Exception as e:
                    logging.log(f'An error occurred while checking for download completion...{e}')
                    logging.log('Beginning cleanup...')
                    sys.exit()
        
        logging.log(f'The "{target_process.name()}" process has ended...')
        # give the system 1 second to terminate target process
        time.sleep(1)

    def find_all_process_instances(target_process: str, is_initial_search: bool=False) -> list[int]:
        '''
        Searches for instances of a specified process name

        **Parameters**:  
        - *target_process* -- `str`
            - String representing the name of the target process to be found
        - *is_initial_search* -- `bool`
            - Flag used to determine if this is the initial search
        '''

        __instance_pids = []
        __instance_found = False
        __attempts = DEFAULT_ATTEMPTS
        
        while not __instance_found and __attempts > 0:
            for process in psutil.process_iter(['pid', 'name']):
                try:
                    if process.name() == target_process:
                        __instance_pids.append(process.pid)
                        
                # pass any "psutil" exceptions that are encountered
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    pass
                
            if __instance_pids:
                __instance_found = True
                if is_initial_search:
                    logging.log(f'Initial search identified {len(__instance_pids)} preexisting "{target_process}" instance(s)')
            
            # if this is an initial search, if no target process instances were found, exit while loop
            elif is_initial_search:
                logging.log(f'Initial search found no preexisting "{target_process}" instances')
                break
                
            else:
                __attempts -= 1
                logging.log(f'"{target_process}" instance not found -- continuing search..., {__attempts}/5 attempts remaining')
                # give the system some time to recognize new instances of target_process
                time.sleep(0.5)
                pass
            
        return __instance_pids
    
    def find_target_instance_pid(target_process: str, initial_instance_pids: list[int]) -> int:
        '''
        Searches for a pid for a given process

        **Parameters**:  
        - *target_process* -- `str`
            - String representing the name of the target process to be found
        - *initial_instance_pids* -- `list[int]`
            - List of integers representing process pids
        ---
        **Returns**:
        - **__target_instance_pid**: An `int` representing the target instances PID
        '''

        __attempts = DEFAULT_ATTEMPTS
        
        while __attempts > 0:
            __new_instance_pids = ProcessMonitor.__find_new_instances(target_process, initial_instance_pids)
            
            # if more than 1 new instance of target_process is found, it is impossible to identify which new instance is the target instance

            if len(__new_instance_pids) == 1:
                __target_instance_pid = __new_instance_pids[0]
                logging.log(f'Identified PID of target "{target_process}" process, {__target_instance_pid}')
                __target_found = True
                
                return __target_instance_pid
            
            # else if 0 new instances of target_process are found, then reattempt up to 5 times to find a new instance of target_process
            elif len(__new_instance_pids) == 0:
                __attempts -= 1
                logging.log(f'Unable to find new "{target_process}" instance -- continuing search..., {__attempts}/5 attempts remaining')
                time.sleep(constants.BACKOFF_BASE ** (DEFAULT_ATTEMPTS - __attempts))
                continue
            
            else:
                logging.log(f'Too many new "{target_process}" instances detected -- unabled to identify target process.')
                logging.log('Beginning cleanup...')
                sys.exit()

    def __find_new_instances(target_process: str, initial_instance_pids: list[int]) -> list[int]:
        '''
        Searches for new instances of a given process and returns a list of their pids

        **Parameters**:  
        - *target_process* -- `str`
            - String representing the name of the target process to be found
        - *initial_instance_pids* -- `list[int]`
            - List of integers representing the pids of the target process
        ---
        **Returns**:
        - **__new_instance_pids**: A list of integers representing process PIDs
        '''

        __new_instance_pids = []
        __attempts = DEFAULT_ATTEMPTS
        
        logging.log(f'Searching for new instances of "{target_process}"...')
        while not __new_instance_pids and __attempts > 0:
            # give the system 1 second for new instances of target_process to appear before checking
            time.sleep(1)
            __current_instance_pids = ProcessMonitor.find_all_process_instances(target_process)
            __new_instance_pids = ProcessMonitor.__compare_lists(initial_instance_pids, __current_instance_pids)
            __attempts -= 1
            
        return __new_instance_pids
    
    def __monitor_download(target_process_pid: int, target_window_title: str) -> int:
        '''
        **Parameters**:  
        - *target_pid* -- `int`
            - Integer representing the PID of the target process whose targeted child window will be monitored
        - *target_window_title* -- `str`
            - String representing the title of the targeted window
        '''
        
        # initial get of all windows that match the `target_window_title`
        __initial_target_windows = pygetwindow.getWindowsWithTitle(target_window_title)
        
        # attempt to identify target "download" window
        __attempts = 2
        while __attempts > 0:
            #1 second sleep to give the window time to appear
            time.sleep(1)
            __target_window_handle = ProcessMonitor.__find_target_window_handle(target_process_pid, target_window_title, __initial_target_windows)
            # if target "Download Database" window cannot be identified
            if __target_window_handle == -1:
                # if a "Download Database" window cannot be found at this point, then most likely an alternate window with title "Crimson 3.2" has appeared
                logging.log(f'"{target_window_title}" window not found')
                ProcessMonitor.__handle_addr_discrepancy_window(CRIMSON_WINDOW_TITLE, target_process_pid)
                __attempts -= 1
            
            else:
                return ProcessMonitor.__monitor_target_window(target_window_title, __target_window_handle, target_process_pid)
            
        else:
            logging.log(f'Unable to identify target "{target_window_title}"...')
            logging.log('Beginning cleanup...')
            sys.exit()

    def __find_target_window_handle(target_process_id: int, target_window_title: str, initial_target_windows: list) -> int:
        '''
        Searches for a target window handle

        **Parameters**:  
        - *target_process_id* -- `int`
            - Integer representing the target's pid
        - *target_window_title* -- `str`
            - String representing the window's name
        - *initial_target_windows* -- `list`
            - List of target window objects
        '''

        # give the system a moment before checking the system windows again
        time.sleep(0.1)

        __attempts = 0
        while __attempts < DEFAULT_ATTEMPTS:
            # re-get all windows that match the `target_window_title`
            __target_windows = pygetwindow.getWindowsWithTitle(target_window_title)
            # compare initial list of potential target windows to current list
            __lists_disparity = ProcessMonitor.__compare_lists(initial_target_windows, __target_windows)
            
            # if a disparity > 0 found, try to identify window associated with target PID
            if len(__lists_disparity) > 0:
                __matching_window_handle = ProcessMonitor.__find_matching_window_handle(__target_windows, target_process_id)
                
                # if window matching target PID not found, use `time.sleep` backoff and increment attempts
                if __matching_window_handle == -1:
                    __attempts = ProcessMonitor.__increment_find_window_attempts(target_window_title, __attempts)
                
                else:
                    logging.log(f'Found "{target_window_title}" window associated with target PID, {target_process_id}' )
                    return __matching_window_handle
                
            # no new windows found, use `time.sleep` backoff and increment attempts
            else:
                time.sleep(constants.BACKOFF_BASE ** (__attempts))
                __attempts = ProcessMonitor.__increment_find_window_attempts(target_window_title, __attempts)

        else:
            return -1
        
    def __find_matching_window_handle(target_windows: list, target_process_id: int) -> int:
        '''
        **Parameters**:  
        - *target_windows* -- `list`
            - List of window objects
        - *target_process_id* -- `int`
            - Integer representing the process id
        '''

        for window in target_windows:
            __window_handle = window._hWnd
            # [0] returns Thread ID, [1] returns Process ID
            __window_associated_pid = win32process.GetWindowThreadProcessId(__window_handle)[1]
            
            if __window_associated_pid == target_process_id:
                return __window_handle
        
        else:
            return -1
        
    def __increment_find_window_attempts(target_window_title: str, attempts: int) -> int:
        '''
        Increments the number of attempts allowed to find a window

        **Parameters**:
        - *target_window_title* -- `str`
            - The target window's name
        - *attempts* -- `int`
            - Number of attempts
        '''
        logging.log(f'Unable to identify target "{target_window_title}" window...')
        attempts += 1
        logging.log(f'Continuing search for target window, {attempts}/5 attempts...')
        time.sleep(constants.BACKOFF_BASE)
        
        return attempts
        
    def __handle_addr_discrepancy_window(target_button_window_title: str, target_process_id: int) -> None:
        '''
        This method is used to 'click' the yes button on the address discrepancy window.

        **Parameters**:  
        - *target_button_window_title* -- `str`
            - String representing the target windows title
        - *target_process_id* -- `int`
            - Integer representing the target pid
        '''
        __button_windows = pygetwindow.getWindowsWithTitle(target_button_window_title)
        for button_window in __button_windows:
            __button_window_handle = button_window._hWnd
            __button_window_associated_pid = win32process.GetWindowThreadProcessId(__button_window_handle)[1]
            if __button_window_associated_pid == target_process_id:
                logging.log(f'Found alternate "{button_window.title}" window associated with target PID, {__button_window_associated_pid}')
                # Search for the three expected buttons
                yes_handle = win32gui.FindWindowEx(__button_window_handle, None, 'Button', '&Yes')
                no_handle = win32gui.FindWindowEx(__button_window_handle, None, 'Button', '&No')
                cancel_handle = win32gui.FindWindowEx(__button_window_handle, None, 'Button', 'Cancel')
                if not (yes_handle and no_handle and cancel_handle):
                    logging.log('One or more expected buttons not found in the discrepancy window')
                    logging.log('Beginning cleanup...')
                    sys.exit()
                logging.log('Crimson has detected a discrepancy between the currently selected download address configured in the database and the last known download address')
                win32api.SendMessage(yes_handle, win32con.BM_CLICK, 0, 0) #If the address discrepancy window is not in the foreground when this is called, the test will fail. 
                logging.log('Accepting download address override...')
                time.sleep(1)
                break
                
    def __monitor_target_window(target_window_title: str, target_window_handle: int, target_process_id: int) -> int:
        '''
        Monitors the target window for errors or completion

        **Parameters**:  
        - *target_window_title* -- `str`
            - String representing the window's name
        - *target_window_handle* -- `int`
            - Target windows handle id
        - *target_process_id* -- `int`
            - Integer representing the target's pid
        '''
        # once target window has been identified, begin monitoring lifespan of window
        logging.log('Monitoring for errors...')
        __start_time = TestTime.get_now()
        __open_window_handles = [window._hWnd for window in pygetwindow.getAllWindows()]

        while target_window_handle in __open_window_handles:
            # assume: it is not possible for the target process to die and another process of an identical PID spawn in the span of the 0.05s sleep
            time.sleep(0.05)
            __open_window_handles = [window._hWnd for window in pygetwindow.getAllWindows()]
            
            children = []
            # callback method required by win32gui.EnumChildWindows()
            def enum_child_proc(hwnd, lParam):
                children.append(hwnd)
                return True
            
            win32gui.EnumChildWindows(target_window_handle, enum_child_proc, None)
            
            for child in children:
                window_text = win32gui.GetWindowText(child)
                if 'ERROR' in window_text:
                    logging.log(f'Crimson error encountered during download, "{window_text}"')
                    logging.log(f'Terminating target process, PID {target_process_id}')
                    subprocess.run(["C:\\Windows\\system32\\taskkill.exe",
                                    '/F',
                                    '/PID',
                                    str(target_process_id)])
                    return -1
        
        # reached if target window closes without encountering an error
        logging.log(f'Target "{target_window_title}" window has been closed...')
    
        # write timestamp to log without console output -> override default "info" text coloring for timestamp
        logging.log(f'Download completed in, {TestTime.get_timediff(__start_time)}', print_to_console=False)
        # repeat timestamp to console only with ANSI coloring - cyan
        logging.log(f'Download completed in, \033[0;36m{TestTime.get_timediff(__start_time)}\033[0m', write_to_log=False)
        
        return 1
    
    def __compare_lists(list1: list, list2: list) -> list:
        '''
        Compares two lists and returns a list of the differences

        **Parameters**:  
        - *list1* -- `list`
            - First list to be compared
        - *list2* -- `list`
            - Second list to be compared
        '''
        __differences = []
        
        # check in list1 for any disparities with list2
        for element in list1:
            if element not in list2:
                __differences.append(element)
                
        # check in list2 for any missed disparities with list1 that may exist in list2 out of range of list1
        for element in list2:
            if element not in __differences and element not in list1:
                __differences.append(element)
                
        return __differences