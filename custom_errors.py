
class StatusCodeInvalid(Exception):
    """
    Status code returned by API is not 200
    """
    def __init__(self, status_code, url):
        self.status_code = status_code
        self.url = url

    def __str__(self):
        return f"{self.url} returned non-200 Status Code when called: {self.status_code}"


class ExpectedColumnsNotFound(Exception):
    """
    Columns need to process output not found in table schema derived from API call
    """
    def __init__(self, expected_columns):
        self.expected_columns = expected_columns

    def __str__(self):
        return f"Following requested columns could not be found in response data: {self.expected_columns}"


class InvalidOutcomeType(Exception):
    """
    Outcome type is not recognised and cannot be used to filter table
    """
    def __init__(self, outcome_type):
        self.outcome_type = outcome_type

    def __str__(self):
        return f"Outcome type entered is not recognised: {self.outcome_type}"


class IncorrectNumberOfDates(Exception):
    """
    Number of previous days in the table is not the same as number of days specified in the config
    """
    def __init__(self, dataframe_size):
        self.dataframe_size = dataframe_size

    def __str__(self):
        return f"Number of days does not equal config input: {self.dataframe_size}"

class MisMatchedDateRange(Exception):
    """
    Number of previous days in the table is not the same as number of days specified in the config
    """
    def __init__(self, df_positive_dates, df_negative_dates):
        self.df_positive_dates = df_positive_dates
        self.df_negative_dates = df_negative_dates


    def __str__(self):
        return f"Dates range for tables to not match:\ndf_positive: {self.df_positive_dates} \ndf_negative: {self.df_negative_dates}"
