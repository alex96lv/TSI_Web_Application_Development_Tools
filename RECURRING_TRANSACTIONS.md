# Recurring Transactions Feature

## Overview
The recurring transactions feature allows users to set up automatic scheduled payments such as rent, subscriptions, salaries, and other regular income or expenses.

## Features
- ✅ Create recurring transactions with configurable frequency (daily, weekly, monthly, yearly)
- ✅ Set custom intervals (e.g., every 2 weeks, every 3 months)
- ✅ Define start and end dates (or leave indefinite)
- ✅ Toggle active/inactive status
- ✅ Automatic transaction generation via management command
- ✅ Full CRUD API and UI

## API Endpoints

### List all recurring transactions
```
GET /api/recurring/
Query params:
  - type: income|expense
  - is_active: true|false
```

### Create recurring transaction
```
POST /api/recurring/
Body:
{
  "type": "expense",
  "category": "category_id",
  "amount": 1500.00,
  "description": "Monthly rent",
  "frequency": "monthly",
  "interval": 1,
  "start_date": "2024-01-01T00:00:00Z",
  "end_date": null  // optional, null for indefinite
}
```

### Get specific recurring transaction
```
GET /api/recurring/{id}/
```

### Update recurring transaction
```
PUT /api/recurring/{id}/
```

### Delete recurring transaction
```
DELETE /api/recurring/{id}/
```

### Toggle active status
```
POST /api/recurring/{id}/toggle/
```

## Management Command

### Generate transactions from recurring schedules
```bash
python manage.py generate_recurring_transactions
```

### Options:
- `--dry-run`: Preview what would be generated without creating actual transactions

### Example output:
```
Found 5 active recurring transactions
Generated: expense 1500.0 for user@example.com (ID: 123abc)
Generated: income 5000.0 for user@example.com (ID: 456def)

Successfully generated 2 transactions, skipped 3
```

## Automated Scheduling

### Option 1: Cron (Linux/macOS)
Add to crontab to run every hour:
```bash
crontab -e
```

Add this line:
```
0 * * * * cd /path/to/project && /path/to/venv/bin/python manage.py generate_recurring_transactions >> /var/log/recurring_transactions.log 2>&1
```

### Option 2: Systemd Timer (Linux)
Create `/etc/systemd/system/recurring-transactions.service`:
```ini
[Unit]
Description=Generate Recurring Transactions

[Service]
Type=oneshot
User=www-data
WorkingDirectory=/path/to/project
ExecStart=/path/to/venv/bin/python manage.py generate_recurring_transactions
```

Create `/etc/systemd/system/recurring-transactions.timer`:
```ini
[Unit]
Description=Run recurring transactions generator hourly

[Timer]
OnCalendar=hourly
Persistent=true

[Install]
WantedBy=timers.target
```

Enable and start:
```bash
sudo systemctl enable recurring-transactions.timer
sudo systemctl start recurring-transactions.timer
```

### Option 3: Django-Q or Celery
For more advanced scheduling, integrate with task queues:

**Django-Q example:**
```python
from django_q.tasks import schedule
from django_q.models import Schedule

schedule(
    'recurring_transactions.management.commands.generate_recurring_transactions.Command',
    schedule_type=Schedule.HOURLY,
)
```

**Celery example:**
```python
from celery import shared_task
from django.core.management import call_command

@shared_task
def generate_recurring_transactions():
    call_command('generate_recurring_transactions')

# In celery beat schedule:
app.conf.beat_schedule = {
    'generate-recurring-transactions': {
        'task': 'tasks.generate_recurring_transactions',
        'schedule': 3600.0,  # Every hour
    },
}
```

## Usage in UI

1. Navigate to `/recurring/` page
2. Click "Добавить регулярный платёж" (Add Recurring Payment)
3. Fill in the form:
   - Type: Income or Expense
   - Category: Select from your categories
   - Amount: Transaction amount
   - Description: Optional description
   - Frequency: daily/weekly/monthly/yearly
   - Interval: Every X periods
   - Start date: When to start generating transactions
   - End date: Optional end date
4. Click "Сохранить" (Save)

The recurring transaction will automatically generate new transactions when the management command runs.

## Model Fields

- `user`: Reference to User
- `category`: Reference to Category
- `type`: 'income' or 'expense'
- `amount`: Transaction amount
- `description`: Optional description
- `frequency`: 'daily', 'weekly', 'monthly', 'yearly'
- `interval`: Integer (e.g., 2 for "every 2 weeks")
- `start_date`: DateTime when recurring starts
- `end_date`: Optional DateTime when recurring ends
- `next_occurrence`: DateTime of next scheduled transaction
- `is_active`: Boolean to enable/disable
- `last_generated`: DateTime of last generated transaction
- `created_at`: Creation timestamp
- `updated_at`: Last update timestamp

## Dependencies

- `python-dateutil==2.8.2` - For advanced date calculations (added to requirements.txt)
