# Text to Image Converter

A lightweight, efficient Python command-line utility that converts text into high-quality image. Perfect for generating clean typography images or saving text logs as visuals.

## 🚀 Features

- **Full UTF-8 Support:** Perfect handling of Czech characters and diacritics (ěščřžýáíéůú).
- **Dynamic Image Sizing:** The final image automatically resizes to perfectly fit your text layout.
- **Customizable Output:** Easily adjust font sizes and image paddings directly from the terminal.
- **Robust Layout Handling:** Built-in multi-line text measurement ensuring text never clips.

## 📋 Requirements

- Python 3.10 or newer
- **Pillow** library (Python Imaging Library)

## 🛠 Installation

### 1. Clone or download this repository:

```
git clone https://github.com/michaldanhel/text-to-image-converter.git
cd text-to-image-converter
```

### 2. Install the required dependencies:

It is highly recommended to specify the Python version you want to use.

**On Windows:**

```
py -3.14 -m pip install Pillow
```

**On macOS / Linux:**

```
python3.14 -m pip install Pillow
```

## 📖 Usage

The script is a command-line tool. You can pass the input text file as a required argument, along with optional parameters for font size and padding.

### Basic Usage (default settings: Font 18px, Padding 20px)

```
python text_to_image.py my_text.txt
```

*This will generate a file named `my_text.png` in the same directory.*

### Advanced Options

You can customize the output using optional flags:

- `--font_size`: Font size in pixels (default is `18`).
- `--padding_size`: Image border padding in pixels (default is `20`).

**Example with custom settings:**

```
python text_to_image.py poems.txt --font_size 24 --padding_size 40
```

## ℹ️ Help Menu

To see all available arguments and options directly in your terminal, run:

```
python text_to_image.py --help
```

## 📂 Project Structure

```
├── LICENSE             # GNU GPL v2.0 License
├── README.md           # Documentation and usage guide
└── text_to_image.py    # The main Python script
```

## 👨‍ About the Author

Hi, I am [Michal Daňhel](https://github.com/michaldanhel) a tech enthusiast and an audiophile. I enjoy building clean, useful scripts and open-source tools that solve everyday tech problems.

If you appreciate this application, you can support my work:
- ☕ [Buy me a Coffee ($5)](https://www.michaldanhel.com/support/buy-me-coffee)
- 🍔 [Buy me a Lunch ($10)](https://www.michaldanhel.com/support/buy-me-lunch)
- 🚀 [Become a Project Sponsor ($25)](https://www.michaldanhel.com/support/become-project-sponsor)
- 💸 [Choose your own amount](https://www.michaldanhel.com/support/choose-own-amount)

## 📂 License

Copyright (C) 2026 Michal Daňhel

This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
