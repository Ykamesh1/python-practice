# ---------------------
# parctical_email_slicer
# ---------------------

thename = input("whats\'s your name ?").strip().capitalize()

theemail = input("what\'s your email").strip()


theusername = theemail[:theemail.index("@")]
thewebsite = theemail[theemail.index("@") + 1:]

print(f"hello{thename} your email is {theemail}")
print(f"your username is {theusername}\nyour website is {thewebsite}")
