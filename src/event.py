"""Object for an individual event.

All possible events should be able to be represented using this class.
"""


class Event:

    def __init__(self, title, snippet, date, link, scope):
        """
        Construct an Event object.
        :param title: the primary main of the event.
        :type: str
        :param snippet: first 50-ish words of the article giving a vague idea of the story.
        :type: str
        :param date: the time of the year the event is.
        :type: datetime.date
        :param link: a hyperlink to more details (a dedicated page) about the event.
        :type: str
        :param scope: the scope of the event. Either LOCAL, NATIONAL, or INTERNATIONAL.
        :type: EventScope
        """

        self.title = title
        self.date = date
        self.snippet = snippet
        self.link = link
        self.scope = scope

    @classmethod
    def eventbrite(cls, **kwargs):
        """
        eventbrite does not have a snippet on events. In order to retrieve this information, the link would have to be
        found and then that page requested for each event. This would take way too long. Thus, snippet="" for
        every eventbrite event.
        :param kwargs: the other arguments to build the Event.
        :type: dict
        :return: the Event sourced from eventbrite.
        :rtype: Event
        """
        return Event(snippet="", **kwargs)
