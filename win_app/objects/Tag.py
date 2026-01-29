import logging

class Tag:
    def __init__(self, name: str, expected_value: str | int = ''):
        try:
            self.__tag_name = str(name)
            self.__expected_value = expected_value
        
        except ValueError as ve:
            logging.log('critical', f'ValueError encountered during init of Tag, {self.__tag_name}, {ve}')
        
        except Exception as e:
            logging.log(f'Exception encountered during init of Tag, {self.__tag_name}, {e}')

    def get_tag_name(self):
        return self.__tag_name
    
    def get_expected_value(self):
        return self.__expected_value