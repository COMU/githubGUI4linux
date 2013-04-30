_ = None
try:
    import gettext
    gettext.textdomain('github4linux')
    _ = gettext.gettext
except ImportError:
    def dummytrans (text):
        """ Return argument without change """
        return(text)

    _ = dummytrans
