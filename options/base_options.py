import argparse
import ast
import os
import sys
from typing import Dict, Union

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class BaseOptions:
    """
    This class defines options used during all types of experiments.
    It also implements several helper functions such as parsing, printing, and saving the options.
    """

    def __init__(self) -> None:
        """
        Initializes the BaseOptions class

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        self._parser = argparse.ArgumentParser()
        self._initialized = False
        self._float_or_none = self.float_or_none
        self._list_or_none = self.list_or_none

    def initialize(self) -> None:
        """
        Initializes the BaseOptions class

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        self._parser.add_argument(
            "--experiment_name",
            type=str,
            required=False,
            default="Local_RAG",
            help="experiment name",
        )

        self._parser.add_argument(
            "--pdf_path",
            type=str,
            required=False,
            default="../RAG-from-Scratch/human-nutrition-text.pdf",
            help="path to the PDF file",
        )

        self._parser.add_argument(
            "--url",
            type=str,
            required=False,
            default="https://pressbooks.oer.hawaii.edu/humannutrition2/open/download?type=pdf",
            help="URL to download the PDF file",
        )

        self._parser.add_argument(
            "--page_offset",
            type=int,
            required=False,
            default=41,
            help="page offset for the PDF",
        )

        self._parser.add_argument(
            "--num_pages",
            type=int,
            required=False,
            default=2,
            help="number of pages for testing",
        )

    # Add more arguments as needed

    def parse(self) -> argparse.Namespace:
        """
        Parses the arguments passed to the script

        Parameters
        ----------
        None

        Returns
        -------
        opt: argparse.Namespace
            The parsed arguments
        """
        if not self._initialized:
            self.initialize()
        self._opt = self._parser.parse_args()
        self._opt.is_train = self._is_train

        args = vars(self._opt)
        self._print(args)

        return self._opt

    def _print(self, args: Dict) -> None:
        """
        Prints the arguments passed to the script

        Parameters
        ----------
        args: dict
            The arguments to print

        Returns
        -------
        None
        """
        print("------------ Options -------------")
        for k, v in args.items():
            print(f"{str(k)}: {str(v)}")
        print("-------------- End ---------------")

    def float_or_none(self, value: str) -> Union[float, None]:
        """
        Converts a string to float or None

        Parameters
        ----------
        value: str
            The value to convert

        Returns
        -------
        float
            The converted value
        """
        if value.lower() == "none":
            return None
        try:
            return float(value)
        except ValueError:
            raise argparse.ArgumentTypeError(
                "Invalid float or 'none' value: {}".format(value)
            )

    def list_or_none(self, value: str) -> Union[list, None]:
        """
        Converts a string to list or None

        Parameters
        ----------
        value: str
            The value to convert

        Returns
        -------
        list
            The converted value
        """
        if value.lower() == "none":
            return None
        try:
            return ast.literal_eval(value)
        except ValueError:
            raise argparse.ArgumentTypeError(
                "Invalid list or 'none' value: {}".format(value)
            )
