"""Flask Application entry point."""

from app_demo import create_app

app = create_app()

with app.app_context():
    from app_demo.utils import context_processor