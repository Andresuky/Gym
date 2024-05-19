from mongoengine import Document, StringField, IntField, EmbeddedDocument, EmbeddedDocumentField, ListField

class Provider(Document):
    name = StringField(required=True) 
    repeticiones = IntField()  
    duracion = IntField()
    tiempo = IntField() 
    logo = FileField()
    youtube_url = StringField()
