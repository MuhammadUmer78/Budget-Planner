import json
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph

class BudgetPlanner:
    def __init__(self, filename='budget.json'):
        self.filename = filename
        self.load_budget()

    def load_budget(self):
        try:
            with open(self.filename, 'r') as file:
                self.budget = json.load(file)
        except FileNotFoundError:
            self.budget = []

    def save_budget(self):
        with open(self.filename, 'w') as file:
            json.dump(self.budget, file, indent=4)

    def add_item(self, name, category, amount, date=None):
        if date is None:
            date = datetime.now().strftime('%Y-%m-%d')
        item = {
            'name': name,
            'category': category,
            'amount': amount,
            'date': date
        }
        self.budget.append(item)
        self.save_budget()
        print(f"Added: {item}")

    def view_budget(self):
        if not self.budget:
            print("No budget items found.")
        else:
            for i, item in enumerate(self.budget, start=1):
                print(f"{i}. {item['name']} - {item['category']} - {item['amount']} - {item['date']}")

    def delete_item(self, index):
        try:
            item = self.budget.pop(index - 1)
            self.save_budget()
            print(f"Deleted: {item}")
        except IndexError:
            print("Invalid index. Please try again.")

    def update_item(self, index, name=None, category=None, amount=None, date=None):
        try:
            item = self.budget[index - 1]
            if name:
                item['name'] = name
            if category:
                item['category'] = category
            if amount:
                item['amount'] = amount
            if date:
                item['date'] = date
            self.save_budget()
            print(f"Updated: {item}")
        except IndexError:
            print("Invalid index. Please try again.")

    def generate_pdf(self, filename='budget_report.pdf'):
        doc = SimpleDocTemplate(filename, pagesize=letter)
        elements = []

        # Create styles
        styles = getSampleStyleSheet()
        centered_style = ParagraphStyle(name='Centered', parent=styles['Heading1'], alignment=1)

        # Add a title
        title = Paragraph("Budget Report", centered_style)
        elements.append(title)
        elements.append(Paragraph("<br/><br/>", styles['Normal']))  # Adding space

        if not self.budget:
            elements.append(Paragraph("No budget items found.", styles['Normal']))
        else:
            # Table data
            data = [['No.', 'Name', 'Category', 'Amount', 'Date']]
            for i, item in enumerate(self.budget, start=1):
                data.append([i, item['name'], item['category'], item['amount'], item['date']])
            
            # Table style
            table_style = TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ])

            # Create the table
            table = Table(data)
            table.setStyle(table_style)
            elements.append(table)

        # Build the PDF
        doc.build(elements)
        print(f"PDF report generated: {filename}")

    def run(self):
        while True:
            print("\nBudget Planner")
            print("1. Add Budget Item")
            print("2. View Budget")
            print("3. Delete Budget Item")
            print("4. Update Budget Item")
            print("5. Generate PDF Report")
            print("6. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                name = input("Enter the name of the item: ")
                category = input("Enter the category: ")
                amount = float(input("Enter the amount: "))
                self.add_item(name, category, amount)
            elif choice == '2':
                self.view_budget()
            elif choice == '3':
                self.view_budget()
                index = int(input("Enter the index of the item to delete: "))
                self.delete_item(index)
            elif choice == '4':
                self.view_budget()
                index = int(input("Enter the index of the item to update: "))
                name = input("Enter the new name (or leave blank to keep current): ")
                category = input("Enter the new category (or leave blank to keep current): ")
                amount = input("Enter the new amount (or leave blank to keep current): ")
                date = input("Enter the new date (or leave blank to keep current): ")
                self.update_item(index, name or None, category or None, float(amount) if amount else None, date or None)
            elif choice == '5':
                self.generate_pdf()
            elif choice == '6':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    app = BudgetPlanner()
    app.run()
