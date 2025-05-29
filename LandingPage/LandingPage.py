import reflex as rx
from rxconfig import config

class State(rx.State):
    pass

def download_buttons():
    return rx.hstack(
        rx.link(
            rx.button(
                rx.image(src="/image.png", width="40px", height="40px"),
                "Available on App Store",
                left_icon="apple",
                color_scheme="gray",
                size="4",
                height="90px",
                width="240px",
            ),
            href="#",
            is_external=True
        ),
        rx.link(
            rx.button(
                rx.image(src="/Playstore.png", width="50px", height="60px"),
                "Available on Google Play",
                left_icon="play",
                color_scheme="gray",
                size="4",
                height="90px",
                width="240px",
            ),
            href="#",
            is_external=True
        ),
        spacing="4",
        justify="center",
    )


def navbar():
    return rx.flex(
        rx.hstack(
            rx.image(src="/Mano.png", width="42px"),
            rx.hstack(
                rx.link("About", href="#", font_size="1.3rem"),
                rx.link("Testimonials", href="#", font_size="1.3rem"),
                rx.link("FAQ", href="#", font_size="1.3rem"),
                rx.link("Download", href="#", font_size="1.3rem"),
                spacing="6",
                align="center"
            ),
            spacing="8"
        ),
        rx.hstack(
            rx.button("Free download", variant="outline", size="4"),
            rx.button("Upgrade to Pro 🔐", color_scheme="red", size="4"),
            spacing="6"
        ),
        justify="between",
        align="center",
        padding_x="10%",
        padding_y="1em",
        margin_top="2em",
        border_bottom="1px solid #eee",
        width="100%",
        position="sticky",
        top="0",
        bg="white",
        z_index="10"
    )

def hero_section():
    return rx.center(
        rx.vstack(
            rx.heading("Simple & Reliable.", size="9", color="blue.900", text_align="center"),
            rx.text(
                "Simpler remembers your important details, so you can fill carts, not forms. "
                "And everything is encrypted so you can speed safely through checkout.",
                font_size="1.5rem",
                color="gray.600",
                text_align="center",
                max_width="700px",
            ),
            download_buttons(),
            rx.image(src="/Ilustracion.png", width="100%", margin_top="2em"),
            spacing="6",
            align="center"
        ),
        padding_y="6em",
        min_height="80vh"
    )

def AboutUs():
    return rx.center(
        rx.hstack(
            rx.vstack(
                rx.image("/Dinero.png", width="100px"),
                rx.text("Pay better", font_size="2.7rem", font_family="Spartan Thin"),
                rx.text(
                    "Speed through checkout and offset delivery at the same time.",
                    max_width="300px",
                    text_align="center",
                    size="5"
                ),
                spacing="2",
                align="center",
            ),
            rx.vstack(
                rx.image("/Mapa.png", width="100px"),
                rx.text("Track better", font_size="2.7rem", font_family="Spartan Thin"),
                rx.text(
                    "Get real-time delivery updates from cart to home in one place.",
                    max_width="300px",
                    text_align="center",
                    size="5"
                ),
                spacing="2",
                align="center",
            ),
            rx.vstack(
                rx.image("/basket.png", width="100px"),
                rx.text("Shop better", font_size="2.7rem", font_family="Spartan Thin"),
                rx.text(
                    "Upgrade with personal settings from your favorite stores.",
                    max_width="300px",
                    text_align="center",
                    size="5"
                ),
                spacing="2",
                align="center",
            ),
            spacing="9"
        ),
        padding_y="4em"
    )

def LearnMore():
     return rx.hstack(
        rx.vstack(
            rx.heading(
                "A thoughtful way to pay",
                font_size="2.5rem",
                font_weight="bold",
                color="#0A2D4D",
                text_align="left"
            ),
            rx.text(
                "Simpler App remembers your important details, so you can fill carts, not forms. "
                "And everything is encrypted so you can speed safely through checkout.",
                font_size="1.1rem",
                color="gray.700",
                max_width="650px",
                text_align="left",
                line_height="1.8"
            ),
            rx.text(
                "Now, you can offset the carbon emissions produced by your deliveries—for free. "
                "All you have to do is check out with Shop Pay, one of the first carbon-neutral way to pay.",
                font_size="1.1rem",
                color="gray.700",
                max_width="650px",
                text_align="left",
                line_height="1.8"
            ),
            rx.button(
                "Learn More",
                right_icon="external-link",
                variant="solid",
                color_scheme="teal",
                size="3",
                width="180px",
                height="50px",
                border_radius="8px",
                font_weight="medium",
                margin_top="1em"
            ),
            spacing="4",
            align="start",
            padding_x="13rem"
        ),

        rx.image(
            src="/SVG.png",
            width="900px",
            height="auto",
        ),

        spacing="2",
        align="center",
        justify="start",
        width="100%",
        padding_y="6em"
    )

def index() -> rx.Component:
    return rx.box(
        navbar(),
        hero_section(),
        AboutUs(),
        LearnMore()
    )

app = rx.App()
app.add_page(index, title="Landing Page Reflex")
