def title_case(title, minor_words=''):
    title = [word.title() if word not in minor_words.lower().split() else word for word in title.lower().split()]
    return (title[0].title() + ' ' + ' '.join(title[1:])).rstrip() if len(title) else ''
