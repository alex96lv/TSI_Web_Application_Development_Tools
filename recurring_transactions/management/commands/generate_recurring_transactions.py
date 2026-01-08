from django.core.management.base import BaseCommand
from recurring_transactions.models import RecurringTransaction
from datetime import datetime


class Command(BaseCommand):
    help = 'Generate transactions from recurring transactions that are due'

    def add_arguments(self, parser):
        parser.add_argument(
            '--dry-run',
            action='store_true',
            help='Show what would be generated without actually creating transactions',
        )

    def handle(self, *args, **options):
        dry_run = options['dry_run']

        # Get all active recurring transactions
        recurring_transactions = RecurringTransaction.objects(is_active=True)

        generated_count = 0
        skipped_count = 0

        self.stdout.write(self.style.SUCCESS(f'Found {len(recurring_transactions)} active recurring transactions'))

        for recurring in recurring_transactions:
            if recurring.should_generate_transaction():
                if dry_run:
                    self.stdout.write(
                        self.style.WARNING(
                            f'[DRY RUN] Would generate: {recurring.type} {recurring.amount} '
                            f'for {recurring.user.email} (Category: {recurring.category.name})'
                        )
                    )
                else:
                    try:
                        transaction = recurring.generate_transaction()
                        self.stdout.write(
                            self.style.SUCCESS(
                                f'Generated: {transaction.type} {transaction.amount} '
                                f'for {transaction.user.email} (ID: {transaction.id})'
                            )
                        )
                        generated_count += 1
                    except Exception as e:
                        self.stdout.write(
                            self.style.ERROR(
                                f'Error generating transaction for recurring ID {recurring.id}: {str(e)}'
                            )
                        )
            else:
                skipped_count += 1

        if dry_run:
            self.stdout.write(
                self.style.WARNING(
                    f'\n[DRY RUN] Summary: Would generate {generated_count} transactions, '
                    f'skipped {skipped_count}'
                )
            )
        else:
            self.stdout.write(
                self.style.SUCCESS(
                    f'\nSuccessfully generated {generated_count} transactions, '
                    f'skipped {skipped_count}'
                )
            )
