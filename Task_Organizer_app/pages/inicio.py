import reflex as rx

def inicio()->rx.Component:
    def handle_login():
        # Aquí puedes agregar lógica para registrar al usuario (si es necesario)
        return rx.redirect("/pantalla_principal")
    
    return rx.box(
        rx.container(
            rx.heading(
                rx.text("Iniciar sesion"),
                align="center",
                color="#000000",
                size="xl",
                margin_bottom="40px",
                margin_top="-30px",
            ),
            rx.input(
                placeholder="correo electronico",
                type="e-mail",
                margin_top="10px",
                bg="#757575"
            
                #border="2px solid #ccc",
            ),
            rx.input(
                placeholder="contraseña",
                type="password",
                margin_top="10px",
                bg="#757575"
                #border="2px solid #ccc",
            ),
            rx.button("Iniciar Sesión",
                background_color="#007BFF",
                padding="12px",
                margin_top="20px",
                width="100%",
                on_click=handle_login,
            ),
            rx.link("¿Olvidaste tu contraseña?",
                href="https://accounts.google.com/signin/v2/recoveryidentifier",
                color="#007BFF",
                margin_top="20px",
                text_align="center",
                display="block"
            ),
            rx.divider(margin_top="10px", margin_bottom="20px"),
            rx.text("o continua con:", align="center",margin_butom="10px",color="#BDBDBD"),
            rx.hstack(
                rx.link(
                    rx.image(src="https://img.icons8.com/?size=512&id=17949&format=png",
                    width="24px",
                    height="24px",
                    alt="Google",
                    ),
                href="https://accounts.google.com/AccountChooser/signinchooser?service=CPanel&continue=https%3A%2F%2Fadmin.google.com%2Fctech.mx%2FDashboard&hl=es&ddm=1&flowName=GlifWebSignIn&flowEntry=AccountChooser",
                ),
                rx.link(
                    rx.image(src="https://img.freepik.com/vector-premium/ilustracion-arte_929495-41.jpg?semt=ais_hybrid",
                    width="24px",
                    height="24px",
                    alt="Facebook"
                    ),
                href="https://www.facebook.com"
                ),
                rx.link(
                    rx.image(src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ_63oeY4HoVAvm8HHv0nuNH_88ZRD9PJRdxA&s",
                    width="24px",
                    height="24px",
                    alt="Instagram"
                    ),
                    href="https://www.instagram.com",
                ),
                justify="center",
                spacing="9",
                margin_top="15px"
            ),
            rx.link("¿No tienes una cuenta? Regístrate",
                href="/registro",
                color="#007BFF",
                margin_top="20px",
                text_align="center",
                display="block",
            ),
            #padding="16px",
            margin_top="50px",
            width="90%",
            max_width="400px",
            background_color="#ffffff",
            border_radius="8px",
            box_shadow="md",
        ),
        height="100vh",
        background_color="#f9f9f9",
        display="flex",
        justify_content="center",
        align_items="center",
    )