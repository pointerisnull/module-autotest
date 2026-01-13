class Tag:
    def __init__(self, name: str, expected_value: str | int = ''):
        self.__tag_name = str(name)
        self.__expected_value = expected_value

    def get_tag_name(self):
        return self.__tag_name
    
    def get_expected_value(self):
        return self.__expected_value