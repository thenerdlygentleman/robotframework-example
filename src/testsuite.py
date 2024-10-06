import datetime
import logging
import os
from pathlib import Path

from robot import run_cli
from robot.api import ExecutionResult

TMP_DIRECTORY_PATH = Path(__file__).parent.parent / "tmp"
RESOURCES_DIRECTORY_PATH = Path(__file__).parent / "resources"
TESTS_DIRECTORY_PATH = Path(__file__).parent / "tests"
CONSTANTS_FILE_PATH = Path(__file__).parent / "constants.py"

logger = logging.getLogger(__name__)


class TestSuite:
    """Class to run the test."""

    def __init__(self) -> None:
        """Module for starting the robot framework test suite."""
        self.time = datetime.datetime.now(tz=datetime.timezone.utc).strftime(
            "%Y%m%d_%H%M%S"
        )
        self.test_files_directory = TMP_DIRECTORY_PATH / self.time
        self.summary_markdown_file = (
            self.test_files_directory / f"summary_{self.time}.md"
        )
        self.report_file = self.test_files_directory / f"report_{self.time}.html"
        self.log_file = self.test_files_directory / f"log_{self.time}.html"
        self.output_file = self.test_files_directory / f"output_{self.time}.xml"

    def run(
        self,
        debug: bool = False,
        tags_list: list | None = None,
        test_list: list | None = None,
        variable_list: list | None = None,
        variablefile_list: list | None = None,
    ) -> None:
        """Run the test suite."""
        Path.mkdir(self.test_files_directory)

        command = f"""
            --outputdir {self.test_files_directory}
            --log {self.log_file}
            --report {self.report_file}
            --output {self.output_file}
            --pythonpath {RESOURCES_DIRECTORY_PATH}
            --variablefile {CONSTANTS_FILE_PATH}
			--variable TEST_FILES_DIRECTORY:{self.test_files_directory}
        """

        if debug:
            command += " --loglevel DEBUG"

        if tags_list is not None:
            for tag in tags_list:
                command += f" --include {tag}"

        if variable_list is not None:
            for variable in variable_list:
                command += f" --variable {variable}"

        if variablefile_list is not None:
            for variablefile in variablefile_list:
                command += f" --variablefile {variablefile}"

        if test_list is not None:
            for test in test_list:
                command += f" {test}"

        command = command.split()

        logger.debug(msg=command)

        run_cli(command, exit=False)

        self._open_log()
        self._create_markdown_summary()

    def _open_log(self) -> None:
        """Open the log after the test run."""
        log_file = f"{self.test_files_directory}/log_{self.time}.html"

        user_input = input(f"Do you want to open the {log_file} [y/n]: ")

        if user_input == "y":
            os.system(f"open {log_file}")
            logger.debug("%s was opened", log_file)
        else:
            logger.debug("%s was not opened", log_file)

    def _create_markdown_summary(self) -> None:
        """Creates a markdown summary file."""
        with Path.open(self.summary_markdown_file, "w") as markdown_file:
            markdown_file.write("# Robot Framework Report\n\n")
            markdown_file.write(
                "|**Suite**|**Test**|**Status**|**Message**|**Start**|**End**|\n"
            )
            markdown_file.write(
                "|---------|--------|----------|-----------|---------|-------|\n"
            )
            for suite in ExecutionResult(self.output_file).suite.suites:
                for test in suite.tests:
                    markdown_file.write(
                        f"|{suite.name}|{test.name}|{test.status}|{test.message}|{test.starttime}|{test.endtime}|\n"
                    )
