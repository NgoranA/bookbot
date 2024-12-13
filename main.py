def print_number_of_words(contents):
    words = contents.split()
    print(f"{len(words)} words found in the document")


def count_characters(contents):
    results = {}
    converted_text = contents.lower()
    for char in converted_text:
        if char in results:
            results[char] += 1
        else:
            results[char] = 1
    return results


def sort_on(dict):
    return dict["count"]


def get_book_text(path):
    with open(path) as f:
        return f.read()


def main():
    book_path = "books/frankenstein.txt"
    file_contents = get_book_text(book_path)

    print(f"--- Begin report of {book_path} ---")

    print_number_of_words(file_contents)

    print()

    results = count_characters(file_contents)

    results_list = []
    for val in results:
        results_list.append({"char": val, "count": results[val]})
    results_list.sort(reverse=True, key=sort_on)
    for val in results_list:
        if val["char"].isalpha():
            print(f"The '{val["char"]}' character was found {val["count"]} times")
    print("--- End report ---")


main()
