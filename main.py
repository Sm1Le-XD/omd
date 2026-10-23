import csv
from dataclasses import dataclass
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "Corp_Summary.csv"
OUTPUT_FILE = BASE_DIR / "department_summary.csv"


@dataclass
class Employee:
    department: str
    team: str
    salary: int


def read_employees(file_path: Path = INPUT_FILE) -> list[Employee]:
    """Читает данные сотрудников из CSV-файла."""
    with file_path.open(encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file, delimiter=";")
        return [
            Employee(
                department=row["Департамент"].strip(),
                team=row["Отдел"].strip(),
                salary=int(row["Оклад"]),
            )
            for row in reader
        ]


def print_hierarchy(employees: list[Employee]) -> None:
    """1. Выводит для каждого департамента входящие в него команды."""
    departments: dict[str, set[str]] = {}
    for employee in employees:
        departments.setdefault(employee.department, set()).add(employee.team)

    for department in sorted(departments):
        print(f"{department}:")
        for team in sorted(departments[department]):
            print(f"  - {team}")


def summarize_departments(
        employees: list[Employee],
) -> list[tuple[str, int, int, int, float]]:
    """2. Считает количество сотрудников и статистику окладов
    по департаментам.
    """
    salaries_by_department: dict[str, list[int]] = {}
    for employee in employees:
        salaries_by_department.setdefault(employee.department, []).append(
            employee.salary
        )

    return [
        (
            department,
            len(salaries),
            min(salaries),
            max(salaries),
            sum(salaries) / len(salaries),
        )
        for department, salaries in sorted(salaries_by_department.items())
    ]


def print_department_summary(employees: list[Employee]) -> None:
    """Выводит сводку по департаментам на экран."""
    print(
        f"{'Департамент':<20} {'Сотрудников':>12} "
        f"{'Мин. оклад':>12} {'Макс. оклад':>12} {'Средний оклад':>15}"
    )
    for department, count, minimum, maximum, average in summarize_departments(
            employees
    ):
        print(
            f"{department:<20} {count:>12} {minimum:>12} "
            f"{maximum:>12} {average:>15.2f}"
        )


def write_department_summary(
        employees: list[Employee], file_path: Path = OUTPUT_FILE
) -> None:
    """3. Записывает сводку по департаментам в CSV-файл."""
    headers = [
        "Департамент",
        "Количество сотрудников",
        "Минимальный оклад",
        "Максимальный оклад",
        "Средний оклад",
    ]
    with file_path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(headers)
        for summary in summarize_departments(employees):
            department, count, minimum, maximum, average = summary
            writer.writerow(
                [department, count, minimum, maximum, f"{average:.2f}"]
            )

    print(f"Отчёт сохранён в файл: {file_path}")


def main(
        variant: int,
        input_file: Path = INPUT_FILE,
        output_file: Path = OUTPUT_FILE,
) -> None:
    employees = read_employees(input_file)
    if variant == 1:
        print_hierarchy(employees)
    elif variant == 2:
        print_department_summary(employees)
    elif variant == 3:
        write_department_summary(employees, output_file)


if __name__ == "__main__":
    main(variant=3)
