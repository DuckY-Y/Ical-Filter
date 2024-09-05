import requests

BLACKLIST = ["JAVA1", "Netwerken", "ICT.P.IP.V22", "Ontwerpen", "Query", "ICT.P.KBSa1.V22", "Kenmerkende beroepssituatie 1"]  # Add the words you want to blacklist
URL = "https://ical.windesheim.nl/api/Rooster-v10?culture=en&ke............." # Add your iCal link here
OUTPUT_NAME = "filtered_calendar.ics"

def download_calendar(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def filter_calendar(ical_data, blacklist):
    lines = ical_data.splitlines()
    filtered_lines = []
    exclude = False
    current_event = []
    in_event = False

    for line in lines:
        if line.startswith("BEGIN:VEVENT"):
            exclude = False
            current_event = []
            in_event = True

        if in_event:
            current_event.append(line)
        else:
            filtered_lines.append(line)

        if not exclude and in_event:
            for keyword in blacklist:
                if keyword.lower() in line.lower():
                    exclude = True
                    print(f"Excluding event containing: {keyword}")
                    break

        if line.startswith("END:VEVENT"):
            if not exclude:
                filtered_lines.extend(current_event)
            in_event = False

    return "\n".join(filtered_lines)

def save_filtered_calendar(filtered_cal, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(filtered_cal)

if __name__ == "__main__":
    ical_data = download_calendar(URL)
    filtered_cal = filter_calendar(ical_data, BLACKLIST)
    save_filtered_calendar(filtered_cal, OUTPUT_NAME)
    
    print(f"Filtered calendar saved as '{OUTPUT_NAME}'")