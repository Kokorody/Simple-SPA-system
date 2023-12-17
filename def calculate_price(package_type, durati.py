def calculate_price(package_type, duration, is_member):
    discount = 0
    price = 0

    if package_type == 'A' and duration == 1:
        price = 31
        if is_member == "Yes":
            discount = 0.05
    elif package_type == 'A' and duration < 1:
        price = 21
        if is_member == "Yes":
            discount = 0.05
    elif package_type == 'A' and duration > 1:
        price = 31 + 31 * (duration - 1)
        if is_member == "Yes":
            discount = 0.05
    elif package_type == 'B' and duration == 1:
        price = 31
        if is_member == "Yes":
            discount = 0.05
    elif package_type == 'B' and duration < 1:
        price = 21
        if is_member == "Yes":
            discount = 0.05
    elif package_type == 'B' and duration > 1:
        price = 31 + 31 * (duration - 1)
        if is_member == "Yes":
            discount = 0.05
    elif package_type == 'C' and duration == 2:
        price = 95
        if is_member == "Yes":
            discount = 0.1
    elif package_type == 'C' and duration < 2:
        price = 85
        if is_member == "Yes":
            discount = 0.1
    elif package_type == 'C' and duration > 2:
        price = 95 + 42 * (duration - 2)

    net_price = price - (price * discount) if is_member[0] == 'Y' else price
    return net_price


def generate_receipt(name, package_type, duration, is_member, net_price):
    print("\n-------------- Honeybliss Spa Beauty --------------")
    print(f"Customer Name: {name}")
    print(f"Package Type: {package_type}")
    print(f"Treatment Duration: {duration:.2f} hour(s)")
    print(f"Membership: {is_member}")
    print(f"Net Price (USD): {net_price:.2f}")
    print("---------------------------------------------------\n")


def main():
    name = input("Enter your name: ")
    package = input("Enter the type of package (A, B, or C): ").upper()
    duration = float(input("Enter the treatment duration in hours: "))
    membership = input("Are you a member? (Yes or No): ").capitalize()

    valid_packages = ['A', 'B', 'C']
    valid_package = package in valid_packages

    if valid_package:
        net_price = calculate_price(package, duration, membership)
        if net_price != 0:
            generate_receipt(name, package, duration, membership, net_price)
        else:
            print("Invalid Honeybliss Spa Package")
    else:
        print("Invalid Honeybliss Spa Package")


if __name__ == "__main__":
    main()
