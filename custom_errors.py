
class StatusCodeInvalid(Exception):

    def __init__(self, status_code, url):
        self.status_code = status_code
        self.url = url

    def __str__(self):
        return f"{self.url} returned non-200 Status Code when called: {self.status_code}"


class ExpectedColumnsNotFound(Exception):

    def __init__(self, expected_columns):
        self.expected_columns = expected_columns

    def __str__(self):
        return f"Following requested columns could not be found in response data: {self.expected_columns}"


class InvalidOutcomeType(Exception):

    def __init__(self, outcome_type):
        self.outcome_type = outcome_type

    def __str__(self):
        return f"Outcome type entered is not recognised: {self.outcome_type}"


class IncorrectNumberOfDates(Exception):

    def __init__(self, dataframe_size):
        self.dataframe_size = dataframe_size

    def __str__(self):
        return f"Number of days does not equal config input: {self.dataframe_size}"