import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time
import sys
import getpass

def send_emails_from_excel(excel_file, sender_email, password, subject, message_body):
    try:
        # Excel faylni o'qish
        print("Excel faylni o'qiyapman...")
        df = pd.read_excel(excel_file)
        
        # Gmail ustunini topish
        email_column = None
        for column in df.columns:
            if 'mail' in column.lower() or 'gmail' in column.lower() or 'email' in column.lower():
                email_column = column
                break
        
        if email_column is None:
            print("Xato: Gmail ustuni topilmadi. Ustun nomida 'mail', 'gmail' yoki 'email' bo'lishi kerak.")
            return
        
        # Gmail serverga ulanish
        print("Gmail serverga ulanish...")
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        
        try:
            server.login(sender_email, password)
            print(f"Muvaffaqiyatli kirildi: {sender_email}")
        except Exception as e:
            print(f"Kirish xatosi: {e}")
            print("Tekshiring:")
            print("1. Gmail parolingiz to'g'rimi?")
            print("2. Kamroq xavfsiz ilovalar uchun ruxsat berilganmi?")
            print("   https://myaccount.google.com/lesssecureapps")
            print("3. Ikki bosqichli tekshiruv o'chirilganmi?")
            return
        
        # Har bir elektron manzilga xabar yuborish
        total_emails = df[email_column].count()
        successfully_sent = 0
        failed_sent = 0
        skipped = 0
        
        print(f"\nJami {total_emails} ta email manzil topildi. Yuborish boshlanmoqda...")
        
        for index, row in df.iterrows():
            recipient_email = row[email_column]
            
            # Bo'sh qiymatlarni tekshirish
            if pd.isna(recipient_email) or recipient_email == "":
                print(f"O'tkazib yuborildi: {index+2}-qator - elektron manzil yo'q")
                skipped += 1
                continue
                
            try:
                # Xabar tayyorlash
                msg = MIMEMultipart()
                msg['From'] = sender_email
                msg['To'] = recipient_email
                msg['Subject'] = subject
                msg.attach(MIMEText(message_body, 'html'))
                
                # Xabar yuborish
                server.send_message(msg)
                print(f"Yuborildi ({successfully_sent+1}/{total_emails-skipped}): {recipient_email}")
                successfully_sent += 1
                
                # Gmail spam filtri yoqilmasligi uchun ozgina kutish
                time.sleep(2)
                
            except Exception as e:
                print(f"Xato {recipient_email} ga yuborishda: {str(e)}")
                failed_sent += 1
        
        # Serverdan chiqish
        server.quit()
        
        # Natijalarni ko'rsatish
        print("\nNatijalar:")
        print(f"Jami elektron manzillar: {total_emails}")
        print(f"Muvaffaqiyatli yuborilgan: {successfully_sent}")
        print(f"Yuborilmagan: {failed_sent}")
        print(f"O'tkazib yuborilgan: {skipped}")
        print("Yuborish tugadi!")
        
    except Exception as e:
        print(f"Xatolik yuz berdi: {str(e)}")




def main():
    print("Gmail orqali ommaviy xabar yuborish dasturi")
    print("-------------------------------------------")
    
    # Foydalanuvchi ma'lumotlarini so'rash
    excel_file = input("Excel fayl yo'lini kiriting (masalan: fayllar.xlsx): ")
    sender_email = input("Gmail manzilingizni kiriting: ")
    password = getpass.getpass("Gmail parolingizni kiriting: ")
    subject = input("Xabar mavzusini kiriting: ")
    
    print("\nXabar matnini kiriting (HTML formatida).")
    print("Matnni kiritib bo'lgach, alohida qatorda 'END' so'zini yozing:")
    
    message_lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        message_lines.append(line)
    
    message_body = "\n".join(message_lines)
    
    print("\nXabarlar yuborilmoqda, iltimos kuting...")
    # Tasdiqlashsiz to'g'ridan-to'g'ri yuborish
    send_emails_from_excel(excel_file, sender_email, password, subject, message_body)

if __name__ == "__main__":
    main()
