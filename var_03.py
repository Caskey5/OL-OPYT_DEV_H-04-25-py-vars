"""
 • Potrebno je kreirati varijable u kojima će biti pohranjene 
proizvoljne dužine trokuta.
"""

a = 5
b = 10
c = 7

"""
• Potrebno je kreirati varijable u kojima će biti pohranjeni podaci o 
filmu: naziv filma, godina proizvodnje, proječna ocjena, kratki 
opis
"""

movie_name = "Inception"
movie_year = 2010
movie_rating = 8.8
movie_description = "Kratki opis filma Inception."

"""
• Potrebno je kreirati varijable u kojima će biti pohranjeni podaci o 
imenu i prezimenu studenta, završnoj ocjeni te podataka je li 
diplomirao ili nije
"""

student_name = "Ivan"
student_surname = "Ivić"
student_grade = 4
student_graduated = True

"""
 • Kreirati varijablu za čuvanje podataka o studentu: ime i prezime, 
OIB, email, broj telefona, prosječna ocjena, godina upisa 
studija, naziv studija, naziv sveučilišta
"""

# Opcija 1
student = "Ivan Ivić, 12345678901, ivan.ivic@gmail.com, 0975123456, 3.5, 2025, Računarske znanosti, Sveučilište u Zagrebu"

# Opcija 2
Jstudent_oib = "12345678901"
student_email = "ivan.ivic@gmail.com"
student_phone = "0975123456"
student_average_grade = 3.5
student_enrollment_year = 2025
student_study_program = "Računarske znanosti"
student_university_name = "Sveučilište u Zagrebu"

student_phone = int(student_phone)  # Pretvaranje stringa u integer
print(student_phone + 1)
