""" Taking Nikita's beautiful event printing technique and creating an easily
extensible class.
"""


class Printer:

    @staticmethod
    def _print_first():
        print("{:^85} | {:^20}\n{:85} | {:20}".format("Event Name", "Event Date", "", ""))

    def print_event_list(self, events):

        self._print_first()

        for event in events:
            print("{:^85} | {:^20}".format(event.title, event.date.isoformat()))
