"""
Definition of the TelephonyConsumer class
"""

from duologsync.config import Config
from duologsync.consumer.consumer import Consumer

TELEPHONY_KEYS_TO_LABELS = {
    ('context',): {'name': 'context', 'is_custom': True},
    ('credits',): {'name': 'credits', 'is_custom': True},
    ('eventtype',): {'name': 'event_type', 'is_custom': True},
    ('phone',): {'name': 'phone', 'is_custom': True},
    ('timestamp',): {'name': 'rt', 'is_custom': False},
    ('type',): {'name': 'type', 'is_custom': True}
}


class TelephonyConsumer(Consumer):
    """
    An implementation of the Consumer class for telephony logs
    """

    def __init__(self, log_format, log_queue, writer, child_account_id=None):
        super().__init__(log_format, log_queue, writer, child_account_id=child_account_id)
        self.keys_to_labels = TELEPHONY_KEYS_TO_LABELS
        self.log_type = Config.TELEPHONY
