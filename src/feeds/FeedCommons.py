
class FeedCommons:

    def convert(self, dbDict):
        '''Converts a the tinydb table to a standard dict'''
        dict = {}
        for key, value in dbDict.items():
            dict[key] = value
        return dict