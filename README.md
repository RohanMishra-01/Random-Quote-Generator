# Random Quote Generator

A simple command-line based Random Quote Generator built with Python. The user selects how many quotes they want and the program displays randomly picked motivational quotes from a collection of 100+ quotes by famous personalities.

---

## Project Structure

    random-quote-generator/
    │
    ├── main.py           # Entry point — runs the main menu loop
    ├── comp_choice.py    # Randomly picks a quote from the collection
    └── utils.py          # Shared data — list of 100+ quotes with authors

---

## Features

- **Random Quotes** — Picks quotes randomly from a collection of 100+ entries
- **Multiple Quotes** — User can request 1 to 4 quotes in a single session
- **Author Attribution** — Every quote is displayed with the author's name
- **Wide Collection** — Quotes from Einstein, Gandhi, Lincoln, Mandela, and many more

---

## Getting Started

### Prerequisites

- Python 3.x installed on your system

### Installation

1. Clone the repository:

        git clone https://github.com/RohanMishra-01/random-quote-generator.git
        cd random-quote-generator

2. Run the program:

        python main.py

No external dependencies required — pure Python!

---

## Usage

On running `main.py`, you will see:

    --------------------WELCOME--------------------

    How many quotes you want?
    1. One
    2. Two
    3. Three
    4. Four

    Enter your choice:

After entering your choice, quotes are displayed like this:

    ('The secret of getting ahead is getting started.', 'Mark Twain')
    ('Be the change that you wish to see in the world.', 'Mahatma Gandhi')

---

## Quote Collection

The quotes are stored as tuples in `utils.py` in the format:

    ("Quote text here.", "Author Name")

The collection currently includes 100+ quotes from personalities such as:

- Albert Einstein
- Mahatma Gandhi
- Nelson Mandela
- Steve Jobs
- Walt Disney
- Maya Angelou
- Abraham Lincoln
- Winston Churchill
- and many more...

---

## Future Improvements

- [ ] Display quotes in a cleaner formatted style (not as raw tuples)
- [ ] Add a category filter (motivational, life, success, etc.)
- [ ] Allow the user to request any number of quotes, not just 1-4
- [ ] Save favourite quotes to a text file
- [ ] Add a daily quote feature

---

## Contributing

Contributions are welcome. Feel free to fork the repo and submit a pull request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

---

## Author

Developed by [Rohan Mishra](https://github.com/RohanMishra-01)
