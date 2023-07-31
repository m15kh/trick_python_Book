name_for_userid = {
382: 'Alice',
950: 'Bob',
590: 'Dilbert',
}


#first method
def greeting1(userid):
    if userid in name_for_userid:
        print('Hi %s!1' % name_for_userid[userid])
    else:
        print("hi there 1")
greeting1(3820)

# betteer method

def greeting2(userid):
    try:
        print('Hi %s!2' % name_for_userid[userid])
    except KeyError:
        print("hello theree 2")
greeting2(382)

def greeting3(userid):
    print('Hi %s! 3' % name_for_userid.get(userid, "there"))

greeting3(38002)

