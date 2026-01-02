from flask import request, abort, make_response
from functools import wraps

# -- Flask Auth Code

ADMIN_COOKIE_NAME = "admin"
ADMIN_COOKIE_VALUE = "true"


def set_admin_cookie(response):
    """
    Attach an admin cookie to a response.
    """
    response.set_cookie(
        ADMIN_COOKIE_NAME,
        ADMIN_COOKIE_VALUE,
        httponly=True,     # JS can't read it
        secure=True,       # HTTPS only (disable in local dev if needed)
        samesite="Lax",
        max_age=60 * 60    # 1 hour
    )
    return response

def clear_admin_cookie(response):
    """
    Remove the admin cookie.
    """
    response.delete_cookie(ADMIN_COOKIE_NAME)
    return response


def is_admin():
    """
    Check if request has admin cookie.
    """
    return request.cookies.get(ADMIN_COOKIE_NAME) == ADMIN_COOKIE_VALUE


def admin_required():
    """
    Hard stop if user is not admin.
    """
    if not is_admin():
        abort(403)


def admin_required_route(func):
    """
    Decorator for admin-only routes.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        admin_required()
        return func(*args, **kwargs)
    return wrapper

# -- Streamlit Auth Code
def is_email_authorized(email: str) -> bool:
    """
    Database-style authorization check.

    Later, replace the body of this function with:
      - SQL EXISTS query
      - ORM lookup
      - API call

    This function should return True/False only.
    """

    # ---- MOCK DATABASE CHECK ----
    mock_allowed_emails = {
        "alice@example.com",
        "bob@example.com",
        "admin@company.com",
    }

    return email.lower() in mock_allowed_emails
