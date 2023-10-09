def get_income():
        rental_income = int(input("What is your rental income? "))
        laundry_income  = int(input("What is your laundry income? "))
        storage_income = int(input("What is your storage income? "))
        misc_income = int(input("What is your miscellanious income? "))
        total_income = int(rental_income + laundry_income + storage_income + misc_income)
        print(f'Your total income is: {total_income}')

get_income()