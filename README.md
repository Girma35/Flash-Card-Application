```markdown
# Flash Card Application

[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This is a flash card application built with Python and Tkinter. It allows users to learn and test their knowledge of English-Amharic translations using flashcards.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Data Format](#data-format)
- [Usage](#usage)
- [File Descriptions](#file-descriptions)
- [Customization](#customization)
- [License](#license)
- [Acknowledgements](#acknowledgements)
- [Contributing](#contributing)
- [Contact](#contact)

## Features

- Display flashcards with English words.
- Automatically flip the flashcard to reveal the Amharic translation after 3 seconds.
- Mark words as known to remove them from the pool of flashcards.
- Buttons to indicate if a word is known or unknown.
- Beautiful graphical user interface using Tkinter.

## Requirements

- Python 3.x
- pandas
- tkinter (usually included with Python)

## Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/yourusername/flashcard-app.git
   cd flashcard-app
   ```

2. **Install the required Python packages**:
   ```sh
   pip install pandas
   ```

3. **Ensure you have the following directory structure**:
   ```
   flashcard-app/
   ├── data/
   │   └── data.csv
   ├── images/
   │   ├── right.png
   │   ├── wrong.png
   │   ├── card_front.png
   │   └── card_back.png
   ├── main.py
   └── README.md
   ```

## Data Format

The `data/data.csv` file should contain the English and Amharic words in the following format:

```csv
english,amharic
hello,ሰላም
goodbye,ቻው
```

## Usage

1. **Run the application**:
   ```sh
   python main.py
   ```

2. The main window will display a flashcard with an English word. After 3 seconds, it will flip to show the Amharic translation.

3. Use the buttons to indicate if you know the word:
   - **Right Button**: Mark the word as known and remove it from the pool.
   - **Wrong Button**: Skip to the next word without removing it from the pool.

## File Descriptions

- **main.py**: The main script that runs the flashcard application.
- **data/data.csv**: The CSV file containing English-Amharic word pairs.
- **images/right.png**: Image for the "known" button.
- **images/wrong.png**: Image for the "unknown" button.
- **images/card_front.png**: Image for the front side of the flashcard.
- **images/card_back.png**: Image for the back side of the flashcard.
  
## The output of the application
https://github.com/Girma35/Flash-Card-Application/assets/143084812/fba84768-3e0e-4bea-8e5b-22c7d59d6bb5

## Customization

- You can update the `data/data.csv` file to include your own words and translations.
- You can change the images by replacing the files in the `images` directory with your own images.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

- This project uses Tkinter for the graphical user interface.
- The data for translations is stored in a CSV file and loaded using pandas.

## Contributing

Feel free to contribute to this project by submitting issues or pull requests. Any contributions are welcome!

## Contact

For any questions or feedback, please contact [your email](mailto:your.email@example.com).

Enjoy learning new words with your flashcard app!
```

### Key Additions:

- **Badges**: Added badges for Python version and license to the top of the README.
- **Table of Contents**: Included a table of contents for easy navigation.

Make sure to replace placeholders such as `yourusername` and `your.email@example.com` with your actual GitHub username and email address. This structure will make your README look more professional and user-friendly.
```








