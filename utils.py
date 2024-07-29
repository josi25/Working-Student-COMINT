
def generate_date_format():
    date_formats = []
    separators = [' ', ',', '/', '.', '-']  # List of possible separators
    months = ['%m', '%B', '%b']  # List of possible month formats

    for sep in separators:
        for month in months:
            date_formats.append(f'%d{sep}{month}{sep}%Y')
            date_formats.append(f'{month}{sep}%d{sep}%Y')
            date_formats.append(f'{month}{sep}%Y')
            date_formats.append(f'%Y{sep}{month}')

    return date_formats
