from datetime import datetime, timedelta, date


def generate_dates(start_date_str, num_dates, skip):
    start_date = date.fromisoformat(start_date_str)

    return [str(start_date + timedelta(days=i * skip)) for i in range(num_dates)]


print(generate_dates("2024-09-19", 5, 3))
