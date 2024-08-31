import reflex as rx

from .navbar import sidebar
from maverik.components.container import container


def page_container(page: rx.Component) -> rx.Component:
    return container(
        rx.grid(
            sidebar(),
            page,
            gap="1rem",
            grid_template_columns="1fr 3fr",
            height="100vh",
            spacing="4",
        ),
        max_width="1300px",
    )


def signup_welcome_page() -> rx.Component:
    return page_container(
        rx.container(
            rx.box(
                rx.vstack(
                    rx.heading("¡Bienvenido a Maverick!", size="5"),
                    rx.text(
                        "Nos alegra tenerte aquí. Queremos que sepas que estamos comprometidos con tu privacidad y seguridad.",
                        as_="p",
                    ),
                    rx.text(
                        "Para que puedas disfrutar de nuestros servicios sin preocupaciones no vamos a pedirte tus datos personales.",
                        as_="p",
                    ),
                    rx.text(
                        "¡Con Maverick, podes enfocarte en tus metas financieras con confianza!",
                        as_="p",
                    ),
                    rx.button("Continuar"),
                    justify="left",
                ),
                width="100%",
                padding="10px",
            ),
            size="4",
        )
    )


def signup_page_1() -> rx.Component:
    return page_container(rx.text("pagina 1"))


def signup_page_2() -> rx.Component:
    return page_container(rx.text("pagina 2"))
