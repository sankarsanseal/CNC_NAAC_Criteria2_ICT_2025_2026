import smtplib
import streamlit as st
from email.message import EmailMessage

st.header(f"Selected Department: {st.session_state.selected_department}" )






st.title("Send Email with Attachment")

with st.form("email_form"):
  recipient = st.text_input("Recipient Email")
  subject = st.text_input("Subject", "File from Streamlit App")
  body = st.text_area("Message", "Please find the attached file below.")
  uploaded_file = st.file_uploader("Choose a file to attach")

  submitted = st.form_submit_button("Send Email")

if submitted and uploaded_file is not None:
  try:
    # Build email message
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = st.secrets["EMAIL_USER"]
    msg["To"] = recipient
    msg.set_content(body)

    # Attach the uploaded file from memory
    file_data = uploaded_file.getvalue()
    file_name = uploaded_file.name
    msg.add_attachment(
        file_data,
        maintype="application",
        subtype="octet-stream",
        filename=file_name,
    )

    # Connect to SMTP server via TLS
    with smtplib.SMTP(
        st.secrets["SMTP_SERVER"], int(st.secrets["SMTP_PORT"])
    ) as server:
      server.starttls()
      server.login(st.secrets["EMAIL_USER"], st.secrets["EMAIL_PASSWORD"])
      server.send_message(msg)

    st.success("Email sent successfully!")

  except Exception as e:
    st.error(f"Failed to send email: {e}")