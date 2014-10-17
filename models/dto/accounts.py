from models.kinds.accounts import Profile


class AccountDto(object):

    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.email = kwargs.get('email')
        self.fbid = kwargs.get('fbid')
        self.verified = kwargs.get('verified')
        self.profiles = kwargs.get('profiles')
        self.selected_profile = kwargs.get('selected_profile')


class ProfileDto(object):

    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.account_id = kwargs.get('account_id')
        self.first = kwargs.get('first')
        self.last = kwargs.get('last')
        self.phone_number = kwargs.get('phone_number')

    @staticmethod
    def to_profile_ndb(profile_dto):
        assert(type(profile_dto) == ProfileDto)
        return Profile(account_id=profile_dto.account_id,
                       first=profile_dto.first,
                       last=profile_dto.last,
                       phone_number=profile_dto.phone_number)

    @staticmethod
    def from_profile_ndb(profile_ndb):
        assert(type(profile_ndb) == Profile)
        return ProfileDto(id=profile_ndb.id,
                          account_id=profile_ndb.account_id,
                          first=profile_ndb.first,
                          last=profile_ndb.last,
                          phone_number=profile_ndb.phone_number)
