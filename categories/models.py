from mongoengine import Document, StringField, ReferenceField, DateTimeField, BooleanField, DictField
from datetime import datetime


class Category(Document):
    """Category model for organizing transactions"""

    name = StringField(required=True, max_length=100)  # Default/fallback name
    name_translations = DictField(default=dict)  # {'ru': 'Название', 'en': 'Name', 'lv': 'Nosaukums'}
    type = StringField(required=True, choices=['income', 'expense'])
    icon = StringField(max_length=50, default='⚡')
    color = StringField(max_length=7, default='#6366f1')  # Hex color code
    user = ReferenceField('User', required=True)
    is_default = BooleanField(default=False)
    created_at = DateTimeField(default=datetime.utcnow)

    meta = {
        'collection': 'categories',
        'indexes': [
            'user',
            'type',
            'name'
        ]
    }

    def get_name(self, lang='ru'):
        """Get category name in specified language"""
        if self.name_translations and lang in self.name_translations:
            return self.name_translations[lang]
        return self.name

    def to_dict(self):
        """Convert category to dictionary"""
        return {
            'id': str(self.id),
            'name': self.name,
            'name_translations': self.name_translations or {},
            'type': self.type,
            'icon': self.icon,
            'color': self.color,
            'is_default': self.is_default,
        }

    def __str__(self):
        return f"{self.icon} {self.name}"
