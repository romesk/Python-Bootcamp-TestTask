import csv
from typing import Callable


class FilmNotes:
    def __init__(self, csv_path: str = "films_notes.csv") -> None:

        self.csv_path = csv_path
        self.fields = ('Film Name', 'Note', 'Rating')

        # Add headers to CSV file
        with open(csv_path, 'w', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(self.fields)

    def add_note(self, film_name: str, note: str, rating: int) -> None:
        """
        Add note to CSV file.
        :param film_name: Film Name
        :param note: Note about a film
        :param rating: Rating of a film. Must be from 1 to 5
        """

        if rating not in range(1, 5+1):
            raise ValueError("Rating must be from 1 to 5.")

        with open(self.csv_path, 'a', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow((film_name, note, rating))

    def remove_note(self, film_name: str) -> None:
        """
        Remove note from CSV file by Film Name.
        :param film_name: Name of Film
        """

        lines_to_write = []

        with open(self.csv_path, 'r', encoding='utf-8') as file_in:
            csv_file_in = csv.reader(file_in)
            for line in csv_file_in:
                if line[0] != film_name:
                    lines_to_write.append(line)

        with open(self.csv_path, 'w', encoding='utf-8') as file_out:
            writer = csv.writer(file_out)
            writer.writerows(lines_to_write)

    def output(self, title: str = "") -> None:
        """
        Output all the notes to the console
        """

        self._output_table(self._get_all_notes(), title)

    @staticmethod
    def _output_table(data: list, title: str = "") -> None:
        """
        Pretty output List of Lists as a Table
        :param title: Name of a table to be printed
        """

        if title:
            print(f'[{title}]:')

        col_spacer = " | "

        # get max width of each col
        widths = [0] * len(data[0])
        for row in data:
            widths[:] = [max(widths[index], len(str(col))) for index, col in enumerate(row)]

        for i, row in enumerate(data, start=1):
            print(col_spacer.join("{:<{width}}".format(col, width=widths[index]) for index, col in enumerate(row)))

    def _get_all_notes(self, sort: bool = False, key: Callable = None, reverse: bool = False) -> list:

        with open(self.csv_path, 'r', encoding='utf-8') as file:
            data = list(csv.reader(file))

        if sort:
            data.sort(key=key, reverse=reverse)

        return data

    def get_films_with_highest_rating(self, amount: int = 5, output: bool = True) -> list:
        """
        Get films with the highest rating
        :param amount: Number of films to be returned
        :param output: Whether to output table to console
        :return: list of films
        """

        amount += 1  # first row is Headers

        data = self._get_all_notes(sort=True,
                                   key=lambda x: x[2],
                                   reverse=True)
        if output:
            self._output_table(data[:amount], "With Highest Rating")

        return data[:amount]

    def get_films_with_lowest_rating(self, amount: int = 5, output: bool = True) -> list:
        """
        Get films with the lowest rating
        :param amount: Number of films to be returned
        :param output: Whether to output table to console
        :return: list of films
        """

        amount += 1  # first row is Headers

        data = self._get_all_notes(sort=True,
                                   key=lambda x: x[2],
                                   reverse=False)

        if output:
            self._output_table(data[:amount], "With Lowest Rating")

        return data[:amount]

    def get_average_rating(self) -> float:
        """
        Get average rating between all the notes
        :return: average rating
        """

        notes = self._get_all_notes()
        ratings = [int(note[2]) for note in notes[1:]]

        return sum(ratings) / len(ratings)


def main() -> None:
    """
    Sample usage of FilmNotes class
    """

    film_notes = FilmNotes()

    film_notes.add_note('Film1', "Cool", 4)
    film_notes.add_note('Film2', "Not bad", 3)
    film_notes.add_note('Film3', "Perfect", 5)
    film_notes.add_note('Film4', "Impressive", 5)
    film_notes.add_note('Film5', "Awful", 1)

    film_notes.output("Filled")
    print('\n', end="")  # just for beautiful output

    film_notes.remove_note('Film1')
    film_notes.output('After removing')
    print('\n', end="")

    film_notes.get_films_with_highest_rating(3)
    print('\n', end="")

    film_notes.get_films_with_lowest_rating(2)
    print('\n', end="")

    avg_rate = film_notes.get_average_rating()
    print(f"Average rating is: {avg_rate}")


if __name__ == '__main__':
    main()
