def vowel_filter(func):
    def wrapper():
        vowels = set('aeoui' + 'aeoui'.upper())
        result = func()
        return [c for c in result if c in vowels]
    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]



print(get_letters())