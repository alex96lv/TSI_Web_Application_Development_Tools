#!/usr/bin/env python3
"""
Script to clear all user data from MongoDB database
Use this before publishing project to Git
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'expense_tracker.settings')
django.setup()

from users.models import User
from categories.models import Category
from transactions.models import Transaction
from budgets.models import Budget
from goals.models import Goal
from recurring_transactions.models import RecurringTransaction

def clear_database():
    """Clear all user data from database"""
    print('Clearing database...\n')

    # Count before deletion
    users_count = User.objects.count()
    categories_count = Category.objects.count()
    transactions_count = Transaction.objects.count()
    budgets_count = Budget.objects.count()
    goals_count = Goal.objects.count()
    recurring_count = RecurringTransaction.objects.count()

    print(f'Found:')
    print(f'  Users: {users_count}')
    print(f'  Categories: {categories_count}')
    print(f'  Transactions: {transactions_count}')
    print(f'  Budgets: {budgets_count}')
    print(f'  Goals: {goals_count}')
    print(f'  Recurring Transactions: {recurring_count}')
    print()

    # Ask for confirmation
    response = input('Delete all data? (yes/no): ')
    if response.lower() != 'yes':
        print('Cancelled.')
        return

    # Delete all data
    RecurringTransaction.objects.delete()
    print('✓ Deleted all recurring transactions')

    Goal.objects.delete()
    print('✓ Deleted all goals')

    Budget.objects.delete()
    print('✓ Deleted all budgets')

    Transaction.objects.delete()
    print('✓ Deleted all transactions')

    Category.objects.delete()
    print('✓ Deleted all categories')

    User.objects.delete()
    print('✓ Deleted all users')

    print('\n✅ Database cleared successfully!')
    print('\nNote: Password reset codes and tokens are stored in MongoDB with TTL and will expire automatically.')

if __name__ == '__main__':
    try:
        clear_database()
    except Exception as e:
        print(f'❌ Error: {e}')
        import traceback
        traceback.print_exc()
