import re


def normalize_phone(phone_number: str) -> str:
    cleaned_number = re.sub(r'[^\d+]', '', phone_number)
    if cleaned_number.startswith('+'):
        if cleaned_number.startswith('+380'):
            return cleaned_number
        else:
            raise ValueError("Підтримуються лише українські номери телефонів з кодом +380.")
    else:
        cleaned_number = '+38' + cleaned_number

    return cleaned_number
