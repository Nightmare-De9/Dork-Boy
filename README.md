# Dork-Boy - Google Dork Search Tool

Dork-Boy is a powerful command-line tool designed for performing advanced Google Dork searches efficiently using complete Google dependency. With its interactive interface and extensive search capabilities, Dork-Boy simplifies the process of uncovering publicly accessible information through Google search queries. This tool is suitable for cybersecurity enthusiasts, penetration testers, and researchers who want to explore the web more effectively.

Dork-Boy leverages Google search to retrieve targeted results based on user-defined queries, helping users gather information quickly and accurately. Its robust design ensures seamless operation with options for saving search results and re-running queries without restarting the tool.

## Features

- Perform Google Dork searches easily.
- Save search results to a file.
- Retry search without restarting the program.
- Enhanced input validation and error handling.
- Interactive command-line interface.

## Requirements

- Python 3.x
- `google` module

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Nightmare-De9/Dork-Boy.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Dork-Boy
   ```
3. Install dependencies:
   ```bash
   pip install google
   ```

## How to Use

1. Run the script:

   ```bash
   python3 dork_boy.py
   ```

2. Follow the prompts:

   - Enter a Google Dork search query.
   - Specify the number of websites to display.
   - Choose whether to save the output to a file.
   - If saving, provide a file name.

3. Review the search results displayed on the console.

4. Choose whether to perform another search or exit the program.

## Example

```
[+] Enter The Dork Search Query: intitle:"index of" password
[+] Enter The Number Of Websites To Display: 5
[+] Save the output to a file? (Y/N): Y
[~] File name: search_results

[+] 1: http://example.com/index
[+] 2: http://example.org/data
...
[?] Search again? (Y/N): N
```

## License

This project is based on the original work by **Bulls Eye (Jolanda de Koff)** and revised by **Nightmare-De9**.

- GitHub (Original Author): [BullsEye0](https://github.com/BullsEye0)
- GitHub (Reviser): [Nightmare-De9](https://github.com/Nightmare-De9)

**Disclaimer:** Use this tool responsibly. The creators are not liable for any misuse or illegal activities involving this software.
