# Find My Save File

Find My Save File is a terminal tool that helps you locate game save files and game directories easily.

## Features

- **Search for Game Directories**: Searches for game folders in your `~/Games` directory by name
- **Find Save Files**: Automatically locates save files with common extensions (`.sav`, `.dat`, `.profile`, `.conf`)
- **Easy-to-use**: Simple terminal interface with minimal setup required

## Usage

To run the tool, use the following command:

```bash
./findMySave.sh
```

When prompted, enter the name of the game or folder you're looking for:

```
Enter folder name: MyGame
```

The tool will search your `~/Games` directory and return the matching game folders, then display all save files found within that directory.

## How It Works

1. **Game Directory Search**: Scans `~/Games` for directories matching your input (case-insensitive)
2. **Save File Detection**: Searches within the found directory for files matching common save file patterns
3. **Results Display**: Outputs all matching save files to the terminal

## Adding Custom Patterns

To add custom file patterns for save file detection, edit `main.py` and modify the `search_pattern` variable in the `search_for_save()` function:

```python
search_pattern = r".*\(sav\|dat\|profile\|conf\|CUSTOM_EXTENSION\).*"
```

Add your custom extension within the pattern. For example, to add `.backup` files:

```python
search_pattern = r".*\(sav\|dat\|profile\|conf\|backup\).*"
```

The pattern uses regex syntax with `\|` as the OR operator. Add each extension separated by `\|`.

## Removing Patterns

To remove file extensions from the search pattern, simply delete the extension from the pattern string in `main.py`:

**Before:**
```python
search_pattern = r".*\(sav\|dat\|profile\|conf\).*"
```

**After (removing `.dat`):**
```python
search_pattern = r".*\(sav\|profile\|conf\).*"
```

## Configuration

To change the search directory from `~/Games` to a different location, edit `main.py` and modify the `search_root` variable:

```python
search_root = os.path.expanduser("~/YOUR_CUSTOM_PATH")
```

## Requirements

- Python 3
- Unix-like system (Linux, macOS, or WSL on Windows)
- `find` command-line utility

## License

This project is licensed under the MIT License.