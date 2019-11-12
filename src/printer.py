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
            print("{:^85} | {:^20}\n{:85} | {:20}".format(
                "Event Name", "Event Date", "", ""))

    def print_event_list(self, events, debug=False):
        """
        Prints the list of events in a very nice way...

        :param events: all events to be printed.
        :type: list
        """

        self._print_first(debug)

        for event in events:
            if debug:
                print(event.title, event.date,
                      event.link, event.scope)
            else:
                print("{:^85} | {:^20}".format(
                    event.title, event.date.isoformat()))
