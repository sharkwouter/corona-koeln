import dateparser


class Report:
    """
    A report with Corona numbers for a specific day
    """

    def __init__(self, day, total_cases=-1, hospitalized=-1, deaths=-1, infected=-1):
        """
        Can raise a ValueError
        :param day: date of the current day
        :param total_cases: amount of people confirmed cases until now
        :param hospitalized: current amount of hospitalized patients
        :param deaths: totals deaths until now
        :param infected: current amount of confirmed cases
        """
        self.day = dateparser.parse(day)
        self.total_cases = total_cases
        self.hospitalized = hospitalized
        self.deaths = deaths
        self.infected = infected
