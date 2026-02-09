from io import StringIO

from django.core.management import call_command
from django.test import TestCase

from django_managed_commands.models import CommandExecution


class TestSendNotificationsCommand(TestCase):
    """Test cases for send_notifications management command."""

    def setUp(self):
        """Clear CommandExecution records before each test."""
        CommandExecution.objects.all().delete()

    def test_command_creates_execution_record(self):
        """Verify that running the command creates a CommandExecution record."""
        # Run the command
        call_command("send_notifications")

        self.assertTrue(
            CommandExecution.objects.filter(command_name="main.send_notifications").exists()
        )

    def test_command_success(self):
        """
        Verify the command completes successfully.
        Ideally you'd want to add specific assertions before the `call_command()`,
        and after it, based on your command's expected side-effects.
        """
        # You can add pre-execution assertions here

        call_command("send_notifications")

        execution = CommandExecution.objects.get(command_name="main.send_notifications")
        self.assertTrue(execution.success)
        self.assertIsNotNone(execution.duration)

        # Side-effect assertions should be around here

    def test_command_failure(self):
        # TODO: Implement failure test for your specific error scenarios:
        # - Trigger an error condition
        # - Verify ComandExecution::success is False
        # - Verify ComandExecution::error_message is populated
        # - Verify database changes were rolled back
        pass

    def test_command_dry_run_rolls_back(self):
        """Verify that a `--dry-run` flag reverts the transaction, and no record is stored"""
        out = StringIO()
        call_command("send_notifications", "--dry-run", stdout=out)

        self.assertIn("DRY RUN", out.getvalue())
        self.assertIn("rolled back", out.getvalue())
        self.assertFalse(
            CommandExecution.objects.filter(command_name="main.send_notifications").exists()
        )

    def test_can_run_multiple_times(self):
        call_command("send_notifications")
        call_command("send_notifications")
        call_command("send_notifications")

        self.assertEqual(
            CommandExecution.objects.filter(command_name="main.send_notifications").count(),
            3,
        )
