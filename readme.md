# Budget Planner
The Budget Planner is a Python-based application designed to help you manage your budget by adding, viewing, updating, deleting budget items, and generating a PDF report. It stores budget data in a JSON file and uses the ReportLab library to generate the PDF report.

## Features
- **Add Budget Item:** Add a new budget item with name, category, amount, and date.
- **View Budget:** Display all budget items.
- **Delete Budget Item:** Remove a budget item by its index.
- **Update Budget Item:** Update the details of an existing budget item.
- **Generate PDF Report:** Create a PDF report of the budget items.

## Installation
1. Clone the repository:
```sh
git clone https://github.com/MuhammadUmer78/Budget-Planner.git
```

2. Change to the project directory:
```sh
cd Budget-Planner
```

3. Install the required dependencies:
```sh
pip install -r requirements.txt
```

## Usage
To run the Budget Planner application, use the following command:
```sh
python budget_planner.py
```

### Menu Options
1. **Add Budget Item:** Add a new item to the budget.
2. **View Budget:** Display the current list of budget items.
3. **Delete Budget Item:** Remove an item from the budget by its index.
4. **Update Budget Item:** Update the details of an existing budget item by its index.
5. **Generate PDF Report:** Create a PDF report of the current budget items.
6. **Exit:** Exit the application.

## Example

### Adding a Budget Item
```sh
Choose an option: 1
Enter the name of the item: Groceries
Enter the category: Food
Enter the amount: 100.50
```

### Viewing the Budget
```sh
Choose an option: 2
1. Groceries - Food - 100.5 - 2024-07-10
```

### Deleting a Budget Item
```sh
Choose an option: 3
Enter the index of the item to delete: 1
```

### Updating a Budget Item
```sh
Choose an option: 4
Enter the index of the item to update: 1
Enter the new name (or leave blank to keep current): 
Enter the new category (or leave blank to keep current): 
Enter the new amount (or leave blank to keep current): 150.75
Enter the new date (or leave blank to keep current): 
```

### Generating a PDF Report
```sh
Choose an option: 5
```

## Dependencies
- **json:** For handling JSON data.
- **datetime:** For managing date and time.
- **reportlab:** For generating PDF reports.

Install ReportLab with:
```sh
pip install reportlab
```

## License
This project is licensed under the MIT License. See the [License](LICENSE) file for details.

## Contributing
Contributions are welcome! Please create a pull request or submit an issue for any bugs or feature requests.