import random

def rng_picker(lowerLimit, upperLimit, amount):
    min_num = min(lowerLimit, upperLimit)
    max_num = max(lowerLimit, upperLimit)
    if max_num - min_num + 1 < amount:
        print("Error: The range of numbers is smaller than the amount of numbers to generate.")
        return []
    random_numbers = random.sample(range(min_num, max_num + 1), amount)
    return random_numbers

def main():
    while True:
        print("--------------- GENERATE RANDOM NUMBERS ---------------")
        lowerLimit = int(input("--> Enter the lower limit: \t"))
        upperLimit = int(input("--> Enter the upper limit: \t"))
        amount = int(input("--> Enter the amount of numbers to generate: "))
        

        if lowerLimit == upperLimit:
            print("Please enter two different numbers!")
            return
        
        random_numbers = rng_picker(lowerLimit, upperLimit, amount)
        
        print("=======================================================")
        print(f"Results: {random_numbers}")
        print("=======================================================")
        
        quit = input("Do you want to quit? (yes/no): ").lower()
        if quit == 'yes':
            break

        print("\n")

if __name__ == "__main__":
    main()
