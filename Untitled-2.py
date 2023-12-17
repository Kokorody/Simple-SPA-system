# Function to calculate net price based on package, duration, and membership
def calculate_price(package_type, duration, is_member):
    discount = 0
    price = 0

    # Package type A, duration 1
    if package_type == 'A' and duration == 1:
        price = 31
        if is_member.lower() == "yes":
            discount = 0.05
    # Package type A, duration > 1
    elif package_type == 'A' and duration > 1:
        price = 31 * duration
    # Package type B, duration < 1
    elif package_type == 'B' and duration < 1:
        price = 21
    # Package type C, duration 2
    elif package_type == 'C' and duration == 2:
        price = 95
        if is_member.lower() == "yes":
            discount = 0.1
    # Package type C, duration < 2
    elif package_type == 'C' and duration < 2:
        price = 85
    # Package type C, duration > 2
    elif package_type == 'C' and duration > 2:
        price = 95 + 42 * (duration - 2)

    # Calculate net price based on membership discount
    net_price = price - (price * discount) if is_member.lower() == 'yes' else price
    return net_price


# Function to generate receipt
def generate_receipt(name, package_type, duration, is_member, net_price):
    print("\n--------------------- Receipt ---------------------")
    print(f"Customer Name: {name}")
    print(f"Package Type: {package_type}")
    print(f"Treatment Duration: {duration:.2f} hour(s)")
    print(f"Membership: {is_member}")
    print(f"Net Price (USD): {net_price:.2f}")
    print("--------------------------------------------------\n")


# Main function
def main():
    # Get user input
    name = input("Enter your name: ")
    package = input("Enter the type of package (A, B, or C): ").upper()
    duration = float(input("Enter the treatment duration in hours: "))
    membership = input("Are you a member? (Yes or No): ").capitalize()

    # Check if the entered package is valid
    valid_packages = ['A', 'B', 'C']
    valid_package = package in valid_packages

    # Calculate and display receipt if the package is valid
    if valid_package:
        net_price = calculate_price(package, duration, membership)
        if net_price != 0:
            generate_receipt(name, package, duration, membership, net_price)
        else:
            print("Invalid Honeybliss Spa Package")
    else:
        print("Invalid Honeybliss Spa Package")


# Execute the main function if the script is run
if __name__ == "__main__":
    main()
