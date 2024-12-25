from abc import ABC, abstractmethod


class AbstractItemInfo(ABC):

    def __init__(self, object_id):
        self.object_id: str = object_id
        self.class_type: str = self.__class__.__name__

    @classmethod
    @abstractmethod
    def from_string(cls, line) -> 'AbstractItemInfo':
        pass

    @abstractmethod
    def __str__(self):
        pass

    # def get_class_type(self) -> str:
    #     return self.class_type.replace("grp", "")
    
    # @abstractmethod
    # def get_item_type(self) -> str:
    #     return "none"

    # @abstractmethod
    # def get_weight(self):
    #     return 0

    # @abstractmethod
    # def get_material(self):
    #     return "NONE"

    # @abstractmethod
    # def get_icon(self):
    #     return "Icon.etc_question_mark_i00"

    # @abstractmethod
    # def get_consume_type(self):
    #     return "normal"