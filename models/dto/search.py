class SearchQueryDto(object):

    _props = [
        'cursor', 'care_services', 'zipcode', 'languages', 'licenses',
        'expertise', 'transportation', 'languages', 'gender', 'live_in',
        'location', 'care_date', 'wage_min', 'wage_max'
    ]

    def __init__(self, **kwargs):
        for k in self._props:
            if k in kwargs:
                setattr(self, k, kwargs.get(k))


class SearchResultDto(object):

    _props = [
        'cursor', 'user', 'headline', 'wage',
        'references', 'rating', 'response_time'
    ]

    def __init__(self, **kwargs):
        for k in self._props:
            if k in kwargs:
                setattr(self, k, kwargs.get(k))