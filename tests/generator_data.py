import random
from faker import Faker


class GeneratorData:

    def generator_password(self):
        password = random.randint(100000, 999999)

        return password

    def generator_email(self):
        faker = Faker()
        email = faker.email()

        return email