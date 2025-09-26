'''
 Name: Simon Field
 Class: CPSC 222, Section 01
 Date Submitted: September 19, 2025
 Assignment: Project 2
 Description: This program demonstrates Zipf's Law using MatPlotLib.
 Sources:
  Python, 9/19/2025, https://docs.python.org/3/howto/argparse.html
  Python, 9/19/2025, https://docs.python.org/3/library/argparse.html
  Python, 9/19/2025, https://docs.python.org/3/library/enum.html
  W3Schools, 9/19/2025, https://www.w3schools.com/python/matplotlib_labels.asp
  StackOverflow, 9/19/2025, https://stackoverflow.com/questions/1951742/how-can-i-symlink-a-file-in-linux
 Observations:
  "Zipf's law claimed that the fit between curve and data was better for shorter texts than for longer texts."
  My findings showed that for longer texts (MM, UL), the log-log curve was much more linear than for smaller texts (MR)
  I hypothesize this is owing to the larger variety of words generally present in a longer composition

  For MR, the conventional curve was more limited in its representation of the most frequent words,
  as smaller texts seem to rely on more basic language given the smaller footprint.
'''

import sys
import argparse
import re
import matplotlib.pyplot as plt
from enum import Enum
from operator import itemgetter

class PlotType(Enum):
    """Enum for plot type"""
    LL = 'LL'
    C = 'C'

class PlotName(Enum):
    """Enum for plot name"""
    LL = "log-log"
    C = "conventional"

class DataType(Enum):
    """Enum for data type"""
    MM = 'MM'
    UL = 'UL'
    MR = 'MR'

class DataName(Enum):
    """Enum for data file name"""
    MM = "middlemarch.txt"
    UL = "ulysses.txt"
    MR = "the_masque_of_the_red_death.txt"

def main() -> None:
    parser = argparse.ArgumentParser(description="Data Science 1: Zipfian Explorations")
    parser.add_argument(
        "plot_type",
        type=str,
        choices=[e.value for e in PlotType],
        help=f"Type of plot: {[f"{e.value} ({get_plot_name(e)})" for e in PlotType]}"
    )
    parser.add_argument(
        "data_type",
        type=str,
        choices=[e.value for e in DataType],
        help=f"Data type: {[f"{e.value} ({get_data_file(e)})" for e in DataType]}"
    )
    args = parser.parse_args()

    # Convert arguments to enums
    try:
        plot_type = PlotType(args.plot_type)
        plot_name = get_plot_name(plot_type)
        data_type = DataType(args.data_type)
        data_file = get_data_file(data_type)
    except ValueError as e:
        print(f"Invalid argument: {e}")
        sys.exit(1)

    print(f"Plot Name: {plot_name}")
    print(f"Data File: {data_file}")

    fin = open_file(data_file)
    fst: str = fin.read()
    lst: list[str] = string_to_list(fst)
    dic: list[tuple[str, int]] = list_to_dict(lst)

    plot_dic(dic, plot_type)


def get_plot_name(plotType: PlotType) -> PlotName:
    """Gets the name of the plot (log-log or conventional) from the plot type argument abbreviation."""
    return PlotName[plotType.name].value

def get_data_file(dataType: DataType) -> DataName:
    """Gets the data file name from the data type argument abbreviation."""
    return DataName[dataType.name].value

def open_file(filePath: str):
    while (True):
        try:
            fin = open(filePath, 'r')
            break
        except:
            print("Invalid file name, Try again")
    return fin

def string_to_list(string: str) -> list[str]:
    """Convert a string to a list of strings, each element of which represents a word."""
    string = re.sub('\n', ' ', string)
    string = re.sub('-', ' ', string)
    lst = string.split(' ')
    cleaned_lst = [re.sub(r'[^a-zA-Z]', '', word) for word in lst]
    return cleaned_lst

def list_to_dict(lst: list[str]):
    """Converts a list of strings (list of words) to a dictionary of words and their frequency in the list."""
    count_dict: dict[str, int] = {}
    for word in lst:
        if word in count_dict:
            count_dict[word] = count_dict[word] + 1
        else:
            count_dict[word] = 1

    sorted_lst: list[tuple[str, int]] = sorted(count_dict.items(), key = itemgetter(1), reverse = True)
    return sorted_lst

def plot_dic(dic: list[tuple[str, int]], plot_type: PlotType) -> None:
    """Plots the dictionary of words and frequencies using MatPlotLib."""
    words, freqs = zip(*dic)
    ranks: range = range(1, len(freqs) + 1)

    fig, ax = plt.subplots()
    if plot_type == PlotType.LL:
        sc = ax.scatter(ranks, freqs, marker='o')
        ax.set_xscale('log')
        ax.set_yscale('log')
        ax.set_xlabel('Rank (log)')
        ax.set_ylabel('Frequency (log)')
        ax.set_title('Log-Log Plot of Word Frequencies')
    elif plot_type == PlotType.C:
        sc = ax.scatter(ranks, freqs, marker='o')
        ax.set_xlabel('Rank')
        ax.set_ylabel('Frequency')
        ax.set_title('Conventional Plot of Word Frequencies')
    else:
        print("Unknown plot type.")
        return

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()