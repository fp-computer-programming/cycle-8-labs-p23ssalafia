#Author: Sean Salafia 12/2/22

def invite_to_party(names):
    for name in names:
        print("Hi " + name + ", I'd like to invite you to my party! Please let me know if you can make it.")
    return names

# Example usage:
names = ["Sean", "Jan", "Preston"]
invitees = invite_to_party(names)
print(invitees)
