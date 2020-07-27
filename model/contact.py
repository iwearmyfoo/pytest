class Contact:

    def __init__(self,  firstname=None, midname=None, lastname=None, nickname=None, title=None, company=None,
                 address=None, homephone=None, mobilephone=None, workphone=None, faxphone=None, firstmail=None,
                 secondmail=None, thirdmail=None, homepage=None, bday=None, bmonth=None, byear=None, aday=None,
                 amonth=None, ayear=None, secondaryaddress=None, additionalphone=None, notes=None, name=None, id=None):
        self.firstname = firstname
        self.midname = midname
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.faxphone = faxphone
        self.firstmail = firstmail
        self.secondmail = secondmail
        self.thirdmail = thirdmail
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.secondaryaddress = secondaryaddress
        self.additionalphone = additionalphone
        self.notes = notes
        self.name = name
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.name)













