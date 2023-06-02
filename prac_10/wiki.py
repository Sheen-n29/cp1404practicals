import wikipedia

while True:
    user_search = input("Enter something you want to search:  ")
    if not user_search:
        break

    try:
        page = wikipedia.page(user_search, auto_suggest=True)
        print("Title:", page.title)
        print("Summary:", page.summary)
        print("URL:", page.url)
    except wikipedia.exceptions.PageError as e:
        print("Page Error: The page does not exist.")

    print()
