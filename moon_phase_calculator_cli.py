import sys
from datetime import datetime
import ephem
from moon_phase_class import MoonCalculator

class MoonPhaseCLI(MoonCalculator):
    """
    CLI implementation of moon phase calculations
    """
    def display(self):
        """
        Display moon details in a formatted output
        """
        details = self.moon_details
        
        print(f"Date: {self.date.strftime('%Y-%m-%d')}")
        print(f"Moon Phase (Numeric): {details['phase_numeric']:.4f}")
        print(f"Moon Phase (Name): {details['phase_name']}")
        print(f"Moon Illumination: {details['illumination_percent']:.2f}%")
        print(f"Illumination Description: {details['illumination_description']}")
        print(f"Moon Age: {details['moon_age_days']:.2f} days")
        print(f"Next New Moon: {ephem.Date(details['next_new_moon']).datetime().strftime('%Y-%m-%d')}")

def main():
    """
    Main entry point for the moon phase CLI application
    """
    # Check if a date is provided as a command-line argument
    if len(sys.argv) > 1:
        try:
            # Attempt to parse the date from command-line argument
            input_date = datetime.strptime(sys.argv[1], '%Y-%m-%d')
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD.")
            sys.exit(1)
    else:
        # Use current date if no argument provided
        input_date = datetime.now()
    
    # Create and display moon phase information
    moon_cli = MoonPhaseCLI(input_date)
    moon_cli.display()

if __name__ == "__main__":
    main()