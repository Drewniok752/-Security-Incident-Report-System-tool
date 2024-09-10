
import pandas as pd
from datetime import datetime

# Define paths
REPORT_PATH = r'C:\Users\Damian\Desktop\SIRS_project.txt'

def generate_report():
    """Generate a detailed report with sample incidents."""
    # Sample data
    data = {
        'id': [1, 2, 3],
        'event_id': ['E001', 'E002', 'E003'],
        'source_name': ['System', 'Application', 'Security'],
        'event_type': ['Error', 'Warning', 'Alert'],
        'description': ['Disk space is low.', 'Application not responding.', 'Unauthorized access attempt.']
    }
    
    df = pd.DataFrame(data)
    
    # Create a detailed report content
    report_content = (
        f"Date and Time: {datetime.now()}\n"
        f"Report: Detailed Incident Report\n\n"
        f"Summary of Incident Report:\n\n"
        f"Number of incidents: {len(df)}\n\n"
        f"{df.to_string(index=False)}\n\n"
        f"Details:\n"
        f"- Total Incidents: {len(df)}\n"
        f"- Event Types:\n"
        f"  - {', '.join(df['event_type'].unique())}\n"
        f"- Source Names:\n"
        f"  - {', '.join(df['source_name'].unique())}\n"
    )
    
    # Save to file
    with open(REPORT_PATH, 'w') as report_file:
        report_file.write(report_content)
    
    print(f"Report generated and saved to {REPORT_PATH}")

def main():
    """Main function to run the script."""
    print("Starting SIRS project script")
    generate_report()
    print("Script finished")

if __name__ == "__main__":
    main()

