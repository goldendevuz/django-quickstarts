from django_managed_commands.base import ManagedCommand


class Command(ManagedCommand):
    """
    send_notifications management command.

    Extends ManagedCommand which provides:
    - Automatic execution tracking in CommandExecution model
    - Database transaction wrapping (rollback on failure)
    - Built-in --dry-run flag (executes but rolls back all changes)
    - Timing and duration recording
    - Run-once support via `run_once = True`
    """

    help = "send_notifications command - add your description here"

    # Set to True if this command should only run once successfully
    run_once = False

    def add_arguments(self, parser):
        """
        Add your custom arguments here.
        Docs: https://docs.djangoproject.com/en/stable/howto/custom-management-commands/

        Do not remove the super() call - it provides the --dry-run flag.
        """
        super().add_arguments(parser)
        # parser.add_argument("--my-arg", type=str, help="Custom argument")

    def execute_command(self, *args, **options):
        # TODO: Add your command logic here
        # The --dry-run flag is handled automatically by the base class:
        # - All database changes are rolled back at the end
        # - No execution record is created

        self.stdout.write(self.style.SUCCESS("send_notifications completed successfully"))
