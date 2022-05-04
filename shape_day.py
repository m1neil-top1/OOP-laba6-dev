def day_shape(days):
    if days == 21:
        return "день."
    elif days >= 22 and days <= 24:
        return "дня."
    elif days >= 5 and days <= 20 or days >= 25 and days <= 30:
        return "дней."
