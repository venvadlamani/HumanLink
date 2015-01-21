import services.accounts
import services.asserts as asserts
import services.email
import services.exp as exp
from models.kinds.messages import (
    Thread,
    Message,
    Member,
)
from models.dto.messages import (
    ThreadDto,
    MessageDto,
)


def create_thread_ndb(actor_id, recipients, text, subject=''):
    """Creates a new thread with given recipients, body text, and subject.

    TODO(kanat): check if recipient is a valid account.

    :param actor_id: (int) ID of the account acting.
    :param recipients: (list) list of account IDs in the thread.
    :param text: (str) body text of the initial message.
    :param subject: (str) optional subject line of the thread.
    :return: (kinds.messages.Thread)
    """
    asserts.valid_id_type(actor_id)
    asserts.not_empty(recipients)
    asserts.type_of(text, basestring)
    asserts.type_of(subject, basestring)

    thd = Thread()
    for account_id in set(recipients):
        if account_id != actor_id:
            thd.add_member(account_id)
    if not len(thd.members):
        raise exp.BadRequestExp('Recipients not specified.')
    thd.add_member(actor_id)
    thd.put()
    # Populate MessageDto.
    message_dto = MessageDto()
    message_dto.thread_id = thd.id
    message_dto.text = text
    send_ndb(actor_id, message_dto)
    return thd


def create_thread(actor_id, recipients, text, subject=''):
    """See `create_thread_ndb`.

    :return: (dto.messages.ThreadDto)
    """
    thd = create_thread_ndb(actor_id, recipients, text, subject)
    return _build_thread_dto(actor_id, thd)


def send_ndb(actor_id, message_dto):
    """Sends a reply in a thread.

    :param actor_id: (int) ID of the account acting.
    :param message_dto: (dto.messages.MessageDto) message details.
    :return: (kinds.messages.Message)
    """
    asserts.valid_id_type(actor_id)
    asserts.type_of(message_dto, MessageDto)

    thread_id = message_dto.thread_id

    _assert_thread_member(actor_id, thread_id)

    thd = Thread.get_by_id(thread_id)
    msg = Message(thread_id=thd.id, sender_id=actor_id)
    msg.text = message_dto.text
    if hasattr(message_dto, 'message_type'):
        msg.message_type = message_dto.message_type
    msg.put()
    thd.last_message_id = msg.id
    thd.put()
    return msg


def send(actor_id, thread_id, text):
    """See `send_ndb`.

    :param actor_id: (int) ID of the account acting.
    :param thread_id: (int) ID of the thread.
    :param text: (str) reply message text.
    :return: (dto.messages.MessageDto)
    """
    message_dto = MessageDto()
    message_dto.thread_id = thread_id
    message_dto.text = text
    msg = send_ndb(actor_id, message_dto)
    return _build_messages_dto(actor_id, msg)


def threads_ndb(actor_id, limit=25):
    """Returns the latest threads the account is a member of.

    :param actor_id: (int) ID of the account.
    :param limit: (int) max number of threads.
    :return: (list<kinds.messages.Thread>)
    """
    asserts.valid_id_type(actor_id)

    query = Thread.query(
        Thread.members == Member(account_id=actor_id, hidden=False))
    query = query.order(-Thread.updated)
    thds = query.fetch(limit=limit)

    return thds


def threads(actor_id, limit=25):
    """Account's inbox. See `threads_ndb`.

    :return: (list<dto.messages.ThreadDto>)
    """
    thds = threads_ndb(actor_id, limit)
    return [_build_thread_dto(actor_id, thd) for thd in thds]


def messages_ndb(actor_id, thread_id, limit=25):
    """Returns the latest messages in the given thread.

    TODO(kanat): Update kinds.Messages.Member.last_seen.

    :param actor_id: (int) ID of the account acting.
    :param thread_id: (int) ID of the thread.
    :param limit: (int) max number of messages.
    :return: (list<kinds.messages.Message>)
    """
    asserts.valid_id_type(actor_id)
    asserts.valid_id_type(thread_id)

    _assert_thread_member(actor_id, thread_id)

    msgs = Message.gql('WHERE thread_id = :1 ORDER BY created DESC',
                       thread_id).fetch(limit=limit)
    return [msg for msg in msgs if actor_id not in msg.hidden_member_ids]


def messages(actor_id, thread_id, limit=25):
    """See `messages_ndb`.

    :return: (list<dto.messages.MessageDto>)
    """
    msgs = messages_ndb(actor_id, thread_id, limit)
    # NOTE: maybe pre-fetch ndb.get_multi() with [msg.sender_id for msg in msgs]
    return [_build_messages_dto(actor_id, msg) for msg in msgs]


def leave_thread(actor_id, thread_id):
    """Unsubscribes the account from the thread.

    :param actor_id: (int) ID of the account acting.
    :param thread_id: (int) ID of the thread to leave.
    :return: (None)
    """
    asserts.valid_id_type(actor_id)
    asserts.valid_id_type(thread_id)

    thread = Thread.get_by_id(thread_id)
    member = thread.find_member(actor_id)
    if member is not None and member.hidden is False:
        member.hidden = True
        thread.put()


def hide_message(actor_id, message_id):
    """Hides the given message from the account.

    :param actor_id: (int) ID of the account acting.
    :param message_id: (int) ID of the message to hide.
    :return: (None)
    """
    asserts.valid_id_type(actor_id)
    asserts.valid_id_type(message_id)

    msg = Message.get_by_id(message_id)

    _assert_thread_member(actor_id, msg.thread_id)

    if actor_id not in msg.hidden_member_ids:
        msg.hidden_member_ids.append(actor_id)
        msg.put()


def _assert_thread_member(actor_id, thread_id):
    if not _is_thread_member(actor_id, thread_id):
        raise exp.PermissionExp()


def _is_thread_member(actor_id, thread_id):
    thread = Thread.get_by_id(thread_id)
    member = thread.find_member(actor_id)
    return member is not None and member.hidden is False


def _build_thread_dto(actor_id, thread):
    # TODO(kanat): Implement unread_count.
    last_msg = Message.get_by_id(thread.last_message_id)
    members = [services.accounts.account_meta(m.account_id)
               for m in thread.members]
    return ThreadDto(id=thread.id,
                     subject=thread.subject,
                     updated=thread.updated,
                     members=members,
                     preview=last_msg.text[:300],
                     unread_count=0)


def _build_messages_dto(actor_id, msg):
    dto = MessageDto.from_message_ndb(msg)
    dto.sender = services.accounts.account_meta(msg.sender_id)
    return dto
