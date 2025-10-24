from split_evens_odds import SplitEvensOdds

def main():
    lst = SplitEvensOdds()
    lst.build_forward_list([1, 2, 3, 4, 5, 6, 7, 8, 15, 14, 13, 12, 11, 10, 9])

    print("Original List:")
    lst.display()

    evens, odds = lst.split_even_odd()

    print("\nEvens List:")
    evens.display()

    print("\nOdds List:")
    odds.display()

    print("\nOriginal List after split:")
    lst.display()

if __name__ == "__main__":
    main()