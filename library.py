def print_menu():
    print("\n📚 Welcome to your Personal Library Manager - Created by Farhana Yousuf! 📚")
    print("\nMenu:")
    print("1️⃣. Add a book")
    print("2️⃣. Remove a book")
    print("3️⃣. Edit a book")
    print("4️⃣. Search for a book")
    print("5️⃣. Display all books")
    print("6️⃣. Display statistics")
    print("7️⃣. Exit")

def add_book(library):
    print("\n✅ Add a new book:")
    # Title input with validation
    title = ""
    while not title:
        title = input("📖 Enter the book title: ").strip()
        if not title:
            print("❌ Title cannot be empty. Please try again.")
    
    # Author input with validation
    author = ""
    while not author:
        author = input("🖋️ Enter the author: ").strip()
        if not author:
            print("❌ Author cannot be empty. Please try again.")
    
    # Year input with validation
    while True:
        year_input = input("📅 Enter the publication year: ").strip()
        if year_input.isdigit():
            year = int(year_input)
            break
        print("❌ Invalid year. Please enter a valid integer.")
    
    genre = input("🎭 Enter the genre: ").strip()
    
    # Read status validation
    read_status = ""
    while read_status.lower() not in ['yes', 'no', 'y', 'n']:
        read_status = input("👀 Have you read this book? (yes/no): ").strip()
        if read_status.lower() not in ['yes', 'no', 'y', 'n']:
            print("❌ Invalid input. Please enter 'yes' or 'no'.")
    read = read_status.lower() in ['yes', 'y']
    
    # Add the new book
    library.append({
        'title': title,
        'author': author,
        'year': year,
        'genre': genre,
        'read': read
    })
    print("\n🎉 Book added successfully!")

def remove_book(library):
    print("\n❌ Remove a book")
    title = input("Enter the title of the book to remove: ").strip().lower()
    matches = [book for book in library if book['title'].lower() == title]
    
    if not matches:
        print("\n📭 No books found with that title.")
        return
    
    print(f"\n🔍 Found {len(matches)} book(s) matching '{title.title()}':")
    for idx, book in enumerate(matches, 1):
        print(f"{idx}. {book['title']} by {book['author']} ({book['year']})")
    
    confirm = input("\n⚠️ Are you sure you want to remove all? (yes/no): ").strip().lower()
    if confirm in ['yes', 'y']:
        for book in matches:
            library.remove(book)
        print(f"\n🗑️ {len(matches)} book(s) removed successfully!")
    else:
        print("\n🚫 Removal cancelled.")

def edit_book(library):
    print("\n✏️ Edit a book")
    title = input("Enter the title of the book to edit: ").strip().lower()
    matches = [book for book in library if book['title'].lower() == title]
    
    if not matches:
        print("📭 No books found with that title.")
        return
    
    print("\n📚 Matching books:")
    for idx, book in enumerate(matches, 1):
        print(f"{idx}. {book['title']} by {book['author']} ({book['year']})")
    
    try:
        choice = int(input("Enter the number of the book to edit: ")) - 1
        if choice < 0 or choice >= len(matches):
            print("❌ Invalid selection.")
            return
    except ValueError:
        print("❌ Invalid input. Please enter a number.")
        return
    
    book = matches[choice]
    print("\n📝 Leave fields blank to keep current values.")
    
    # Edit title
    new_title = input(f"📖 Title [{book['title']}]: ").strip()
    if new_title:
        book['title'] = new_title
    
    # Edit author
    new_author = input(f"🖋️ Author [{book['author']}]: ").strip()
    if new_author:
        book['author'] = new_author
    
    # Edit year
    while True:
        new_year = input(f"📅 Year [{book['year']}]: ").strip()
        if not new_year:
            break
        if new_year.isdigit():
            book['year'] = int(new_year)
            break
        print("❌ Invalid year. Please enter a valid integer.")
    
    # Edit genre
    new_genre = input(f"🎭 Genre [{book['genre']}]: ").strip()
    if new_genre:
        book['genre'] = new_genre
    
    # Edit read status
    current_status = 'yes' if book['read'] else 'no'
    new_read = input(f"👀 Read? (yes/no) [{current_status}]: ").strip().lower()
    while new_read and new_read not in ['yes', 'no', 'y', 'n']:
        new_read = input("❌ Invalid input. Enter yes/no: ").strip().lower()
    if new_read:
        book['read'] = new_read in ['yes', 'y']
    
    print("\n🎉 Book updated successfully!")

def search_books(library):
    print("\n🔍 Search for a book")
    print("1. Search by title")
    print("2. Search by author")
    choice = input("Enter your choice: ").strip()
    
    if choice not in ['1', '2']:
        print("❌ Invalid choice. Returning to menu.")
        return
    
    search_term = input("Enter the search term: ").strip().lower()
    results = []
    
    if choice == '1':
        for book in library:
            if search_term in book['title'].lower():
                results.append(book)
    else:
        for book in library:
            if search_term in book['author'].lower():
                results.append(book)
    
    if not results:
        print("\n📭 No matching books found.")
        return
    
    print(f"\n📚 Matching Books ({len(results)}):")
    for idx, book in enumerate(results, 1):
        read_status = "✅ Read" if book['read'] else "❌ Unread"
        print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")

def display_all_books(library):
    print("\n📚 Your Library:")
    if not library:
        print("📭 Your library is empty.")
        return
    for idx, book in enumerate(library, 1):
        read_status = "✅ Read" if book['read'] else "❌ Unread"
        print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")

def display_statistics(library):
    print("\n📊 Library Statistics:")
    total = len(library)
    print(f"📖 Total books: {total}")
    
    if total == 0:
        print("📈 Percentage read: 0.0%")
        return
    
    read_count = sum(1 for book in library if book['read'])
    percentage = (read_count / total) * 100
    print(f"📈 Percentage read: {percentage:.1f}%")

def save_library(library):
    try:
        with open('library.txt', 'w') as f:
            for book in library:
                line = f"{book['title']}|{book['author']}|{book['year']}|{book['genre']}|{book['read']}\n"
                f.write(line)
        print("\n💾 Library saved successfully!")
    except Exception as e:
        print(f"❌ Error saving library: {e}")

def load_library():
    library = []
    try:
        with open('library.txt', 'r') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split('|')
                if len(parts) != 5:
                    continue
                title, author, year_str, genre, read_str = parts
                try:
                    year = int(year_str)
                    read = read_str == 'True'
                    library.append({
                        'title': title,
                        'author': author,
                        'year': year,
                        'genre': genre,
                        'read': read
                    })
                except ValueError:
                    continue
    except FileNotFoundError:
        pass
    return library

def main():
    library = load_library()
    while True:
        print_menu()
        choice = input("\n👉 Enter your choice: ").strip()
        
        if choice == '1':
            add_book(library)
        elif choice == '2':
            remove_book(library)
        elif choice == '3':
            edit_book(library)
        elif choice == '4':
            search_books(library)
        elif choice == '5':
            display_all_books(library)
        elif choice == '6':
            display_statistics(library)
        elif choice == '7':
            save_library(library)
            print("\n👋 Library saved to file. Goodbye! - Farhana Yousuf")
            break
        else:
            print("\n❌ Invalid choice. Please enter a number between 1️⃣ and 7️⃣.")

if __name__ == "__main__":
    main()