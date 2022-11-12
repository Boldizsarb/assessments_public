"""
This module is responsible for the overall program flow. It controls how the user interacts with the
program and how the program behaves. It uses the other modules to interact with the user, carry out
processing, and for visualising information.

Note:   any user input/output should be done using the appropriate functions in the module 'tui'
        any processing should be done using the appropriate functions in the module 'process'
        any visualisation should be done using the appropriate functions in the module 'visual'
"""


# Task 10: Import required modules
# TODO: Your code here
import tui
import csv
import process
import visual


# Task 11: Create an empty list named 'covid_records'.
# This will be used to store the data read from the source data file.
# TODO: Your code here

covid_records = []
file = "covid_19_data.csv"


def run():
    # Task 12: Call the function welcome of the module 'tui'.
    # This will display our welcome message when the program is executed.
    # TODO: Your code here
    tui.welcome()
    file = "covid_19_data.csv"

    # Task 13: Load the data.
    # - Use the appropriate function in the module 'tui' to display a message to indicate that the data loading
    # operation has started.
    # - Load the data. Each line in the file should be a record in the list 'covid_records'.
    # You should appropriately handle the case where the file cannot be found or loaded.
    # - Use the appropriate functions in the module 'tui' to display a message to indicate how many records have
    # been loaded and that the data loading operation has completed.
    # TODO: Your code here
    # indicating that the process has started
    # displaying data loading
    tui.progress("Loading data", 0)
    try:
        with open("covid_19_data.csv") as csv_file:
            csv_reader = csv.reader(csv_file)
            headings = next(csv_reader)
            next(csv_reader)
            for line in csv_reader:
                covid_records.append(line)
    except IOError:
        tui.error("Could not read the file")

    tui.total_records(len(covid_records))
    tui.progress("Loading data", 100)

    ######################################################################

    while True:
        # Task 14: Using the appropriate function in the module 'tui', display a menu of options
        # for the different operations that can be performed on the data (menu variant 0).
        # Assign the selected option to a suitable local variable
        # TODO: Your code here

        # Task 15: Check if the user selected the option for processing data.  If so, then do the following:
        # - Use the appropriate function in the module tui to display a message to indicate that the data processing
        # operation has started.
        # - Process the data (see below).
        # - Use the appropriate function in the module tui to display a message to indicate that the data processing
        # operation has completed.
        #
        # To process the data, do the following:
        # - Use the appropriate function in the module 'tui' to display a menu of options for processing the data
        # (menu variant 1).
        # - Check what option has been selected
        #
        #   - If the user selected the option to retrieve an individual record by serial number then
        #       - Use the appropriate function in the module 'tui' to indicate that the record retrieval process
        #       has started.
        #       - Use the appropriate function in the module 'process' to retrieve the record and then appropriately
        #       display it.
        #       - Use the appropriate function in the module 'tui' to indicate that the record retrieval process has
        #       completed.
        #
        #   - If the user selected the option to retrieve (multiple) records by observation dates then
        #       - Use the appropriate function in the module 'tui' to indicate that the records retrieval
        #       process has started.
        #       - Use the appropriate function in the module 'process' to retrieve records with
        #       - Use the appropriate function in the module 'tui' to display the retrieved records.
        #       - Use the appropriate function in the module 'tui' to indicate that the records retrieval
        #       process has completed.
        #
        #   - If the user selected the option to group records by country/region then
        #       - Use the appropriate function in the module 'tui' to indicate that the grouping
        #       process has started.
        #       - Use the appropriate function in the module 'process' to group the records
        #       - Use the appropriate function in the module 'tui' to display the groupings.
        #       - Use the appropriate function in the module 'tui' to indicate that the grouping
        #       process has completed.
        #
        #   - If the user selected the option to summarise the records then
        #       - Use the appropriate function in the module 'tui' to indicate that the summary
        #       process has started.
        #       - Use the appropriate function in the module 'process' to summarise the records.
        #       - Use the appropriate function in the module 'tui' to display the summary
        #       - Use the appropriate function in the module 'tui' to indicate that the summary
        #       process has completed.
        # TODO: Your code here

        # Task 21: Check if the user selected the option for visualising data.
        # If so, then do the following:
        # - Use the appropriate function in the module 'tui' to indicate that the data visualisation operation
        # has started.
        # - Visualise the data by doing the following:
        #   - call the appropriate function in the module 'tui' to determine what visualisation is to be done.
        #   - call the appropriate function in the module 'visual'
        # - Use the appropriate function in the module 'tui' to display a message to indicate that the
        # data visualisation operation has completed.
        # TODO: Your code here
        
        # Task 25: Check if the user selected the option for exporting data.  If so, then do the following:
        # - Use the appropriate function in the module 'tui' to retrieve the type of data to be exported.
        # - Check what option has been selected
        #
        # - Use the appropriate function in the module 'tui' to indicate that the export operation has started.
        # - Export the data (see below)
        # - Use the appropriate function in the module 'tui' to indicate that the export operation has completed.
        #
        # To export the data, you should demonstrate the application of OOP principles including the concepts of
        # abstraction and inheritance.  You should create suitable classes with appropriate methods.
        # You should use these to write the records (either all or only those for a specific country/region) to a JSON file.
        # TODO: Your code here

        # Task 26: Check if the user selected the option for exiting the program.
        # If so, then break out of the loop
        # TODO: Your code here

        # Task 27: If the user selected an invalid option then use the appropriate function of the
        # module tui to display an error message
        # TODO: Your code here

        tui.menu(0)
        selected_option = int(input())

        # task 15
        if selected_option == 1:
            tui.progress("Processing Data....", 0)
            tui.menu(1)
            processing_option = int(input())
            if processing_option == 1:
                # displaying that that the program has started
                tui.progress("Retrieving Data...", 0)
                # retrieving the data
                # displaying that record
                tui.display_record(process.retrieve_by_serialn("covid_19_data.csv"))
                # displaying the state of the process
                tui.progress("Retrieving Data....", 100)
            # task 17
            elif processing_option == 2:
                # displaying that that the program has started
                tui.progress("Retrieving data by observation dates", 0)
                # retrievign and displaying data
                tui.display_records(process.retrieving_by_obs("covid_19_data.csv"))
                tui.progress("Retrieving Data by observation dates", 100)
            # Task 18
            elif processing_option == 3:
                # displaying the state of the operation
                tui.progress("Retrieving Data, by Country/Region", 0)
                # retrieving and displaying data
                process.retrieve_by_cr(covid_records)
                # displaying process state
                tui.progress("Retrieving Data by Country/Region", 100)
            # Task 19
            elif processing_option == 4:
                tui.progress("Summarising data", 0)
                tui.display_records(process.summary("covid_19_data.csv"))
                # process.summary("covid_19_data.csv")
                tui.progress("Summarizing data", 100)
            else:
                tui.error("The selected option is not available")

        elif selected_option == 2:
            tui.menu(2)
            visual_option = int(input())
            if visual_option == 1:
                # Visualizing by country or region
                tui.progress("Visualization by Country/Region", 0)
                visual.display_cases_countries()
                tui.progress("Visualization by Country/Region", 100)
                # visualizing by observation
            elif visual_option == 2:
                tui.progress("Visualization by observation chart", 0)
                visual.top_deadly_countries()
                tui.progress("Visualization by observation chart", 100)
            elif visual_option == 3:
                tui.progress("Animation summary", 0)
                tui.error("Animation is missing, sorry!")
                tui.progress("Animation summary", 100)
            elif visual_option == 4:
                tui.progress("Visualisation by Cases", 0)
                visual.all_cases()
                tui.progress("Visualisation by Cases", 100)
            else:
                tui.error("The chosen option is not available!")
        # exporting data:
        elif selected_option == 3:
            tui.progress("Exporting Data", 0)
            tui.error("Sorry, exporting is not available!")
            #tui.progress("Exporting Data", 100)


        elif selected_option == 4:
            break

        else:
            tui.error("The selected option is not available")


if __name__ == "__main__":
    run()
