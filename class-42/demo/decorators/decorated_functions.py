from decorators import camelize, lowerize

@camelize
@lowerize
def fun_with_words(first_noun, second_noun, verb):
    return f"{first_noun}s love tO {verb} ALL the {second_noun}s"


print(fun_with_words('Cat','CARROT','SINg'))
