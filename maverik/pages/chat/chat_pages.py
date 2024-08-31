import reflex as rx

from . import style
from .navbar import sidebar
from .state import State
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
        min_width="960px",
        max_width="1300px",
    )


def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(question, style=style.question_style),
            text_align="right",
        ),
        rx.box(
            rx.text(answer, style=style.answer_style),
            text_align="left",
        ),
        margin_y="1em",
    )


def chat() -> rx.Component:
    return rx.box(
        rx.foreach(
            State.chat_history,
            lambda messages: qa(messages[0], messages[1]),
        ),
        style=style.chat_history,
    )


def action_bar() -> rx.Component:
    return rx.hstack(
        rx.text_area(
            placeholder="Realiza una pregunta",
            style=style.input_style,
            rows="2",
            on_change=State.set_question,
        ),
        rx.button(
            "Consultar",
            style=style.button_style,
            on_click=State.answer,
        ),
    )


def chat_page() -> rx.Component:
    return page_container(
        rx.container(
            rx.vstack(
                chat(),
                action_bar(),
                align="left",
            ),
            size="3",
        )
    )
