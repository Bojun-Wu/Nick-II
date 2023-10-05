from django.core.exceptions import ValidationError
import re
from django.utils.translation import gettext_lazy as _


def validate_name(value):
    pattern = re.compile(r'[^\u4e00-\u9fa5]')
    if not value:
        raise ValidationError(_("必要欄位"))
    elif pattern.search(value):
        raise ValidationError(_("請輸入中文"))
    else:
        return value
    