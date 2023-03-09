class User:
    active_users = []

    def __init__(self,name,email):
        self.name = name
        self.email = email

    def __comparable(self):
        return { key: value.lower() for key, value in self.__dict__.items() }

    def __eq__(self,other):
        return self.__comparable() == other.__comparable()

    def __ne__(self, other):
        return self.__comparable() != other.__comparable()

    def activate(self):
        if not self.is_active():
            self.__class__.active_users.append(self)

    def deactivate(self):
        if self.is_active():
            self.__class__.active_users.remove(self)

    def is_active(self):
        return self in self.__class__.active_users

me = User("alex","amcurley@amazon.com")
me.name = "Alex Curley"
print(me.name)

print(f"Active: {me.is_active()}. Active users: {User.active_users}")
# me.activate()
# me.activate()
# print(f"Active: {me.is_active()}. Active users: {User.active_users}")
# me.deactivate()
# me.deactivate()
# print(f"Active: {me.is_active()}. Active users: {User.active_users}")

# print(f"Active users off of `me`: {me.active_users}, Class level {User.active_users}")
# me.active_users = "Just Me"
# print(f"Active users off of `me`: {me.active_users}, Class level {User.active_users}")
# user1 = User("Kevin", "kbacon@EXAMPLE.com")
# user2 = User("keviN", "kbacon@EXAMPLE.COM")
# user3 = User("Keith", "keith@EXAMPLE.COM")
