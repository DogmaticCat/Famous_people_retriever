import wikipedia
from database_service import initialize_db, add_person, retrieve_all


def main():
    initialize_db()
    start_query()


def start_query():
    while True:
        term = ask_for_input()
        try:
            page = fetch_page(term)
            term = page.title if page.title else term
            store_person(term, wikipedia.summary(page.title, sentences=3))
            break
        except wikipedia.exceptions.PageError:
            print("I don't know this person")
            suggestion = wikipedia.search(term)
            try:
                if yes_or_no("\nDid you mean " + suggestion[0] + "?\n"):
                    store_person(term, wikipedia.summary(term, sentences=3))
                    break
            except IndexError:
                continue
        except wikipedia.exceptions.DisambiguationError as error:
            print("Ambiguous search, too many results: ")
            continue

def ask_for_input():
    return input("\nPlease enter the full name of someone famous:\n")


def fetch_page(title):
    return wikipedia.page(title=title)


def store_person(title, summary):
        add_person(title, summary)
        print("Title: [" + title + "] has been added to database with the following summary:\n[" + summary + "]")



def yes_or_no(question):
    while True:
        answer = input(question + " (y/n):\n").lower().strip()
        if answer.startswith("y"):
            return True
        elif answer.startswith("n"):
            return False
        else:
            print("\nWrong input. Please type Y for yes or N for no\n")
            continue


if __name__ == "__main__":
    main()
