# iCal Filter

This project filters events from an iCal calendar based on a blacklist of keywords.

## Files

- `file.py`: Contains the main logic for downloading, filtering, and saving the iCal calendar.
- `README`: This file.

## Usage

1. **Set Up**: Ensure you have the necessary dependencies installed. This script requires the `requests` library. You can install it using pip:
    ```sh
    pip install requests
    ```

2. **Configuration**: Update the `BLACKLIST` and `URL` variables in `file.py` with your desired blacklist keywords and the iCal URL.

3. **Run the Script**: Execute the script to download, filter, and save the calendar:
    ```sh
    python3 file.py
    ```

4. **Output**: The filtered calendar will be saved as `filtered_calendar.ics`.

## Example

Here's an example of how to use the script:

1. Update the `BLACKLIST` and `URL` in `file.py`:
    ```py
    BLACKLIST = ["JAVA1", "Netwerken", "ICT.P.IP.V22", "Ontwerpen", "Query", "ICT.P.KBSa1.V22", "Kenmerkende beroepssituatie 1"]
    URL = "https://ical.windesheim.nl/api/Rooster-v10?culture=en&key=your_key_here"
    ```

2. Run the script:
    ```sh
    python3 file.py
    ```

3. The filtered calendar will be saved as `filtered_calendar.ics`.

## Functions

- `download_calendar(url)`: Downloads the iCal data from the given URL.
- `filter_calendar(ical_data, blacklist)`: Filters the iCal data based on the blacklist keywords.
- `save_filtered_calendar(filtered_cal, output_file)`: Saves the filtered iCal data to a file.

## License

This project is licensed under the MIT License.
