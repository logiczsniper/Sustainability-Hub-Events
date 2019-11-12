""" Taking Nikita's beautiful event printing technique and creating an easily
extensible class.
"""


class Printer:

    @staticmethod
    def _print_first(debug=False):
        """
        Prints the first line. Should be kept hidden; no exposure needed.
        """
        if debug:
            print("Title, Date, Link, Scope")
        else:
            print("{:^12}| {}\n{:^12}|".format("Date", "Title", ""))

    def print_event_list(self, events, debug=False):
        """
        Prints the list of events in a very nice way...

        :param events: all events to be printed.
        :type: list
        """

        self._print_first(debug)

        for index, event in enumerate(events):
            if debug:
                print("{:3}) {} | {:^13} | {}\n{}\n{}\n".format(
                    index, event.date, event.scope, event.title,
                    event.location, event.link))
            else:
                print(" {} | {} ".format(event.date.isoformat(),
                                         event.title))
