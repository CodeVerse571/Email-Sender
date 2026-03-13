import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# CONFIGURACIÓN
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_REMITENTE = "eandreszambrano4@gmail.com"
PASSWORD = "hacjtprclfngxfyq"

ESPERA_SEGUNDOS = 10


DESTINATARIOS = [
    "servicioalcliente@gessacr.com",
    "Yanellis.Filos@philips.com",
    "jcastroe@juntadepensiones.cr",
    "gcascante@juntadepensiones.cr",
    "alejandro.solorzano@vidaplena.fi.cr",
    "rulloa@cajadeande.fi.cr",
    "vvasquez@cajadeande.fi.cr",
    "fvargas@sociedaddesegurosdevida.cr",
    "dcordoba@sociedaddesegurosdevida.cr",
    "jcgonzalez@utn.ac.cr",
    "info@cenarec.go.cr",
    "servicios@cpic.or.cr",
    "nestor.solano@grupomonge.com",
    "genteycultura@grupopromerica.com",
    "info@mjolner.dk",
    "raul.gutierrez@factork-software.com",
    "giovanna.francesa.alfaro@intel.com"
]


ASUNTO = "Consulta sobre práctica profesional en desarrollo de software – 2026"

MENSAJE = """
Estimado/a,

Mi nombre es Eduardo Andrés Zambrano, estudiante de Ingeniería en Software en la Universidad Técnica Nacional (UTN).

Actualmente me encuentro en búsqueda de una práctica profesional para el segundo cuatrimestre del 2026 y quisiera consultar si su empresa cuenta con oportunidades para estudiantes en el área de desarrollo de software.

Quedo atento a cualquier información y con gusto puedo compartir mi currículum si lo consideran pertinente.

Muchas gracias por su tiempo.

Saludos cordiales,
Eduardo Andrés Zambrano
Estudiante de Ingeniería en Software – UTN
"""


def enviar_correos():
    enviados = 0
    fallidos = 0

    try:
        print("Conectando al servidor...")

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_REMITENTE, PASSWORD)

        print("Conexión establecida\n")

        for correo in DESTINATARIOS:
            try:
                msg = MIMEMultipart()
                msg["From"] = EMAIL_REMITENTE
                msg["To"] = correo
                msg["Subject"] = ASUNTO

                msg.attach(MIMEText(MENSAJE, "plain"))

                server.sendmail(EMAIL_REMITENTE, correo, msg.as_string())

                enviados += 1
                print(f"Enviado a: {correo}")

            except Exception as e:
                fallidos += 1
                print(f"Error con {correo}: {e}")

            print(f"Esperando {ESPERA_SEGUNDOS} segundos...\n")
            time.sleep(ESPERA_SEGUNDOS)

        server.quit()

        print("\n===== RESULTADO =====")
        print(f"Enviados: {enviados}")
        print(f"Fallidos: {fallidos}")

    except Exception as e:
        print("Error al conectar con el servidor:", e)


if __name__ == "__main__":
    enviar_correos()