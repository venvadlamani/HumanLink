class PendingDto(object):

    _props = [
        'account_id', 'first', 'last', 'account_type',
        'created', 'status', 'message',
    ]

    def __init__(self, **kwargs):
        self.account_id = kwargs.get('account_id')
        self.first = kwargs.get('first')
        self.last = kwargs.get('last')
        self.account_type = kwargs.get('account_type')
        self.created = kwargs.get('created')
        self.status = kwargs.get('status')
        self.message = kwargs.get('message')

    @classmethod
    def list_from_req_account(cls, reqs, accounts):
        """Builds a list of PendingDto's from given connections requests
        and corresponding accounts.

        :param reqs: (list<kinds.connections.ConnRequest>) connections requests
        :param accounts: (list<kinds.accounts.Account>) corresponding accounts
        :return: (list<dto.connections.PendingDto>)
        """
        dtos = []
        for req, account in zip(reqs, accounts):
            dto = PendingDto(account_id=account.id,
                             first=account.first,
                             last=account.last,
                             account_type=account.account_type,
                             created=req.created,
                             status=req.status,
                             message=req.message)
            dtos.append(dto)
        return dtos


class ConnDto(object):

    _props = [
        'account_id', 'first', 'last', 'account_type', 'is_favorite',
        'created', 'status', 'message',
    ]

    def __init__(self, **kwargs):
        self.account_id = kwargs.get('account_id')
        self.first = kwargs.get('first')
        self.last = kwargs.get('last')
        self.account_type = kwargs.get('account_type')
        self.is_favorite = kwargs.get('is_favorite')
        self.created = kwargs.get('created')
        self.status = kwargs.get('status')
        self.message = kwargs.get('message')

    @classmethod
    def list_from_req_account(cls, reqs, accounts):
        """Builds a list of ConnDto's from given connection requests
        and corresponding accounts.

        :param reqs: (list<kinds.connections.ConnRequest>) connection requests
        :param accounts: (list<kinds.accounts.Account>) corresponding accounts
        :return: (list<dto.connections.ConnDto)>)
        """
        dtos = []
        for req, account in zip(reqs, accounts):
            dto = ConnDto(account_id=account.id,
                          first=account.first,
                          last=account.last,
                          account_type=account.account_type,
                          is_favorite=False,
                          created=req.updated,
                          status=req.status,
                          message=req.message)
            dtos.append(dto)
        return dtos
