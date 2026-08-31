""" Determine what Bob will reply to someone when they say something to him or ask him a question."""
def response(hey_bob):
    """
    Function that determine what Bob will reply to someone when they say something to him or ask       him a question.

    Parameters :
        hey_bob : String it can be question or phrase

    Return :
        response : string Bob only ever answers one of five things:
        "Sure." This is his response if you ask him a question, such as "How are you?" The               convention used for questions is that it ends with a question mark.
        "Whoa, chill out!" This is his answer if you YELL AT HIM. The convention used for                yelling is ALL CAPITAL LETTERS.
        "Calm down, I know what I'm doing!" This is what he says if you yell a question at him.
        "Fine. Be that way!" This is how he responds to silence. The convention used for silence         is nothing, or various combinations of whitespace characters.
        "Whatever." This is what he answers to anything else.
    """
    if hey_bob.strip() == "" :
        return "Fine. Be that way!"
    if hey_bob.strip().endswith("?") :
        if hey_bob.isupper():
            return "Calm down, I know what I'm doing!"
        return "Sure."
    if hey_bob.isupper() :
        return "Whoa, chill out!"
        
    return "Whatever."
    
    
    
