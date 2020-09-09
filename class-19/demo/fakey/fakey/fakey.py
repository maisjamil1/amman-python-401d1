from faker import Faker
import shutil


fake = Faker('en_US')
# fake2 = Faker('ar_SA')

# print(dir(fake))
# arabic_name = fake2.name()

# print(arabic_name, arabic_name[0])

print(fake.paragraph())


content = ''

for i in range(100):
    content += fake.paragraph()
    content += ' ' + fake.email() + ' '
    content += fake.paragraph()
    content += ' ' + fake.phone_number() + ' '
    content += fake.paragraph()
    content += '\n'

# print(content)

with open('fake_text.txt', 'w+') as file:
    file.write(content)



shutil.copy('fake_text.txt', '..')


def create_fake_contacts(contacts_num):

    contacts = 'first name,last name,phone number,email\n'
    for i in range(contacts_num):
        contacts += fake.first_name()+','
        contacts += fake.last_name()+','
        contacts += fake.phone_number()+','
        contacts += fake.email()+'\n'

    with open('contacts.csv', 'w+') as cont:
        cont.write(contacts)

create_fake_contacts(50)











