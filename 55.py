import string

def generate_hashtag(input_string):
    cleaned_string = input_string.translate(str.maketrans('', '', string.punctuation))
    hashtag = '#' + ''.join(word.capitalize() for word in cleaned_string.split())
    return hashtag[:140]

# Приклади
print(generate_hashtag('Python Community'))           # #PythonCommunity
print(generate_hashtag('i like python community!'))   # #ILikePythonCommunity
print(generate_hashtag('Should, I. subscribe? Yes!')) # #ShouldISubscribeYes

