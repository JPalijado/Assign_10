import qrcode

qr = qrcode.QRCode(version = 1, box_size = 20, border = 5)

name_data = "Name: Samuel Gideon Forrester \n"
qr.add_data(name_data)

occupation_data = "Occupation: Senior Computer Engineer \n"
qr.add_data(occupation_data)

company_data = "Company: Alt+F4 Technologies \n"
qr.add_data(company_data)

telephone_num_data = "Telephone Number: 260-7934 \n"
qr.add_data(telephone_num_data)

mobile_num_data = "Mobile Number: 09358245639 \n"
qr.add_data(mobile_num_data)

email_data = "E-mail: samuelforrester@altf4.com \n"
qr.add_data(email_data)

address_data = "Address: Narra St. Lone Pine Subd. Brgy. Cupang, Antipolo City, Rizal \n"
qr.add_data(address_data)

qr.make(fit = True)
img = qr.make_image(fill = 'black', back_color = 'white')
img.save('Identification Card QR Code.png')
