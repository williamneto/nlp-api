from datetime import datetime

from mongoengine import Document, StringField, ReferenceField, DateTimeField

class Session(Document):
    started = DateTimeField()

class SessionEntry(Document):
    session = ReferenceField(
        Session
    )
    operation = StringField()
    type = StringField()
    text = StringField()
    datetime = DateTimeField(
        default=datetime.now()
    )

class CompletionAnswer(Document):
    input = ReferenceField(
        SessionEntry
    )
    text = StringField()
    datetime = DateTimeField(
        default=datetime.now()
    )