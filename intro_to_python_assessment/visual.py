"""
This module is responsible for visualising the data using Matplotlib.
"""

"""
Task 22 - 24: Write suitable functions to visualise the data as follows:

- Display the number of confirmed cases per country/region using a pie chart
- Display the top 5 countries for deaths using a bar chart
- Display a suitable (animated) visualisation to show how the number of confirmed cases, deaths and recovery change over
time. This could focus on a specific country or countries.

Each function should visualise the data using Matplotlib.
"""

# TODO: Your code here
from intro_to_python_assessment import process
import matplotlib.pyplot as plt
import random
import matplotlib.colors as mcolors


def display_cases_countries():
    # pie chart
    # extracting country names
    def all_names():
        data = process.summary("covid_19_data.csv")
        # returning the names (keys) of the countries
        x = data.keys()
        return x

    def allnumbers():
        # numbers
        data = process.summary("covid_19_data.csv")

        x = data.values()
        # only the values are shown
        c = list(x)

        # sorting the numbers by magnitude
        # sort not need when displaying all the countries by cases

        return c[0][0], c[1][0], c[2][0], c[3][0], c[4][0], c[5][0], c[6][0], c[7][0], c[8][0], c[9][0], c[10][0], \
               c[11][0], c[12][0], c[13][0], c[14][0], c[15][0], c[16][0], c[17][0], c[18][0], c[19][0], c[20][0], \
               c[21][0], c[22][0], c[23][0], c[24][0], c[25][0], c[26][0], c[27][0], c[28][0], c[29][0], c[30][0], \
               c[31][0]

    labels = all_names()
    # the name retriever works
    # the number is not, had to do it manually
    sizes = allnumbers()

    fig1, ax1 = plt.subplots()
    # colors are going to be different and can be visualized better
    colors = random.choices(list(mcolors.CSS4_COLORS.values()), k=32)
    patches, texts = plt.pie(sizes, colors=colors, shadow=False, startangle=90)
    plt.legend(patches, labels, loc="best")
    ax1.axis('equal')
    plt.show()

    ##################################################################

def top_deadly_countries():
    # bar chart
    def five_numbers():
        # numbers
        data = process.summary("covid_19_data.csv")
        # {'Mainland China': [38340, 905, 838], 'Hong Kong': [65, 0, 0], 'Macau': [46, 0, 0], 'Taiwan': [52, 0, 0], 'US': [37, 0, 0], 'Japan': [55, 0, 6], 'Thailand': [96, 0, 49], 'South Korea': [36, 0, 0], 'China': [0, 0, 0], 'Kiribati': [0, 0, 0], 'Singapore': [53, 0, 0], 'Philippines': [2, 0, 0], 'Malaysia': [38, 0, 0], 'Vietnam': [18, 0, 0], 'Australia': [41, 0, 4], 'Mexico': [0, 0, 0], 'Brazil': [0, 0, 0], 'Colombia': [0, 0, 0], 'France': [30, 0, 0], 'Nepal': [7, 0, 0], 'Canada': [12, 0, 0], 'Cambodia': [5, 0, 0], 'Sri Lanka': [5, 0, 0], 'Ivory Coast': [1, 0, 0], 'Germany': [17, 0, 0], 'Finland': [3, 0, 0], 'United Arab Emirates': [12, 0, 0], 'India': [2, 0, 0], 'Italy': [2, 0, 0], 'UK': [2, 0, 0], 'Russia': [2, 0, 0], 'Sweden': [1, 0, 0]}

        x = data.values()
        # only the values are shown
        c = list(x)
        # sorting the numbers by magnitude
        c.sort(reverse=True)
        # returning the 5 countries with the most cases.
        return c[0][0], c[1][0], c[2][0], c[3][0], c[4][0]

    def label(group):
        # making the numbers visible on the bars!
        for c in group:
            height = c.get_height()
            ax.annotate(str(height), xy=(c.get_x(), height))

    countries = ['Mainland China','Thailand', 'Hong Kong', 'Japan','Singapore' ]
    confirmed_cases = five_numbers()

    # bar chart
    fig, ax = plt.subplots()
    visual = ax.bar(countries, confirmed_cases)
    # Title:
    ax.set_title('Top 5 countries with the most confirmed cases')
    # y title:
    ax.set_ylabel('Total number of cases')
    # visible numbers on the bars
    label(visual)
    plt.show()

##########################################
def all_cases():
    # bar chart with all cases, better visually.
    def all_names():
        data = process.summary("covid_19_data.csv")
        # returning the names (keys) of the countries
        x = data.keys()
        return x
    def allnumbers():
        # numbers
        data = process.summary("covid_19_data.csv")

        x = data.values()
        # only the values are shown
        # we need the a list to be able to use index numbers
        c = list(x)
        # Returning only the cases of the countries

        return c[0][0], c[1][0], c[2][0], c[3][0], c[4][0], c[5][0], c[6][0], c[7][0], c[8][0], c[9][0], c[10][0], \
               c[11][0], c[12][0], c[13][0], c[14][0], c[15][0], c[16][0], c[17][0], c[18][0], c[19][0], c[20][0], \
               c[21][0], c[22][0], c[23][0], c[24][0], c[25][0], c[26][0], c[27][0], c[28][0], c[29][0], c[30][0], \
               c[31][0]

    # labels
    def label(group):
        # making the numbers visible on the bars!
        for c in group:
            height = c.get_height()
            ax.annotate(str(height), xy=(c.get_x(), height))

    countries = all_names()
    confirmed_cases = allnumbers()

    fig, ax = plt.subplots()
    visual = ax.bar(countries, confirmed_cases)
    # Title:
    ax.set_title('All countries with confirmed cases')
    # y title:
    ax.set_ylabel('Total number of cases')
    # visible numbers on the bars
    label(visual)
    plt.show()




