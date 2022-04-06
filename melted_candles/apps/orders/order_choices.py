CREATED = 1
PAID = 2
CANCELLED = 3
BOUNCED = 4
COMPLETED = 5


ORDER_CHOICES = (
    (CREATED, 'Created'),
    (PAID, 'Paid'),
    (CANCELLED, 'Cancelled'),
    (BOUNCED, 'Bounced'),
    (COMPLETED, 'Completed'),
    )

DEFAULT_STATUS = CREATED