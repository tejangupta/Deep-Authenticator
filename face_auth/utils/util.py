import os
import sys
from datetime import datetime

import yaml
from dateutil.parser import parse
from dotenv import dotenv_values

from face_auth.exception import AppException


class CommonUtils:
    @staticmethod
    def read_yaml_file(file_path: str) -> dict:
        """
        Reads a YAML file and returns the contents as a dictionary.
        file_path: str
        """
        try:
            with open(file_path, "rb") as yaml_file:
                return yaml.safe_load(yaml_file)
        except Exception as e:
            raise AppException(e, sys) from e

    @staticmethod
    def get_time():
        """
        :return current time:
        """
        return datetime.now().strftime("%H:%M:%S").__str__()

    @staticmethod
    def get_date():
        """
        :return current date:
        """
        return datetime.now().date().__str__()

    @staticmethod
    def get_difference_in_second(future_date_time: str, past_date_time: str):
        """
        :param future_date_time:
        :param past_date_time:
        :return difference in second:
        """
        future_date = parse(future_date_time)
        past_date = parse(past_date_time)
        difference = future_date - past_date
        total_seconds = difference.total_seconds()
        return total_seconds

    def get_difference_in_millisecond(self, future_date_time: str, past_date_time: str):
        """
        :param future_date_time:
        :param past_date_time:
        :return difference in millisecond:
        """
        total_seconds = self.get_difference_in_second(future_date_time, past_date_time)
        total_millisecond = total_seconds * 1000
        return total_millisecond

    @staticmethod
    def get_environment_variable(variable_name: str):
        """
        :param variable_name:
        :return environment variable:
        """
        if os.environ.get(variable_name) is None:
            environment_variable = dotenv_values(".env")
            return environment_variable[variable_name]
        else:
            return os.environ.get(variable_name)
