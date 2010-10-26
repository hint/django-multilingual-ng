from django.db import models

from multilingual.query import MultilingualModelQuerySet
from multilingual.languages import *
from multilingual.utils import get_multilingual_ordering


class MultilingualManager(models.Manager):
    """
    A manager for multilingual models.

    TO DO: turn this into a proxy manager that would allow developers
    to use any manager they need.  It should be sufficient to extend
    and additionaly filter or order querysets returned by that manager.
    """

    def get_query_set(self):
        """
        Applies ordering by a translated field to the queryset
        """
        qs = MultilingualModelQuerySet(self.model)
        ordering = get_multilingual_ordering(self.model)
        if ordering:
            return qs.order_by(ordering)
        return qs
Manager = MultilingualManager # backwards compat, will be depricated