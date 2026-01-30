from pathlib import Path
from objects.Tag import Tag
import logging

class Database:
    
    def __init__(self, database_filepath: Path, debug_port: int, eval_tags: list[Tag] = []):
        try: 
            self.__filepath = Path(database_filepath)
            self.__filename = database_filepath.split("\\")[-1:][0]
            self.__eval_tags_list = eval_tags
            self.__debug_port = debug_port

        except ValueError as ve:
            logging.error(f'ValueError encountered during init of Database, {self.__filename}, {ve}')
        
        except Exception as e:
            logging.error(f'Exception encountered during init of Database, {self.__filename}, {e}')

    def get_filepath(self) -> Path:
        return self.__filepath
    
    def get_debug_port(self) -> int:
        return self.__debug_port
    
    def get_eval_tags_list(self) -> list[Tag]:
        return self.__eval_tags_list
    
    def get_filename(self) -> str:
        return self.__filename