
class MerchantId(object):
    def __init__(self):
        self.merid = ''

    def setMerchantId(self,merchantid):

        self.merid = merchantid
        return self.merid

    def getMerchantId(self):
        return self.merid


mid = MerchantId()
print(id(mid))
