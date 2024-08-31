import reflex as rx

# Common styles for questions and answers.
shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px"
chat_margin = "20%"
message_style = dict(
    padding="1em",
    border_radius="5px",
    margin_y="0.5em",
    box_shadow=shadow,
    max_width="30em",
    display="inline-block",
)

chat_history = dict(
    padding="30px 30px 20px",
    border_bottom="2px solid white",
    overflow_y="scroll",
    height="70vh",
)

# Set specific styles for questions and answers.
question_style = message_style | dict(
    margin_left=chat_margin,
    background_color=rx.color("gray", 4),
)
answer_style = message_style | dict(
    margin_right=chat_margin,
    background_color=rx.color("accent", 8),
)

# Styles for the action bar.
input_style = dict(
    border_width="1px",
    box_shadow=shadow,
    width="100%",
    padding="10px 20px",
    font="14px/22px 'Lato', Arial, sans-serif",
    margin_bottom="10px",
    border_radius="5px",
)
button_style = dict(
    background_color=rx.color("accent", 10),
    box_shadow=shadow,
)
