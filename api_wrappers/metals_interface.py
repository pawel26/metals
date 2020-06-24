from abc import ABC, abstractmethod


class MetalsInterface(ABC):

    @abstractmethod
    def fetch_latest(self):
        pass

    @abstractmethod
    def fetch_historical(self, *args, **kwargs):
        pass

    @abstractmethod
    def rate_fluctuation(self, *args, **kwargs):
        pass
