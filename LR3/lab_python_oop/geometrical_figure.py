from abc import ABC, abstractmethod

class GeometricalFigure(ABC):
    @abstractmethod
    def calculate_area(self):
        pass
