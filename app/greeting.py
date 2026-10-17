"""Clean sample module: no secrets, no risky calls. HefestoAI passes it."""

import os


def greeting(name: str) -> str:
    """Return a greeting for ``name``."""
    return f"Hello, {name}!"


def api_base_url() -> str:
    """Read configuration from the environment instead of hardcoding it."""
    return os.environ.get("DEMO_API_BASE_URL", "http://localhost:8000")


if __name__ == "__main__":
    print(greeting("HefestoAI"))
