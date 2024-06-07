def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        text = file_contents.lower()
        wordCount = len(text.split())

    def sort_dict(dict):
        return dict["count"]

    dictCount = {}
    for letter in text:
        if letter.isalpha():
            if letter in dictCount:
                dictCount[letter] += 1
            else:
                dictCount[letter] = 1
            
    listOfDicts = []
    for dict in dictCount:
        listOfDicts.append({"letter":dict, "count":dictCount[dict]})

    listOfDicts.sort(reverse=True, key=sort_dict)

    def printList(list):
        print("---=== Book Report of books/frankenstein.txt ===---")
        print(f"This book contains {wordCount} words.")
        print("")
        for dict in list:
            print(f"The '{dict["letter"]}' character was found '{dict["count"]}' times.")

        print("---=== End ===---")

    printList(listOfDicts)
    
main()